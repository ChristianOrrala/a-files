# ATLAS — <project>

> The architecture map: each part of the repository, what it does, which files it works through, what it depends on and what checks it. A map, not a full file index.

## Map

| Part | What it does | Works through | Depends on | Checked by |
|---|---|---|---|---|
| <part> | <one line> | `path/`, `path/file` | <parts> | <tests or scripts> |

## Flow

<a few lines or a small diagram of how the parts connect>

Below: Parts in detail, How to maintain this file.

<!-- hot zone ends -->

## Parts in detail

### <part>

<only what the map row cannot say: data flow, invariants, pitfalls>

## How to maintain this file

- A row per part of the repository, at the level of a folder or a working
  unit, never file by file. "Works through" names the entry points and the
  files an agent opens first; every path in backticks must exist.
- Update it in the same commit that adds, moves, renames or removes a part.
- "Parts in detail" holds only what a row cannot say: data flow, invariants,
  pitfalls.
- The check (`tools/check_tracking.py`) refuses a path in the map that points
  at nothing.

Template: this file as it stands, with the placeholders in angle brackets.
