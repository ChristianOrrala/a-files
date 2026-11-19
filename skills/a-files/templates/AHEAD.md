# AHEAD — <project>

> What the owner chose to plan: what comes next, milestones, ideas, research, spikes and proposals. Nothing here is in progress, and nothing enters without his decision.

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
- **Entered:** <YYYY-MM-DD>, <the owner's words or request>
- **Decided:** <for approved or dropped: date, by whom, why>

## History

| ID | Title | Kind | State | Ability | Write-up |
|---|---|---|---|---|---|

## How to maintain this file

- **An item enters on the owner's decision.** An agent proposes an item, in
  its report or when asked, and does not write the row. When the owner asks
  for an item, or says yes to a proposal, it gets the next free identifier, an
  index row with state `open`, an entry under Items and, in that entry, the
  **Entered** line: the date and his words or request. A long write-up goes to
  `docs/research/` and the row links it. Widening an item that exists needs
  his decision too.
- What a session finds and will not do now is written down where the work
  keeps its record, never here; the owner rules on it when the work closes.
- **Approved:** the state becomes `approved`, and the ability gets its index
  row in `ABILITIES.md` (status `planned`) and its entry; the item names it in
  the Ability column.
- **Scheduled:** the state becomes `next` and the item joins Next up, in order.
- **Started:** the state becomes `started`, once, when the first work on the
  item starts; the row moves to History, and the work appears in `ACTIVE.md`.
  An item that leaves Next up for a work section of `ACTIVE.md` goes back to
  `approved` until then.
- **Dropped:** the state becomes `dropped`, the row moves to History, and the
  entry says why and when. Identifiers are never reused.
- **Removed:** an item the owner never chose goes on his word only. Its row
  and its entry are deleted, its number stays used, and History gains one
  line: `Removed on the owner's word: AH-0xx, <YYYY-MM-DD>, "<his words>"`
  (several identifiers, or a range such as `AH-0xx to AH-0yy`, on one line).
- Milestones list the items and abilities they include and how we know they
  are reached.
- The check (`tools/check_tracking.py`) reports a kind or state outside the
  lists, an approved, next or started item without an ability, a link to
  nothing, a removed identifier that History does not name as removed on the
  owner's word, and a new item whose entry has no Entered line with a date.

Template: this file as it stands, with the placeholders in angle brackets.
