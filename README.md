# The A-files

*Five files every coding agent reads first.*

A way for a repository to keep its rules, its current work, its abilities,
its future and its map in five Markdown files at the root (`AGENTS.md`,
`ACTIVE.md`, `ABILITIES.md`, `AHEAD.md`, `ATLAS.md`), so that every coding
agent and every person starts each session from the same picture, and the
picture stays true. Version 1.2.2.

## What is in it

| Path | What it is |
|---|---|
| `skills/a-files/` | The skill: adopts the five files, maps and moves existing tracking files with every reference to them, closes out work, fixes what the check reports, joins a specification method |
| `skills/a-files/references/method.md` | The method guide: the five files, hot zones, keeping in step, the life of an item, the check, wiring each agent, adoption, naming, limits |
| `skills/a-files/templates/` | A template for every file |
| `skills/a-files/scripts/check_tracking.py` | The check of the five files' shape (Python 3.9+, standard library only) |
| `skills/a-files/scripts/pre-commit` | The git hook that runs the check before every commit |
| `skills/a-files/scripts/relink.py` | Plans, applies and verifies moves with every reference to them |
| `examples/minimal/` | A small invented project with every file filled in; the check passes on it |

## Install

**As a plugin.** In Claude Code, add the marketplace that lists this plugin
and install `a-files` from it (`/plugin install a-files@<marketplace>`).
Tools that read Agent Plugins (Codex, Kiro, Cursor, GitHub Copilot) install
the same folder through their own plugin command.

**As a skill folder.** Copy `skills/a-files/` into the folder where your
agent finds skills: `.agents/skills/` in the project (Codex, Antigravity,
Cursor, GitHub Copilot), `.claude/skills/` (Claude Code) or `.kiro/skills/`
(Kiro; a custom Kiro agent also needs the skill in its `resources` list).

Then ask the agent: *Adopt the A-files in this repository.*

**By hand, without an agent skill.**

```bash
cp -R skills/a-files/templates/. /path/to/repo/       # then fill in the placeholders in angle brackets
mkdir -p /path/to/repo/tools
cp skills/a-files/scripts/check_tracking.py /path/to/repo/tools/
git -C /path/to/repo config core.hooksPath           # what runs at commit today: a hooks path,
ls /path/to/repo/.githooks/pre-commit /path/to/repo/.git/hooks/pre-commit   # a hook file
```

With no hooks path, no hook file and no hook manager (husky, pre-commit,
lefthook), install the hook:

```bash
mkdir -p /path/to/repo/.githooks
cp skills/a-files/scripts/pre-commit /path/to/repo/.githooks/pre-commit
git -C /path/to/repo config core.hooksPath .githooks
```

Otherwise never replace what runs: add the one line
`python3 tools/check_tracking.py` to the existing pre-commit hook (in the
hooks path, in `.git/hooks/`, or in the hook manager's settings), as section
10 of the method guide says. Then run `python3 tools/check_tracking.py` at the
repository's root until it prints nothing.

`cp -R` overwrites files with the same name. In a repository that already
has some of these files, read section 10 of the method guide first.

## Requirements

Python 3.9 or later and git. Nothing leaves the machine: the check reads the
five files and the last commit.
