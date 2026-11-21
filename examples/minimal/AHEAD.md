# AHEAD — Repair Desk

> What the owner chose to plan, and what is under way from it: what comes next, milestones, ideas, research, spikes and proposals. Nothing enters without his decision.

## Next up

1. AH-002 Remind the customer by text the day before

## Milestones

| Milestone | Exit check | Includes |
|---|---|---|
| 1.1, fewer no-shows | Cancellation and reminders in production; no-shows counted for four weeks | AB-003, AH-002, AB-004 |

## Index

| ID | Title | Kind | State | Ability | Write-up |
|---|---|---|---|---|---|
| AH-001 | Gift vouchers online | idea | open | AB-002 | — |
| AH-002 | Remind the customer by text the day before | proposal | next | AB-004 | [research 01](docs/research/01-sms-providers.md) |
| AH-003 | Cancel a booking | proposal | started | AB-003 | — |

Kind: `idea`, `research`, `spike`, `proposal`, `fix`. State: `open`, `approved`, `next`, `started`, `done`, `dropped`.

Below: Items, History, How to maintain this file.

<!-- hot zone ends -->

## Items

### AH-001 Gift vouchers online

- **What:** sell repair vouchers on the booking page.
- **Why:** customers asked for them after paper vouchers were retired (AB-005).
- **Write-up:** none
- **Entered:** 2026-09-12, the owner: "keep the vouchers idea, I'll decide after the season"

### AH-002 Remind the customer by text the day before

- **What:** one text message the day before a booked repair.
- **Why:** about one booking in ten is a no-show.
- **Write-up:** [docs/research/01-sms-providers.md](docs/research/01-sms-providers.md)
- **Entered:** 2026-09-14, the owner: "add reminders by text, with a spike on the providers first"
- **Decided:** approved 2026-09-28 by the owner, after the spike.

### AH-003 Cancel a booking

- **What:** customers cancel online up to the evening before.
- **Why:** cancellations by phone took the workshop's time.
- **Write-up:** none
- **Entered:** 2026-09-08, the owner asked for it after a week of phone cancellations
- **Decided:** approved 2026-09-20; started 2026-10-01 as AB-003.

### AH-004 Loyalty points

- **What:** points per repair, redeemable for parts.
- **Why:** proposed by a customer.
- **Write-up:** none
- **Entered:** 2026-09-10, the owner: "note the points idea"
- **Decided:** dropped 2026-09-15 by the owner: the workshop prefers fair prices to points.

### AH-005 Two bookings for the same slot

- **What:** two customers who book the last slot at the same moment both get it; the second is refused.
- **Why:** it happened twice in October (AB-001).
- **Write-up:** none
- **Entered:** 2026-10-20, the owner: "fix the double booking"
- **Decided:** approved 2026-10-20 by the owner.
- **Done:** 2026-10-24, a test books the last slot twice at once and the second is refused; work on the branch `fix/same-slot`

## History

Done and dropped items, moved here from the index so the hot zone stays short.

| ID | Title | Kind | State | Ability | Write-up |
|---|---|---|---|---|---|
| AH-005 | Two bookings for the same slot | fix | done | AB-001 | — |
| AH-004 | Loyalty points | idea | dropped | — | — |

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
- **Approved:** state `approved`, and the ability gets its row in
  `ABILITIES.md` (status `planned`) and its entry. **Scheduled:** state
  `next`, in Next up. **Started:** state `started`, the row stays in the
  index, the work appears in `ACTIVE.md`. **Done:** state `done`, a **Done**
  line in the entry (the date, how it was checked, the work's commits or the
  work in words), the row moves to History. **Dropped:** state `dropped`, the
  row moves to History, the entry says why.
- A `fix` is a planned repair: it names the ability it repairs, which may be
  done, or none.
- **Removed:** an item the owner never chose goes on his word only. Its row
  and its entry are deleted, its number stays used, and History gains one
  line: `Removed on the owner's word: AH-0xx, <YYYY-MM-DD>, "<his words>"`
  (several identifiers, or a range such as `AH-0xx to AH-0yy`, on one line).
