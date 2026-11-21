# AHEAD — <project>

> What the owner chose to plan, and what is under way from it: what comes next, milestones, ideas, research, spikes and proposals. Nothing enters without his decision.

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

Kind: `idea`, `research`, `spike`, `proposal`, `fix`. State: `open`, `approved`, `next`, `started`, `done`, `dropped`.

Below: Items, History, How to maintain this file.

<!-- hot zone ends -->

## Items

### AH-001 <title>

- **What:** <one or two lines>
- **Why:** <the reason or the question>
- **Write-up:** <docs/research/... or "none">
- **Entered:** <YYYY-MM-DD>, <the owner's words or request>
- **Decided:** <for approved or dropped: date, by whom, why>
- **Done:** <for done: YYYY-MM-DD, how it was checked, the work's commits or the work in words>

## History

Done and dropped items, moved here from the index.

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
  item starts; the row stays in the index, and the work appears in
  `ACTIVE.md`. An item that leaves Next up for a work section of `ACTIVE.md`
  goes back to `approved` until then.
- **Done:** when the work is finished and nothing of the owner's waits on it,
  the state becomes `done`, the entry gains its **Done** line and the row moves
  to History, in the work's own last commit. The line holds the date, how the
  work was checked, and the work's commits when they will survive the merge,
  else the work in words (the branch, the pull request); a proof in words
  alone counts. It never says whether the work is merged: a Done line on the
  default branch is merged. When the owner still has a step after the merge
  (a publish, an acceptance), the item stays `started` and the line goes in
  the commit that records his step.
- **A fix** is a planned repair. It names the ability it repairs, which may
  be `done` and does not change, or none (`—`).
- **Dropped:** the state becomes `dropped`, the row moves to History, and the
  entry says why and when. Identifiers are never reused.
- **Removed:** an item the owner never chose goes on his word only. Its row
  and its entry are deleted, its number stays used, and History gains one
  line: `Removed on the owner's word: AH-0xx, <YYYY-MM-DD>, "<his words>"`
  (several identifiers, or a range such as `AH-0xx to AH-0yy`, on one line).
- Milestones list the items and abilities they include and how we know they
  are reached.
- The check (`tools/check_tracking.py`) reports a kind or state outside the
  lists, an approved, next or started item without an ability (a fix aside), a
  link to nothing, a removed identifier that History does not name as removed
  on the owner's word, a new item whose entry has no Entered line with a date,
  a done item without its Done line, a Done line whose commit the default
  branch does not hold, a started item whose abilities are all done, an
  ability left in progress after all its items closed, and a row out of place.

Template: this file as it stands, with the placeholders in angle brackets.
