# The A-files

*Five files every coding agent reads first.*

Coding agents start every session knowing nothing about where the work
stands. One long instruction file and a status note don't fix that: the file
gets too long to follow, and the note goes stale.

The A-files split that job into five short Markdown files at the repository's
root. Every agent and every person starts from the same picture, and a check
before each commit keeps that picture in shape.

**Version 1.2.3.**

## The five files

| File | Holds |
|---|---|
| `AGENTS.md` | The rules, the warm-up, and an index of every file an agent needs |
| `ACTIVE.md` | The work in progress: progress, the next step, pending items, debt, blockers |
| `ABILITIES.md` | Every ability of the product: planned, in progress, done or retired |
| `AHEAD.md` | Everything not started: next up, milestones, ideas, research, spikes |
| `ATLAS.md` | The architecture map: each part, its files, what it depends on, what checks it |

## How it works

- **Hot zones.** The top of each file is short and capped. At every session
  start an agent reads the five hot zones and the last fifteen commits: about
  400 lines at most. It opens anything else only when the task needs it.
- **Keep in step.** Each A-file is updated in the same commit as the work it
  describes. Start or finish work, and `ACTIVE.md` changes in that commit.
- **Stable identifiers.** Abilities (`AB-001`) and items ahead (`AH-001`) are
  never deleted or reused, so history stays readable.
- **A check that holds.** `check_tracking.py` refuses a commit that breaks the
  files' shape: a missing field, a hot zone over its cap, a broken link, an
  identifier that disappeared. A script holds even when a model skips an
  instruction.

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
| The check refuses a commit | *Fix what the tracking check reports.* |

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
some of these files, read section 10 of the method guide first.

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

If something already runs, don't replace it. Add one line,
`python3 tools/check_tracking.py`, to the existing pre-commit hook or to the
hook manager's settings.

Last, run `python3 tools/check_tracking.py` at the repository's root and fix
what it reports until it prints nothing.

## License

MIT. Copyright (c) 2026 Christian Orrala. See [LICENSE](LICENSE).
