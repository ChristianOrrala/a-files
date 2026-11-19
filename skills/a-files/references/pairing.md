# Pairing with a specification method

The A-files track the work; a specification method writes down what the
system does. When a project uses both, the rules below join them. Each keeps
its own files, and neither moves the other's.

## Detection

The A-files are present when `ACTIVE.md` at the root holds the line
`<!-- hot zone ends -->`. A use-case method is present when the guideline file
(`AGENTS.md` or `CLAUDE.md`) holds the section `## Working from specifications`;
other methods are recognized by their folders (`specs/`, `.kiro/specs/`,
`openspec/`). Whichever is set up second makes the joining edits (P1 and P5);
joining twice changes nothing.

## The contract

<!-- pairing contract: start -->
| # | Where | Rule |
|---|---|---|
| P1 | `AGENTS.md` | The joining holds for an `AGENTS.md` with or without an end of hot zone. With one, the specification rules section sits below the hot zone and is named in its `Below:` line; without one, the section stands at the end of the file and nothing names it. When the project keeps `ABILITIES.md` (the file exists or the index lists it: a row of the index table, wherever the table sits), the keep-in-step list says that a use case changing Status is followed by the ability whose `Specs` line names it, and that a newly mapped use case joins an ability's `Specs` line; a small setup without it gets neither row. |
| P2 | `ABILITIES.md` | An ability entry may carry `- **Specs:**` with use case identifiers (`UC-003, UC-007`) or relative links to specification files. An ability is `done` only when every use case it names is `Done`, and it is not `planned` while one of them is `Implemented`, `Tested` or `Done`. An ability `in progress` whose use cases are all `Done` is reported: mark it `done`, or name in its `Specs` line the use case still to build. An ability whose use cases wait only on acceptance outstanding is not blocked; work it does not touch goes on. |
| P3 | `ACTIVE.md`, `AHEAD.md` | The next step comes from the current work first: the use cases and abilities `ACTIVE.md` names; when there is no current work and `ACTIVE.md` holds no work section (work the owner committed to, which keeps the desk), the first item of AHEAD's Next up, through its ability's `Specs` line. A use case that is `Implemented` or `Tested` and not named by the current work is a mismatch to resolve. |
| P4 | `AHEAD.md` | `AHEAD.md` is entered on the owner's decision, so the specification side writes an item only where he chose. A deferred requirement keeps its row in the requirements catalog; an AHEAD item cites its identifier (`FR-012`). A change request the person accepts for later becomes an AHEAD item that links its change record. A recovery change log entry decided `later` becomes an AHEAD item that cites it, written on the owner's yes; the entries of one use case share one item. Each of these items carries its **Entered** line: the date and his words. A new item without it is reported by the check as `ITEM_WITHOUT_DECISION`. A missing use case noted while implementing goes to the specification side's own open-work list. Nothing is copied. |
| P5 | `ATLAS.md` | One row maps the specifications: their folder and files, and the checks that cover them. |
| P6 | The finish check | A change that moves a use case's Status while `ABILITIES.md` and `ACTIVE.md` stay unchanged gets a warning. |
| P7 | The session start | The state shown when a session starts includes the current work and the Debt from `ACTIVE.md`, and the Next up list from `AHEAD.md`. |
| P8 | `docs/decisions/` | Decision records follow the A-files naming: four digits, then the subject. |
| P9 | `AHEAD.md` | A drift to align later, whether the person answered so at the end of an agent's turn or nobody was present to ask, never becomes an AHEAD item: it goes to the specification side's own open-work list, shown at session start, where the owner may make it an item. The same drift is recorded once. |
| P10 | `tools/check_tracking.py` | Whatever reads the A-files check from outside its code (the a-files plugin's end-of-turn hook, or a tool of the specification side) reads it only through its command line, so that command line is part of this contract: the reader runs the check with `--strict`, and again without it when the check exits 2 (an earlier check that does not know the option); exit 0 means the A-files are clean and nothing is sent; exit 1 means problems, each printed as one line `path:line: ERROR CODE: message`; any other exit code means the check could not run, and nothing is sent. A message names its subject as an identifier, a quoted or bold name, or a path, and a number in it is a count or a position, so a finding whose count or position changes is the same finding. |
<!-- pairing contract: end -->

## The joining edits

**P1.** Where `AGENTS.md` has an end of hot zone, the `Below:` line in its hot
zone gains `Working from specifications` (a `Below:` line is added above the
marker when there is none). An `AGENTS.md` without the marker needs no naming:
the rules section stands at the end of the file. In both forms the
keep-in-step list gains, before its last item:

    - `ABILITIES.md` when a use case changes Status: the ability whose `Specs` line names it follows it;
    - `ABILITIES.md` when a use case is mapped: it joins an ability's `Specs` line;

**P5.** The map table of `ATLAS.md` gains one row, with paths in backticks only
for what exists:

    | Specifications | What the system does, written before it is built | `docs/vision.md`, `docs/use_cases.md`, `docs/use_cases/`, `docs/test_cases/` | — | the validator and the lint of the specification skills |

With another method, the row names that method's folder.

## What the A-files side does

- The check verifies that every link and backticked path in a `Specs` line
  points at a file. Identifiers are left to the specification method, which
  knows its files.
- When it adopts the A-files in a project that has specifications, the skill
  proposes abilities from the use case map or the specification folders, each
  with its `Specs` line, for the person to accept. Use cases already `Done`
  make their abilities `done`, with the specifications as evidence; use cases
  in progress go into ACTIVE's Now; a deferred requirement is cited from
  AHEAD, never copied.
- When `ABILITIES.md` delegates to a kept file (`- **Home:**`), abilities take
  no part in the pairing: no `Specs` line is read, and the specification side
  says so instead of checking statuses.

The plugin's agent hooks send the note before the first edit and the check's
findings at the end of a turn. With a specification method installed too, those
two come from here only; the other side's hooks leave them out, so each arrives
once.

## What the specification side does

Its router reads ACTIVE's current work and AHEAD's Next up (P3) and shows the
current work, the Debt and the Next up list when a session starts (P7); its
finish check warns when a use case moves alone (P6); its setup makes the P1 and P5 edits when it arrives
second; with `ABILITIES.md`, its use-case mapping suggests the ability each new
use case joins; its
end-of-turn question records a drift the person puts off as an AHEAD item in
the shape P9 states: outside setup, its one edit to an A-file, and only on the
person's answer. It does not run this side's check: the A-files' findings at
the end of a turn come from this side's hook, which reads the check through its
command line and its output lines alone (P10); changing the option, the exit
codes or the line format is a change to the contract.
