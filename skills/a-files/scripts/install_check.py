#!/usr/bin/env python3
"""Install the check from this skill in place; --hook applies the agreed shell hook.

    python3 "<skill-folder>/scripts/install_check.py" --root . [--hook]

Existing checks are never overwritten. Existing shell hooks gain the reporting
line before their commands; other hook formats need their own integration.
"""
import argparse
import codecs
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
LINE = "python3 tools/check_tracking.py --staged || true\n"


def git(root, *args):
    done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, encoding="utf-8",
                          errors="surrogateescape")
    if done.returncode:
        raise ValueError(done.stderr.strip() or "git " + " ".join(args) + " failed")
    return done.stdout.strip()


def install(root, with_hook):
    root = root.resolve()
    git(root, "rev-parse", "--git-dir")
    check = root / "tools/check_tracking.py"
    check_exists = os.path.lexists(check)
    configured = subprocess.run(["git", "-C", str(root), "config", "--local", "--get", "core.hooksPath"],
                                capture_output=True, text=True, encoding="utf-8", errors="surrogateescape")
    if configured.returncode not in (0, 1):
        raise ValueError(configured.stderr.strip())
    hooks_path = configured.stdout.strip()
    hook = Path(git(root, "rev-parse", "--git-path", "hooks/pre-commit"))
    if not hook.is_absolute():
        hook = root / hook
    original = None
    set_path = False
    if with_hook:
        if configured.returncode == 1:
            inherited = subprocess.run(["git", "-C", str(root), "config", "--get", "core.hooksPath"],
                                       capture_output=True, text=True, encoding="utf-8", errors="surrogateescape")
            if inherited.returncode == 0:
                raise ValueError("hooks folder is shared by other repositories; the owner must choose "
                                 "where the hook goes with a local core.hooksPath")
            if inherited.returncode != 1:
                raise ValueError(inherited.stderr.strip())
        # Managers need an explicit step in their own format, never a shell
        # line inserted in a generated launcher (method guide, section 10).
        managers = (".pre-commit-config.yaml", ".pre-commit-config.yml", ".husky",
                    "lefthook.yml", "lefthook.yaml", ".lefthook.yml", ".lefthook.yaml")
        if any((root / name).exists() for name in managers):
            raise ValueError("hook manager found; propose its own check step instead of --hook")
        if not hooks_path and not os.path.lexists(hook):
            hook = root / ".githooks/pre-commit"
            set_path = True
        if hook.is_symlink():
            raise ValueError("hook is a symlink; inspect its owner before integrating")
        if os.path.lexists(hook):
            original = hook.read_bytes()
            text = original.decode("utf-8")
            first = text.splitlines()[0] if text else ""
            if first.startswith("#!") and not re.fullmatch(
                    r"#!\s*(?:/\S*/(?:sh|bash|dash|ksh|zsh)|/usr/bin/env\s+(?:sh|bash|dash|ksh|zsh))(?:\s+.*)?", first):
                raise ValueError("existing hook is not a shell hook; propose its own check step")
            # Keep one reporting line first even if an earlier integration
            # put it last, where it could swallow the owner's refusal.
            lines = [line for line in text.splitlines(keepends=True) if line.rstrip("\r\n") != LINE.rstrip()]
            if first.startswith("#!") and not lines[0].endswith("\n"):
                lines[0] += "\n"
            lines.insert(1 if first.startswith("#!") else 0, LINE)
            content = "".join(lines).encode("utf-8")
        else:
            content = (HERE / "pre-commit").read_bytes()
    # Read all shipped inputs before writing. If a later operation fails,
    # restore the owner's hook and remove only files this invocation created.
    check_content = (HERE / "check_tracking.py").read_bytes()
    check_matches = check_exists and check.is_file() and check.read_bytes() == check_content
    check_created = hook_changed = False
    try:
        if not check_exists:
            check.parent.mkdir(parents=True, exist_ok=True)
            with check.open("xb") as handle:
                check_created = True
                handle.write(check_content)
        if with_hook:
            hook.parent.mkdir(parents=True, exist_ok=True)
            if original is None:
                with hook.open("xb") as handle:
                    hook_changed = True
                    handle.write(content)
                hook.chmod(0o755)
            else:
                hook_changed = True
                hook.write_bytes(content)
            if set_path:
                git(root, "config", "--local", "core.hooksPath", ".githooks")
    except (OSError, ValueError):
        if hook_changed:
            if original is None:
                hook.unlink()
            else:
                hook.write_bytes(original)
        if check_created:
            check.unlink()
        raise
    if check_exists:
        print("Left tools/check_tracking.py untouched; it " +
              ("matches the plugin." if check_matches else "differs from the plugin (or is not a readable file)."))
    else:
        print("Installed tools/check_tracking.py from the plugin folder.")
    if with_hook:
        label = os.path.relpath(hook, root)
        print(("Extended existing " if original is not None else "Installed ") + label + ".")
        if set_path:
            print("Set core.hooksPath .githooks.")
        print("No existing hook replaced. No A-files created or committed.")
    else:
        print("Hook not installed; no hook or git configuration changed.")
        if os.path.lexists(hook):
            print("Propose the reporting line first in the existing shell hook: " + LINE.strip())
        else:
            print("With no existing hook or manager, propose the shipped .githooks/pre-commit "
                  "and git config core.hooksPath .githooks. Ask before running the installer; "
                  "a later yes is a re-run with --hook, leaving the existing check untouched.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    parser.add_argument("--hook", action="store_true", help="apply the explicitly agreed shell hook integration")
    args = parser.parse_args(argv)
    try:
        install(Path(args.root), args.hook)
    except (OSError, ValueError) as error:
        print("Install failed: %s. Nothing installed; no existing hook replaced. "
              "Do not commit a partial adoption; inspect git status before retrying." % error, file=sys.stderr)
        return 1
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
    sys.exit(main())
