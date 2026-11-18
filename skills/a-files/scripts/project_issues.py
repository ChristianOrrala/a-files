#!/usr/bin/env python3
"""Project AHEAD.md's actionable items to GitHub issues of the same repository.

AHEAD.md stays the source of truth. This script, which a project opts into, shows its items to the tools that take
their work from GitHub issues. It reads the A-files through the check (`check_tracking.py --format json`, beside this
script), lists the issues that carry its marker with `gh`, and plans one thing per item: create, update, close,
reopen, flag as out of step, or nothing.

What is projected: items in `approved`, `next` or `started`; with --include-open, `open` items too. A `dropped` item
is considered only to close an issue that exists; no issue is ever created for it.

An issue is identified by a hidden marker in its body, `<!-- a-files:AH-NNN -->`, never by its title. The script owns
the title, the labels `a-files`, `kind: <kind>` and `state: <state>`, and the part of the body between that marker and
`<!-- a-files:end -->`; text outside it, comments, assignees and other labels belong to people and tools. Inside its
part the script keeps one hidden line, `<!-- a-files:last: open|closed -->`: the state it last set.

Open or closed, as the A-files say: closed as not planned when the item is `dropped`, closed as completed when the
item's ability (the first AB-NNN of its Ability column) is `done`, open otherwise (a `started` item stays open).
A change made on GitHub is never overwritten: when an issue's state differs from what the A-files say and is not the
state the script last set, the issue is labelled `a-files: out of step` and commented once, and its state is left
alone. `--report` lists those for an agent to align with the owner; `--keep-a-files AH-NNN` and `--accept-github
AH-NNN` carry out the owner's answer for one item (and only for the items named).

A run writes nothing (to GitHub or to the project) unless --apply is given; the script never writes a file of the
project and never deletes an issue. A second run on unchanged state plans nothing.

Output: the plan, one line per action, or `nothing to do`. With --report, one JSON object on stdout:
{"repo", "out_of_step": [{id, issue, url, issue_state, state_reason, a_files_state, ability, ability_status,
item_state}]}.

Exit codes: 0 when it ran (whatever it found, and when AHEAD.md is kept elsewhere and nothing was done), 1 when gh
fails during --apply, 2 on usage errors, 3 when it could not run (gh missing or not signed in, no repository, the
check failed, no commit for the links), with one line on stderr.

The environment variable A_FILES_GH names the gh executable to run instead of `gh` (the tests use it).

Usage:
    project_issues.py [--root DIR] [--repo OWNER/NAME] [--ref COMMIT] [--include-open] [--apply]
    project_issues.py --report [--root DIR] [--repo OWNER/NAME]
    project_issues.py --apply [--keep-a-files AH-NNN] [--accept-github AH-NNN]

Requires Python 3.9+, standard library only; git for the commit the links point at, and the GitHub CLI (`gh`),
signed in, for everything else.
"""
import argparse
import codecs
import json
import os
import posixpath
import re
import subprocess
import sys
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "check_tracking.py")
# The exit code of a run that could not start, apart from 2, a usage error.
COULD_NOT_RUN = 3
GH_TIMEOUT_SECONDS = 120
CHECK_TIMEOUT_SECONDS = 120
# Items projected by default; --include-open adds "open".
PROJECTED = ("approved", "next", "started")
LISTED_LABEL = "a-files"
OUT_LABEL = "a-files: out of step"
KIND_PREFIX = "kind: "
STATE_PREFIX = "state: "
LABEL_STYLE = {
    LISTED_LABEL: ("5319E7", "Projected from AHEAD.md by the a-files"),
    KIND_PREFIX: ("1D76DB", "The kind of the AHEAD.md item this issue projects"),
    STATE_PREFIX: ("FBCA04", "The state of the AHEAD.md item this issue projects"),
    OUT_LABEL: ("D93F0B", "Closed or reopened on GitHub against what the A-files say"),
}
END = "<!-- a-files:end -->"
LAST = re.compile(r"<!-- a-files:last: (open|closed) -->")
MARKER_FOR = "<!-- a-files:%s -->"
FOUND_MARKER = re.compile(r"<!-- a-files:(AH-\d{3}) -->")
AB_ID = re.compile(r"\bAB-\d{3}\b")
AH_ID = re.compile(r"^AH-\d{3}$")
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
# A Markdown link, or a backticked token (a path, perhaps), in a Write-up cell.
WRITE_UP = re.compile(r"\[([^\]\n]*)\]\(([^)\s]+)((?:\s+\"[^\"]*\")?)\)|`([^`\s]+)`")
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
# The commit in a link to a file: ignored when a body is compared, so that a push that does not change an item
# does not rewrite its issue.
BLOB = re.compile(r"/blob/[^/\s)#]+/")
NOTE = ("AHEAD.md is the source of truth. When work starts from this issue, the main session moves %s from AHEAD to "
        "ACTIVE as the A-files say; this issue is updated from AHEAD.md.")
