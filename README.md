# The A-files

*Five files every coding agent reads first.*

Coding agents start every session knowing nothing about where the work
stands. One long instruction file and a status note don't fix that: the file
gets too long to follow, and the note goes stale.

The A-files split that job into five short Markdown files at the repository's
root. Every agent and every person starts from the same picture, and a check
before each commit keeps that picture in shape.

They serve one owner directing agents, not a team tracker: one person decides
the work, and the agents read and keep the same picture across sessions. A
team that needs assignments and reviews keeps an issue tracker beside them.
A project on GitHub may also project AHEAD's actionable items to issues, so
the tools that read issues see them; AHEAD stays the source of truth.

**Version 2.3.0.**

## The five files

| File | Holds |
|---|---|
| `AGENTS.md` | The rules, the warm-up, and an index of every file an agent needs |
| `ACTIVE.md` | The work in progress: progress, the next step, pending items, debt, blockers |
| `ABILITIES.md` | Every ability of the product: planned, in progress, done or retired |
| `AHEAD.md` | What the owner chose to plan: next up, milestones, ideas, research, spikes |
| `ATLAS.md` | The architecture map: each part, its files, what it depends on, what checks it |

**Small or full.** Adoption offers the small setup (`AGENTS.md` and
`ACTIVE.md`) or the full one. A small setup grows later: add a file from its
template, name it in the index of `AGENTS.md`, and the check expects it from
then on.

## How it works

- **Hot zones.** `AGENTS.md` is loaded whole by the tools that read it, so it
  holds only how to work here and where to look next. The top of each of the
  other four is short and capped. At every session start an agent reads those
  hot zones and the last fifteen commits: 360 lines of hot zones at most. Before changing a file, it checks
  git status and states Finished, Remaining, Blocked by and Next step in four short
  lines, writing "nothing" where a line is empty.
  It opens anything else only when the task needs it.
- **Keep in step.** Each A-file is updated in the same commit as the work it
  describes. Start or finish work, and `ACTIVE.md` changes in that commit.
- **A desk for long work.** Work the owner commits to for days or weeks gets a
  section of its own in `ACTIVE.md`, in the form the work needs. If it has to
  wait, it stays there, and nothing else starts until the owner says so.
- **A plan the owner decides.** An agent proposes an item for `AHEAD.md` and
  does not write it. What a session finds and will not do now is written down
  where the work keeps its record, and the owner rules on it when the work
  closes. Work is reported as unfinished while a defect or a required check
  stands in what was asked.
- **Stable identifiers.** Abilities (`AB-001`) and items ahead (`AH-001`) are
  never reused, so history stays readable. An ability is never deleted; an
  item goes only on the owner's word, and its number stays used.
- **Status once, in the index row.** An ability's status is written in its
  row only. Done abilities can move to a table below the hot zone, so the
  session-start read stays short in a long-lived product.
- **A check that reports.** `check_tracking.py` reports, at every commit, what
  breaks the files' shape: a missing field, a hot zone over its cap, a broken
  link, an identifier that disappeared, or `BLOCKER_WITHOUT_SOURCE` when a blocker lacks a dated owner message, specification ID or file path, or failing check by name. The commit hook runs it on what is
  staged, as the commit will hold it, and notes an A-file whose changes are
  not staged. The commit goes through; the problems are shown. A script's
  report holds even when a model skips an instruction. A repository that
  wants a strict hook runs the check with `--staged --strict` (Install below
  gives the line for a hook of your own); by hand it reads the working tree.
  A clean run prints nothing; `--summary` says what it inspected,
  `--format json` gives the run and the registers it read as data, and
  `--version` names the A-files version it belongs to.

## Install

Claude Code:

```text
/plugin marketplace add ChristianOrrala/agents
/plugin install a-files@christianorrala
```

Codex:

```text
codex plugin marketplace add ChristianOrrala/agents
codex plugin add a-files@christianorrala
```

Then approve each hook once in Codex's `/hooks`.

Kiro CLI and OpenCode run the plugin from a full copy, kept in one place:

```sh
git clone --branch v2.3.0 https://github.com/ChristianOrrala/a-files.git ~/.local/share/agent-plugins/a-files
```

- **Kiro CLI:** link the copy's `skills/a-files` folder as
  `~/.kiro/skills/a-files`, copy `hooks/kiro/a-files.json` to
  `~/.kiro/hooks/`, trust the workspace, and set the V3 engine once:
  `kiro-cli settings chat.agentEngine v3`. Kiro runs hooks on no other engine.
- **OpenCode:** add the copy's `hooks/opencode` folder, as an absolute path,
  to the `plugins` array of `opencode.json`. Not `opencode plugin add`: it
  fetches only that folder, and the module then finds no hook script and
  stays silent.

