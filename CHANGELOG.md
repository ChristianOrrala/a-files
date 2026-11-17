# Changelog

All notable changes to the A-files. Versions follow semantic versioning.

## 2.0.1 (2026-11-17)

A text release: the install and upgrade steps are complete enough to follow without help. No script behaves differently; only the version lines change.

- **Upgrading from 1.x.** The README has the commands per tool to leave the marketplace `christian-orrala` for `christianorrala`, and how to bring a project's check to this release with `install_check.py --upgrade`.
- **Kiro CLI runs hooks only on its V3 engine** (`kiro-cli settings chat.agentEngine v3`). The README no longer says Kiro installs the plugin through its own plugin command: it takes the skill folder and the hook file.
- **OpenCode needs a full copy of the plugin.** `opencode plugin add` fetches only `hooks/opencode`, without the hook script. The README shows a clone of the repository and the absolute path to list in `opencode.json`.

**What an upgrade asks of you:** update the plugin; in Kiro, set the V3 engine if you have not.

## 2.0.0 (2026-11-17)

The A-files get agent hooks of their own, carried by the plugin.

- **Two hooks.** At session start, a note for the agent: before the first edit, say where things stand in four short lines (Finished, Remaining, Blocked by, Next step), checked against git. At the end of a turn, what the check reports, each finding once per session, as a note for the agent: it asks the owner nothing and never stops the work. Both run `scripts/afiles_hook.py`.
- **Only where the A-files are adopted.** They act in a project whose `ACTIVE.md` carries the hot-zone marker. Elsewhere, and outside git, they print nothing, exit 0 and write no file.
- **Four tools.** `hooks/hooks.json` serves Claude Code (on with the plugin) and Codex (approve each hook once in `/hooks`); `hooks/kiro/a-files.json` goes in `~/.kiro/hooks/` with the skill folder in `~/.kiro/skills/a-files/`; `hooks/opencode/` is listed in the `plugins` array of `opencode.json`. Seen firing on Claude Code 2.1.326, Codex 0.167.0, Kiro CLI 3.3.0 and OpenCode 2.3.0.
- **With a specification method installed too,** the note and the findings come from this plugin only, so each arrives once.
- **The root `plugin.json` declares no `$schema`.** Codex loads no plugin hooks from a plugin whose root manifest declares it.
- The check, the installer and the commit hook are unchanged; the commit hook is still the check that holds for everyone.
- **Install lines name the catalog `ChristianOrrala/agents`,** marketplace `christianorrala` (`/plugin install a-files@christianorrala`). The marketplace `christian-orrala` in `ChristianOrrala/plugins` still lists the plugin; to move, remove it and add the new one, then install again.

**What an upgrade asks of you:** update the plugin and turn its hooks on in your tool. Nothing changes in a project.

## 1.8.2 (2026-11-16)

- **The installer upgrades an earlier check.** `install_check.py --upgrade` replaces a `tools/check_tracking.py` from an earlier release when it is committed and unchanged since; it names both releases and refuses a check changed by hand or from a later release.
- **No second check in a hook that already runs it.** `install_check.py --hook` leaves an existing shell hook as it is when one of its commands already runs `tools/check_tracking.py`, and takes out a reporting line an earlier install put beside such a command. A check named only in a comment does not count.
- The check itself, its default output, its JSON object and its exit codes are unchanged.

**What an upgrade asks of you:** update the plugin. To bring a project's installed check to 1.8.2, run `scripts/install_check.py --upgrade` against the project.

## 1.8.1 (2026-11-14)

- **A broken link in place of an A-file is unreadable, not missing.** The check reports it with `UNREADABLE` and names the link, where 1.8.0 reported the file as absent.
- **Output never ends in an encoding error.** Under a legacy Windows code page or a C locale, the check, the installer and the relink script write a character the console cannot write as its escape (`→`) instead of stopping.
- The installer and the relink script read git's answers as UTF-8, so a path with non-ASCII characters is read the same on every system.
- The default output, the JSON object and the exit codes are otherwise unchanged.

**What an upgrade asks of you:** update the plugin. To bring a project's installed check to 1.8.1, preserve or remove the existing `tools/check_tracking.py` as appropriate, then re-run `scripts/install_check.py` against the project.

## 1.8.0 (2026-11-13)

