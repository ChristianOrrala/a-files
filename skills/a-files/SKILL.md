---
name: a-files
description: >-
  Use when the user wants to adopt the A-files, set up or clean up the files agents read at session
  start, close out a piece of work, promote or schedule an item, sort a full AHEAD, review an
  AGENTS.md, fix what the tracking check reports, link abilities to a spec-driven method's
  specifications in the same project, or project AHEAD to GitHub issues. Adopts and keeps the
  A-files, five Markdown files at a repository's root that every coding agent reads first: AGENTS.md
  (rules, warm-up, index), ACTIVE.md (the work in progress), ABILITIES.md (what the product can do),
  AHEAD.md (what the owner chose to plan) and ATLAS.md (the architecture map), with a keep-in-step
  rule and a check that reports at commit time what breaks their shape, never refusing the commit.
  Maps existing tracking files (a board, a feature list, a roadmap, notes), asks whether to move
  them into the A-files or keep them, and checks every link, import and instruction that names what
  moves. Not for writing specifications; not an issue tracker.
---

# Keeping the A-files

Five files at the root give every agent and every person the same picture at the start of a session: the rules, the
work in progress, what the product can do, what is ahead, and the map. They serve one owner directing agents, not a
team tracker. This skill adopts them in a repository and keeps them true. The daily rules (the warm-up, keeping the
files in step) live in the project's `AGENTS.md`, which every tool reads anyway. Before the first change, the warm-up
states Finished, Remaining, Blocked by and Next step in four short lines, using "nothing" for an empty line and
checking `git log` and `git status`.

The whole method, with its reasons: [references/method.md](references/method.md).

## The five files

| File | Holds | Hot zone cap |
|---|---|---|
| `AGENTS.md` | How to work here and where to look next: warm-up, the index of every file an agent needs, keep in step, commands, rules | None: the tools load it whole |
| `ACTIVE.md` | The piece being worked, the larger work it belongs to (a work section), what is pending and what blocks it | 60 lines |
| `ABILITIES.md` | Every ability of the product, planned to retired, never deleted | 100 lines |
| `AHEAD.md` | What the owner chose to plan: Next up, milestones, ideas, research, proposals. Entered on his decision only | 100 lines |
| `ATLAS.md` | The map: parts, the files they work through, dependencies, checks | 100 lines |

Each of the last four opens with its title and a one-line contract (`> ...`). Its hot zone ends with the line `<!--
hot zone ends -->`, and everything below is named in the hot zone. `AGENTS.md` has no hot zone: one written earlier
may keep its marker, and each fact in it names its home instead of copying from it. Identifiers `AB-001` and `AH-001`
are never reused; an AHEAD item is removed only on the owner's word. An ability's status is written once, in its index
row; done abilities may move to an index table below the hot zone.

**Small or full.** The small setup keeps `AGENTS.md` and `ACTIVE.md`; the full one adds the other three. The check
always expects `ACTIVE.md`, and another A-file once the index of `AGENTS.md` lists it, the file exists, or it held
identifiers in the last commit. In the small setup, remove the other three files' rows from the index of `AGENTS.md`,
and their mentions from the warm-up and keep in step. Without `AHEAD.md`, blocked work stays in ACTIVE's Pending and
Next new work names what the owner chose next. At adoption, a feature list, a roadmap or an architecture document has
no A-file to go to: it stays where it is, or the setup grows to hold it. A small setup grows later: add the file from
its template and name it in the index.

Templates: [templates/AGENTS.md](templates/AGENTS.md), [templates/ACTIVE.md](templates/ACTIVE.md),
[templates/ABILITIES.md](templates/ABILITIES.md), [templates/AHEAD.md](templates/AHEAD.md),
[templates/ATLAS.md](templates/ATLAS.md), [templates/CLAUDE.md](templates/CLAUDE.md) (for Claude Code, which reads
`AGENTS.md` through it), [templates/CHANGELOG.md](templates/CHANGELOG.md), and under `templates/docs/` a plan, a
decision record and a research write-up.

## Adopt

Look before anything moves. Adoption takes two replies. The first surveys, shows the mapping and the planned moves
(steps 1, 2 and 4), offers the small setup (`AGENTS.md` and `ACTIVE.md`) or the full one, proposes the check and the
hook (step 6), and ends with the questions; it creates, moves and removes nothing and installs no hook. The second
applies, after the person has answered in a new message. A request to adopt the A-files, or to set the repository up,
is not that answer. A request that already gives every choice (the alignment for each area, and that you may go ahead
without waiting) is: then apply in the same reply, still showing the mapping first. The hook is a choice of its own
(the check is copied either way): install it only when the request or the answer says so, and otherwise end with it as
a question. Full alignment settles the instructions that name what moves: adapt them to the new home. A decision the
request does not settle (a bare name it cannot place) stays a question; nothing is guessed. A new repository, with no
tracking files yet, takes the same two replies: the first lists the files it would create from the templates for each
setup, asks which (small or full, above), and proposes the check and the hook.

