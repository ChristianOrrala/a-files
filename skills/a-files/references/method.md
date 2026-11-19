# The A-files

*Five files every coding agent reads first.*

Version 2.2.1, 2026-11-19

A way for a repository to keep its rules, its current work, its abilities, its
future and its map in five Markdown files at the root, so that any coding
agent (Claude Code, Codex, Gemini through Antigravity, Cursor, Copilot) and
any person starts every session from the same picture, and the picture stays
true.

## Contents

1. [Why](#1-why)
2. [The five files](#2-the-five-files)
3. [Hot zones and the warm-up](#3-hot-zones-and-the-warm-up)
4. [Keeping the files in step](#4-keeping-the-files-in-step)
5. [The life of an item](#5-the-life-of-an-item)
6. [Identifiers and states](#6-identifiers-and-states)
7. [The other homes](#7-the-other-homes)
8. [The check and the hook](#8-the-check-and-the-hook)
9. [Wiring each agent](#9-wiring-each-agent)
10. [Adopting the method](#10-adopting-the-method)
11. [Naming](#11-naming)
12. [Limits](#12-limits)
13. [Questions](#13-questions)
14. [Pairing with a specification method](#14-pairing-with-a-specification-method)

## 1. Why

Agents start every session knowing nothing about where the work stands. The
usual answer, one long instruction file plus a status note, fails in known
ways, as the research behind the method found:

- **Long instruction files cost more than they help.** Instruction following
  drops as instructions multiply, and earlier lines are followed better.
- **Status notes go stale or bloat,** and an agent rewrites Markdown readily:
  a finished feature disappears, a wish list grows.
- **Rules written as prose are skipped** by some models some of the time;
  rules enforced by a script hold.

The method answers with five single-purpose files read at every start (the
guide whole, the top part of the other four), a rule to update them with the
work, stable identifiers that are never reused, and a check that reports, at
every commit, what breaks their shape; it informs and never refuses the
commit.

**Who they serve.** The A-files serve one owner directing agents, not a team
tracker. One person decides what the work is; the agents, in one session or
several, read the same picture and keep it in step. A team that needs
assignments, reviews and parallel boards uses an issue tracker beside them
(section 13).

## 2. The five files

| File | Job | Never holds |
|---|---|---|
| `AGENTS.md` | How to work in this repository and where to look next: what it is, the warm-up, the index of every file an agent needs, the keep-in-step rule, the commands and the local rules | State, plans, history: anything another file owns |
| `ACTIVE.md` | What is being done now: the piece being worked, the larger work it belongs to when the owner committed to one, pending, blocked and deferred items, debt | Ideas, future abilities |
| `ABILITIES.md` | Every ability of the product, planned, in progress, done or retired; one entry each, never deleted | The agent's own abilities; ideas not approved |
| `AHEAD.md` | What the owner chose to plan: the next-up queue, milestones, ideas, research, spikes and proposals, each pointing to its full write-up. Nothing enters without his decision | Work in progress; what a session found and nobody chose |
| `ATLAS.md` | The architecture map: each part of the repository, what it does, the files it works through, what it depends on, what checks it | A full file index |

All five start with A so they are recognized and sorted together as one set.
The names were chosen against the meanings agent tools already give to
others: "atlas" is the common name for a codebase map, which is exactly this
file's job; `ABILITIES.md` says in its first line that it is not about the
agent's own abilities, a reading the word invites.

A repository keeps one map: `ATLAS.md` replaces an `ARCHITECTURE.md`.

**What `AGENTS.md` is for.** The tools that read it load the whole file into
every session (section 9), so each line in it is paid for at every start, and
believed. Each live fact has one home, and `AGENTS.md` names that home instead
of copying from it: the current work is in `ACTIVE.md`, what the product can do
in `ABILITIES.md`, the plan in `AHEAD.md`, the map in `ATLAS.md`, a rule's date
and story in its decision record. A copy goes stale when its home changes, and
an agent follows the copy. A rule keeps its exception and its reason beside
it, where losing them would change what an agent does. A procedure for one
kind of task keeps, in `AGENTS.md`, what triggers it and its one essential
constraint, with the path to the rest.

Three questions for whoever edits the file, agent or owner. Nothing checks
them:

1. **What could an agent get wrong before it finds the fuller source?** Keep
   the shortest wording that still carries the trigger, the exception and the
   reason.
2. **Which file owns this fact?** If it changes with the work, it lives there,
   and `AGENTS.md` names the file.
3. **What is the evidence for dropping it?** An obsolete claim, a conflict, an
   exact copy. Check that the instruction can still be reached when it is
   needed.

A file that is already right passes with no edits, and may come out just as
long.

**The small setup and the full one.** A small repository may keep only
`AGENTS.md` and `ACTIVE.md`: the rules and the current work. The full setup
adds `ABILITIES.md`, `AHEAD.md` and `ATLAS.md`. A small setup grows later:
add a file from its template and name it in the index of `AGENTS.md`, and
from then on the check expects it. The warm-up reads the hot zones of the
files the repository has.

Without `AHEAD.md`, blocked work stays in ACTIVE's Pending, and Next new work
names what the owner chose next, since there is no Next up to take it from.
Without `ABILITIES.md`, abilities are not tracked: the current work names
what it changes in its own words.

## 3. Hot zones and the warm-up

**Hot zone.** The top of `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md` and `ATLAS.md`,
ended by a line that says exactly:

```text
<!-- hot zone ends -->
```

| File | Hot zone cap | Holds in its hot zone |
|---|---|---|
| `ACTIVE.md` | 60 lines | Now (fixed fields), the work section when there is one, Pending, Debt, Next new work |
| `ABILITIES.md` | 100 lines | Contract, status list, index (done rows may sit in a table below) |
| `AHEAD.md` | 100 lines | Next up, milestones, index of open items |
| `ATLAS.md` | 100 lines | The map table, the flow |

Each of the four opens with its title and a one-line contract in a quotation
block (`> ...`). Everything below a hot zone is reached only through a pointer
in it: the hot zone ends with a line such as `Below: Items, History, How to
maintain this file.`

`AGENTS.md` has no hot zone and no cap in lines: the tools load it whole, so a
line that ends a zone saves nothing there. What keeps it short is what it is
for (section 2). A repository adopted earlier may keep the marker in its
`AGENTS.md`; it does no harm, and the skill's review of the file offers to take
it out once the tools installed in the repository read the file without it.

**Warm-up.** At every session start an agent does the following, in order:

1. follow `AGENTS.md`: the tool has usually supplied it, and the agent opens
   it once if it has not;
2. read the hot zones of `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md` and `ATLAS.md`
   (those the repository keeps);
3. read `git log --oneline -15`;
4. before the first change, say where things stand in four short lines: **Finished**, **Remaining**, **Blocked by** and **Next step**, writing "nothing" where a line is empty. Check them against `git log` and `git status`, not only against `ACTIVE.md`.

Check the source before honoring a carried-over blocker and say so.
**Remaining** names the unfinished parts of committed work, and any line of
ACTIVE's Pending that says findings await the owner.

The owner sees the agent’s picture before any work, and a stale `ACTIVE.md` shows up early.

The four hot zones are at most 360 lines at their caps; `AGENTS.md` is as long as it needs to be. Anything else is opened when the task needs it.

`AGENTS.md` names the other files by path and never imports them (`@file`):
an import loads the whole file in every session.

## 4. Keeping the files in step

The rule in `AGENTS.md`: in the same commit as the work, an agent updates

| When it | It updates |
|---|---|
| Starts, finishes, defers or drops work | `ACTIVE.md` |
| Changes an ability's state | `ABILITIES.md` |
| Records that the owner added, approved, scheduled or dropped an item, or finishes a spike | `AHEAD.md`, and `ABILITIES.md` when an item is approved |
| Adds, moves, renames or removes a part of the repository | `ATLAS.md` |
| Makes or records a decision or a standing rule | `docs/decisions/` |

Two more rules:

- **One editor.** Only the main session edits the A-files. Parallel workers
  (subagents, other branches) report to it; shared status files are where
  parallel work collides.
- **One home per fact.** A standing rule is a decision record, never only a
  line in `ACTIVE.md`. A limit of one ability is in its entry, never repeated
  as debt.

A request authorizes what it asks to happen now, under its stated conditions; preparing for approval authorizes preparation only. A reserved approval requires an owner reply granting the named slice; record its date and words. An agent-written record, tests, a review verdict, a status label or an answer to another question cannot grant it. If a reply is unclear or approves one slice and defers another, work on the approved slice, do as much as it allows, state your reading and say what still waits. A missing specification, format or lint warning, or an open technical name adds no condition. Record the reply where the method records the decision or approval.

## 5. The life of an item

```text
found by a session      ─► written down where the work keeps its record; the owner rules on it (below)
entered by the owner    ─► AHEAD (open, with its Entered line; a write-up in docs/research/ when it is long)
approved                ─► AHEAD (approved) + an ABILITIES index row (status planned) and its entry
scheduled               ─► AHEAD (next), in the Next up queue
started                 ─► ACTIVE current work, or a part of its work section; ABILITIES in progress;
                           AHEAD (started), once, row moved to History; a plan in docs/plans/ when the
                           work spans sessions
done                    ─► ABILITIES done, with evidence; gone from ACTIVE; CHANGELOG at release
dropped                 ─► AHEAD (dropped), row moved to History, the entry says why
```

**The work section.** A task fits in Now. Work the owner commits to for days
or weeks does not: a refactor in stages, a road to a release, a handful of
items taken together. For that work ACTIVE's hot zone holds one section more,
between Now and Pending, headed by the name of the committed work and the
ability it builds when there is one. Now keeps its eight fields and names the
piece being worked; between two pieces its Current work may say "none" while
the section stays.

The section's form follows the work: a table of parts, a short list of item
numbers with a state each, a question with what is known so far. The method
fixes only what a reader must be able to recover from it:

1. what the owner committed to, and how he will know it is done;
2. what in it is unfinished;
3. what can happen next, and what waits and on what;
4. where the proof and the detail are.

Four rules keep it from becoming a second backlog or a history:

- **Each fact once.** What Now says, the section does not repeat. What the
  plan or an item's entry says, the section points to.
- **Items by number.** An AHEAD item or an ability appears by its identifier
  and a few words. Its text stays in its entry.
- **Finished parts shrink, then leave.** A finished part keeps at most one
  line with a pointer to its proof, and only while that line helps a reader
  resume. A tick with no proof is not a finished part.
- **Steps go in the plan.** The section names parts. The steps inside a part
  are in the plan under `docs/plans/`, which committed work always has.

**When committed work has to wait.** The work section stays on the desk, and
the part that waits says what it waits on, with the source a blocker needs.
The agent takes another part of the same work that can go on. When none can,
it says so and stops: nothing else starts until the owner says so, and the
agent does not take the first item of Next up. If the owner starts unrelated
work, he says whether the committed work stays on the desk beside it or is put
away. Put away, the section is removed and one Pending line takes its place,
with the date, his word and the plan to resume from. One work section at a
time is the default; a second joins only on his word.

**One current piece of work.** Now names one current piece of work at a time.
With no work section, work that is blocked, or waits on the owner, moves to
Pending or back to AHEAD, with what it waits on; it never holds up unrelated
work, which can then become the current work. When the desk is clear, with no
current work and no work section, `ACTIVE.md` names the first item of AHEAD's
Next up as the next new work. Being first is not leave to start, and
`ACTIVE.md` never invents new work.

**Items inside committed work.** An item named in a work section keeps its
row and its state until the first part that works on it starts; from then it
is `started`, once, however many parts it spans. An item is in a work section
or in Next up, never both: one that leaves Next up for a section goes back to
`approved` in the same commit. A part that matches no item changes nothing in
`AHEAD.md`.

**What a session finds.** A finding is something a session notices and will
not do now: a defect, a missing check, a debt, an improvement, a question. The
method fixes three things about it and no more:

1. **It is written down with its evidence, and never in `AHEAD.md`.** Where is
   the agent's choice: it knows how the repository keeps its records. For an
   agent with no place of its own, the default is the plan of the work that
   found it, under Surprises; for a short task with no plan, a list below
   ACTIVE's hot zone that the hot zone names.
2. **The next session can find it.** ACTIVE's Pending carries one line per
   piece of work, never one per finding: how many findings await the owner, and
   where they are.
3. **The owner rules on it.** When the work closes or is handed off, the
   session shows him what it found outside what he asked for, with related
   small things proposed together. He chooses, for each or for the lot: do
   them now in one go, make an item (section 6), or drop them. Once he has
   ruled, the Pending line goes.

A finding that needs the owner's answer before the work can go on is not
parked: it goes to Waiting on owner. A session that ends without the owner
leaves the Pending line in place, and the next warm-up says it under
Remaining. Debt that will bite the next work stays in ACTIVE's Debt; other
debt is a finding.

**The result asked for stays binding.** A verified defect, or a required
check not run, that stands in the result the owner asked for keeps that work,
or that part of it, unfinished. It is not a finding to park and not an AHEAD
item. The session fixes it within the scope it was given; when time, access or
scope stops it, it stops with the reason and the next step, in Now and in the
work section. A session may end while its work is unfinished. The boundary is
the result that was agreed, not who wrote the faulty code: a fault that was
there before can stand in the result, and an improvement nobody asked for is
outside it and is a finding. Only the owner accepts less than he asked for;
the limit is then written in the ability's known limits with his decision and
its date, and an agent does not use known limits to close work. The warm-up
and the closing report say "unfinished" for such work, never "done, with
follow-ups".

**When committed work is done.** It is done when what its section gives as
"done when" is met and nothing above stands in it. In the closing commit the
session shows the owner what the work found, he rules on it, and the work
section is removed. Nothing is copied at that moment: each part's proof was
recorded as it finished, in the ability's entry, the plan and the changelog.

**Blockers.** Name what a blocker stops and its source: an owner message with an ISO date, a specification identifier or file path, or `failing check: <name>`. Check the source before honoring a carried-over blocker and say so. Implemented and tested with acceptance outstanding is not blocked; show acceptance as outstanding and continue unrelated work.

## 6. Identifiers and states

| Identifier | Form | Rules |
|---|---|---|
| Ability | `AB-001` | Three digits; never reused, never removed |
| AHEAD item | `AH-001` | Three digits; never reused. Removed only on the owner's word, and the number stays used |

Not `A-001`: projects that write use case specifications label alternative
flows `A1`, `A2`.

| File | Field | Values |
|---|---|---|
| `ABILITIES.md` | Status | `planned` (approved, not built), `in progress`, `done` (built, checked, evidence linked), `retired` (removed; the reason stays) |
| `ABILITIES.md` | Specs (optional) | Use case identifiers (`UC-003`) or relative links to the specifications that define the ability; the check verifies that each link points at a file |
| `ACTIVE.md`, `ABILITIES.md`, `AHEAD.md`, `ATLAS.md` | Home (optional, in the hot zone) | The tracking file kept as the home at adoption (never an A-file or a guideline file); the check verifies that it exists and no longer asks for the A-file's own fields, index, entries or map |
| `AHEAD.md` | Kind | `idea`, `research`, `spike`, `proposal` |
| `AHEAD.md` | State | `open`, `approved`, `next`, `started`, `dropped` |
| `AHEAD.md` | Entered (in the entry) | The owner's decision to keep the item: an ISO date, then his words or his request. The check looks for it on an item that is new since the last commit |

**An item enters on the owner's decision.** An agent proposes an item, in its
report or when asked, and does not write the row. A direct request from the
owner ("add an item for X", "put that in AHEAD") is the decision; no second
yes is asked for. The entry records it in its `Entered` line. Keeping an item
is not leave to build it: `open` still means not approved. Related small
things may be proposed as one item when they make one piece of work with one
way to tell it is done; the owner may also keep a small item on its own.
Widening an item that exists needs his decision as a new item does.

**Removed on the owner's word.** An item the owner never chose can be removed
when he says so. Its row and its entry go, its number stays used, and History
gains one line that begins `Removed on the owner's word:` and names the
identifiers (singly, or as a range such as `AH-069 to AH-089`), the date and
his words. The check counts an identifier named there as present, and reports
one that is used again. Where items are projected to issues, the removed
item's issue closes as not planned.

An AHEAD item that is `approved`, `next` or `started` names its ability. An
ability's status is written once, in its index row: agents read the row at
session start, and the row moves with the ability when done abilities sit
below the hot zone. Entries carry no Status line. In a repository adopted
earlier, an old entry that still carries a Status line is compared with its
row, and a mismatch is reported; drop the line, or keep it in step.

## 7. The other homes

| Home | Holds | Template |
|---|---|---|
| `docs/plans/YYYY-MM-DD-subject.md` | One plan per piece of work that spans sessions: goal, steps, progress log, decisions, surprises (the default home of what the work finds, section 5), how to resume. A fresh session can continue from the plan alone | `templates/docs/plans/` |
| `docs/decisions/NNNN-subject.md` | Decisions and standing rules, numbered, never reused; superseded records stay | `templates/docs/decisions/` |
| `docs/research/NN-subject.md` | Research and spike write-ups: question, what was done, findings with sources, answer | `templates/docs/research/` |
| `CHANGELOG.md` | Notable changes per release, from the first release (Keep a Changelog) | `templates/CHANGELOG.md` |

`ACTIVE.md` links the active plan; `AHEAD.md` links write-ups; decisions link
the research behind them.

## 8. The check and the hook

`tools/check_tracking.py` (Python 3.9+, standard library only) checks the
shape of the A-files, not their truth.

**Which files it expects.** `ACTIVE.md` is always expected, and so is
`AGENTS.md`: that is the small setup. `ABILITIES.md`, `AHEAD.md` and `ATLAS.md` are
expected when the index of `AGENTS.md` lists them (a row of its index table,
wherever the table sits; without an index table, a name in its first 100
lines), when
the file exists, or when it held identifiers in the last commit, so a file deleted
together with its index line is still reported. (`ATLAS.md` holds no
identifiers, so removing it with its index line is how a repository shrinks
back.)

It reports:

- a missing expected A-file; in the four files that have a hot zone, a missing
  contract line, a missing end of hot zone, or a hot zone over its cap; an
  `AGENTS.md` that neither lists in its index table nor names in its first 100
  lines `ACTIVE.md` and every other A-file that exists;
- a section below a hot zone that the hot zone does not name;
- a link in a hot zone, or a path in the atlas map, that points at nothing; in
  `AGENTS.md`, a link above its end-of-hot-zone line when it has one, and
  anywhere in the file when it has none;
- an `ACTIVE.md` without one of its fields, or `BLOCKER_WITHOUT_SOURCE` when a blocker lacks a dated owner message, specification ID or file path, or failing check by name;
- an `AB-` or `AH-` identifier in ACTIVE's hot zone that its register does not
  have (`UNKNOWN_ABILITY`, `UNKNOWN_ITEM`), when that register was read; only
  a full identifier is read, so a placeholder such as `AB-0xx` is not one;
- an identifier in the wrong form, a status, kind or state outside the lists,
  an identifier listed twice across the file's index tables, an index row
  without its entry or the reverse, and an old entry that still carries a
  Status line different from its row (the row holds the status, section 6);
- an `ABILITIES.md` whose index tables hold no row; its hot zone may hold no
  ability row when a table below holds them, so done abilities can move
  below. A table that lacks any of the ID, Ability and Status columns, such
  as an area summary, is not an index, and the check ignores it. `AHEAD.md`
  keeps its index rows in its hot zone;
- a link or backticked path in an ability's `Specs` line that does not point
  at a file, and a `Home` that is not a file in the project or that names an
  A-file or a guideline file;
- an identifier that was in the last commit and is gone, unless `AHEAD.md`
  names it in a line that begins `Removed on the owner's word:`; and an
  identifier named there that is used again;
- `ITEM_WITHOUT_DECISION`: an AHEAD item that was not in the last commit and
  whose entry has no `Entered` line with an ISO date. An `AHEAD.md` the last
  commit did not hold is new as a whole. This is a reminder at commit time,
  not proof: the check reads that the line is there, never its words, and an
  agent can write the line itself;
- an AHEAD item that is approved, next or started without an ability, or an
  item naming an ability that `ABILITIES.md` does not have, or naming one
  when there is no `ABILITIES.md` (unless the file is already reported
  missing or unreadable: one file, one finding).

**What it leaves alone.** The check says nothing about the length of `AGENTS.md`,
about its sections, or about a missing end-of-hot-zone line in it. It does not
require a work section, read its form, count sections, or judge whether a part
is done or an item was really chosen.

Templates inside fenced code blocks are ignored, so each file can carry its own
template. Output: one line `path:line: ERROR CODE: message` per problem; an
A-file it cannot read or decode is the problem `UNREADABLE`. Exit 0 when it
ran, whatever it found; with `--strict`, 1 on problems; 2 on a usage error; 3
when it could not run (`--staged` without git or outside a repository).
`--no-git` skips the comparison with the last commit.

**Notes.** What is not a problem is a note on standard error (`path: NOTE:
message`): in staged mode an A-file with unstaged changes, or one whose
changes git could not compare; a comparison with the last commit that was
skipped because git, the repository or the first commit is missing. The
A-files keep notes off standard output on purpose: the plugin's end-of-turn
hook, and any tool paired with them, run the check with `--strict`, and again
without it when it exits 2, and read its exit code and its `path:line: ERROR CODE: message`
lines (pairing P10), so the problem lines are the only lines there. The
option, the exit codes, the codes and the line format change only with the
pairing contract.

**Summary, data and version.** A clean run prints nothing, so a run that
inspected every file looks like one that inspected none. On request the check
says more; each option is read-only and keeps the exit codes above:

- `--summary` ends the run with one line on standard error, in place of the
  line that counts the problems: `checked AGENTS.md, ACTIVE.md, ...: 0
  problems`, with a file marked `absent`, `unreadable` or `(kept in <home>)`.
- `--format json` prints one JSON object on standard output instead of the
  problem lines and the notes. `schema` (1) and `a_files_version` say what
  wrote it; `mode` (`working tree` or `staged`) and
  `compared_with_last_commit` say how it read; `files` gives each A-file with
  `present`, `readable` and its `home`; `findings` give `file`, `line`,
  `severity` (`error`), `code` and `message`, and `problems` counts them;
  `notes` hold the notes. Then what it parsed: `active.fields`, each field of
  ACTIVE's Now with its `value` (indented lines below it joined in) and
  `line`; `abilities` and `ahead_items`, one record per identifier with its
  index row's `line`, the `section` it sits under and its `columns` as the
  header names them, its `entry_line`, and from the entry `known_limits` and
  `evidence` (abilities) or `belongs_to` (items), each a `value` and a `line`
  or null. An entry with no row has no columns and a null line; a file kept at
  another home gives no records. `removed_items` lists the identifiers
  `AHEAD.md` says were removed on the owner's word. `registers` says, for `abilities` and
  `ahead_items`, whether the check `read` the file's rows, and when not, the
  `reason`: `absent`, `unreadable`, `kept_elsewhere`, or `no_hot_zone` (the
  file has no marker, so its index cannot be told from its entries). An empty
  list with `read` true means the register has no rows. The schema number
  rises only when a key changes its meaning or goes away.
- `--version` prints the version of the A-files the check came with, the
  version of the plugin, so a project can tell which check it has installed.

**Staged mode.** Run by hand, the check reads the working tree. With
`--staged` it reads every A-file and every path it checks from the index,
the files as the commit will hold them, and compares their identifiers with
the last commit; it also notes an A-file whose changes are not staged. A
path that exists only in the working tree is reported, since the commit
lacks it. Without git or outside a repository `--staged` could not run
(exit 3); before the first commit it reads the index and compares nothing.

**The hook.** `scripts/pre-commit` runs `python3 tools/check_tracking.py --staged`
before every commit and never refuses it: the problems in what is staged are
shown, with a note for each A-file whose changes are left out, and the commit
goes through, and so it does, with a line saying so, when the check cannot
run. A repository that chooses a strict pipeline replaces the hook's lines
with `exec python3 tools/check_tracking.py --staged --strict`, its own
choice, made on purpose. Once
the person agrees to it (section 10), install it as `.githooks/pre-commit` in
the repository and enable it once per clone:

```bash
git config core.hooksPath .githooks
```

The hook reads what is staged, so its report describes the commit; a change
left unstaged is noted, not counted.

**The agent hooks.** The plugin also carries two agent hooks (`hooks/`, run by
`scripts/afiles_hook.py`): at session start, a note to state Finished,
Remaining, Blocked by and Next step before the first edit; at the end of a turn,
the check's findings, each once per session, as a note for the agent that asks
nothing of the owner and never stops the work. They act only where `ACTIVE.md`
carries the hot-zone marker. They are earlier feedback; the commit hook above
is still the check that holds for everyone.

## 9. Wiring each agent

| Agent | Reads `AGENTS.md` | What to add |
|---|---|---|
| Codex | Natively (root, then folders down to the working directory) | Nothing |
| Antigravity (Gemini) | Natively, or `GEMINI.md` | Nothing |
| Gemini CLI | When its `context.fileName` setting lists it; the default name is `GEMINI.md` | That setting |
| Cursor, Copilot, Windsurf | Natively | Nothing |
| Claude Code | Natively from v2.1.277, when no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` sits in the working directory or above it; otherwise through an import | A `CLAUDE.md` holding `@AGENTS.md` (template provided): it works in every version, and beside those files |
| Aider | When configured | `read: AGENTS.md` in `.aider.conf.yml` |

Claude Code: with a `CLAUDE.md` present, it ignores `AGENTS.md` files in
subfolders unless a `CLAUDE.md` beside each imports it, or the user setting
that loads both kinds is on.

**How much of the file arrives** (each tool's documentation, read on
2026-11-19). These tools load the file whole; none stops at a marker. Some
cut by size:

- Claude Code gives the model the whole of each instruction file it loads at
  launch, up to 4 MiB, and skips a larger one. It strips block-level HTML
  comments from a `CLAUDE.md` before the text reaches the model; whether that
  covers an imported `AGENTS.md` is not stated.
- Codex stops adding project instruction files once their combined size
  reaches 32 KiB (`project_doc_max_bytes`): one budget for all of them, so a
  long file can cut the ones after it.
- Antigravity truncates a single rule file over 24,000 bytes, and when the
  always-on rules together pass 20,000 tokens it replaces the largest with a
  one-line pointer.

The others name no size limit as read that day: Gemini CLI, Cursor, GitHub
Copilot (its code review dropped a 4,000-character cap on 2026-06-12) and
OpenCode found none; for Kiro, Amp and Devin Desktop (once Windsurf) none
was found in the current documentation, though Windsurf's older pages
truncated a file over 6,000 characters.

The check reports none of this: the limits differ by tool and change with
their releases. A file that nears one is shortened with the three questions of
section 2.

Session tooling outside the repository (a personal assistant that opens each
session, a project scaffold) should start sessions with the warm-up and create
new repositories from `templates/`.

## 10. Adopting the method

**Small or full.** Every adoption offers the small setup (`AGENTS.md` and
`ACTIVE.md`) or the full one (all five files), and the person chooses; a
small setup grows later (section 2). In the small setup, the index of
`AGENTS.md` lists only `ACTIVE.md` (step 2 below), since the check expects
every A-file the index lists.

**A new repository.** It takes the same two replies as any adoption (below):
the first lists the files it would create from `templates/` for the small
setup and for the full one, asks which, and proposes the check and the hook,
creating nothing; the second, after the person answers, does the steps.

1. Read each chosen file in `templates/` in this skill's folder and write
   the project file from it, never by running a copy command (keep `docs/`
   as it is).
2. Fill `AGENTS.md`: purpose, commands, rules, any extra row in the index;
   in the small setup, remove the other three files' rows from the index,
   and their mentions from the warm-up and keep in step.
3. Fill `ACTIVE.md` with the current work; in the full setup, `ATLAS.md` with
   the parts that exist, `ABILITIES.md` with what the product can do and
   `AHEAD.md` with what the owner says is planned, each item with its
   `Entered` line.
4. Inspect the existing hook and both the local and effective `core.hooksPath`.
   Ask one question before running the installer: the check alone or the check and the hook?
   Honor the choice if the request or adoption answer already supplies it.
   Then run `python3 "<skill-folder>/scripts/install_check.py" --root .` once in place
   from this skill's base directory, from the project root. The script
   copies `scripts/check_tracking.py` to `tools/check_tracking.py` only when
   absent; an existing check is left untouched and reported as matching or
   differing from the plugin's. A later yes to the hook is a re-run with `--hook`.
   A later release of the check is a re-run with `--upgrade`: it replaces an
   earlier check that is committed and unchanged since, names both releases,
   and refuses a check the project's history does not hold as it stands.
   Every shell hook change goes through the script; never write or copy the
   hook by hand or run an agent copy command. Install the hook only if the
   person said yes to it, or the request already says to install it: add
   `--hook` to that command. With no commit hook yet, it installs the shipped
   `scripts/pre-commit` as `.githooks/pre-commit` and sets
   `git config core.hooksPath .githooks`; with one (a hooks path, a file in
   `.git/hooks/`), add the line
   `python3 tools/check_tracking.py --staged || true` to it through the script instead of
   replacing it, before the hook's first command: after the shebang when
   there is one, at the top when there is none. The added line never decides
   the hook's result unless a strict check is asked for. The check only
   reports and exits 0, so as the hook's last line it would decide the
   result, and a failing command of the person's own before it would no
   longer refuse the commit; `|| true` keeps a hook that runs with `set -e`
   going when the check cannot run. For a strict check, which refuses a
   commit while the A-files have problems, use
   `python3 tools/check_tracking.py --staged --strict || exit 1`, placed the
   same way; the person's later commands still decide otherwise. The
   `|| true` and `|| exit 1` lines are for a shell hook. Some hook managers,
   such as the pre-commit framework, run a step without a shell, so a hook
   manager gets a step of its own running
   `python3 tools/check_tracking.py --staged`, which reports and exits 0, or
   `python3 tools/check_tracking.py --staged --strict` to refuse; never
   `|| true` in a step. The step takes no file names, runs on every commit,
   one that only deletes files included, and shows its output, so the
   report is seen. For example, the pre-commit framework, in
   `.pre-commit-config.yaml`: a `repo: local` hook with
   `entry: python3 tools/check_tracking.py --staged`, `language: system`,
   `pass_filenames: false`, `always_run: true` and `verbose: true`; for the
   strict check, `entry: python3 tools/check_tracking.py --staged --strict`.
   The script never replaces a hook and stops for hook managers or non-shell
   hooks: integrate those with their own step above. With no local hooks path
   but a global or system one, `--hook` refuses before any change: the folder
   is shared by other repositories and the owner must choose where the hook
   goes. Without `--hook`, the check can still be installed. Installing reads the
   plugin's folder, and a tool's permission mode may ask for access. On a
   refused or failed step, report the command, what is installed and what is
   missing; commit nothing half-written, and resolve the failure before resuming.
5. Run `python3 tools/check_tracking.py` until it is clean; commit.

**A repository with its own tracking files.** Use the first reply to survey
the repository, show the mapping and proposed moves, offer the small or the
full setup, propose the check and hook, and end with questions, without creating, moving or removing anything
or installing a hook; apply only in a second reply after the person answers
in a new message. Asking to adopt the method or set up the repository does
not supply those answers. If the request already specifies the alignment
for every area and explicitly says to go ahead without waiting, show the
mapping first and apply in that same reply.
The hook is a choice of its own (the check is copied either way): it is
installed only when the request or the answer says so. Full alignment
settles the instructions that name what moves: they are adapted to the new
home. A decision the request does not settle (a bare name it cannot place)
stays a question; nothing is guessed.

First show what exists and where it would go:

| Old content | New home |
|---|---|
| A status or board note | `ACTIVE.md` Now, Pending and Debt |
| A board of work in progress, or the parts of long work under way | `ACTIVE.md`: Now for the piece being worked, and a work section for the larger work (section 5) |
| A feature list | `ABILITIES.md`, one entry per feature, with a new `AB-` identifier |
| Under the small setup: a feature list, a roadmap or an architecture document | No A-file holds it: it stays where it is (left out), or the setup grows to hold it; the person chooses |
| A roadmap, backlog or idea list | `AHEAD.md`: milestones, Next up, items. A backlog is entered on the owner's word at adoption: he says which items come in, and each carries its `Entered` line with the date of the adoption |
| An architecture or layout document | `ATLAS.md` (keep a design rationale as a decision record) |
| Standing rules found in a status note | `docs/decisions/` |
| Decision, plan and research notes in other folders | `docs/decisions/`, `docs/plans/`, `docs/research/` |
| Finished items kept as history | Delete; git keeps them |

Then ask the person, once for everything or area by area:

| Choice | What happens |
|---|---|
| **Full alignment** | Everything goes to the root and `docs/`. An old file's content merges into its A-file and the old file is removed; notes in other folders move into `docs/` with `git mv` and take the naming rules of section 11 |
| **Keep it as the home** | The old file or folder stays the home. The A-file keeps its title, contract line and hot zone, and its hot zone carries `- **Home:** <the kept file>`: the check verifies that the file exists and no longer asks for the A-file's own fields, index or entries. The keep-in-step rule names the kept file. The warm-up reads it too, and the check cannot verify its shape |
| **Leave it out** | Files that are not tracking (notes, a design rationale) stay as they are |

Nothing moves before the person agrees.

**Specifications are never moved by this method.** Whatever method wrote
them (use cases under `docs/`, Spec Kit's `specs/`, Kiro's `.kiro/specs/`,
OpenSpec's `openspec/`, loose documents), the A-files link them where they
are: a `Specs` line per ability (section 6), an ATLAS row and an index row in
`AGENTS.md` for their folder. Moving them into another layout is the
specification method's decision; some tools read only their own folder.

**Every move keeps its references.** `scripts/relink.py` runs in three
steps. `plan` lists every reference to each old path (links, `@file`
imports, paths in settings, CI, hooks and scripts, paths in backticks) and
flags a bare name in prose for a decision. `apply` runs the moves with
`git mv` and rewrites the exact references. A folder whose new path is an
existing folder moves into it file by file; a file whose new path exists is
refused, so its content is merged and the old file removed first. `verify`
reports every broken link and every old path still named (with `--strict` it
exits 1 while one remains).
Write the adoption record after `apply` and before the final `verify`, keeping
its old names as history, and pass `--keep docs/decisions/NNNN-adopt-the-a-files.md`
to that verification so its mentions are listed as `KEPT`, not problems;
the repeatable `--keep FILE` option also protects records from `apply` rewrites.

Agent instructions get the same treatment: every instruction file
(`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursor/rules/`,
`.github/copilot-instructions.md`, `.kiro/steering/`, `.windsurf/rules`,
`.clinerules`) is read. Under full alignment, an instruction that names a
moved file is adapted to the new home unless the person said otherwise; in
other cases (an area kept as the home, an instruction that describes the old
way of working), it is removed, adapted or kept, as the person decides.
References from outside the repository (wikis, issues, other repositories)
cannot be checked; the report says so.

Record the adoption as a decision (template
`templates/docs/decisions/NNNN-subject.md`): what moved, what was kept, what
was left out.

## 11. Naming

The method is called **the A-files**: the five files' names all start with A,
and the name echoes The X-Files so it sticks. In a sentence: "this repository
uses the A-files". The subtitle, *five files every coding agent reads first*,
says what it is to someone who has not met it.

| What | Convention | Example |
|---|---|---|
| Files at the root that people and tools look for | Uppercase name, `.md` | `AGENTS.md`, `ACTIVE.md`, `CHANGELOG.md` |
| Files under `docs/` | Lowercase, words joined by hyphens | `docs/research/01-sms-providers.md` |
| Decision records | Four digits, never reused, then the subject | `0007-retire-paper-vouchers.md` |
| Plans | The date the work started, then the subject | `2026-10-01-cancel-a-booking.md` |
| Research and spikes | Two digits, then the subject | `01-sms-providers.md` |
| Dates | ISO 8601 | `2026-10-03` |
| Commit subjects | Area, colon, what changed | `booking: refuse a ninth repair on a full day` |
| Branches | Kind, slash, subject: `feat`, `fix`, `docs`, `chore` | `feat/cancel-a-booking` |
| Release tags | `v` and a semantic version | `v1.2.0` |

## 12. Limits

- **The check verifies shape, not truth.** It cannot tell that `ACTIVE.md`
  describes yesterday's work; only the keep-in-step rule and review do.
- **Models vary from run to run.** No instruction is followed every time; the
  check and the hook are the floor that holds regardless.
- **One owner.** The method assumes one person directing the work; it has no
  assignments, reviews or permissions for a team.
- **The warm-up costs tokens.** Up to 360 lines of hot zones per session at
  the caps, and `AGENTS.md` whole; that is the price of a shared picture. The
  caps and the three questions of section 2 keep it from growing.
- **The owner's decision cannot be checked.** The check sees whether a new
  AHEAD item carries its `Entered` line, not whether the owner said it.
- **One editor at a time.** The method does not merge parallel edits to the
  A-files; it avoids them.

## 13. Questions

**Why not an issue tracker?** The A-files serve one owner directing agents,
not a team tracker. They work offline, travel with the code, and are read by
every agent without credentials. Use a tracker when a team or a public remote
exists; then `AHEAD.md` items can link their issues (an `Issue` column or an
`- **Issue:**` line), or be projected to them.

**What does projecting to issues add?** Many tools read issues and not
`AHEAD.md`. A project with a GitHub remote may opt in: a workflow run on the
host after each push projects the approved, next and started items (and, by a
setting, the open ones) to issues of the same repository. It is one way:
nothing it does writes an A-file, the agent hooks and the check stay offline,
and nothing leaves the machine before the owner pushes. Each projected fact
keeps one home: the issue shows it, `AHEAD.md` and `ABILITIES.md` decide it. An
issue closed or reopened on the host against the A-files (a pull request that
closes it, a board rule) is labelled out of step, never overwritten; an agent
gathers the facts and the owner decides which side wins. Another host needs
another template, not another rule.

**Why Markdown and not JSON?** People review Markdown. JSON resists careless
rewriting better; the check gives Markdown the same protection by reporting
removed identifiers and broken shape at every commit.

**Where do bugs go?** A defect in what the owner asked for keeps that work
unfinished (section 5). A defect found outside it is a finding: written down
with its evidence, and ruled on by the owner, who may make it an item. AHEAD
has no kind for bugs.

**What if the ABILITIES index outgrows its hot zone?** Keep the planned and
in-progress rows in the hot zone and move the done and retired rows to an
index table below it, named in the `Below:` line. Each identifier keeps one
row: the check reads every index table of the file as one index and reports
an identifier listed twice. When every ability is done, the hot zone may hold
no ability row at all, only an area summary: a table that lacks any of the
ID, Ability and Status columns is not an index, and the check ignores it.

**Can a file stay empty?** Yes: an empty section says "None." or "Nothing
scheduled", and `ACTIVE.md` keeps every field with "none" or "—".

## 14. Pairing with a specification method

A project may also write down what its system does with a spec-driven method.
The two stay separate and are joined by a few rules, kept in the skill's
pairing reference:

- an ability names the specifications that define it in a `Specs` line;
- the current work in `ACTIVE.md` names the use cases or abilities being
  worked on, and the next new work comes from AHEAD's Next up;
- whichever method is set up second joins the other: it names its section in
  the hot zone of `AGENTS.md` where the file has one, adds two rows to the
  keep-in-step rule, and maps the specifications in `ATLAS.md`.
