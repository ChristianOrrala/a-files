# AGENTS.md

<One paragraph: what this repository is, what it is for, and where its main
code lives.>

## Warm-up

At the start of every session, do the following in order:

1. follow this file; open it once if your tool has not given it to you;
2. read the hot zones of `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md` and `ATLAS.md`;
3. read `git log --oneline -15`;
4. before the first change, say where things stand in four short lines: **Finished**, **Remaining**, **Blocked by** and **Next step**, writing "nothing" where a line is empty. Check them against `git log` and `git status`, not only against `ACTIVE.md`. Before honoring a `Blocked by` line from an earlier session, check its named source and say whether it holds; a missing or invalid source makes the blocker a guess.

Open anything else only when the task needs it; the index says where it is.

## Index

| File | Holds | Updated |
|---|---|---|
| `ACTIVE.md` | The work in progress: the piece being worked, the larger work it belongs to, what is pending and what blocks it | At every session end |
| `ABILITIES.md` | Every ability of the product: planned, in progress, done, retired | When an ability changes state |
| `AHEAD.md` | What the owner chose to plan: next up, milestones, ideas, research, spikes | When the owner adds, approves, schedules or drops an item |
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
- `AHEAD.md` when the owner adds, approves, schedules or drops an item, or a
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
- **Authorization:** A request authorizes what it asks to happen now, under its stated conditions; preparing for approval authorizes preparation only. A reserved approval requires an owner reply granting the named slice; record its date and words. An agent-written record, tests, a review verdict, a status label or an answer to another question cannot grant it. If a reply is unclear or approves one slice and defers another, work on the approved slice, do as much as it allows, state your reading and say what still waits. A missing specification, format or lint warning, or an open technical name adds no condition.
- **AHEAD is the owner's:** an agent proposes an item and does not write the row; the owner decides what enters `AHEAD.md`. What a session finds and will not do now is written down with its evidence where the work keeps its record, never in `AHEAD.md`, and shown to the owner when the work closes. Work with a defect or a required check open in what was asked is reported as unfinished.
- **Never:** <what an agent must never do: secrets in files, force-push, editing generated files>
- **Say what a code means:** when you write to a person, follow every identifier with its title in parentheses, every time: `AB-009 (Export invoices)`, `AH-007 (Gift vouchers)`. Take the title from the file name, heading or table row, and look it up if you don't have it. This applies to messages only: files, commit lines, code markers and test names keep the identifier their format requires.

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
