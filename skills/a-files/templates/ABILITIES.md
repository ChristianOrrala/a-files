# ABILITIES — <project>

> Every ability of the product: planned, in progress, done or retired. One entry each, never deleted. Not the agent's abilities.

Status: `planned` (approved, not built), `in progress`, `done` (built, checked, evidence linked), `retired` (removed; the reason stays).

## Index

| ID | Ability | Status | Area |
|---|---|---|---|
| AB-001 | <name> | done | <area> |

Below: Planned, Built, Retired, How to maintain this file.

<!-- hot zone ends -->

## Planned

### AB-0xx <name>

- **From:** AH-0xx
- **What it will do:** <one or two lines>
- **Specs:** <optional: use case identifiers, or links to the specifications that define it>

## Built

### AB-001 <name>

- **What it does:** <one or two lines>
- **Specs:** <optional: use case identifiers, or links to the specifications that define it>
- **Known limits:** <or "none known">
- **Next:** <AH-0xx, or "nothing planned">
- **Evidence:** <spec, tests, evaluation>

## Retired

### AB-0xx <name>

- **Why:** <reason, date>

## How to maintain this file

- An ability gets its index row, with status `planned`, and its entry under
  Planned when an item of `AHEAD.md` is approved. The entry moves to Built
  when work starts.
- The status lives in the index row only, and changes in the same commit as
  the work. An entry carries no Status line; an older entry that still has one
  is compared with its row, and a mismatch is reported.
- Nothing is deleted. A removed ability becomes `retired`, moves under
  Retired, and keeps the reason. Identifiers are never reused.
- **Next** names the AHEAD item that continues the ability, or says
  "nothing planned". **Evidence** links the spec, tests or evaluation.
- When the index outgrows the hot zone, keep the planned and in-progress rows
  in the hot zone and move the done and retired rows to an index table below
  it, named in the `Below:` line; each identifier keeps one row. When every
  ability is done, the hot zone may hold no ability row at all, only an area
  summary: a table that lacks any of the ID, Ability and Status columns is not
  an index, and the check ignores it.
- The check (`tools/check_tracking.py`) reports a missing entry, a status
  outside the list, an identifier listed twice, a removed identifier, and an
  old entry whose Status line disagrees with its row.

Template: this file as it stands, with the placeholders in angle brackets.