NO_VALUE = ("", "-", "\u2014", "none")
READ_REASONS = {
    "absent": "AHEAD.md does not exist",
    "unreadable": "AHEAD.md cannot be read",
    "kept_elsewhere": "AHEAD.md is kept elsewhere (its Home), so its items are not read",
    "no_hot_zone": "AHEAD.md has no hot zone end marker, so its items are not read",
}


class CannotRun(Exception):
    """The run cannot start or go on: exit 3 with the message on stderr."""


class GhFailed(Exception):
    """A gh call ended in an error: exit 1 during --apply, exit 3 while reading."""


def first_line(text):
    lines = (text or "").strip().splitlines()
    return lines[0] if lines else ""


def gh(args, text=None, cwd=None):
    """Run gh (A_FILES_GH, or gh) with list arguments and no shell; its standard output."""
    exe = os.environ.get("A_FILES_GH") or "gh"
    env = dict(os.environ, GH_PROMPT_DISABLED="1", GH_NO_UPDATE_NOTIFIER="1")
    try:
        done = subprocess.run([exe] + list(args), input=text, capture_output=True, text=True, encoding="utf-8",
                              env=env, timeout=GH_TIMEOUT_SECONDS, cwd=cwd)
    except FileNotFoundError:
        raise CannotRun("gh is not installed (or A_FILES_GH does not name it): install the GitHub CLI and sign in")
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise GhFailed("gh %s could not run: %s" % (" ".join(args[:2]), exc))
    if done.returncode != 0:
        raise GhFailed("gh %s failed: %s" % (" ".join(args[:2]), first_line(done.stderr) or "exit %d" % done.returncode))
    return done.stdout


def run_check(root):
    """The check's JSON object for the root folder."""
    try:
        done = subprocess.run([sys.executable, CHECK, "--root", root, "--format", "json"], capture_output=True,
                              text=True, encoding="utf-8", timeout=CHECK_TIMEOUT_SECONDS)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise CannotRun("the check could not run: %s" % exc)
    if done.returncode != 0:
        raise CannotRun("the check could not run (exit %d): %s" % (done.returncode, first_line(done.stderr)))
    try:
        return json.loads(done.stdout)
    except ValueError:
        raise CannotRun("the check's output is not JSON")


def git_ref(root, ref):
    """(the commit the links point at, the root folder's path inside the repository, "" or "dir/")."""
    def git(*args):
        try:
            done = subprocess.run(["git"] + list(args), cwd=root, capture_output=True, text=True, encoding="utf-8",
                                  errors="replace", timeout=60)
        except (OSError, subprocess.TimeoutExpired):
            return None
        return done.stdout.strip() if done.returncode == 0 else None
    prefix = git("rev-parse", "--show-prefix") or ""
    if ref:
        return ref, prefix
    sha = git("rev-parse", "HEAD")
    if not sha:
        raise CannotRun("no commit to point the links at: run it inside a git repository with a commit, or give --ref")
    return sha, prefix


