# Changelog

All notable changes to the A-files. Versions follow semantic versioning.

## 1.2.2

- The pairing contract (P4): a recovery change log entry decided later
  becomes an AHEAD item that cites it; the entries of one use case share one
  item.

## 1.2.1

The first public release. Earlier versions were internal.

- The `a-files` skill: adopts and keeps five files at a repository's root
  that every coding agent reads first (`AGENTS.md`, `ACTIVE.md`,
  `ABILITIES.md`, `AHEAD.md`, `ATLAS.md`), each with a hot zone read at
  session start.
- A check of their shape, a git hook that runs it before every commit (installed
  only with your yes), and a reference check that keeps every link, import and
  instruction right when a tracking file moves.
- A minimal example project.
- Works alone or with upspec in the same project.
