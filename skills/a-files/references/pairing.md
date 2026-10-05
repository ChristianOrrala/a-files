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
| P1 | `AGENTS.md` | The specification rules section sits below the hot zone and is named in its `Below:` line. The keep-in-step list says that a use case changing Status is followed by the ability whose `Specs` line names it, and that a newly mapped use case joins an ability's `Specs` line. |
| P2 | `ABILITIES.md` | An ability entry may carry `- **Specs:**` with use case identifiers (`UC-003, UC-007`) or relative links to specification files. An ability is `done` only when every use case it names is `Done`, and it is not `planned` while one of them is `Implemented`, `Tested` or `Done`. |
| P3 | `ACTIVE.md`, `AHEAD.md` | The next step comes from the current work first: the use cases and abilities `ACTIVE.md` names; when there is no current work, the first item of AHEAD's Next up, through its ability's `Specs` line. A use case that is `Implemented` or `Tested` and not named by the current work is a mismatch to resolve. |
| P4 | `AHEAD.md` | A deferred requirement keeps its row in the requirements catalog; an AHEAD item cites its identifier (`FR-012`). A change request accepted for later becomes an AHEAD item that links its change record. A recovery change log entry decided `later` becomes an AHEAD item that cites it; the entries of one use case share one item. Nothing is copied. |
| P5 | `ATLAS.md` | One row maps the specifications: their folder and files, and the checks that cover them. |
| P6 | The finish check | A change that moves a use case's Status while `ABILITIES.md` and `ACTIVE.md` stay unchanged gets a warning. |
| P7 | The session start | The state shown when a session starts includes the current work from `ACTIVE.md`. |
| P8 | `docs/decisions/` | Decision records follow the A-files naming: four digits, then the subject. |
<!-- pairing contract: end -->

## The joining edits

**P1.** In the hot zone of `AGENTS.md`, the `Below:` line gains
`Working from specifications` (a `Below:` line is added above the marker when
there is none). The keep-in-step list gains, before its last item:

    - `ABILITIES.md` when a use case changes Status: the ability whose `Specs` line names it follows it;
    - `ABILITIES.md` when a use case is mapped: it joins an ability's `Specs` line;

**P5.** The map table of `ATLAS.md` gains one row, with paths in backticks only
for what exists:

    | Specifications | What the system does, written before it is built | `docs/vision.md`, `docs/use_cases/`, `docs/test_cases/` | — | the validator and the lint of the specification skills |

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

## What the specification side does

Its router reads ACTIVE's current work and AHEAD's Next up (P3) and shows the
current work when a session starts (P7); its finish check warns when a use
case moves alone (P6); its setup makes the P1 and P5 edits when it arrives
second; its use-case mapping suggests the ability each new use case joins.
