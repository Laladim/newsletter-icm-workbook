#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check that this computer is ready to run the newsletter workbook.

Run from the repository root before the guided setup:

    python3 scripts/preflight.py

Each check prints PASS, WARN, or FAIL with the next step. Only a FAIL stops
setup. The last check runs the fictional smoke test, so a pass proves the
workbook runs end to end here, not just that files exist.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MINIMUM_PYTHON = (3, 9)
AGENTS = {"claude": "Claude Code", "codex": "Codex"}


def report(status: str, check: str, detail: str) -> None:
    print(f"{status:<4} {check}: {detail}")


def check_python() -> bool:
    found = ".".join(str(part) for part in sys.version_info[:3])
    if sys.version_info[:2] >= MINIMUM_PYTHON:
        report("PASS", "Python", f"{found}")
        return True
    wanted = ".".join(str(part) for part in MINIMUM_PYTHON)
    report("FAIL", "Python", f"{found} found; install Python {wanted} or newer")
    return False


def check_repository() -> bool:
    missing = [name for name in ["AGENTS.md", "SETUP.md", "START-HERE.md"] if not (ROOT / name).is_file()]
    if missing:
        report("FAIL", "Workbook files", f"missing {', '.join(missing)}; clone the full repository again")
        return False
    report("PASS", "Workbook files", f"found in {ROOT.name}")
    return True


def check_agent() -> None:
    found = [label for command, label in AGENTS.items() if shutil.which(command)]
    if found:
        report("PASS", "AI coding agent", f"{' and '.join(found)} found")
        return
    report(
        "WARN",
        "AI coding agent",
        "neither Claude Code nor Codex is on this computer's command path; "
        "install one for the guided path, or use the workbook-only path in START-HERE.md",
    )


def check_git() -> None:
    if shutil.which("git"):
        report("PASS", "Git", "found; you can pull workbook updates")
    else:
        report("WARN", "Git", "not found; download updates as a zip instead of pulling")


def check_smoke_test() -> bool:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "smoke-test.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode == 0 and "SMOKE TEST PASSED" in result.stdout:
        report("PASS", "End-to-end run", "a fictional newsletter passed both gates and Stages 01 to 08")
        return True
    tail = (result.stdout + result.stderr).strip().splitlines()[-3:]
    report("FAIL", "End-to-end run", "smoke test failed; see TROUBLESHOOTING notes. Last lines: " + " | ".join(tail))
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--skip-run", action="store_true", help="skip the end-to-end smoke test")
    args = parser.parse_args()

    ok = check_python() and check_repository()
    check_agent()
    check_git()
    if ok and not args.skip_run:
        ok = check_smoke_test()

    print("PREFLIGHT PASSED: paste the kickoff instruction next." if ok else "PREFLIGHT FAILED: fix each FAIL line above.")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
