# Adopting the A-files

The steps of an adoption, read whole before step 1. The two replies, and what
may happen in each, are in `SKILL.md` under Adopt; nothing here overrides them.

## Contents

- Steps
- Validation
- Report
- Worked example

## Steps

1. **Survey.** List the tracking files that exist (status notes, boards, feature lists, roadmaps, TODO lists,
   architecture documents, notes of decisions, plans or research in other folders), every agent instruction file, and
   any specifications. Show a table: each old file, what it holds, and the A-file or `docs/` folder it would go to
   (the mapping table in section 10 of the method guide).
2. **Ask: full alignment or keep.** Once for everything, or area by area:

   | Choice | What happens |
   |---|---|
   | Full alignment | Everything goes to the root and `docs/`: content merges into the A-files, notes move into `docs/decisions/`, `docs/plans/`, `docs/research/` |
   | Keep it as the home | The old file stays the home: the A-file's hot zone carries `- **Home:** BOARD.md` (the kept file), the check verifies that file instead of the A-file's own fields or register, and keep-in-step names it. Abilities kept elsewhere take no part in the pairing with a specification method |
   | Leave it out | Files that are not tracking stay as they are |

3. **Specifications stay where they are.** Never move them. Link them: a `Specs` line on each ability they define, a
   row in ATLAS and in the `AGENTS.md` index for their folder. If the person wants them in another layout, that is the
   specification method's decision: say so and hand over.
4. **Plan the moves.** Run `python3 scripts/relink.py plan --move OLD NEW [--move OLD NEW ...]`. The script is in this
   skill's folder; use the base directory shown when the skill was loaded. Show every reference it lists, every bare
   name it flags for a decision, and every line marked `[instruction]` with a proposal: remove it, adapt it to the new
   home, or keep it; under full alignment, the proposal is to adapt it. Show the files that would be created from the
   templates; never overwrite one, merge into it. Get a yes.
5. **Apply.** Read each template in the skill folder and write the project file from it, never by running a copy
   command. Fill the files from the repository, marking what you could not establish as a question. Merge the old
   content into the A-files and remove each merged old file. A board of work in progress becomes Now and a work
   section of `ACTIVE.md`. A backlog comes into `AHEAD.md` on the owner's word: ask which items come in, and give each
   its **Entered** line with the date of the adoption. Then `python3 scripts/relink.py apply --move OLD NEW ...` moves
   what still has to move and rewrites the exact references. Settle each decision as the person chose, then verify
   until it reports no problem. Once the adoption record exists, use `python3 scripts/relink.py verify --move OLD NEW
   ... --keep docs/decisions/NNNN-adopt-the-a-files.md`.
6. **Install the check.** Before running the installer, look at what runs
   today: `git config --local --get core.hooksPath`, `git config --get core.hooksPath`, an existing
   `.githooks/pre-commit` or `.git/hooks/pre-commit`, a hook manager (husky,
   pre-commit, lefthook). Ask one question first: the check alone or the check and the hook?
   Honor a choice already supplied in the request or adoption answer.
   Then run [scripts/install_check.py](../scripts/install_check.py) once in place
   from this skill's base directory, from the project root:
   `python3 "<skill-folder>/scripts/install_check.py" --root .`, adding `--hook`
   only when the person chose the shell hook. The script copies
   [scripts/check_tracking.py](../scripts/check_tracking.py) into `tools/check_tracking.py`
   only when absent. An existing check is left untouched, with a report of
   whether it matches or differs from the plugin's. A later yes to the hook
   is a re-run with `--hook`; the existing check is still left untouched.
   Every shell hook installation or reporting-line insertion goes through
   this script; never write or copy a hook by hand or run an agent copy command.
   Never replace a hook: with none, propose
   [scripts/pre-commit](../scripts/pre-commit) as `.githooks/pre-commit` and
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
7. **Join a specification method** when the project has one (`SKILL.md`, Join a specification method); with a GitHub remote, offer the projection to issues (`references/issues.md`), default no.
8. **Record the adoption** as `docs/decisions/NNNN-adopt-the-a-files.md` from
   the decision template after `apply` and before the final `verify`: what
   moved, what was kept, what was left out. Keep the old names as written:
   this is the record of the move. Run the final `verify` with `--keep` as
   shown in step 5.
9. Show the hot zones before committing.

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

A repository with `BOARD.md`, `FEATURES.md`, a `CLAUDE.md` that says "Read BOARD.md at session start", and a README
linking both files.

```text
Old file       Holds                  Goes to
BOARD.md       current tasks          ACTIVE.md, Now and Pending
FEATURES.md    seven features         ABILITIES.md, AB-001 to AB-007
CLAUDE.md      the board instruction  adapted: "@AGENTS.md"; the warm-up reads ACTIVE.md
```

The person chooses full alignment. The A-files are created from the templates, the board and the features are merged
into them, and the two old files are removed. `relink.py apply --move BOARD.md ACTIVE.md --move FEATURES.md
ABILITIES.md` then rewrites the README's two links; the instruction in `CLAUDE.md` is adapted as agreed; `verify`
reports no problem and the check prints nothing.
