# AGENTS.md

<One paragraph: what this repository is, what it is for, and where its main
code lives.>

## Warm-up

At the start of every session, read in this order:

1. this file's hot zone (it ends at the line `<!-- hot zone ends -->`);
2. the hot zones of `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md` and `ATLAS.md`;
3. `git log --oneline -15`.

Open anything else only when the task needs it; the index says where it is.

## Index

| File | Holds | Updated |
|---|---|---|
| `ACTIVE.md` | The work in progress and what blocks new work | At every session end |
| `ABILITIES.md` | Every ability of the product: planned, in progress, done, retired | When an ability changes state |
| `AHEAD.md` | Everything not started: next up, milestones, ideas, research, spikes | When an item is proposed, approved, scheduled or dropped |
| `ATLAS.md` | The architecture map: parts, files, dependencies, checks | When a part is added, moved or removed |
| `docs/decisions/` | Decisions and standing rules | When a decision is made |
| `docs/plans/` | One plan per piece of work that spans sessions | During that work |
| `docs/research/` | Research and spike write-ups | When one is finished |
| `CHANGELOG.md` | Release history | At each release |
| <another file an agent must find> | <what it holds> | <when it changes> |

## Keep in step

In the same commit as the work, an agent updates:

- `ACTIVE.md` when it starts, finishes, defers or drops work;
- `ABILITIES.md` when an ability changes state;
- `AHEAD.md` when an item is proposed, approved, scheduled or dropped, or a
  spike ends (and `ABILITIES.md` when an item is approved);
- `ATLAS.md` when a part of the repository is added, moved, renamed or removed;
- `docs/decisions/` for a decision or a standing rule, never only an A-file.

Only the main session edits the A-files; parallel workers report to it.
Run `python3 tools/check_tracking.py` before every commit: it checks their
shape. Where the repository installed the hook in `.githooks/`, the hook runs
it (enable it once per clone: `git config core.hooksPath .githooks`).

## Commands

- Build: `<command>`
- Test: `<command>`
- Lint: `<command>`

## Rules

- **Always:** <what an agent must always do in this repository>
- **Ask first:** <what needs the owner's yes: dependencies, schema changes, deletions, anything leaving the machine>
- **Never:** <what an agent must never do: secrets in files, force-push, editing generated files>

Below: Before committing, Naming.

<!-- hot zone ends -->

## Before committing

```bash
<test command>
python3 tools/check_tracking.py
```

## Naming

| What | Convention | Example |
|---|---|---|
| Files at the root that people and tools look for | Uppercase name, `.md` | `README.md`, `AGENTS.md`, `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md`, `ATLAS.md`, `CHANGELOG.md` |
| Files under `docs/` | Lowercase, words joined by hyphens | `docs/research/01-sms-providers.md` |
| Decision records | Four digits, never reused, then the subject | `docs/decisions/0001-adopt-the-a-files.md` |
| Plans | The date the work started, then the subject | `docs/plans/2026-10-04-cancel-a-booking.md` |
| Research and spikes | Two digits, then the subject | `docs/research/01-sms-providers.md` |
| Abilities and AHEAD items | `AB-` or `AH-` and three digits, never reused | `AB-009`, `AH-007` |
| Dates | ISO 8601 | `2026-10-03` |
| Commit subjects | Area, colon, what changed | `booking: refuse a ninth repair on a full day` |
| Branches | Kind, slash, subject; kinds `feat`, `fix`, `docs`, `chore` | `feat/cancel-a-booking` |
| Release tags | `v` and a semantic version | `v1.2.0` |
