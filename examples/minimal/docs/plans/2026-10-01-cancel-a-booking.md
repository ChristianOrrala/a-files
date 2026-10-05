# Plan: cancel a booking

> One piece of work that spans sessions. Started 2026-10-01. Ability: AB-003. State: in progress.

## Goal

A customer cancels a booking online up to 18:00 the evening before; the slot
is free again at once. Checked by tests of the cut-off and of the freed slot,
each proven by a guard check.

## Steps

- [x] The cut-off rule and its boundary tests: 17:59 cancels, 18:00 is refused
- [x] The slot frees up: a cancelled day shows one more free slot
- [ ] The confirmation page: shows the work order number and the freed day
- [ ] Guard check of the cut-off rule: break it, see the test fail, restore
- [ ] Owner's wording for the cancellation message

## Progress log

- 2026-10-01: rule and tests done; branch `feat/cancel-a-booking`
- 2026-10-03: confirmation page started

## Decisions

- 2026-10-02: the cut-off is 18:00 in the workshop's time zone, because the workshop plans the next day at closing time

## Surprises

- Bookings that already have a diagnosis need a decision of the owner; deferred (ACTIVE, Pending).

## How to resume

`git switch feat/cancel-a-booking`, run `python3 -m unittest discover -s tests`
(green at the last commit), then build the confirmation page in
`web/templates/`.
