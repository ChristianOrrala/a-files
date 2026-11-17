---
name: a-files
description: >-
  Adopts and keeps the A-files, five Markdown files at a repository's root that every coding agent
  reads first: AGENTS.md (rules, warm-up, index), ACTIVE.md (the work in progress), ABILITIES.md
  (what the product can do), AHEAD.md (everything not started) and ATLAS.md (the architecture map),
  each with a hot zone read at session start, a keep-in-step rule and a check that reports at commit
  time what breaks their shape, never refusing the commit. Maps existing tracking files (a board, a feature list, a roadmap, notes),
  asks whether to move them into the A-files or keep them, and checks every link, import and
  instruction that names what moves. Use when the user wants to adopt the A-files, set up or clean
  up the files agents read at session start, close out a piece of work, promote or schedule an item,
  fix what the tracking check reports, or link abilities to the specifications of a spec-driven
  method in the same project. Not for writing specifications and not for an issue tracker.
---

# Keeping the A-files

Five files at the root give every agent and every person the same picture at
the start of a session: the rules, the work in progress, what the product can
do, what is ahead, and the map. They serve one owner directing agents, not a
team tracker. This skill adopts them in a repository and keeps them true. The daily rules (the warm-up, keeping the files in step)
live in the project's `AGENTS.md`, which every tool reads anyway. Before the first change,
the warm-up states Finished, Remaining, Blocked by and Next step in four short lines,
using "nothing" for an empty line and checking `git log` and `git status`.

The whole method, with its reasons: [references/method.md](references/method.md).

## The five files

| File | Holds | Hot zone cap |
|---|---|---|
| `AGENTS.md` | Rules, warm-up, the index of every file an agent needs, keep in step | 100 lines; the file under 200 |
| `ACTIVE.md` | The current piece of work, what is pending in it and what blocks it | 60 lines |
| `ABILITIES.md` | Every ability of the product, planned to retired, never deleted | 100 lines |
| `AHEAD.md` | Everything not started: Next up, milestones, ideas, research, proposals | 100 lines |
| `ATLAS.md` | The map: parts, the files they work through, dependencies, checks | 100 lines |

Each opens with its title and a one-line contract (`> ...`). Its hot zone
ends with the line `<!-- hot zone ends -->`, and everything below is named in
the hot zone. Identifiers `AB-001` and `AH-001` are never reused or removed.
An ability's status is written once, in its index row; done abilities may
move to an index table below the hot zone.

**Small or full.** The small setup keeps `AGENTS.md` and `ACTIVE.md`; the full
one adds the other three. The check always expects `ACTIVE.md`, and another
A-file once the index of `AGENTS.md` lists it, the file exists, or it held
identifiers in the last commit. In the small setup, remove the other three
files' rows from the index of `AGENTS.md`, and their mentions from the
warm-up and keep in step. Without `AHEAD.md`, blocked work stays in ACTIVE's
Pending and Next new work names what the owner chose next. At adoption, a
feature list, a roadmap or an architecture document has no A-file to go to:
it stays where it is, or the setup grows to hold it. A small setup grows later: add the file from its template and name
it in the index.

Templates: [templates/AGENTS.md](templates/AGENTS.md), [templates/ACTIVE.md](templates/ACTIVE.md),
[templates/ABILITIES.md](templates/ABILITIES.md), [templates/AHEAD.md](templates/AHEAD.md),
[templates/ATLAS.md](templates/ATLAS.md), [templates/CLAUDE.md](templates/CLAUDE.md) (for Claude
Code, which reads `AGENTS.md` through it), [templates/CHANGELOG.md](templates/CHANGELOG.md), and
under `templates/docs/` a plan, a decision record and a research write-up.

## Adopt

Look before anything moves. Adoption takes two replies. The first surveys,
shows the mapping and the planned moves (steps 1, 2 and 4), offers the small
setup (`AGENTS.md` and `ACTIVE.md`) or the full one, proposes the
check and the hook (step 6), and ends with the questions; it creates, moves
and removes nothing and installs no hook. The second applies, after the
person has answered in a new message. A request to adopt the A-files, or to
set the repository up, is not that answer. A request that already gives every
choice (the alignment for each area, and that you may go ahead without
waiting) is: then apply in the same reply, still showing the mapping first.
The hook is a choice of its own (the check is copied either way): install
it only when the request or the answer says so, and otherwise end with it as
a question. Full alignment settles the instructions that name what moves:
adapt them to the new home. A decision the request does not settle (a bare
name it cannot place) stays a question; nothing is guessed. A new
repository, with no tracking files yet, takes the same two replies: the
first lists the files it would create from the templates for each setup,
asks which (small or full, above), and proposes the check and the hook.