- **The check says what it inspected, on request** (0055). `--summary` ends the run with one line naming the A-files it inspected, those absent or kept elsewhere, and the number of problems. A clean run without it still prints nothing.
- **The check as data.** `--format json` prints the run as one JSON object: the files inspected, the findings with file, line, severity, code and message, the notes, and what the check parsed: the fields of ACTIVE's Now, the abilities and the AHEAD items with their columns and lines, an ability's Known limits and Evidence, an item's Belongs to, and the home of a file kept elsewhere. The object carries a schema number.
- **The check states its version.** `--version` prints it, and the JSON object carries it, so a project can tell which A-files it has installed.
- **The data says which registers it read.** `registers` gives, for the abilities and the AHEAD items, whether the check read the file's rows and, when not, why: `absent`, `unreadable`, `kept_elsewhere` or `no_hot_zone`. An empty list then means a register with no rows, not one the check could not read.
- **The pairing rule P2 says what it expects of an ability in progress** (0055): one whose use cases are all `Done` is reported; mark it `done`, or name in its `Specs` line the use case still to build. The contract reads the same in both products.
- The default output, the line format and the exit codes are unchanged, with and without `--staged` and `--strict`; the new options write nothing.

**What an upgrade asks of you:** update the plugin. For the new options in a project, refresh its installed check: preserve or remove the existing `tools/check_tracking.py` as appropriate, then re-run `scripts/install_check.py` against the project; the installer leaves an existing check untouched. The templates and the hook are unchanged, so nothing else needs copying.

## 1.7.0

- Adoption runs `scripts/install_check.py` in place from the plugin folder. Choose the check alone or the check and hook first; the installer refuses to change a hooks folder shared through global or system configuration. Install commands quote the plugin path.
- The `AGENTS.md` template states what a request authorizes and how reserved approval is granted (0048).
- The check advises `BLOCKER_WITHOUT_SOURCE` when a blocker names no source, and the warm-up checks the source of a carried-over blocker before honoring it (0049).

**What an upgrade asks of you:** update the plugin. Add the new authorization rule and warm-up sentence from the `AGENTS.md` template to each project's `AGENTS.md` by hand. To refresh the installed check, preserve or remove the existing `tools/check_tracking.py` as appropriate, then re-run `scripts/install_check.py` against the project; the installer leaves an existing check untouched. Choose the hook option only if needed.

## 1.6.0

Before the first change, the warm-up states Finished, Remaining, Blocked by and Next step in four short lines, writing "nothing" where a line is empty, checked against git and not only against `ACTIVE.md`. Projects that already adopted the A-files add step 4 to their `AGENTS.md` by hand. No change to the check or the hook.

## 1.5.0

The `AGENTS.md` template gains a rule: in a message to a person, every identifier is followed by its title in parentheses. A repository that already adopted the A-files adds the line by hand. No change to the check or the hook.

## 1.4.0

The pairing contract says what a specification method reads at session start. No change to the check or the hook.

- **The pairing contract.** One line changed (P7): the state shown at session start includes the Debt of `ACTIVE.md` and the Next up list of `AHEAD.md`, which upspec 1.4.0 reads. Both products carry the same wording.
- **The method guide.** Its version line reads 1.4.0, with the date of this release.
- **Evaluations.** None ran for this release. The 1.3.0 scores stay what they were, for 1.3.0.

**What an upgrade asks of you:** update the plugin. The check, the templates and the hook are unchanged, so nothing in a project needs copying.

## 1.3.0

The check informs; it never refuses a commit. A project may start with two files, the commit hook checks what the commit will hold, and an ability's status is written once.

- **The check reports, and never refuses a commit.**
  - It exits 0 when it ran, whatever it found. With `--strict` it exits 1 on problems, for a repository that chooses a strict pipeline. 2 is a usage error, 3 that it could not run.
  - The commit hook shows the problems and lets the commit through, and so it does when the check cannot run. A repository that wants commits refused uses `--staged --strict` in its hook (upgrade step 6 gives the line for a hook of your own).
  - Problems go to stdout, one `path:line: ERROR CODE: message` line each, and notes to stderr, where they never count as problems.