**Upgrading from 1.x.** Releases before 2.0.0 came from the marketplace
`christian-orrala`. On each computer, once:

```sh
claude plugin uninstall a-files@christian-orrala
claude plugin marketplace remove christian-orrala
claude plugin marketplace add ChristianOrrala/agents
claude plugin install a-files@christianorrala

codex plugin remove a-files@christian-orrala
codex plugin marketplace remove christian-orrala
codex plugin marketplace add ChristianOrrala/agents
codex plugin add a-files@christianorrala
```

A step for a tool or marketplace you never installed fails harmlessly. Kiro
CLI and OpenCode: as above. In a project, nothing has to change; to bring its
check to this release, re-run the check installer with `--upgrade` (see
Without an agent, below), and commit the result with the line
`No behavior change: none, tooling only.` when the project also uses a
spec-driven commit guard.

Other agents that read skill folders (Cursor, GitHub Copilot, Antigravity)
copy `skills/a-files/` into the folder where your agent finds skills:

| Agent | Skills folder |
|---|---|
| Claude Code | `.claude/skills/` |
| Codex, Antigravity, Cursor, GitHub Copilot | `.agents/skills/` |
| Kiro | `.kiro/skills/` (a custom Kiro agent also needs the skill in its `resources` list) |

**Requirements:** Python 3.9 or later and git. Nothing leaves your machine.

Adoption reads the installed plugin's folder: templates are read and project
files are written from them, and the check installer runs in place from the
skill's base directory. A tool's permission mode may ask for access to that
folder. On a refused or failed step, report the command, what is installed
and what is missing; commit nothing half-written. Resolve that access or
failure before resuming.

## Usage

Ask your agent in plain words:

| When | Ask |
|---|---|
| Starting | *Adopt the A-files in this repository.* |
| Finishing a piece of work | *Close out this work in the A-files.* |
| The check reports a problem | *Fix what the tracking check reports.* |
| An issue is labelled out of step | *Align the A-files with the issues.* |

When the repository already tracks work in other files (a board, a feature
list, a roadmap, notes), adoption maps them first. It asks whether to move
them into the A-files or keep them. When they move, it finds every link,
import and instruction that names them and fixes those too. It asks before it
installs the git hook.

The skill also links abilities to specifications when the project uses a
spec-driven method.

## GitHub issues (opt-in)

With a GitHub remote, adoption and the check's upgrade ask once, default no,
whether to project AHEAD's approved, next and started items (open ones too, if
you choose) to the repository's issues. On a yes, `install_check.py --issues`
copies `tools/project_issues.py` and `.github/workflows/a-files-issues.yml`.
After each push that changes `AHEAD.md` or `ABILITIES.md`, and when one of its
issues is closed or reopened on GitHub, the workflow keeps
one issue per item: its title, its `kind:` and `state:` labels and a marked
part of its body; the rest of the issue is yours. Issues close as not planned
when an item is dropped and as completed when the item is done. Nothing is
written to the A-files, nothing is deleted, and nothing leaves your machine
before you push. A change made on GitHub (a pull request that closes an issue,
a board rule) is never overwritten: the issue is labelled
`a-files: out of step`, and an agent gathers the facts and asks you which side
wins. `python3 tools/project_issues.py` alone shows the plan and writes
nothing.

## Agent hooks

The plugin carries two agent hooks, run by `skills/a-files/scripts/afiles_hook.py`.
At session start the agent gets a note to say where things stand in four short
lines before its first edit. At the end of a turn it gets what the check
reports, each finding once per session, as a note for the agent: it asks the
owner nothing, and continues the turn once, only to deliver the note. Both act only where `ACTIVE.md` carries the hot-zone marker and stay
silent elsewhere. The git hook stays; it is the check that holds for everyone.

| Tool | Turn them on |
|---|---|
| Claude Code | Install the plugin. |
| Codex | Install from the marketplace, then approve each hook once in `/hooks`; an unapproved hook is skipped without a word. |
| Kiro CLI | Link or copy the skill folder to `~/.kiro/skills/a-files/` and `hooks/kiro/a-files.json` to `~/.kiro/hooks/`; trust the workspace; hooks run only on the V3 engine (`kiro-cli settings chat.agentEngine v3`). |
| OpenCode | List the `hooks/opencode` folder of a full copy of the plugin in the `plugins` array of `opencode.json`, in the project or globally; `opencode plugin add` fetches that folder alone, without the hook script. |

## What's in the folder