# --- reading the A-files' items -------------------------------------------------------------------------------------

def facts(item, abilities):
    """What the projection needs of one AHEAD item, with its ability's name and status."""
    columns = item.get("columns") or {}
    found = AB_ID.findall(columns.get("Ability", ""))
    ability = found[0] if found else None
    row = (abilities.get(ability) or {}).get("columns", {}) if ability else {}
    return {
        "id": item["id"],
        "title": columns.get("Title", "").strip(),
        "kind": columns.get("Kind", "").strip("` "),
        "state": columns.get("State", "").strip("` "),
        "ability": ability,
        "ability_name": row.get("Ability", "").strip() or None,
        "ability_status": row.get("Status", "").strip("` ") or None,
        "line": item.get("line"),
        "what": (item.get("what") or {}).get("value"),
        "why": (item.get("why") or {}).get("value"),
        "write_up": columns.get("Write-up", "").strip(),
    }


def desired(f):
    """(open or closed, the reason it closes for, what the A-files say) for an item."""
    if f["state"] == "dropped":
        return "closed", "not planned", "AHEAD says dropped"
    if f["ability_status"] == "done":
        return "closed", "completed", "AHEAD says %s, ABILITIES says %s is done" % (f["state"], f["ability"])
    return "open", None, "AHEAD says %s" % f["state"]


def wanted_labels(f):
    labels = [LISTED_LABEL]
    if f["kind"]:
        labels.append(KIND_PREFIX + f["kind"])
    if f["state"]:
        labels.append(STATE_PREFIX + f["state"])
    return labels


# --- the issue body -------------------------------------------------------------------------------------------------

def clean(text):
    """Text for the body that cannot open or close a comment of ours."""
    return text.replace("<!--", "&lt;!--")


def blob_url(ctx, path):
    return "https://github.com/%s/blob/%s/%s" % (ctx["repo"], quote(ctx["ref"], safe=""), quote(path, safe="/"))


def project_link(ctx, target):
    """A relative link or path as a link to the file at the commit; absolute URLs and anchors stay as they are."""
    if SCHEME.match(target) or target.startswith(("#", "//")):
        return target
    path, hash_, fragment = target.partition("#")
    path = posixpath.normpath(posixpath.join(ctx["prefix"], path.lstrip("/"))) if path else ""
    if not path or path == "." or path.startswith(".."):
        return target
    return blob_url(ctx, path) + (hash_ + fragment)


def write_up_text(ctx, value):
    """The Write-up cell with its relative links, and its backticked paths, pointing at the commit."""
    def rewrite(match):
        if match.group(2) is not None:
            return "[%s](%s%s)" % (match.group(1), project_link(ctx, match.group(2)), match.group(3))
        token = match.group(4)
        if SCHEME.match(token) or not ("/" in token or re.search(r"\.[A-Za-z0-9]{1,5}$", token)):
            return match.group(0)
        url = project_link(ctx, token)
        return match.group(0) if url == token else "[`%s`](%s)" % (token, url)
    return clean(WRITE_UP.sub(rewrite, value))


def owned_text(f, ctx, last):
    """The part of the body the script owns, from the item's marker to the end marker (no trailing newline)."""
    parts = [MARKER_FOR % f["id"]]
    parts.append("What: " + clean(f["what"] or "\u2014"))
    parts.append("Why: " + clean(f["why"] or "\u2014"))
    if f["ability"]:
        parts.append("Ability: %s%s" % (f["ability"], " \u2014 " + clean(f["ability_name"]) if f["ability_name"] else ""))
    if f["write_up"].lower() not in NO_VALUE:
        parts.append("Write-up: " + write_up_text(ctx, f["write_up"]))
    ahead = blob_url(ctx, posixpath.join(ctx["prefix"], "AHEAD.md"))
    if f["line"]:
        parts.append("Source: [AHEAD.md, line %d](%s#L%d)" % (f["line"], ahead, f["line"]))
    else:
        parts.append("Source: [AHEAD.md](%s)" % ahead)
    parts.append(NOTE % f["id"])
    text = "\n\n".join(parts)
    if last:
        text += "\n" + "<!-- a-files:last: %s -->" % last
    return text + "\n" + END