- **The hook checks what is staged.** With `--staged`, the hook's mode, the check reads every A-file and every path it checks from the git index, as the commit will hold them, compares identifiers with the last commit, and notes an A-file whose changes are not staged. A run by hand reads the working tree. `--staged` without git, or outside a repository, could not run (exit 3).
- **The check in a hook you already have.** The README, the skill and the method guide give the line, `python3 tools/check_tracking.py --staged || true`, and its place: before the hook's first command. The added line never decides the hook's result unless a strict check is asked for: since the check only reports, a line added last would decide the hook's result and drop your own refusal. They also give a strict line for a shell hook of your own, and, for a hook manager that runs a step without a shell, such as the pre-commit framework, a step that takes no file names, runs on every commit and shows its output.
- **A small setup.** `AGENTS.md` and `ACTIVE.md` are always expected. `ABILITIES.md`, `AHEAD.md` and `ATLAS.md` are expected when the index in `AGENTS.md` lists them, when the file exists, or when it held identifiers in the last commit, so a file deleted together with its index line is still reported. Adoption offers the small setup or the full one, and a small setup can grow later.
- **Done abilities below the hot zone.** The hot zone of `ABILITIES.md` may hold no ability row when an index table below it holds them. A table without the ID, Ability and Status columns, such as an area summary, is not an index and is ignored.
- **The status is written once, in the index row.** New entries carry no Status line. An old entry that still has one is read: it must agree with its row, and a mismatch is reported.
- **Fewer repeated findings.** A missing or unreadable `ABILITIES.md` is reported once, not again for each AHEAD item that names an ability. An AHEAD item that names an ability when there is no `ABILITIES.md` is reported.
- **Who the A-files serve.** The README and the method guide say it: one owner directing agents, not a team tracker. Blocked work moves to Pending or back to `AHEAD.md` and never holds up unrelated work; there is still one current piece of work.
- **The pairing contract.** Two new rows, worded the same in both products: what "later" at the end of an agent's turn writes into `AHEAD.md`, and how a specification method's hook runs the check and reads its output. The keep-in-step rows for abilities are added only when the project keeps `ABILITIES.md`.
- **Evaluations.** Only e4 ran on 1.3.0, the case whose grader changed (both setups offered): **once** with the skill, 1.00, and once without, 0.60, so the score is a single run and noisy. e1 to e3 were not rerun: their prompts and graders did not change.

**What an upgrade asks of you:**
1. Update the plugin.
2. Copy the new `scripts/check_tracking.py` to `tools/` in each project.
3. If the project uses the commit hook, replace `.githooks/pre-commit` with the new `scripts/pre-commit`. The 1.2.4 hook refuses a commit on any problem; the new one reports. To keep refusing, use the line the new hook names: `exec python3 tools/check_tracking.py --staged --strict`.
4. Nothing blocks any more. A pipeline step that should fail on problems adds `--strict`.
5. An old entry's Status line is still read; remove it when you next touch the entry, and keep the status in the row.
6. If you added the check's line to a hook of your own, check where it sits. A line added last decides the hook's result. With the 1.2.4 check there, a failing command of your own before it, such as your tests, already went through whenever the A-files were clean; with the 1.3.0 check, which exits 0 even when it finds problems, it goes through every time. Put `python3 tools/check_tracking.py --staged || true` before the hook's first command: after the shebang when there is one, at the top when there is none. The added line never decides the hook's result unless a strict check is asked for: for one, use `python3 tools/check_tracking.py --staged --strict || exit 1`, placed the same way. The `|| true` and `|| exit 1` lines are for a shell hook. Some hook managers, such as the pre-commit framework, run a step without a shell, so a hook manager takes a step of its own running `python3 tools/check_tracking.py --staged`, which reports and exits 0, or `python3 tools/check_tracking.py --staged --strict` to refuse; never `|| true` in a step. The step takes no file names, runs on every commit, one that only deletes files included, and shows its output, so the report is seen. For example, the pre-commit framework, in `.pre-commit-config.yaml`: a `repo: local` hook with `entry: python3 tools/check_tracking.py --staged`, `language: system`, `pass_filenames: false`, `always_run: true` and `verbose: true`; for the strict check, `entry: python3 tools/check_tracking.py --staged --strict`.
7. A hot zone of `ABILITIES.md` with no ability row fails the 1.2.4 check (`NO_INDEX`): keep one open row in the hot zone while any project still runs the 1.2.4 check.

## 1.2.4

- The pairing contract names the use case overview `docs/use_cases.md`
  and the short change record.
- Specification fixtures use the current formats: front matter, the
  generated Mermaid overview, Examples tables and the short change record.

**How to migrate:** Update the plugin. In a paired specification project,
  ask the specification agent to move the specs to the current formats;
  the A-files and their Specs links keep the same identifiers and paths.

## 1.2.3

- The README is rewritten: the problem the files solve, a table of the five
  files, how they work, install steps for Claude Code, Codex and other agents,
  example prompts, and the manual steps in order.

## 1.2.2

- The pairing contract (P4): a recovery change log entry decided later
  becomes an AHEAD item that cites it; the entries of one use case share one
  item.

## 1.2.1

The first public release. Earlier versions were internal.

- The `a-files` skill: adopts and keeps five files at a repository's root
  that every coding agent reads first (`AGENTS.md`, `ACTIVE.md`,
  `ABILITIES.md`, `AHEAD.md`, `ATLAS.md`), each with a hot zone read at
  session start.
- A check of their shape, a git hook that runs it before every commit (installed
  only with your yes), and a reference check that keeps every link, import and
  instruction right when a tracking file moves.
- A minimal example project.
- Works alone or with upspec in the same project.