| Path | What it is |
|---|---|
| `skills/a-files/` | The skill |
| `skills/a-files/references/method.md` | The method guide: the five files, hot zones, keeping in step, the check, adoption, naming, limits |
| `skills/a-files/templates/` | A template for each file |
| `skills/a-files/scripts/check_tracking.py` | The check (standard library only) |
| `skills/a-files/scripts/install_check.py` | Installs the check and, with `--hook`, the agreed shell hook without replacing an existing hook; with `--upgrade`, brings an earlier check to this release; with `--issues`, installs the projection to issues |
| `skills/a-files/scripts/project_issues.py` | The opt-in projection of AHEAD to GitHub issues; a dry run unless `--apply` |
| `skills/a-files/templates/github/a-files-issues.yml` | The workflow that runs it after a push |
| `skills/a-files/scripts/afiles_hook.py` | The agent hooks: the session-start note and the findings at the end of a turn |
| `hooks/` | The hook files for Claude Code and Codex, Kiro CLI and OpenCode |
| `skills/a-files/scripts/pre-commit` | The git hook that runs the check before every commit |
| `skills/a-files/scripts/relink.py` | Plans, applies and verifies file moves, with every reference to them |
| `examples/minimal/` | A small invented project with every file filled in; the check passes on it |

## Without an agent

Read each chosen template and create its file in your repository, filling
the placeholders in angle brackets. Merge existing files rather than
overwriting them; read section 10 of the method guide first. For the small
setup, keep only `AGENTS.md` and `ACTIVE.md` (and `CLAUDE.md` for Claude Code),
and remove the other three files' index rows from `AGENTS.md`, with their
mentions in the warm-up and in keep in step.

Before choosing whether to install a hook with the check, see what already runs:

```bash
git -C /path/to/repo config --local --get core.hooksPath
git -C /path/to/repo config --get core.hooksPath
ls /path/to/repo/.githooks/pre-commit /path/to/repo/.git/hooks/pre-commit
```

Choose the check alone or the check and the hook before running the installer.
An agent asks this one question first, honoring a choice already supplied in
the request or adoption answer. Run the installer once in place from the plugin folder. To install only the
check, leaving hooks and git configuration alone:

```bash
python3 "skills/a-files/scripts/install_check.py" --root "/path/to/repo"
```

If you agree to the shell hook too, add `--hook` to that command instead.
With no hook it installs the shipped `.githooks/pre-commit` and sets
`core.hooksPath .githooks`. With an existing shell hook, it inserts the line
below first, preserving the hook's commands and mode; a hook that already runs
the check is left as it is. An existing
`tools/check_tracking.py` is left untouched, with a report saying whether it
matches or differs from the plugin's. For a later yes to the hook, re-run with `--hook`;
the check is still left untouched. To bring an earlier check to the plugin's
release, re-run with `--upgrade`: it replaces a check that is committed and
unchanged since, names both releases, and refuses any other. Every shell hook installation or
reporting-line insertion goes through the script; never write or copy the
hook by hand. Hook managers and non-shell hooks need their own step; the
installer stops rather than editing them. If only a global or system
`core.hooksPath` is set, `--hook` refuses before any change: that folder is
shared by other repositories and the owner must choose where the hook goes.
The check alone can still be installed.

If something already runs, don't replace it. The script adds this line to the existing
pre-commit hook, before the hook's first command: after the shebang when
there is one, at the top when there is none.

```sh
python3 tools/check_tracking.py --staged || true
```

The added line never decides the hook's result unless a strict check is
asked for. The check only reports: it exits 0 even when it finds problems,
so added as the hook's last line it would decide the result, and a failing
command of your own before it would no longer refuse the commit. `|| true`
keeps it from stopping a hook that runs with `set -e` when the check cannot
run. For a strict check, which refuses a commit while the A-files have
problems, the proposed line is the following; your own commands after it
still decide otherwise:

```sh
python3 tools/check_tracking.py --staged --strict || exit 1
```

The `|| true` and `|| exit 1` lines are for a shell hook. Some hook
managers, such as the pre-commit framework, run a step without a shell, so
`||` would reach the check as an argument and every commit would be
refused. Give the check a step of its own running
`python3 tools/check_tracking.py --staged`, which reports and exits 0, or
`python3 tools/check_tracking.py --staged --strict` to refuse; never
`|| true` in a step. The step takes no file names, runs on every commit,
one that only deletes files included, and shows its output, so the report
is seen. For example, the pre-commit framework, in `.pre-commit-config.yaml`
(by default it passes the staged file names, which the check refuses, runs
a step only when files match, and hides a passing step's output):

```yaml
repos:
  - repo: local
    hooks:
      - id: a-files
        name: A-files check
        entry: python3 tools/check_tracking.py --staged
        language: system
        pass_filenames: false
        always_run: true
        verbose: true
```

For the strict check, the same step with
`entry: python3 tools/check_tracking.py --staged --strict`.

Last, run `python3 tools/check_tracking.py` at the repository's root and fix
what it reports until it prints nothing.

## License

MIT. Copyright (c) 2026 Christian Orrala. See [LICENSE](LICENSE).