def owned_span(body, identifier):
    """(start, end) of the owned part in a body: from the marker to the end of the end marker; when the end marker is
    missing, only the marker itself, so that nothing a person wrote is replaced."""
    marker = MARKER_FOR % identifier
    start = body.find(marker)
    if start < 0:
        return None
    end = body.find(END, start + len(marker))
    return (start, end + len(END)) if end >= 0 else (start, start + len(marker))


def splice(body, identifier, owned):
    """The body with its owned part replaced by owned; everything outside it kept."""
    span = owned_span(body, identifier)
    return body[:span[0]] + owned + body[span[1]:]


def last_of(body, identifier):
    """The state the projection last set, from the owned part, or None."""
    span = owned_span(body, identifier)
    found = LAST.search(body[span[0]:span[1]]) if span else None
    return found.group(1) if found else None


def comparable(text):
    """The body as compared with what it should be: the commit in its links and the AHEAD line it cites do not count,
    so that a push, or a row added above the item, rewrites no issue whose text says the same."""
    text = BLOB.sub("/blob/REF/", text.replace("\r\n", "\n").strip())
    return re.sub(r"AHEAD\.md, line \d+\]\(([^)#]*)#L\d+\)", r"AHEAD.md, line N](\1#LN)", text)


# --- planning -------------------------------------------------------------------------------------------------------

def label_names(issue):
    return [label["name"] if isinstance(label, dict) else str(label) for label in issue.get("labels") or []]


def reason_text(issue):
    reason = (issue.get("stateReason") or "").lower().replace("_", " ")
    return "%s (%s)" % (issue["state"].lower(), reason) if reason else issue["state"].lower()


def out_comment(f, issue, want, says):
    return ("%s (%s) is out of step with the A-files.\n\n"
            "The A-files say: %s, so this issue should be %s. On GitHub this issue is %s.\n\n"
            "The projection leaves it as it is: a change made on GitHub is never overwritten. An agent will ask the "
            "owner which side wins: take GitHub's version, keep the A-files' version, or decide later.\n\n"
            "AHEAD.md is the source of truth."
            % (f["id"], f["title"] or "untitled", says, want, reason_text(issue)))


