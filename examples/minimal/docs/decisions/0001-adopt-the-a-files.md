# 0001. Adopt the A-files to track the work

Status: Accepted. Date: 2026-09-01. Decided by: the owner.

## Context

Several coding agents work in this repository in turn. Each new session spent
its first minutes working out where things stood, and twice an agent started
new work while a cancellation bug was still open.

## Decision

The repository tracks its work in the A-files: `AGENTS.md` (rules and index),
`ACTIVE.md` (work in progress), `ABILITIES.md` (every ability), `AHEAD.md`
(everything not started) and `ATLAS.md` (the architecture map), as the A-files
method describes. Every session starts with the warm-up; the check runs before
every commit.

## Consequences

- A session starts from the same picture whatever agent runs it.
- New work starts only when `ACTIVE.md` is empty.
- The files cost a few minutes per session to keep in step; the check refuses
  a commit that breaks their shape.
