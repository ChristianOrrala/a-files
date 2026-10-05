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

- **Status:** planned
- **From:** AH-0xx
- **What it will do:** <one or two lines>
- **Specs:** <optional: use case identifiers, or links to the specifications that define it>

## Built

### AB-001 <name>

- **Status:** done
- **What it does:** <one or two lines>
- **Specs:** <optional: use case identifiers, or links to the specifications that define it>
- **Known limits:** <or "none known">
- **Next:** <AH-0xx, or "nothing planned">
- **Evidence:** <spec, tests, evaluation>

## Retired

### AB-0xx <name>

- **Status:** retired
- **Why:** <reason, date>

## How to maintain this file

- An ability gets its entry when an item of `AHEAD.md` is approved, with
  status `planned`, under Planned. It moves to Built when work starts.
- The status changes in the same commit as the work, in the index row and in
  the entry together.
- Nothing is deleted. A removed ability becomes `retired`, moves under
  Retired, and keeps the reason. Identifiers are never reused.
- **Next** names the AHEAD item that continues the ability, or says
  "nothing planned". **Evidence** links the spec, tests or evaluation.
- When the index outgrows the hot zone, keep the planned and in-progress rows
  and one row per area in the hot zone, and move the full index below it.
- The check (`tools/check_tracking.py`) refuses a missing entry, a status
  outside the list, a mismatch between index and entry, and a removed
  identifier.

Template: this file as it stands, with the placeholders in angle brackets.
