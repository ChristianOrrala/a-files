# ACTIVE — <project>

> What is being done now, and what must be resolved before new work starts. Not ideas, not future abilities.

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

- [ ] <an unfinished or deferred item of the current work> (<why it waits>)

## Debt

- <debt that blocks new work>: <where it bites>

## Next new work

<only when Now has no current work: the first item of AHEAD's Next up>

Below: How to maintain this file.

<!-- hot zone ends -->

## How to maintain this file

- **Now** is rewritten at the end of every session. Every field stays, with
  "none", "nothing" or "—" when empty. The hot zone stays under 60 lines.
- **Pending** holds unfinished or deferred items of the current work, and the
  owner's decisions it waits on. An item is deleted when it is done and
  committed; git keeps it.
- **Debt** holds debt that blocks new work or will bite it. Debt that can wait
  is an idea in `AHEAD.md`.
- **Next new work** is filled only when Now has no current work: the first
  item of AHEAD's Next up. This file never invents new work.
- Ideas, future abilities and milestones belong in `AHEAD.md`; abilities and
  their state in `ABILITIES.md`. See METHOD.md.

Template: this file as it stands, with the placeholders in angle brackets.
