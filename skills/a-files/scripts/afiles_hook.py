#!/usr/bin/env python3
"""Agent hooks of the a-files plugin: a light note at session start and the check's findings before the stop.

Usage:
    afiles_hook.py session-start|before-stop [--emit auto|claude|codex|kiro|raw]
    afiles_hook.py --version

The tool's JSON event arrives on stdin. The hook acts only in a git repository whose ACTIVE.md carries the
hot-zone marker; anywhere else, and on any error, it prints nothing, writes nothing and exits 0.
Both moments only inform the agent; only the stop may continue the turn, once per finding.

Self-contained: standard library only. It runs check_tracking.py, which sits beside it.
"""
import argparse
import codecs
import hashlib
import json
import os
import re
import select
import subprocess
import sys

A_FILES_VERSION = "2.1.0"
MARKER = "<!-- hot zone ends -->"
LIMIT = 3900
MAX_FINDINGS = 5
MAX_MEMORY_FILES = 8
HERE = os.path.dirname(os.path.abspath(__file__))

SESSION_NOTE = (
    "Note for the agent: this project keeps the A-files. Before your first edit, say where things stand "
    "in four short lines: Finished, Remaining, Blocked by, Next step (write \"nothing\" for an empty line). "
    "Check them against git log and git status, not only against ACTIVE.md. When the request already says "
    "exactly what to do, one short line is enough. This asks nothing of the owner."
)
STOP_HEAD = (
    "Notes for the agent: the A-files are out of step. None of this needs the owner. Before you end your turn, "
    "align them now or list them in your handoff. Change only what the current task authorizes."
)
FINDING = re.compile(r"^(?P<path>.+?):(?P<line>\d+): ERROR (?P<code>[A-Za-z0-9_-]+): (?P<message>.*)$")


def read_event():
    """The event JSON from stdin; {} when there is none within about a second."""
    try:
        if sys.stdin is None or sys.stdin.isatty():
            return {}
        ready, _, _ = select.select([sys.stdin], [], [], 1.0)
        if not ready:
            return {}
        data = json.loads(sys.stdin.read() or "{}")
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def git(args, cwd):
    result = subprocess.run(["git"] + args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                            encoding="utf-8", errors="replace", timeout=10)
    return result.stdout.strip() if result.returncode == 0 else ""


def project_root(event):
    cwd = event.get("cwd")
    if not isinstance(cwd, str) or not os.path.isdir(cwd):
        cwd = os.getcwd()
    return git(["rev-parse", "--show-toplevel"], cwd)


def adopted(root):
    try:
        with open(os.path.join(root, "ACTIVE.md"), encoding="utf-8", errors="replace") as handle:
            return MARKER in handle.read()
    except OSError:
        return False


def cap(text):
    return text if len(text) <= LIMIT else text[:LIMIT - 3].rstrip() + "..."


def run_check(root):
    script = os.path.join(HERE, "check_tracking.py")
    if not os.path.isfile(script):
        return ""
    base = [sys.executable or "python3", script, "--root", root]
    result = subprocess.run(base + ["--strict"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            encoding="utf-8", errors="replace", timeout=30, cwd=root)
    if result.returncode == 2:
        result = subprocess.run(base, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                encoding="utf-8", errors="replace", timeout=30, cwd=root)
    return result.stdout


def parse_findings(output):
    found = []
    for line in output.splitlines():
        match = FINDING.match(line.strip())
        if match:
            found.append((match.group("path"), match.group("code"), match.group("message").strip(), line.strip()))
    return found


def key_of(path, code, message):
    subject = re.sub(r"\bline \d+\b", "line", message)
    return "%s|%s|%s" % (code, path, subject)


def memory_file(root, session):
    digest = hashlib.sha1(session.encode("utf-8")).hexdigest()[:16]
    path = git(["rev-parse", "--git-path", "afiles-hook-%s.json" % digest], root)
    if not path:
        return ""
    return path if os.path.isabs(path) else os.path.join(root, path)


def prune(directory, keep_path):
    try:
        names = [os.path.join(directory, n) for n in os.listdir(directory)
                 if n.startswith("afiles-hook-") and n.endswith(".json")]
        names.sort(key=lambda p: os.path.getmtime(p))
        while len(names) > MAX_MEMORY_FILES:
            victim = names.pop(0)
            if victim != keep_path:
                os.remove(victim)
    except OSError:
        pass


def new_findings(root, session, findings):
    path = memory_file(root, session)
    if not path:
        return []
    try:
        with open(path, encoding="utf-8") as handle:
            sent = json.load(handle)
        sent = set(sent) if isinstance(sent, list) else set()
    except (OSError, ValueError):
        sent = set()
    fresh, seen = [], set()
    for item in findings:
        key = key_of(item[0], item[1], item[2])
        if key not in sent and key not in seen:
            fresh.append(item)
            seen.add(key)
    if fresh:
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(sorted(sent | seen), handle)
        prune(os.path.dirname(path), path)
    return fresh


def stop_text(fresh):
    lines = [STOP_HEAD, ""]
    lines += ["- " + item[3] for item in fresh[:MAX_FINDINGS]]
    if len(fresh) > MAX_FINDINGS:
        lines.append("- and %d more." % (len(fresh) - MAX_FINDINGS))
    return cap("\n".join(lines))


def emit(moment, kind, text):
    if kind == "auto":
        kind = "codex" if os.environ.get("PLUGIN_ROOT") else "claude"
    if moment == "session-start":
        if kind in ("claude", "codex"):
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": text}}))
        else:
            print(text)
        return 0
    if kind == "raw":
        print(text)
        return 2
    print(json.dumps({"decision": "block", "reason": text}))
    return 0


def run(moment, kind):
    event = read_event()
    root = project_root(event)
    if not root or not adopted(root):
        return 0
    if moment == "session-start":
        return emit(moment, kind, cap(SESSION_NOTE))
    if event.get("stop_hook_active") is True:
        return 0
    findings = parse_findings(run_check(root))
    if not findings:
        return 0
    session = str(event.get("session_id") or event.get("sessionId") or "default")
    fresh = new_findings(root, session, findings)
    if not fresh:
        return 0
    return emit(moment, kind, stop_text(fresh))


def main(argv):
    parser = argparse.ArgumentParser(description="Agent hooks of the a-files plugin.")
    parser.add_argument("moment", nargs="?", choices=("session-start", "before-stop"))
    parser.add_argument("--emit", default="auto", choices=("auto", "claude", "codex", "kiro", "raw"))
    parser.add_argument("--version", action="store_true")
    try:
        args = parser.parse_args(argv)
    except SystemExit:
        return 0
    if args.version:
        version = A_FILES_VERSION
        try:
            with open(os.path.join(HERE, "check_tracking.py"), encoding="utf-8") as handle:
                found = re.search(r'^A_FILES_VERSION = "([^"]+)"', handle.read(), re.M)
            version = found.group(1) if found else version
        except OSError:
            pass
        print("a-files %s" % version)
        return 0
    if not args.moment:
        return 0
    try:
        return run(args.moment, args.emit)
    except BaseException:
        return 0


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
    code = main(sys.argv[1:])
    try:
        sys.stdout.flush()
    except Exception:
        pass
    sys.exit(code)
