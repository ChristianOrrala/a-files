# AGENTS.md

Repair Desk is a small web app where a bike workshop's customers book a
repair and the workshop tracks its work orders. Python, one service, code in
`src/`, pages in `web/`, tests in `tests/`. (An invented example.)

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

- Run: `python3 -m src.app`
- Test: `python3 -m unittest discover -s tests`
- Lint: `ruff check .`

## Rules

- **Always:** write the test for a booking rule before changing the rule; keep times in the workshop's time zone.
- **Ask first:** new dependencies, database schema changes, anything that sends a message to a real customer.
- **Never:** customer phone numbers or names in tests or logs; secrets in files; force-push.

Below: Before committing, Naming.

<!-- hot zone ends -->

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
