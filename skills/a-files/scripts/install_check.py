#!/usr/bin/env python3
"""Install the check from this skill in place; --hook applies the agreed shell hook.

    python3 "<skill-folder>/scripts/install_check.py" --root . [--hook]

Existing checks are never overwritten. Existing shell hooks gain the reporting
line before their commands; other hook formats need their own integration.
"""
import argparse
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
LINE = "python3 tools/check_tracking.py --staged || true\n"


def git(root, *args):
    done = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if done.returncode:
        raise ValueError(done.stderr.strip() or "git " + " ".join(args) + " failed")
    return done.stdout.strip()


def install(root, with_hook):
    root = root.resolve()
    git(root, "rev-parse", "--git-dir")
    check = root / "tools/check_tracking.py"
    check_exists = os.path.lexists(check)
    configured = subprocess.run(["git", "-C", str(root), "config", "--local", "--get", "core.hooksPath"],
                                capture_output=True, text=True)
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
                                       capture_output=True, text=True)
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


if __name__ == "__main__":
    sys.exit(main())