def plan_item(f, issue, ctx, decision=None):
    """(the action for the item or None, its mismatch for --report or None).

    An action: {id, kind, number, title, body, add, remove, transition, reason, comment, line}."""
    want, reason, says = desired(f)
    title = ("%s %s" % (f["id"], f["title"])).strip()
    wanted = wanted_labels(f)
    if issue is None:
        action = {"id": f["id"], "kind": "create", "number": None, "title": title, "add": wanted, "remove": [],
                  "body": owned_text(f, ctx, "open") + "\n", "transition": None, "reason": None, "comment": None}
        action["line"] = '%s create "%s"' % (f["id"], title)
        return action, None
    actual = issue["state"].lower()
    body = issue.get("body") or ""
    last = last_of(body, f["id"])
    labels = label_names(issue)
    flagged = OUT_LABEL in labels
    # Out of step: the issue's state is not what the A-files say, and not the state the script last set.
    out = actual != want and not (last is not None and actual == last)
    mismatch = None
    if out:
        mismatch = {"id": f["id"], "issue": issue["number"], "url": issue.get("url"), "issue_state": actual,
                    "state_reason": (issue.get("stateReason") or "").lower() or None, "a_files_state": want,
                    "ability": f["ability"], "ability_status": f["ability_status"], "item_state": f["state"]}
    transition, comment = None, None
    if decision == "accept":
        new_last, out_now = actual, False
    elif decision == "keep" or (actual != want and not out):
        new_last, out_now = want, False
        transition = want if actual != want else None
    elif out:
        new_last, out_now = last, True
    else:
        new_last, out_now = want, False
    new_body = splice(body, f["id"], owned_text(f, ctx, new_last))
    changes = []
    if issue["title"] != title:
        changes.append("title")
    if comparable(new_body) != comparable(body):
        changes.append("body")
    add = [label for label in wanted if label not in labels]
    remove = [label for label in labels if label.startswith((KIND_PREFIX, STATE_PREFIX)) and label not in wanted]
    if out_now and not flagged:
        add.append(OUT_LABEL)
        comment = out_comment(f, issue, want, says)
    if not out_now and flagged:
        remove.append(OUT_LABEL)
    if add or remove:
        changes.append("labels")
    if decision == "keep" and (flagged or transition):
        comment = ("%s: the owner kept the A-files' state. This issue is %s, as AHEAD.md and ABILITIES.md say."
                   % (f["id"], want if not reason else "%s (%s)" % (want, reason)))
    flagging = out_now and not flagged
    if not (transition or changes or comment):
        return None, mismatch
    number = issue["number"]
    if decision == "keep":
        kind, line = "keep", "%s keep-a-files #%d (%s)" % (f["id"], number, "close" if transition == "closed" else
                                                           "reopen" if transition else "label removed")
    elif decision == "accept":
        kind, line = "accept", "%s accept-github #%d (%s)" % (f["id"], number, actual)
    elif transition:
        kind = "close" if transition == "closed" else "reopen"
        line = "%s close #%d (%s)" % (f["id"], number, reason) if transition == "closed" else "%s reopen #%d" % (f["id"], number)
    elif flagging:
        kind, line = "out of step", "%s out of step #%d: %s on GitHub, %s" % (f["id"], number, actual, says)
    else:
        kind, line = "update", "%s update #%d (%s)" % (f["id"], number, ", ".join(changes) or "labels")
    return {"id": f["id"], "kind": kind, "number": number, "title": title if "title" in changes else None,
            "body": new_body if "body" in changes else None, "add": add, "remove": remove, "transition": transition,
            "reason": reason, "comment": comment, "line": line}, mismatch


def plan(facts_list, by_id, ctx, include_open, decisions):
    """(actions, mismatches) over the items; with decisions, only the items named in them."""
    selected = PROJECTED + (("open",) if include_open else ())
    actions, mismatches = [], []
    for f in sorted(facts_list, key=lambda f: f["id"]):
        if decisions and f["id"] not in decisions:
            continue
        issue = by_id.get(f["id"])
        if issue is None:
            if f["state"] not in selected or desired(f)[0] == "closed":
                continue                        # never an issue for a dropped item, nor a closed one for finished work
        elif f["state"] not in selected and f["state"] != "dropped" and not decisions:
            continue
        action, mismatch = plan_item(f, issue, ctx, decisions.get(f["id"]))
        if mismatch:
            mismatches.append(mismatch)
        if action:
            actions.append(action)
    return actions, mismatches


# --- carrying the plan out ------------------------------------------------------------------------------------------

def ensure_labels(repo, actions):
    """Create each label the actions add, once (--force: it exists, or it is made)."""
    names = []
    for action in actions:
        names += [label for label in action["add"] if label not in names]
    for name in names:
        prefix = next((p for p in (KIND_PREFIX, STATE_PREFIX) if name.startswith(p)), name)
        color, description = LABEL_STYLE[prefix]
        gh(["label", "create", name, "--repo", repo, "--force", "--color", color, "--description", description])


def carry_out(repo, action):
    if action["kind"] == "create":
        args = ["issue", "create", "--repo", repo, "--title", action["title"], "--body-file", "-"]
        for label in action["add"]:
            args += ["--label", label]
        gh(args, action["body"])
        return
    number = str(action["number"])
    # The state first: if the edit then fails, the next run still sees an issue that matches and records it.
    if action["transition"] == "closed":
        gh(["issue", "close", number, "--repo", repo, "--reason", action["reason"]])
    elif action["transition"] == "open":
        gh(["issue", "reopen", number, "--repo", repo])
    if action["title"] or action["body"] is not None or action["add"] or action["remove"]:
        args = ["issue", "edit", number, "--repo", repo]
        if action["title"]:
            args += ["--title", action["title"]]
        if action["body"] is not None:
            args += ["--body-file", "-"]
        for label in action["add"]:
            args += ["--add-label", label]
        for label in action["remove"]:
            args += ["--remove-label", label]
        gh(args, action["body"])
    if action["comment"]:
        gh(["issue", "comment", number, "--repo", repo, "--body-file", "-"], action["comment"])


