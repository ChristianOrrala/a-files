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

**Version 1.4.0.**

## The five files

| File | Holds |
|---|---|
| `AGENTS.md` | The rules, the warm-up, and an index of every file an agent needs |
| `ACTIVE.md` | The work in progress: progress, the next step, pending items, debt, blockers |
| `ABILITIES.md` | Every ability of the product: planned, in progress, done or retired |
| `AHEAD.md` | Everything not started: next up, milestones, ideas, research, spikes |
| `ATLAS.md` | The architecture map: each part, its files, what it depends on, what checks it |

**Small or full.** Adoption offers the small setup (`AGENTS.md` and
`ACTIVE.md`) or the full one. A small setup grows later: add a file from its
template, name it in the index of `AGENTS.md`, and the check expects it from
then on.

## How it works

- **Hot zones.** The top of each file is short and capped. At every session
  start an agent reads the hot zones of the files the repository keeps and the
  last fifteen commits: about 400 lines at most. It opens anything else only when the task needs it.
- **Keep in step.** Each A-file is updated in the same commit as the work it
  describes. Start or finish work, and `ACTIVE.md` changes in that commit.
- **Stable identifiers.** Abilities (`AB-001`) and items ahead (`AH-001`) are
  never deleted or reused, so history stays readable.
- **Status once, in the index row.** An ability's status is written in its
  row only. Done abilities can move to a table below the hot zone, so the
  session-start read stays short in a long-lived product.
- **A check that reports.** `check_tracking.py` reports, at every commit, what
  breaks the files' shape: a missing field, a hot zone over its cap, a broken
  link, an identifier that disappeared. The commit hook runs it on what is
  staged, as the commit will hold it, and notes an A-file whose changes are
  not staged. The commit goes through; the problems are shown. A script's
  report holds even when a model skips an instruction. A repository that
  wants a strict hook runs the check with `--staged --strict` (Install below
  gives the line for a hook of your own); by hand it reads the working tree.

## Install

Claude Code:

```text
/plugin marketplace add ChristianOrrala/plugins
/plugin install a-files@christian-orrala
```

Codex:

```text
codex plugin marketplace add ChristianOrrala/plugins
codex plugin add a-files@christian-orrala
```

Other agents that read Agent Plugins (Kiro, Cursor, GitHub Copilot) install
this folder through their own plugin command. Or copy `skills/a-files/` into
the folder where your agent finds skills:

| Agent | Skills folder |
|---|---|
| Claude Code | `.claude/skills/` |
| Codex, Antigravity, Cursor, GitHub Copilot | `.agents/skills/` |
| Kiro | `.kiro/skills/` (a custom Kiro agent also needs the skill in its `resources` list) |

**Requirements:** Python 3.9 or later and git. Nothing leaves your machine.

## Usage

Ask your agent in plain words:

| When | Ask |
|---|---|
| Starting | *Adopt the A-files in this repository.* |
| Finishing a piece of work | *Close out this work in the A-files.* |
| The check reports a problem | *Fix what the tracking check reports.* |

When the repository already tracks work in other files (a board, a feature
list, a roadmap, notes), adoption maps them first. It asks whether to move
them into the A-files or keep them. When they move, it finds every link,
import and instruction that names them and fixes those too. It asks before it
installs the git hook.

The skill also links abilities to specifications when the project uses a
spec-driven method.

## What's in the folder

| Path | What it is |
|---|---|
| `skills/a-files/` | The skill |
| `skills/a-files/references/method.md` | The method guide: the five files, hot zones, keeping in step, the check, adoption, naming, limits |
| `skills/a-files/templates/` | A template for each file |
| `skills/a-files/scripts/check_tracking.py` | The check (standard library only) |
| `skills/a-files/scripts/pre-commit` | The git hook that runs the check before every commit |
| `skills/a-files/scripts/relink.py` | Plans, applies and verifies file moves, with every reference to them |
| `examples/minimal/` | A small invented project with every file filled in; the check passes on it |

## Without an agent

Copy the templates and the check into your repository, then fill in the
placeholders in angle brackets:

```bash
cp -R skills/a-files/templates/. /path/to/repo/
mkdir -p /path/to/repo/tools
cp skills/a-files/scripts/check_tracking.py /path/to/repo/tools/
```

`cp -R` overwrites files with the same name. If the repository already has
some of these files, read section 10 of the method guide first. For the small
setup, keep only `AGENTS.md` and `ACTIVE.md` (and `CLAUDE.md` for Claude Code),
and remove the other three files' index rows from `AGENTS.md`, with their
mentions in the warm-up and in keep in step.

Then wire the check into the commit. First see what already runs:

```bash
git -C /path/to/repo config core.hooksPath
ls /path/to/repo/.githooks/pre-commit /path/to/repo/.git/hooks/pre-commit
```

If nothing runs (no hooks path, no hook file and no hook manager such as
husky, pre-commit or lefthook), install the hook:

```bash
mkdir -p /path/to/repo/.githooks
cp skills/a-files/scripts/pre-commit /path/to/repo/.githooks/pre-commit
git -C /path/to/repo config core.hooksPath .githooks
```

If something already runs, don't replace it. Add this line to the existing
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
problems, put this line in its place instead; your own commands after it
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
