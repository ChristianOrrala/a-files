# AHEAD — <project>

> Everything not started yet: what comes next, milestones, ideas, research, spikes and proposals. Nothing here is in progress.

## Next up

1. AH-0xx <title>

## Milestones

| Milestone | Exit check | Includes |
|---|---|---|
| <name> | <how we know it is reached> | AH-0xx, AB-0xx |

## Index

| ID | Title | Kind | State | Ability | Write-up |
|---|---|---|---|---|---|
| AH-001 | <title> | idea | open | — | — |

Kind: `idea`, `research`, `spike`, `proposal`. State: `open`, `approved`, `next`, `started`, `dropped`.

Below: Items, History, How to maintain this file.

<!-- hot zone ends -->

## Items

### AH-001 <title>

- **What:** <one or two lines>
- **Why:** <the reason or the question>
- **Write-up:** <docs/research/... or "none">
- **Decided:** <for approved or dropped: date, by whom, why>

## History

| ID | Title | Kind | State | Ability | Write-up |
|---|---|---|---|---|---|

## How to maintain this file

- A new idea, research question, spike or proposal gets the next free
  identifier, an index row with state `open`, and an entry under Items. A long
  write-up goes to `docs/research/` and the row links it.
- **Approved:** the state becomes `approved` and the item gets its entry in
  `ABILITIES.md` (status `planned`), named in the Ability column.
- **Scheduled:** the state becomes `next` and the item joins Next up, in order.
- **Started:** the state becomes `started`, the row moves to History, and the
  work appears in `ACTIVE.md`.
- **Dropped:** the state becomes `dropped`, the row moves to History, and the
  entry says why and when. Nothing is deleted; identifiers are never reused.
- Milestones list the items and abilities they include and how we know they
  are reached.
- The check (`tools/check_tracking.py`) refuses a kind or state outside the
  lists, an approved, next or started item without an ability, a link to
  nothing, and a removed identifier.

Template: this file as it stands, with the placeholders in angle brackets.
