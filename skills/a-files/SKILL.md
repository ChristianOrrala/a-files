---
name: a-files
description: >-
  Adopts and keeps the A-files, five Markdown files at a repository's root that every coding agent
  reads first: AGENTS.md (rules, warm-up, index), ACTIVE.md (the work in progress), ABILITIES.md
  (what the product can do), AHEAD.md (everything not started) and ATLAS.md (the architecture map),
  each with a hot zone read at session start, a keep-in-step rule and a check that refuses a commit
  breaking their shape. Maps existing tracking files (a board, a feature list, a roadmap, notes),
  asks whether to move them into the A-files or keep them, and checks every link, import and
  instruction that names what moves. Use when the user wants to adopt the A-files, set up or clean
  up the files agents read at session start, close out a piece of work, promote or schedule an item,
  fix what the tracking check reports, or link abilities to the specifications of a spec-driven
  method in the same project. Not for writing specifications and not for an issue tracker.
---

# Keeping the A-files

Five files at the root give every agent and every person the same picture at
the start of a session: the rules, the work in progress, what the product can
do, what is ahead, and the map. This skill adopts them in a repository and
keeps them true. The daily rules (the warm-up, keeping the files in step)
live in the project's `AGENTS.md`, which every tool reads anyway.

The whole method, with its reasons: [references/method.md](references/method.md).

## The five files

| File | Holds | Hot zone cap |
|---|---|---|
| `AGENTS.md` | Rules, warm-up, the index of every file an agent needs, keep in step | 100 lines; the file under 200 |
| `ACTIVE.md` | The work in progress and what blocks new work | 60 lines |
| `ABILITIES.md` | Every ability of the product, planned to retired, never deleted | 100 lines |
| `AHEAD.md` | Everything not started: Next up, milestones, ideas, research, proposals | 100 lines |
| `ATLAS.md` | The map: parts, the files they work through, dependencies, checks | 100 lines |

Each opens with its title and a one-line contract (`> ...`). Its hot zone
ends with the line `<!-- hot zone ends -->`, and everything below is named in
the hot zone. Identifiers `AB-001` and `AH-001` are never reused or removed.

Templates: [templates/AGENTS.md](templates/AGENTS.md), [templates/ACTIVE.md](templates/ACTIVE.md),
[templates/ABILITIES.md](templates/ABILITIES.md), [templates/AHEAD.md](templates/AHEAD.md),
[templates/ATLAS.md](templates/ATLAS.md), [templates/CLAUDE.md](templates/CLAUDE.md) (for Claude
Code, which reads `AGENTS.md` through it), [templates/CHANGELOG.md](templates/CHANGELOG.md), and
under `templates/docs/` a plan, a decision record and a research write-up.

## Adopt

Look before anything moves. Adoption takes two replies. The first surveys,
shows the mapping and the planned moves (steps 1, 2 and 4), proposes the
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
first lists the files it would create from the templates and proposes the
check and the hook.

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
5. **Apply.** Create the files from the templates and fill them from the
   repository, marking what you could not establish as a question. Merge the
   old content into the A-files and remove each merged old file. Then
   `python3 scripts/relink.py apply --move OLD NEW ...` moves what still has
   to move and rewrites the exact references. Settle each decision as the
   person chose, then verify until it reports no problem. Once the adoption
   record exists, use `python3 scripts/relink.py verify --move OLD NEW ... --keep docs/decisions/NNNN-adopt-the-a-files.md`.
6. **Install the check.** Copy [scripts/check_tracking.py](scripts/check_tracking.py) to
   `tools/check_tracking.py` (if that path exists, stop and ask). Before any
   hook, look at what runs today: `git config core.hooksPath`, an existing
   `.githooks/pre-commit` or `.git/hooks/pre-commit`, a hook manager (husky,
   pre-commit, lefthook). Never replace a hook: with none, propose
   [scripts/pre-commit](scripts/pre-commit) as `.githooks/pre-commit` and
   `git config core.hooksPath .githooks`; with one, propose the one line that
   adds `python3 tools/check_tracking.py` to it. Hooks change how every commit
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
- `ABILITIES.md`: the ability becomes `done` in its index row and its entry,
  with **Evidence** linking the specification, tests or evaluation, and
  **Known limits** stated.
- `AHEAD.md`: an item that ended moves to History.
- `ATLAS.md`, when a part was added, moved or removed.
- A decision record for any standing rule the work produced.

## Promote an item

Items in `AHEAD.md` move `open` → `approved` → `next` → `started`. On
approval the ability gets its entry in `ABILITIES.md` with status `planned`,
and the item names it. When work starts, the item goes to History as
`started`, the ability becomes `in progress`, `ACTIVE.md` names the work, and
a plan goes into `docs/plans/` when the work spans sessions. New work starts
only from an empty `ACTIVE.md`.

## Fix what the check reports

`python3 tools/check_tracking.py` prints `path:line: ERROR CODE: message`.

| Code | Fix |
|---|---|
| `MISSING`, `NO_CONTRACT`, `NO_HOT_ZONE_END` | Create the file from its template; add the contract line or the marker |
| `HOT_ZONE_TOO_LONG`, `AGENTS_TOO_LONG` | Move detail below the hot zone and point to it; keep `AGENTS.md` to rules and pointers |
| `UNPOINTED_SECTION` | Name the section in the hot zone's `Below:` line |
| `BROKEN_LINK`, `MISSING_PATH`, `BROKEN_SPEC` | Point the link or path at what exists, or remove it |
| `MISSING_FIELD` | Add the field to ACTIVE's Now, with "none" when it is empty |
| `BAD_ID`, `BAD_STATUS`, `BAD_KIND`, `DUPLICATE_ID`, `NO_ENTRY`, `NOT_IN_INDEX`, `STATUS_MISMATCH` | Make the index row and the entry agree, with values from the lists |
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