1. **Survey.** List the tracking files that exist (status notes, boards,
   feature lists, roadmaps, TODO lists, architecture documents, notes of
   decisions, plans or research in other folders), every agent instruction
   file, and any specifications. Show a table: each old file, what it holds,
   and the A-file or `docs/` folder it would go to (the mapping table in
   section 10 of the method guide).
2. **Ask: full alignment or keep.** Once for everything, or area by area:

   | Choice | What happens |
   |---|---|
   | Full alignment | Everything goes to the root and `docs/`: content merges into the A-files, notes move into `docs/decisions/`, `docs/plans/`, `docs/research/` |
   | Keep it as the home | The old file stays the home: the A-file's hot zone carries `- **Home:** BOARD.md` (the kept file), the check verifies that file instead of the A-file's own fields or register, and keep-in-step names it. Abilities kept elsewhere take no part in the pairing with a specification method |
   | Leave it out | Files that are not tracking stay as they are |

3. **Specifications stay where they are.** Never move them. Link them: a
   `Specs` line on each ability they define, a row in ATLAS and in the
   `AGENTS.md` index for their folder. If the person wants them in another
   layout, that is the specification method's decision: say so and hand over.
4. **Plan the moves.** Run
   `python3 scripts/relink.py plan --move OLD NEW [--move OLD NEW ...]`.
   The script is in this skill's folder; use the base directory shown when the
   skill was loaded. Show every reference it lists, every bare name it flags
   for a decision, and every line marked `[instruction]` with a proposal:
   remove it, adapt it to the new home, or keep it; under full alignment, the
   proposal is to adapt it. Show the files that would be created from the
   templates; never overwrite one, merge into it. Get a yes.
5. **Apply.** Read each template in the skill folder and write the project
   file from it, never by running a copy command. Fill the files from the
   repository, marking what you could not establish as a question. Merge the
   old content into the A-files and remove each merged old file. Then
   `python3 scripts/relink.py apply --move OLD NEW ...` moves what still has
   to move and rewrites the exact references. Settle each decision as the
   person chose, then verify until it reports no problem. Once the adoption
   record exists, use `python3 scripts/relink.py verify --move OLD NEW ... --keep docs/decisions/NNNN-adopt-the-a-files.md`.
6. **Install the check.** Before running the installer, look at what runs
   today: `git config --local --get core.hooksPath`, `git config --get core.hooksPath`, an existing
   `.githooks/pre-commit` or `.git/hooks/pre-commit`, a hook manager (husky,
   pre-commit, lefthook). Ask one question first: the check alone or the check and the hook?
   Honor a choice already supplied in the request or adoption answer.
   Then run [scripts/install_check.py](scripts/install_check.py) once in place
   from this skill's base directory, from the project root:
   `python3 "<skill-folder>/scripts/install_check.py" --root .`, adding `--hook`
   only when the person chose the shell hook. The script copies
   [scripts/check_tracking.py](scripts/check_tracking.py) into `tools/check_tracking.py`
   only when absent. An existing check is left untouched, with a report of
   whether it matches or differs from the plugin's. A later yes to the hook
   is a re-run with `--hook`; the existing check is still left untouched.
   Every shell hook installation or reporting-line insertion goes through
   this script; never write or copy a hook by hand or run an agent copy command.
   Never replace a hook: with none, propose
   [scripts/pre-commit](scripts/pre-commit) as `.githooks/pre-commit` and
   `git config core.hooksPath .githooks`; with one, propose the one line
   `python3 tools/check_tracking.py --staged || true`, placed before the
   hook's first command: after the shebang when there is one, at the top when
   there is none (the check reads what is staged, as the commit will hold
   it). The added line never decides the hook's result unless a strict check
   is asked for: the check only reports and exits 0, so as the hook's last
   line it would decide the result and drop the hook's own refusal. For a
   strict check, propose `python3 tools/check_tracking.py --staged --strict || exit 1`,
   placed the same way. The `|| true` and `|| exit 1` lines are for a shell
   hook. Some hook managers, such as the pre-commit framework, run a step
   without a shell, so propose a step of its own running
   `python3 tools/check_tracking.py --staged`, which reports and exits 0, or
   `python3 tools/check_tracking.py --staged --strict` to refuse; never
   `|| true` in a step. The step takes no file names, runs on every commit,
   one that only deletes files included, and shows its output, so the
   report is seen. For example, the pre-commit framework, in
   `.pre-commit-config.yaml`: a `repo: local` hook with
   `entry: python3 tools/check_tracking.py --staged`, `language: system`,
   `pass_filenames: false`, `always_run: true` and `verbose: true`; for the
   strict check, `entry: python3 tools/check_tracking.py --staged --strict`.
   Add `--hook` to the install command only for an agreed shell hook: the
   script installs the shipped hook and sets `core.hooksPath` when none
   exists, or inserts the reporting line first in an existing shell hook
   that does not already run the check.
   It never replaces a hook; it leaves an existing hook's mode and commands
   intact. Hook managers and non-shell hooks need the separate step above;
   the script stops rather than editing them. With no local hooks path but
   a global or system one, `--hook` refuses before any change: that folder
   is shared by other repositories, and the owner must choose where the hook
   goes. Without `--hook`, the check can still be installed.
   Installing reads this plugin's folder; the tool's permission mode may
   ask for that access. On any refused or failed step, stop and report the
   command, what is installed and what is missing; commit nothing half-written.
   Resolve the reported access or failure before resuming.
   Hooks change how every commit
   behaves, so show the change and install it only after a yes that names it:
   the person's answer, or a request that already says to install the hook.
   Run `python3 tools/check_tracking.py` until it prints nothing.