The nine steps, the hook rules, the validation, the report and a worked example are in
[references/adopt.md](references/adopt.md): read it whole before step 1. They run `scripts/relink.py` for the moves
and `scripts/install_check.py`, which copies `scripts/check_tracking.py` and proposes `scripts/pre-commit` as the hook.

## Close out a piece of work

Work is unfinished while a defect or a required check stands in what was asked: fix it within the scope given, or stop
with the reason and the next step in Now, and report it as unfinished, never as done with follow-ups. Only the owner
accepts less. What the work found and will not do now is written down with its evidence where the work keeps its
record (by default the plan's Surprises), never in `AHEAD.md`. Show it to the owner before closing, or leave one
Pending line saying how many findings await him and where (method guide, section 5).

In the same commit as the last change of the work:

- `ACTIVE.md`: clear Now (every field stays, with "none" or "—"). A work section stays while its committed work is
  unfinished, the finished part shrunk to one line with its proof; it is removed when that work is done. With the
  desk clear, name the first item of AHEAD's Next up as the next new work. Never invent work.
- `ABILITIES.md`: when the ability itself is finished, it becomes `done` in its index row (the status lives there
  only), with **Evidence** linking the specification, tests or evaluation, and **Known limits** stated. While a part
  of it remains, it stays `in progress` and its entry gains the finished part's evidence. An old Status line follows.
- `AHEAD.md`: an item that ended moves to History; an item the owner made from a finding gets its **Entered** line.
- `ATLAS.md`, when a part was added, moved or removed.
- A decision record for any standing rule the work produced.
- With the projection to issues ([scripts/project_issues.py](scripts/project_issues.py)), align with them first ([references/issues.md](references/issues.md)).

## Promote an item

An item enters `AHEAD.md` on the owner's decision: propose it, and write the row, with its **Entered** line, only when
he asks or says yes. Items then move `open` → `approved` → `next` → `started`. On approval the ability gets its index
row in `ABILITIES.md`, with status `planned`, and its entry, and the item names it. When work on it starts, the item
goes to History as `started`, once, the ability becomes `in progress`, `ACTIVE.md` names the work, and a plan goes
into `docs/plans/` when the work spans sessions. Work the owner commits to for days or weeks gets a work section in
`ACTIVE.md`; if it has to wait it stays there, and nothing else starts until he says so. With no work section,
`ACTIVE.md` holds one current piece of work: work that is blocked moves to Pending or back to AHEAD, and it never
holds up unrelated work, which can then start.

## Sort a full AHEAD

For an `AHEAD.md` full of items the owner never chose. The owner starts it. No session starts it on its own. Propose
keep, join, do now or remove for every open item, all at once. The owner rules on the list; one commit applies it,
and kept items gain their **Entered** line. The steps: [references/owner-procedures.md](references/owner-procedures.md).

## Review AGENTS.md

For an `AGENTS.md` that exists. The owner starts it. No session starts it on its own. Propose keep, move or drop for
each passage, with evidence, by three questions: What could an agent get wrong before it finds the fuller source?
Which file owns this fact? What is the evidence for dropping it? A section another tool writes is not edited. The
owner rules on the list; one commit applies it. The steps: [references/owner-procedures.md](references/owner-procedures.md).

## Upgrade the installed check

A project keeps the check it was given at adoption. To bring it to this skill's release, run, from the project
root and this skill's base directory, `python3 "<skill-folder>/scripts/install_check.py" --root . --upgrade`.
It replaces `tools/check_tracking.py` only when the earlier check is committed
and unchanged since, so the earlier one stays in the project's history, and it
names both releases. It refuses, and changes nothing, when the check is not
committed as it stands, was changed by hand at this release, or comes from a
later release than the skill's. Hooks are left alone unless `--hook` is given.
Then run `python3 tools/check_tracking.py`: a newer check can report what the earlier one did not. Fix what it
reports, and commit the check with those fixes. Then offer the projection to issues once, as at adoption.

## Agent hooks

The plugin carries two agent hooks, in `hooks/` beside the skill, both run by
[scripts/afiles_hook.py](scripts/afiles_hook.py):

- at session start, a note: before the first edit, say where things stand in four short lines (Finished, Remaining,
  Blocked by, Next step), checked against git;
- at the end of a turn, the check's findings, each sent once per session as a note for the agent. It never asks the
  owner or stops the work: the agent aligns the files, or says in its handoff which it left and why.

Both act only where `ACTIVE.md` carries the hot-zone marker. The commit hook (references/adopt.md, step 6) stays: it is the check that holds
for everyone; the agent hooks are earlier feedback. With a specification method's plugin also installed, these two
come from here only.

Turning them on: Claude Code, with the plugin. Codex, install from the marketplace, then approve each hook once in
`/hooks` (an unapproved hook is skipped without a word). Kiro CLI, copy the skill folder to `~/.kiro/skills/a-files/`
and `hooks/kiro/a-files.json` to `~/.kiro/hooks/`, and trust the workspace; hooks run only on Kiro's V3 engine.
OpenCode, list the `hooks/opencode` folder of a full copy of the plugin in the `plugins` array of `opencode.json`, in
the project or globally (`opencode plugin add` fetches that folder alone, without the hook script).

## Fix what the check reports

`python3 tools/check_tracking.py` prints `path:line: ERROR CODE: message`; the commit hook runs it with `--staged`, on
what the commit holds, and notes an A-file whose changes are not staged. A clean run prints nothing. To see what it
inspected, add `--summary` (one closing line: the files and the number of problems) or `--format json` (the run as
data, with the registers it read); `--version` names the A-files version it belongs to. None of them writes a file or
changes the exit code.

| Code | Fix |
|---|---|
| `MISSING`, `NO_CONTRACT`, `NO_HOT_ZONE_END` | Create the file from its template, or restore one that held identifiers; add the contract line or the marker (`AGENTS.md` needs neither) |
| `UNREADABLE` | Save the file as UTF-8 text, or fix what stops it being read |
| `NOT_INDEXED` | Name the A-file in `AGENTS.md`'s index table |
| `INVALID_HOME`, `MISSING_HOME` | Name as the home the tracking file that was kept, and check that it exists |
| `HOT_ZONE_TOO_LONG` | Move detail below the hot zone and point to it; in `ACTIVE.md`, shorten the work section by its four rules |
| `UNPOINTED_SECTION` | Name the section in the hot zone's `Below:` line |
| `BROKEN_LINK`, `MISSING_PATH`, `BROKEN_SPEC` | Point the link or path at what exists, or remove it |
| `BLOCKER_WITHOUT_SOURCE` | Name what the blocker stops and its dated owner message, specification ID or path, or failing check by name; check that the source still holds |
| `MISSING_FIELD` | Add the field to ACTIVE's Now, with "none" when it is empty |
| `NO_MAP` | Add the map table to ATLAS's hot zone (Part, What it does, Works through, ...) |
| `BAD_ID`, `BAD_STATUS`, `BAD_KIND`, `DUPLICATE_ID`, `NO_ENTRY`, `NOT_IN_INDEX`, `NO_INDEX` | Make the index rows and the entries agree, with values from the lists; each identifier keeps one row |
| `STATUS_MISMATCH` | The row holds the status: drop the old entry's Status line, or set it to the row's |
| `REMOVED_ID` | Restore the identifier; retire or drop the item instead of deleting it. An item the owner had removed is named in History's line `Removed on the owner's word:` |
| `NO_ABILITY`, `UNKNOWN_ABILITY`, `UNKNOWN_ITEM` | Name an existing ability on the item; list only indexed items in Next up; in `ACTIVE.md`, name only identifiers the registers have |
| `ITEM_WITHOUT_DECISION` | A new AHEAD item has no `- **Entered:** <date>, <the owner's words>` line. If the owner asked for the item, add the line; if he did not, take the item out and propose it to him instead |

Never silence the check, and never delete an identifier to make it pass.

## Join a specification method

When the project also writes specifications (a guideline section `## Working from specifications`, or folders such as
`specs/`, `.kiro/specs/` or `openspec/`), join it as [references/pairing.md](references/pairing.md) says: name its
section in the hot zone of `AGENTS.md` where the file has one, add the two keep-in-step rows, map the specifications in `ATLAS.md`, and give
each ability the `Specs` line of the use cases or specifications that define it. Abilities are proposed from the use
case map or the specification folders, for the person to accept. Use cases already `Done` make their abilities `done`,
with the specifications as evidence; use cases in progress go into ACTIVE's Now. Joining twice changes nothing.
