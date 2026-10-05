# AHEAD — Repair Desk

> Everything not started yet: what comes next, milestones, ideas, research, spikes and proposals. Nothing here is in progress.

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

Kind: `idea`, `research`, `spike`, `proposal`. State: `open`, `approved`, `next`, `started`, `dropped`.

Below: Items, History, How to maintain this file.

<!-- hot zone ends -->

## Items

### AH-001 Gift vouchers online

- **What:** sell repair vouchers on the booking page.
- **Why:** customers asked for them after paper vouchers were retired (AB-005).
- **Write-up:** none

### AH-002 Remind the customer by text the day before

- **What:** one text message the day before a booked repair.
- **Why:** about one booking in ten is a no-show.
- **Write-up:** [docs/research/01-sms-providers.md](docs/research/01-sms-providers.md)
- **Decided:** approved 2026-09-28 by the owner, after the spike.

### AH-003 Cancel a booking

- **What:** customers cancel online up to the evening before.
- **Why:** cancellations by phone took the workshop's time.
- **Write-up:** none
- **Decided:** approved 2026-09-20; started 2026-10-01 as AB-003.

### AH-004 Loyalty points

- **What:** points per repair, redeemable for parts.
- **Why:** proposed by a customer.
- **Write-up:** none
- **Decided:** dropped 2026-09-15 by the owner: the workshop prefers fair prices to points.

## History

Started and dropped items, moved here from the index so the hot zone stays short.

| ID | Title | Kind | State | Ability | Write-up |
|---|---|---|---|---|---|
| AH-003 | Cancel a booking | proposal | started | AB-003 | — |
| AH-004 | Loyalty points | idea | dropped | — | — |

## How to maintain this file

- A new idea, research question, spike or proposal gets the next free
  identifier, an index row with state `open`, and an entry under Items.
- **Approved:** state `approved` and an entry in `ABILITIES.md` (status
  `planned`). **Scheduled:** state `next`, in Next up. **Started:** state
  `started`, the row moves to History, the work appears in `ACTIVE.md`.
  **Dropped:** state `dropped`, the row moves to History, the entry says why.