7. **Join a specification method** when the project has one (below).
8. **Record the adoption** as `docs/decisions/NNNN-adopt-the-a-files.md` from
   the decision template after `apply` and before the final `verify`: what
   moved, what was kept, what was left out. Keep the old names as written:
   this is the record of the move. Run the final `verify` with `--keep` as
   shown in step 5.
9. Show the hot zones before committing.

## Close out a piece of work

In the same commit as the last change of the work:

- `ACTIVE.md`: clear Now (every field stays, with "none" or "—") and name
  the first item of AHEAD's Next up as the next new work. Never invent work.
- `ABILITIES.md`: the ability becomes `done` in its index row (the status
  lives there only; its entry gains **Evidence** linking the specification,
  tests or evaluation, and **Known limits** stated). An older entry that still
  carries a Status line follows the row, or loses the line.
- `AHEAD.md`: an item that ended moves to History.
- `ATLAS.md`, when a part was added, moved or removed.
- A decision record for any standing rule the work produced.

## Promote an item

Items in `AHEAD.md` move `open` → `approved` → `next` → `started`. On
approval the ability gets its index row in `ABILITIES.md`, with status
`planned`, and its entry, and the item names it. When work starts, the item goes to History as
`started`, the ability becomes `in progress`, `ACTIVE.md` names the work, and
a plan goes into `docs/plans/` when the work spans sessions. `ACTIVE.md` holds
one current piece of work: work that is blocked moves to Pending or back to
AHEAD, and it never holds up unrelated work, which can then start.

## Upgrade the installed check

A project keeps the check it was given at adoption. To bring it to this
skill's release, run, from the project root and this skill's base directory,
`python3 "<skill-folder>/scripts/install_check.py" --root . --upgrade`.
It replaces `tools/check_tracking.py` only when the earlier check is committed
and unchanged since, so the earlier one stays in the project's history, and it
names both releases. It refuses, and changes nothing, when the check is not
committed as it stands, was changed by hand at this release, or comes from a
later release than the skill's. Hooks are left alone unless `--hook` is given.
Then run `python3 tools/check_tracking.py`: a newer check can report what the
earlier one did not. Fix what it reports, and commit the check with those fixes.

## Agent hooks

The plugin carries two agent hooks, in `hooks/` beside the skill, both run by
[scripts/afiles_hook.py](scripts/afiles_hook.py):

- at session start, a note: before the first edit, say where things stand in
  four short lines (Finished, Remaining, Blocked by, Next step), checked
  against git;
- at the end of a turn, the check's findings, each sent once per session as a
  note for the agent. It never asks the owner or stops the work: the agent
  aligns the files or lists the findings in its handoff.

Both act only where `ACTIVE.md` carries the hot-zone marker. The commit hook above stays: it is the check that
holds for everyone; the agent hooks are earlier feedback. With a
specification method's plugin also installed, these two come from here only.

