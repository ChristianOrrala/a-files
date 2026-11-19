# ACTIVE — <project>

> What is being done now: the piece being worked, the larger work it belongs to when there is one, what is pending and what blocks it. Not ideas, not future abilities.

## Now

- **Current work:** <AB-0xx and one line, or "none">
- **Progress:** <where it stands>
- **Next step:** <the next step in this work>
- **Blocked by:** <what it stops and its source: owner message and date, specification ID or file path, or failing check: name; or "nothing">
- **Waiting on owner:** <a decision or an action, or "nothing">
- **Restart:** <the commands that bring a session back in>
- **Plan:** <docs/plans/... or "none">
- **Updated:** <YYYY-MM-DD>

## Pending

- [ ] <an unfinished, deferred or blocked item> (<why it waits, or what blocks it>)
- [ ] <findings of a piece of work, for the owner to rule on>: <how many>, in <where they are>

## Debt

- <debt that will bite the next work>: <where it bites>

## Next new work

<only when the desk is clear, with no current work and no work section: the first item of AHEAD's Next up, or, without AHEAD.md, what the owner chose next>

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
  work, which can then become the current work. In the small setup, with no `AHEAD.md`, it stays in Pending.
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
  work and no work section: the first item of AHEAD's Next up, or, in the small setup, what the owner chose next.
  Being first is not leave to start. This file never invents new work.
- Ideas, future abilities and milestones belong in `AHEAD.md`; abilities and
  their state in `ABILITIES.md`. In the small setup, which keeps neither,
  they are not tracked here.

A work section, as an example; its form is free:

```markdown
## <the committed work> (AB-0xx)

Done when <how the owner will know it is done>.

| Part | State | Proof |
|---|---|---|
| 1. <a finished part> | done | <commit, test or record> |
| 2. <the part Now names> | now | |
| 3. <a part that waits> | waits on <what, with its source> | |
| 4. <a later part, or an item: AH-0xx and a few words> | later | |
```

Template: this file as it stands, with the placeholders in angle brackets.