# --- the run --------------------------------------------------------------------------------------------------------

def parse(argv):
    parser = argparse.ArgumentParser(description="Project AHEAD.md's actionable items to GitHub issues (dry run "
                                                 "unless --apply).")
    parser.add_argument("--root", default=".", help="the repository's root folder")
    parser.add_argument("--repo", help="OWNER/NAME (default: the repository gh reports for the folder)")
    parser.add_argument("--ref", help="the commit the links point at (default: git's HEAD)")
    parser.add_argument("--include-open", action="store_true", help="project `open` items as well")
    parser.add_argument("--apply", action="store_true", help="write to GitHub (default: print the plan only)")
    parser.add_argument("--report", action="store_true",
                        help="print the issues out of step as JSON, for the alignment (read-only)")
    parser.add_argument("--keep-a-files", action="append", default=[], metavar="AH-NNN",
                        help="the owner's answer: the A-files' state wins for this item")
    parser.add_argument("--accept-github", action="append", default=[], metavar="AH-NNN",
                        help="the owner's answer: GitHub's state is taken for this item (the A-files are updated "
                             "separately)")
    args = parser.parse_args(argv)
    decisions = {}
    for kind, names in (("keep", args.keep_a_files), ("accept", args.accept_github)):
        for name in names:
            if not AH_ID.match(name):
                parser.error("%r is not an item identifier (AH-NNN)" % name)
            if decisions.get(name, kind) != kind:
                parser.error("%s cannot be both kept and accepted" % name)
            decisions[name] = kind
    if args.report and (args.apply or decisions):
        parser.error("--report only reads; it does not go with --apply, --keep-a-files or --accept-github")
    if args.repo and not REPO.match(args.repo):
        parser.error("--repo is OWNER/NAME")
    args.decisions = decisions
    return args


def list_issues(repo):
    out = gh(["issue", "list", "--repo", repo, "--state", "all", "--label", LISTED_LABEL, "--limit", "1000",
              "--json", "number,title,state,stateReason,labels,body,url"])
    try:
        issues = json.loads(out or "[]")
    except ValueError:
        raise GhFailed("gh issue list gave output that is not JSON")
    by_id = {}
    for issue in sorted(issues, key=lambda i: i["number"]):
        found = FOUND_MARKER.search(issue.get("body") or "")
        if found:
            by_id.setdefault(found.group(1), issue)         # the oldest issue holding a marker is the item's
    return by_id


