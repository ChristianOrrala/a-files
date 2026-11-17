import { spawnSync } from "node:child_process"
import { dirname, resolve } from "node:path"
import { fileURLToPath } from "node:url"

const SCRIPT = resolve(dirname(fileURLToPath(import.meta.url)), "../../skills/a-files/scripts/afiles_hook.py")
const TIMEOUT_MS = 30000

const samePath = (a, b) => typeof a === "string" && typeof b === "string" && resolve(a) === resolve(b)

// Synchronous on purpose: `opencode run` may exit before an async handler finishes.
const run = (moment, project, sessionID) => {
  try {
    const r = spawnSync("python3", [SCRIPT, moment, "--emit", "raw"], {
      cwd: project,
      input: JSON.stringify({ session_id: sessionID, cwd: project }),
      encoding: "utf8",
      timeout: TIMEOUT_MS,
    })
    return { status: r.status, out: (r.stdout || "").trim() }
  } catch (_) {
    return { status: 0, out: "" }
  }
}

const sessionOf = (e) => e.data?.sessionID ?? e.sessionID ?? e.properties?.sessionID ?? e.data?.session?.id ?? e.durable?.aggregateID

export default {
  id: "a-files",
  async setup(ctx) {
    const project = ctx.location?.directory
    if (!project) return () => {}
    const ours = new Set() // sessions whose location is this project
    const foreign = new Set() // sessions located in another project: never acted on
    const waiting = new Set() // execution started before the session's location was known
    const noted = new Set() // session-start already delivered
    const prompted = new Set() // the one continuation per session already sent
    const ac = new AbortController()

    const sessionStart = async (sid) => {
      if (noted.has(sid)) return
      noted.add(sid)
      const { out } = run("session-start", project, sid)
      if (out) await ctx.session.instructions.entry.put({ sessionID: sid, key: "a-files-session-start", value: out })
    }

    void (async () => {
      try {
        for await (const e of ctx.event.subscribe({ signal: ac.signal })) {
          try {
            const sid = sessionOf(e)
            if (!sid) continue
            const where = e.location?.directory ?? e.data?.location?.directory ?? e.properties?.location?.directory
            if (where !== undefined && !ours.has(sid) && !foreign.has(sid)) {
              if (samePath(where, project)) {
                ours.add(sid)
                if (waiting.delete(sid)) await sessionStart(sid)
              } else {
                foreign.add(sid)
                waiting.delete(sid)
              }
            }
            if (foreign.has(sid)) continue
            if (e.type === "session.execution.started") {
              if (ours.has(sid)) await sessionStart(sid)
              else waiting.add(sid)
            } else if (e.type === "session.execution.succeeded" && ours.has(sid) && !prompted.has(sid)) {
              const { status, out } = run("before-stop", project, sid)
              if (status === 2 && out) {
                prompted.add(sid)
                await ctx.session.prompt({ sessionID: sid, text: out })
              }
            }
          } catch (_) {}
        }
      } catch (_) {}
    })()
    return () => ac.abort()
  },
}
