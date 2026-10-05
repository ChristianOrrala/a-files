# The A-files

*Five files every coding agent reads first.*

Version 1.2.1, 2026-10-04

A way for a repository to keep its rules, its current work, its abilities, its
future and its map in five Markdown files at the root, so that any coding
agent (Claude Code, Codex, Gemini through Antigravity, Cursor, Copilot) and
any person starts every session from the same picture, and the picture stays
true.

## Contents

1. [Why](#1-why)
2. [The five files](#2-the-five-files)
3. [Hot zones and the warm-up](#3-hot-zones-and-the-warm-up)
4. [Keeping the files in step](#4-keeping-the-files-in-step)
5. [The life of an item](#5-the-life-of-an-item)
6. [Identifiers and states](#6-identifiers-and-states)
7. [The other homes](#7-the-other-homes)
8. [The check and the hook](#8-the-check-and-the-hook)
9. [Wiring each agent](#9-wiring-each-agent)
10. [Adopting the method](#10-adopting-the-method)
11. [Naming](#11-naming)
12. [Limits](#12-limits)
13. [Questions](#13-questions)
14. [Pairing with a specification method](#14-pairing-with-a-specification-method)

## 1. Why

Agents start every session knowing nothing about where the work stands. The
usual answer, one long instruction file plus a status note, fails in known
ways, as the research behind the method found:

- **Long instruction files cost more than they help.** Instruction following
  drops as instructions multiply, and earlier lines are followed better.
- **Status notes go stale or bloat,** and an agent rewrites Markdown readily:
  a finished feature disappears, a wish list grows.
- **Rules written as prose are skipped** by some models some of the time;
  rules enforced by a script hold.

The method answers with five short, single-purpose files whose top part is
read at every start, a rule to update them with the work, stable identifiers
that are never removed, and a check that refuses a commit that breaks their
shape.

## 2. The five files

| File | Job | Never holds |
|---|---|---|
| `AGENTS.md` | The rules, the warm-up, the index of every file an agent needs, the keep-in-step rule | State, plans, history |
| `ACTIVE.md` | The work in progress, and what must be resolved before new work starts: progress, the next step in this work, pending and deferred items, debt, blockers | Ideas, future abilities |
| `ABILITIES.md` | Every ability of the product, planned, in progress, done or retired; one entry each, never deleted | The agent's own abilities; ideas not approved |
| `AHEAD.md` | Everything not started: the next-up queue, milestones, ideas, research, spikes and proposals, each pointing to its full write-up | Work in progress |
| `ATLAS.md` | The architecture map: each part of the repository, what it does, the files it works through, what it depends on, what checks it | A full file index |

All five start with A so they are recognized and sorted together as one set.
The names were chosen against the meanings agent tools already give to
others: "atlas" is the common name for a codebase map, which is exactly this
file's job; `ABILITIES.md` says in its first line that it is not about the
agent's own abilities, a reading the word invites.

A repository keeps one map: `ATLAS.md` replaces an `ARCHITECTURE.md`.

## 3. Hot zones and the warm-up

**Hot zone.** The top of each file, ended by a line that says exactly:

```text
<!-- hot zone ends -->
```

| File | Hot zone cap | Holds in its hot zone |
|---|---|---|
| `AGENTS.md` | 100 lines (file under 200) | Purpose, warm-up, index, keep in step, commands, rules |
| `ACTIVE.md` | 60 lines | Now (fixed fields), Pending, Debt, Next new work |
| `ABILITIES.md` | 100 lines | Contract, status list, index |
| `AHEAD.md` | 100 lines | Next up, milestones, index of open items |
| `ATLAS.md` | 100 lines | The map table, the flow |

Each A-file opens with its title and a one-line contract in a quotation block
(`> ...`). Everything below a hot zone is reached only through a pointer in
it: the hot zone ends with a line such as `Below: Items, History, How to
maintain this file.`

**Warm-up.** At every session start an agent reads, in this order:

1. the hot zone of `AGENTS.md`;
2. the hot zones of `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md` and `ATLAS.md`;
3. `git log --oneline -15`.

That is at most about 400 lines, the same picture for every agent. Anything
else is opened when the task needs it.

`AGENTS.md` names the other files by path and never imports them (`@file`):
an import loads the whole file in every session.

## 4. Keeping the files in step

The rule in `AGENTS.md`: in the same commit as the work, an agent updates

| When it | It updates |
|---|---|
| Starts, finishes, defers or drops work | `ACTIVE.md` |
| Changes an ability's state | `ABILITIES.md` |
| Proposes, approves, schedules or drops an item, or finishes a spike | `AHEAD.md`, and `ABILITIES.md` when an item is approved |
| Adds, moves, renames or removes a part of the repository | `ATLAS.md` |
| Makes or records a decision or a standing rule | `docs/decisions/` |

Two more rules:

- **One editor.** Only the main session edits the A-files. Parallel workers
  (subagents, other branches) report to it; shared status files are where
  parallel work collides.
- **One home per fact.** A standing rule is a decision record, never only a
  line in `ACTIVE.md`. A limit of one ability is in its entry, never repeated
  as debt.

## 5. The life of an item

```text
idea, research or spike ─► AHEAD (open; a write-up in docs/research/ when it is long)
approved                ─► AHEAD (approved) + an ABILITIES entry with status planned
scheduled               ─► AHEAD (next), in the Next up queue
started                 ─► ACTIVE current work; ABILITIES in progress; AHEAD (started), row moved to History;
                           a plan in docs/plans/ when the work spans sessions
done                    ─► ABILITIES done, with evidence; gone from ACTIVE; CHANGELOG at release
dropped                 ─► AHEAD (dropped), row moved to History, the entry says why
```

**Sorting what is not done.** If it blocks new work or belongs to the current
work, it is in `ACTIVE.md`. If it can wait, it is in `AHEAD.md`. Debt that
blocks or will bite the next work is in `ACTIVE.md`; debt that can wait is an
idea in `AHEAD.md`.

**New work starts only from an empty ACTIVE.** When Now has no current work,
`ACTIVE.md` names the first item of AHEAD's Next up. It never invents new work.

## 6. Identifiers and states

| Identifier | Form | Rules |
|---|---|---|
| Ability | `AB-001` | Three digits; never reused, never removed |
| AHEAD item | `AH-001` | Same |

Not `A-001`: projects that write use case specifications label alternative
flows `A1`, `A2`.

| File | Field | Values |
|---|---|---|
| `ABILITIES.md` | Status | `planned` (approved, not built), `in progress`, `done` (built, checked, evidence linked), `retired` (removed; the reason stays) |
| `ABILITIES.md` | Specs (optional) | Use case identifiers (`UC-003`) or relative links to the specifications that define the ability; the check verifies that each link points at a file |
| `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md`, `ATLAS.md` | Home (optional, in the hot zone) | The tracking file kept as the home at adoption (never an A-file or a guideline file); the check verifies that it exists and no longer asks for the A-file's own fields, index, entries or map |
| `AHEAD.md` | Kind | `idea`, `research`, `spike`, `proposal` |
| `AHEAD.md` | State | `open`, `approved`, `next`, `started`, `dropped` |

An AHEAD item that is `approved`, `next` or `started` names its ability. An
ability's status is written twice, in the index row and in the entry, and the
two agree.

## 7. The other homes

| Home | Holds | Template |
|---|---|---|
| `docs/plans/YYYY-MM-DD-subject.md` | One plan per piece of work that spans sessions: goal, steps, progress log, decisions, surprises, how to resume. A fresh session can continue from the plan alone | `templates/docs/plans/` |
| `docs/decisions/NNNN-subject.md` | Decisions and standing rules, numbered, never reused; superseded records stay | `templates/docs/decisions/` |
| `docs/research/NN-subject.md` | Research and spike write-ups: question, what was done, findings with sources, answer | `templates/docs/research/` |
| `CHANGELOG.md` | Notable changes per release, from the first release (Keep a Changelog) | `templates/CHANGELOG.md` |

`ACTIVE.md` links the active plan; `AHEAD.md` links write-ups; decisions link
the research behind them.

## 8. The check and the hook

`tools/check_tracking.py` (Python 3.9+, standard library only) checks the
shape of the five files, not their truth. It refuses:

- a missing A-file, a missing contract line, a missing end of hot zone, or a
  hot zone over its cap; an `AGENTS.md` over 200 lines or not naming every
  A-file in its first 100 lines;
- a section below a hot zone that the hot zone does not name;
- a link in a hot zone, or a path in the atlas map, that points at nothing;
- an `ACTIVE.md` without one of its fields;
- an identifier in the wrong form, a status, kind or state outside the lists,
  a duplicate, an index row without its entry or the reverse, a status that
  differs between index and entry;
- a link or backticked path in an ability's `Specs` line that does not point
  at a file, and a `Home` that is not a file in the project or that names an
  A-file or a guideline file;
- an identifier that was in the last commit and is gone;
- an AHEAD item that is approved, next or started without an ability, or
  naming one that does not exist.

Templates inside fenced code blocks are ignored, so each file can carry its own
template. Output: `path:line: ERROR CODE: message`; exit 0 clean, 1 problems,
2 usage. `--no-git` skips the comparison with the last commit.

**The hook.** `scripts/pre-commit` runs the check before every commit. Once
the person agrees to it (section 10), install it as `.githooks/pre-commit` in
the repository and enable it once per clone:

```bash
git config core.hooksPath .githooks
```

The hook checks the working tree, so a file left unstaged still counts.

## 9. Wiring each agent

| Agent | Reads `AGENTS.md` | What to add |
|---|---|---|
| Codex | Natively (root, then folders down to the working directory) | Nothing |
| Antigravity CLI (Gemini) | Natively, or `GEMINI.md` | Nothing |
| Cursor, Copilot, Windsurf | Natively | Nothing |
| Claude Code | When no `CLAUDE.md` exists | A `CLAUDE.md` holding `@AGENTS.md` (template provided) |
| Aider | When configured | `read: AGENTS.md` in `.aider.conf.yml` |

Claude Code: with a `CLAUDE.md` present, it ignores `AGENTS.md` files in
subfolders unless a `CLAUDE.md` beside each imports it, or the user setting
that loads both kinds is on.

Session tooling outside the repository (a personal assistant that opens each
session, a project scaffold) should start sessions with the warm-up and create
new repositories from `templates/`.

## 10. Adopting the method

**A new repository.** It takes the same two replies as any adoption (below):
the first lists the files it would create from `templates/` and proposes the
check and the hook, creating nothing; the second, after the person answers,
does the steps.

1. Copy `templates/` into the repository root (keep `docs/` as it is).
2. Fill `AGENTS.md`: purpose, commands, rules, any extra row in the index.
3. Fill `ATLAS.md` with the parts that exist; `ABILITIES.md` with what the
   product can do; `AHEAD.md` with what is planned; `ACTIVE.md` with the
   current work.
4. Copy `scripts/check_tracking.py` to `tools/`. Install the hook only if the
   person said yes to it, or the request already says to install it: with no
   commit hook yet, copy `scripts/pre-commit` to `.githooks/pre-commit` and run
   `git config core.hooksPath .githooks`; with one (a hooks path, a file in
   `.git/hooks/`, a hook manager), add the line that runs the check to it
   instead of replacing it.
5. Run `python3 tools/check_tracking.py` until it is clean; commit.

**A repository with its own tracking files.** Use the first reply to survey
the repository, show the mapping and proposed moves, propose the check and
hook, and end with questions, without creating, moving or removing anything
or installing a hook; apply only in a second reply after the person answers
in a new message. Asking to adopt the method or set up the repository does
not supply those answers. If the request already specifies the alignment
for every area and explicitly says to go ahead without waiting, show the
mapping first and apply in that same reply.
The hook is a choice of its own (the check is copied either way): it is
installed only when the request or the answer says so. Full alignment
settles the instructions that name what moves: they are adapted to the new
home. A decision the request does not settle (a bare name it cannot place)
stays a question; nothing is guessed.

First show what exists and where it would go:

| Old content | New home |
|---|---|
| A status or board note | `ACTIVE.md` Now, Pending and Debt |
| A feature list | `ABILITIES.md`, one entry per feature, with a new `AB-` identifier |
| A roadmap, backlog or idea list | `AHEAD.md`: milestones, Next up, items |
| An architecture or layout document | `ATLAS.md` (keep a design rationale as a decision record) |
| Standing rules found in a status note | `docs/decisions/` |
| Decision, plan and research notes in other folders | `docs/decisions/`, `docs/plans/`, `docs/research/` |
| Finished items kept as history | Delete; git keeps them |

Then ask the person, once for everything or area by area:

| Choice | What happens |
|---|---|
| **Full alignment** | Everything goes to the root and `docs/`. An old file's content merges into its A-file and the old file is removed; notes in other folders move into `docs/` with `git mv` and take the naming rules of section 11 |
| **Keep it as the home** | The old file or folder stays the home. The A-file keeps its title, contract line and hot zone, and its hot zone carries `- **Home:** <the kept file>`: the check verifies that the file exists and no longer asks for the A-file's own fields, index or entries. The keep-in-step rule names the kept file. The warm-up reads it too, and the check cannot verify its shape |
| **Leave it out** | Files that are not tracking (notes, a design rationale) stay as they are |

Nothing moves before the person agrees.

**Specifications are never moved by this method.** Whatever method wrote
them (use cases under `docs/`, Spec Kit's `specs/`, Kiro's `.kiro/specs/`,
OpenSpec's `openspec/`, loose documents), the A-files link them where they
are: a `Specs` line per ability (section 6), an ATLAS row and an index row in
`AGENTS.md` for their folder. Moving them into another layout is the
specification method's decision; some tools read only their own folder.

**Every move keeps its references.** `scripts/relink.py` runs in three
steps. `plan` lists every reference to each old path (links, `@file`
imports, paths in settings, CI, hooks and scripts, paths in backticks) and
flags a bare name in prose for a decision. `apply` runs the moves with
`git mv` and rewrites the exact references. A folder whose new path is an
existing folder moves into it file by file; a file whose new path exists is
refused, so its content is merged and the old file removed first. `verify` fails
while any link is broken or any old path is still named.
Write the adoption record after `apply` and before the final `verify`, keeping
its old names as history, and pass `--keep docs/decisions/NNNN-adopt-the-a-files.md`
to that verification so its mentions are listed as `KEPT`, not problems;
the repeatable `--keep FILE` option also protects records from `apply` rewrites.

Agent instructions get the same treatment: every instruction file
(`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/`,
`.github/copilot-instructions.md`, `.kiro/steering/`, `.windsurf/rules`,
`.clinerules`) is read. Under full alignment, an instruction that names a
moved file is adapted to the new home unless the person said otherwise; in
other cases (an area kept as the home, an instruction that describes the old
way of working), it is removed, adapted or kept, as the person decides.
References from outside the repository (wikis, issues, other repositories)
cannot be checked; the report says so.

Record the adoption as a decision (template
`templates/docs/decisions/NNNN-subject.md`): what moved, what was kept, what
was left out.

## 11. Naming

The method is called **the A-files**: the five files' names all start with A,
and the name echoes The X-Files so it sticks. In a sentence: "this repository
uses the A-files". The subtitle, *five files every coding agent reads first*,
says what it is to someone who has not met it.

| What | Convention | Example |
|---|---|---|
| Files at the root that people and tools look for | Uppercase name, `.md` | `AGENTS.md`, `ACTIVE.md`, `CHANGELOG.md` |
| Files under `docs/` | Lowercase, words joined by hyphens | `docs/research/01-sms-providers.md` |
| Decision records | Four digits, never reused, then the subject | `0007-retire-paper-vouchers.md` |
| Plans | The date the work started, then the subject | `2026-10-01-cancel-a-booking.md` |
| Research and spikes | Two digits, then the subject | `01-sms-providers.md` |
| Dates | ISO 8601 | `2026-10-03` |
| Commit subjects | Area, colon, what changed | `booking: refuse a ninth repair on a full day` |
| Branches | Kind, slash, subject: `feat`, `fix`, `docs`, `chore` | `feat/cancel-a-booking` |
| Release tags | `v` and a semantic version | `v1.2.0` |

## 12. Limits

- **The check verifies shape, not truth.** It cannot tell that `ACTIVE.md`
  describes yesterday's work; only the keep-in-step rule and review do.
- **Models vary from run to run.** No instruction is followed every time; the
  check and the hook are the floor that holds regardless.
- **The warm-up costs tokens.** About 400 lines per session at the caps;
  that is the price of a shared picture, and the caps keep it from growing.
- **One editor at a time.** The method does not merge parallel edits to the
  A-files; it avoids them.

## 13. Questions

**Why not an issue tracker?** Use one when a team or a public remote exists;
then `AHEAD.md` items can link their issues. The A-files work offline, travel
with the code, and are read by every agent without credentials.

**Why Markdown and not JSON?** People review Markdown. JSON resists careless
rewriting better; the check gives Markdown the same protection by refusing
removed identifiers and broken shape.

**What if the ABILITIES index outgrows its hot zone?** Keep the planned and
in-progress rows and one summary row per area in the hot zone, and move the
full index below it; the check accepts an identifier in any index table of the
file.

**Can a file stay empty?** Yes: an empty section says "None." or "Nothing
scheduled", and `ACTIVE.md` keeps every field with "none" or "—".

## 14. Pairing with a specification method

A project may also write down what its system does with a spec-driven method.
The two stay separate and are joined by a few rules, kept in the skill's
pairing reference:

- an ability names the specifications that define it in a `Specs` line;
- the current work in `ACTIVE.md` names the use cases or abilities being
  worked on, and the next new work comes from AHEAD's Next up;
- whichever method is set up second joins the other: it names its section in
  the hot zone of `AGENTS.md`, adds two rows to the keep-in-step rule, and
  maps the specifications in `ATLAS.md`.