def run(args):
    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        raise CannotRun("no such folder: %s" % args.root)
    data = run_check(root)
    register = (data.get("registers") or {}).get("ahead_items") or {}
    if not register.get("read"):
        print("nothing done: %s" % READ_REASONS.get(register.get("reason"), "AHEAD.md's items were not read"))
        return 0
    abilities = {a["id"]: a for a in data.get("abilities") or []}
    facts_list = [facts(i, abilities) for i in data.get("ahead_items") or [] if i.get("columns")]
    known = {f["id"] for f in facts_list}
    for identifier in args.decisions:
        if identifier not in known:
            print("%s is not in AHEAD.md" % identifier, file=sys.stderr)
            return 2
    try:
        repo = args.repo or json.loads(gh(["repo", "view", "--json", "nameWithOwner"], cwd=root) or "{}").get("nameWithOwner")
        if not repo or not REPO.match(repo):
            raise CannotRun("no GitHub repository: give --repo OWNER/NAME, or run where gh knows the repository")
        by_id = list_issues(repo)
    except GhFailed as exc:
        raise CannotRun(str(exc))
    except ValueError:
        raise CannotRun("gh repo view gave output that is not JSON")
    for identifier in args.decisions:
        if identifier not in by_id:
            print("%s has no issue" % identifier, file=sys.stderr)
            return 2
    by_fact = {f["id"]: f for f in facts_list}
    for identifier, decision in args.decisions.items():
        want = desired(by_fact[identifier])[0]
        if decision == "accept" and by_id[identifier]["state"].lower() != want:
            # Taking GitHub's version is the A-files' change first: accepted before it, the next run would read the
            # A-files' older state as a change of theirs and undo the owner's answer.
            print("%s: the A-files still say the issue should be %s; update AHEAD.md or ABILITIES.md to GitHub's "
                  "version first, then accept it" % (identifier, want), file=sys.stderr)
            return 2
    ref, prefix = git_ref(root, args.ref)
    ctx = {"repo": repo, "ref": ref, "prefix": prefix}
    actions, mismatches = plan(facts_list, by_id, ctx, args.include_open, args.decisions)
    if args.report:
        print(json.dumps({"repo": repo, "out_of_step": mismatches}, indent=2))
        return 0
    if not actions:
        print("nothing to do")
        return 0
    if not args.apply:
        for action in actions:
            print(action["line"])
        print("dry run: nothing was written; run with --apply to carry it out", file=sys.stderr)
        return 0
    try:
        ensure_labels(repo, actions)
        for action in actions:
            print(action["line"])
            sys.stdout.flush()
            carry_out(repo, action)
    except GhFailed as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


def main(argv):
    args = parse(argv)
    try:
        return run(args)
    except CannotRun as exc:
        print(str(exc), file=sys.stderr)
        return COULD_NOT_RUN


# The error handlers that never end a write in an encoding error. Every other one can: strict, surrogateescape (which
# a C locale gives standard output), surrogatepass on an encoding other than UTF, and any a program registers.
SAFE_ERRORS = ("backslashreplace", "namereplace", "xmlcharrefreplace", "replace", "ignore")
ESCAPED = "+backslashreplace"


def _escaping(errors):
    """The name of an error handler that writes a character as the handler errors writes it, and as its Python escape
    (\\u2192) where that handler would end the write in an error; registered on first use."""
    name = errors + ESCAPED
    try:
        codecs.lookup_error(name)
    except LookupError:
        original = codecs.lookup_error(errors)

        def handler(exc):
            if not isinstance(exc, UnicodeEncodeError):
                return original(exc)
            one = UnicodeEncodeError(exc.encoding, exc.object, exc.start, exc.start + 1, exc.reason)
            try:
                return original(one)
            except UnicodeEncodeError:
                return codecs.backslashreplace_errors(one)

        codecs.register_error(name, handler)
    return name


def writable_output(*streams):
    """Let standard output and standard error (or the streams given) write any text: a character their encoding cannot
    write, as on a legacy Windows code page or under a C locale, is written as its Python escape (\\u2192 for an
    arrow) instead of ending the run in an encoding error. A stream keeps what its error handler does where that
    handler writes a character: under surrogateescape, a name that is not text in the encoding is still written as its
    bytes. A handler that never raises, and UTF with surrogatepass, are left as they are."""
    for stream in streams or (sys.stdout, sys.stderr):
        errors, encoding = getattr(stream, "errors", None), getattr(stream, "encoding", None) or ""
        if not errors or errors in SAFE_ERRORS or errors.endswith(ESCAPED) or not hasattr(stream, "reconfigure"):
            continue
        try:
            if errors == "surrogatepass" and codecs.lookup(encoding).name.startswith("utf"):
                continue
            stream.reconfigure(errors="backslashreplace" if errors == "strict" else _escaping(errors))
        except (LookupError, ValueError, OSError):
            pass


if __name__ == "__main__":
    writable_output()
    sys.exit(main(sys.argv[1:]))