Turning them on: Claude Code, with the plugin. Codex, install from the
marketplace, then approve each hook once in `/hooks` (an unapproved hook is
skipped without a word). Kiro CLI, copy the skill folder to
`~/.kiro/skills/a-files/` and `hooks/kiro/a-files.json` to `~/.kiro/hooks/`,
and trust the workspace; hooks run only on Kiro's V3 engine. OpenCode, list the `hooks/opencode` folder of a full copy of the plugin in
the `plugins` array of `opencode.json`, in the project or globally (`opencode plugin add` fetches that folder alone,
without the hook script).

## Fix what the check reports

`python3 tools/check_tracking.py` prints `path:line: ERROR CODE: message`; the
commit hook runs it with `--staged`, on what the commit holds, and notes an
A-file whose changes are not staged. A clean run prints nothing. To see what
it inspected, add `--summary` (one closing line: the files and the number of
problems) or `--format json` (the run as data, with the registers it read);
`--version` names the A-files version it belongs to. None of them writes a
file or changes the exit code.

| Code | Fix |
|---|---|
| `MISSING`, `NO_CONTRACT`, `NO_HOT_ZONE_END` | Create the file from its template, or restore one that held identifiers; add the contract line or the marker |
| `HOT_ZONE_TOO_LONG`, `AGENTS_TOO_LONG` | Move detail below the hot zone and point to it; keep `AGENTS.md` to rules and pointers |
| `UNPOINTED_SECTION` | Name the section in the hot zone's `Below:` line |
| `BROKEN_LINK`, `MISSING_PATH`, `BROKEN_SPEC` | Point the link or path at what exists, or remove it |
| `BLOCKER_WITHOUT_SOURCE` | Name what the blocker stops and its dated owner message, specification ID or path, or failing check by name; check that the source still holds |
| `MISSING_FIELD` | Add the field to ACTIVE's Now, with "none" when it is empty |
| `BAD_ID`, `BAD_STATUS`, `BAD_KIND`, `DUPLICATE_ID`, `NO_ENTRY`, `NOT_IN_INDEX`, `NO_INDEX` | Make the index rows and the entries agree, with values from the lists; each identifier keeps one row |
| `STATUS_MISMATCH` | The row holds the status: drop the old entry's Status line, or set it to the row's |
| `REMOVED_ID` | Restore the identifier; retire or drop the item instead of deleting it |
| `NO_ABILITY`, `UNKNOWN_ABILITY`, `UNKNOWN_ITEM` | Name an existing ability on the item; list only indexed items in Next up |

Never silence the check, and never delete an identifier to make it pass.

## Join a specification method

When the project also writes specifications (a guideline section
`## Working from specifications`, or folders such as `specs/`, `.kiro/specs/`
or `openspec/`), join it as [references/pairing.md](references/pairing.md)
says: name its section in the hot zone of `AGENTS.md`, add the two
keep-in-step rows, map the specifications in `ATLAS.md`, and give each
ability the `Specs` line of the use cases or specifications that define it.
Abilities are proposed from the use case map or the specification folders,
for the person to accept. Use cases already `Done` make their abilities
`done`, with the specifications as evidence; use cases in progress go into
ACTIVE's Now. Joining twice changes nothing.

## Validation

- `python3 tools/check_tracking.py` prints nothing.
- `python3 scripts/relink.py verify --move ...` reports no problem for the
  moves made.
- No file was overwritten; every old file was moved, merged, kept or left out
  as the person chose, and the decision record says which.
- No specification was moved.
- The hot zones were shown before the commit.

## Report

1. What was found and where each piece went: the mapping table, with the
   choice taken.
2. The files created, merged, moved and removed, and the references
   rewritten.
3. The instructions removed, adapted or kept.
4. Questions left for the person: everything marked as not established.
5. The check's result, and whether the hook is enabled.

## Worked example

A repository with `BOARD.md`, `FEATURES.md`, a `CLAUDE.md` that says "Read
BOARD.md at session start", and a README linking both files.

```text
Old file       Holds                  Goes to
BOARD.md       current tasks          ACTIVE.md, Now and Pending
FEATURES.md    seven features         ABILITIES.md, AB-001 to AB-007
CLAUDE.md      the board instruction  adapted: "@AGENTS.md"; the warm-up reads ACTIVE.md
```

The person chooses full alignment. The A-files are created from the
templates, the board and the features are merged into them, and the two old
files are removed. `relink.py apply --move BOARD.md ACTIVE.md --move
FEATURES.md ABILITIES.md` then rewrites the README's two links; the
instruction in `CLAUDE.md` is adapted as agreed; `verify` reports no problem
and the check prints nothing.
