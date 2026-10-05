# ABILITIES — Repair Desk

> Every ability of the product: planned, in progress, done or retired. One entry each, never deleted. Not the agent's abilities.

Status: `planned` (approved, not built), `in progress`, `done` (built, checked, evidence linked), `retired` (removed; the reason stays).

## Index

| ID | Ability | Status | Area |
|---|---|---|---|
| AB-001 | Book a repair | done | Booking |
| AB-002 | See the workshop's open work orders | done | Workshop |
| AB-003 | Cancel a booking | in progress | Booking |
| AB-004 | Remind the customer by text the day before | planned | Notifications |
| AB-005 | Paper vouchers at the counter | retired | Booking |

Below: Planned, Built, Retired, How to maintain this file.

<!-- hot zone ends -->

## Planned

### AB-004 Remind the customer by text the day before

- **Status:** planned
- **From:** AH-002
- **What it will do:** one text message the day before a booked repair, with the time and the address.

## Built

### AB-001 Book a repair

- **Status:** done
- **What it does:** a customer picks a day with a free slot, describes the problem and gets a work order number.
- **Known limits:** at most 8 repairs a day; no waiting list.
- **Next:** nothing planned
- **Evidence:** `tests/test_booking.py`

### AB-002 See the workshop's open work orders

- **Status:** done
- **What it does:** the workshop sees every open work order, newest drop-off day first.
- **Known limits:** no search.
- **Next:** AH-001
- **Evidence:** `tests/test_booking.py`

### AB-003 Cancel a booking

- **Status:** in progress
- **What it does:** a customer cancels up to the evening before; the slot frees up.
- **Known limits:** bookings with a diagnosis are not handled yet (ACTIVE, Pending).
- **Next:** nothing planned
- **Evidence:** `tests/test_booking.py`; plan `docs/plans/2026-10-01-cancel-a-booking.md`

## Retired

### AB-005 Paper vouchers at the counter

- **Status:** retired
- **Why:** the workshop stopped selling paper vouchers on 2026-06-30; gift vouchers may return online (AH-001).

## How to maintain this file

- An ability gets its entry when an item of `AHEAD.md` is approved, with
  status `planned`, under Planned. It moves to Built when work starts.
- The status changes in the same commit as the work, in the index row and in
  the entry together.
- Nothing is deleted. A removed ability becomes `retired`, moves under
  Retired, and keeps the reason. Identifiers are never reused.
