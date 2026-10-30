# ACTIVE — Repair Desk

> What is being done now: one current piece of work, what is pending in it and what blocks it. Not ideas, not future abilities.

## Now

- **Current work:** AB-003, cancel a booking: a customer cancels up to the evening before; the slot frees up
- **Progress:** cancellation rule and its tests done; the confirmation page is half built
- **Next step:** the confirmation page in `web/templates/`, then the guard check of the cut-off rule
- **Blocked by:** nothing
- **Waiting on owner:** the wording of the cancellation message
- **Restart:** `git switch feat/cancel-a-booking` and `python3 -m unittest discover -s tests`
- **Plan:** [docs/plans/2026-10-01-cancel-a-booking.md](docs/plans/2026-10-01-cancel-a-booking.md)
- **Updated:** 2026-10-03

## Pending

- [ ] Cancelling a booking that already has a diagnosis (deferred: the owner decides whether it is allowed)

## Debt

- Time-zone handling is spread over three functions in `src/booking.py`: every new time rule touches all three.

## Next new work

Not yet: AB-003 is in progress. After it, AHEAD's Next up starts with AH-002.

Below: How to maintain this file.

<!-- hot zone ends -->

## How to maintain this file

- **Now** is rewritten at the end of every session. Every field stays, with
  "none", "nothing" or "—" when empty. The hot zone stays under 60 lines.
- **One current piece of work.** Now names one piece of work at a time. Work
  that is blocked, or waits on the owner, moves to Pending or back to AHEAD
  (`AHEAD.md`); it never holds up unrelated work, which can then become the
  current work.
- **Pending** holds unfinished, deferred and blocked items, with what each
  waits on, and the owner's decisions they wait on. An item is deleted when it
  is done and committed; git keeps it.
- **Debt** holds debt that will bite the next work. Debt that can wait is an
  idea in `AHEAD.md`.
- **Next new work** is filled only when Now has no current work: the first
  item of AHEAD's Next up. This file never invents new work.
