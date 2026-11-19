# ACTIVE — Repair Desk

> What is being done now: the piece being worked, the larger work it belongs to when there is one, what is pending and what blocks it. Not ideas, not future abilities.

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

Nothing: AB-003 is in progress, so the desk is not clear.

Below: How to maintain this file.

<!-- hot zone ends -->

## How to maintain this file

- **Now** is rewritten at the end of every session and names the piece being
  worked. Every field stays, with "none", "nothing" or "—" when empty. The hot
  zone stays under 60 lines.
- **The work section.** When the current work is one part of something larger
  the owner committed to, the hot zone holds one section more, between Now and
  Pending, headed by the name of that work. Its form follows the work. A
  reader must be able to recover from it: what the owner committed to, and how
  he will know it is done; what in it is unfinished; what can happen next, and
  what waits and on what; where the proof and the detail are. Four rules keep
  it short: each fact once (what Now, the plan or an item's entry says, the
  section points to); items by number, with a few words; a finished part
  shrinks to one line with its proof, then leaves; steps go in the plan. A
  task that fits in Now has no work section. When the work is done, the
  section is removed.
- **Committed work that waits stays here.** With a work section, the part that
  waits says what it waits on, and the agent takes another part of the same
  work that can go on. When none can, it says so and stops: nothing else
  starts until the owner says so, and the agent does not take the first item
  of Next up. If he starts other work, he says whether the committed work
  stays beside it or is put away; put away, the section becomes one Pending
  line with the date, his word and the plan to resume from.
- **One current piece of work.** Now names one current piece of work at a
  time. With no work section, work that is blocked, or waits on the owner,
  moves to Pending or back to AHEAD (`AHEAD.md`); it never holds up unrelated
  work, which can then become the current work.
- **Unfinished stays unfinished.** While a defect or a required check stands
  in what the owner asked for, that work, or that part of it, is unfinished
  here and in every report. Only the owner accepts less.
- **Pending** holds unfinished, deferred and blocked items, with what each
  waits on, and the owner's decisions they wait on. It also holds one line per
  piece of work whose findings await the owner: how many, and where they are,
  never one line per finding. An item is deleted when it is done and
  committed, a findings line when he has ruled; git keeps them.
- **Debt** holds debt that will bite the next work. Other debt is a finding:
  written down where the work keeps its record, for the owner to rule on. An
  agent never adds it to `AHEAD.md`.
- **Next new work** is filled only when the desk is clear, with no current
  work and no work section: the first item of AHEAD's Next up.
  Being first is not leave to start. This file never invents new work.
