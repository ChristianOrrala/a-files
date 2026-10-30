# ACTIVE — <project>

> What is being done now: one current piece of work, what is pending in it and what blocks it. Not ideas, not future abilities.

## Now

- **Current work:** <AB-0xx and one line, or "none">
- **Progress:** <where it stands>
- **Next step:** <the next step in this work>
- **Blocked by:** <what blocks it, or "nothing">
- **Waiting on owner:** <a decision or an action, or "nothing">
- **Restart:** <the commands that bring a session back in>
- **Plan:** <docs/plans/... or "none">
- **Updated:** <YYYY-MM-DD>

## Pending

- [ ] <an unfinished, deferred or blocked item> (<why it waits, or what blocks it>)

## Debt

- <debt that will bite the next work>: <where it bites>

## Next new work

<only when Now has no current work: the first item of AHEAD's Next up, or, without AHEAD.md, what the owner chose next>

Below: How to maintain this file.

<!-- hot zone ends -->

## How to maintain this file

- **Now** is rewritten at the end of every session. Every field stays, with
  "none", "nothing" or "—" when empty. The hot zone stays under 60 lines.
- **One current piece of work.** Now names one piece of work at a time. Work
  that is blocked, or waits on the owner, moves to Pending or back to AHEAD
  (`AHEAD.md`); it never holds up unrelated work, which can then become the
  current work. In the small setup, with no `AHEAD.md`, it stays in Pending.
- **Pending** holds unfinished, deferred and blocked items, with what each
  waits on, and the owner's decisions they wait on. An item is deleted when it
  is done and committed; git keeps it.
- **Debt** holds debt that will bite the next work. Debt that can wait is an
  idea in `AHEAD.md`, or, in the small setup, a Pending item.
- **Next new work** is filled only when Now has no current work: the first
  item of AHEAD's Next up, or, in the small setup, what the owner chose next.
  This file never invents new work.
- Ideas, future abilities and milestones belong in `AHEAD.md`; abilities and
  their state in `ABILITIES.md`. In the small setup, which keeps neither,
  they are not tracked here.

Template: this file as it stands, with the placeholders in angle brackets.
