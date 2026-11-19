# AGENTS.md

Repair Desk is a small web app where a bike workshop's customers book a
repair and the workshop tracks its work orders. Python, one service, code in
`src/`, pages in `web/`, tests in `tests/`. (An invented example.)

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

- Run: `python3 -m src.app`
- Test: `python3 -m unittest discover -s tests`
- Lint: `ruff check .`

## Rules

- **Always:** write the test for a booking rule before changing the rule; keep times in the workshop's time zone.
- **Ask first:** new dependencies, database schema changes, anything that sends a message to a real customer.
- **AHEAD is the owner's:** an agent proposes an item and does not write the row; the owner decides what enters `AHEAD.md`. What a session finds and will not do now is written down with its evidence where the work keeps its record, never in `AHEAD.md`, and shown to the owner when the work closes. Work with a defect or a required check open in what was asked is reported as unfinished.
- **Never:** customer phone numbers or names in tests or logs; secrets in files; force-push.
- **Say what a code means:** when you write to a person, follow every identifier with its title in parentheses, every time: `AB-009 (Export invoices)`, `AH-007 (Gift vouchers)`. Take the title from the file name, heading or table row, and look it up if you don't have it. This applies to messages only: files, commit lines, code markers and test names keep the identifier their format requires.

## Before committing

```bash
python3 -m unittest discover -s tests
python3 tools/check_tracking.py
```

## Naming

| What | Convention | Example |
|---|---|---|
| Decision records | Four digits, never reused, then the subject | `docs/decisions/0001-adopt-the-a-files.md` |
| Plans | The date the work started, then the subject | `docs/plans/2026-10-01-cancel-a-booking.md` |
| Research and spikes | Two digits, then the subject | `docs/research/01-sms-providers.md` |
| Abilities and AHEAD items | `AB-` or `AH-` and three digits | `AB-003`, `AH-002` |
| Commit subjects | Area, colon, what changed | `booking: refuse a ninth repair on a full day` |
