# Projecting AHEAD to GitHub issues

Opt-in, for a project with a GitHub remote, so that the tools and products that
read issues (agent tools, boards, coding agents) see the work AHEAD holds.
AHEAD stays the source of truth; the issues are a projection of it (the
method guide, section 13).

**Offer it** at adoption or at an upgrade, once, as one question: "Project
AHEAD's actionable items (approved, next, started) to this repository's GitHub
issues? Default no." On a yes, ask once whether open ideas, research and
spikes go too, then run
`python3 "<skill-folder>/scripts/install_check.py" --root . --issues`: it copies
`scripts/project_issues.py` to `tools/project_issues.py` and
`templates/github/a-files-issues.yml` to `.github/workflows/`, each only when
absent. Add `--include-open` to the workflow's command when the person chose
the open items. Add to the keep-in-step rule of `AGENTS.md` the line the
installer prints. Nothing reaches GitHub until the person pushes.

**What runs.** After a push that changes `AHEAD.md` or `ABILITIES.md`, and when
an issue it keeps is closed or reopened on GitHub, the workflow runs
`tools/project_issues.py --apply`. Each item has one issue, found
by a hidden marker; its title, its `kind:` and `state:` labels and the part of
the body between its markers are the projection's, the rest is people's. An
issue closes as not planned when its item is dropped and as completed when its
item's ability is `done`. The script never writes an A-file, never deletes an
issue, and never overwrites a change made on GitHub: it labels the issue
`a-files: out of step` and comments once. `python3 tools/project_issues.py`
alone is a dry run.

**Align with the issues** at close-out, when an agent sees the label, or when
asked; never as a recurring task for the person. With `gh`, run
`python3 tools/project_issues.py --report` and, for each mismatch, gather the
facts: the pull request or event that closed or reopened the issue, what it
changed, what AHEAD and ABILITIES say. Then ask the owner one question per
mismatch, with a recommendation:

| Answer | What happens |
|---|---|
| Take GitHub's version | The main session first updates the A-files to match (a merged pull request becomes the ability's evidence), then runs `--accept-github AH-NNN`, which refuses while the A-files still say otherwise |
| Keep the A-files | `--keep-a-files AH-NNN`: the issue returns to what the A-files say, with a comment |
| Later | Nothing changes; the label stays |

A removed item has no Take GitHub's version: the removal is the owner's word, and
`--accept-github` refuses it. Offer Keep the A-files or Later.

A closed issue alone never makes an ability `done`. When work starts from an
issue, the main session moves the item from AHEAD to ACTIVE as the skill's
Promote an item says; workers report to it.
