#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Verify the public newsletter ICM workbook, safety, and file classification."""

from __future__ import annotations

import csv
import fnmatch
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
STAGES = [
    "01_intake",
    "02_source-selection",
    "03_research",
    "04_routing",
    "05_draft",
    "06_quality-review",
    "07_package",
    "08_delivery",
    "09_post-publish",
]
ROOT_FILES = [
    ".gitignore",
    "README.md",
    "START-HERE.md",
    "SETUP.md",
    "NEW-NEWSLETTER-DISCOVERY.md",
    "DISCUSSION-GUIDE.md",
    "FILE-BUILD-MAP.csv",
    "CONTEXT.md",
    "AGENTS.md",
    "CLAUDE.md",
    "VERSION",
    "LICENSE-CODE",
    "LICENSE-CONTENT",
]
PUBLICATION_FILES = [
    "publication-brief.md",
    "CONTEXT.md",
    "editorial-contract.md",
    "source-contract.md",
    "visual-contract.md",
    "delivery-contract.md",
    "skill-bindings.md",
]
SCRIPTS = [
    "scripts/stamp.py",
    "scripts/verify-publication.py",
    "scripts/verify-edition.py",
    "scripts/verify-template.py",
    "scripts/smoke-test.py",
    "_shared/check-rules.py",
]
FORBIDDEN_PUBLIC_TERMS = [
    "cobaltintelligence",
    "laladimalanta",
    "/users/",
    "life-dashboard",
    "claude-sheets-key",
    "pub_a4b9",
    "seg_0a4",
    "beehiiv",
    "cloudinary",
]
FORBIDDEN_GENERIC_ASSUMPTIONS = [
    "alt-lender",
    "alt lender",
    "news list row",
    "news analysis row",
    "product video",
    "nonbank credit",
]
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\b(?:sk|ghp|github_pat)_[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b"),
    re.compile(r"\bya29\.[0-9A-Za-z_-]{20,}\b"),
]
MAP_COLUMNS = [
    "path",
    "purpose",
    "classification",
    "required decisions",
    "evidence to gather",
    "agent role",
    "human decision",
    "output destination",
    "dependency",
    "readiness check",
    "sanitized example",
]
CLASSIFICATIONS = {
    "Copy as-is",
    "Customize for the publication",
    "Generate per edition",
    "Optional",
    "Never publish",
}


def public_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts or "__pycache__" in relative.parts:
            continue
        if relative.parts[0] in {"publications", "editions"} and path.name != ".gitkeep":
            continue
        if relative.parts[0] == ".artifacts":
            continue
        files.append(path)
    return sorted(files)


def map_rows(errors: list[str]) -> list[dict[str, str]]:
    path = ROOT / "FILE-BUILD-MAP.csv"
    if not path.is_file():
        return []
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != MAP_COLUMNS:
            errors.append(
                "FILE-BUILD-MAP.csv headers differ from the required eleven columns"
            )
            return []
        rows = list(reader)
    for number, row in enumerate(rows, start=2):
        if not row["path"].strip():
            errors.append(f"FILE-BUILD-MAP.csv row {number} has no path")
        if row["classification"] not in CLASSIFICATIONS:
            errors.append(
                f"FILE-BUILD-MAP.csv row {number} has invalid classification: "
                f"{row['classification']}"
            )
        for column in MAP_COLUMNS[1:]:
            if not row[column].strip():
                errors.append(
                    f"FILE-BUILD-MAP.csv row {number} has blank {column}"
                )
    return rows


def verify_map_coverage(errors: list[str]) -> None:
    rows = map_rows(errors)
    if not rows:
        return
    patterns = [row["path"] for row in rows]
    for path in public_files():
        relative = str(path.relative_to(ROOT))
        if not any(fnmatch.fnmatch(relative, pattern) for pattern in patterns):
            errors.append(f"unclassified repository artifact: {relative}")


def main() -> int:
    errors: list[str] = []

    for name in ROOT_FILES:
        if not (ROOT / name).is_file():
            errors.append(f"missing root file: {name}")

    agents = ROOT / "AGENTS.md"
    claude = ROOT / "CLAUDE.md"
    if agents.is_file() and claude.is_file() and agents.read_bytes() != claude.read_bytes():
        errors.append("AGENTS.md and CLAUDE.md differ")
    kickoff = "Read SETUP.md and guide me through creating my newsletter ICM workspace."
    for name in ["README.md", "START-HERE.md", "SETUP.md", "AGENTS.md", "CLAUDE.md"]:
        path = ROOT / name
        if path.is_file() and kickoff not in path.read_text():
            errors.append(f"cold-start kickoff is missing from {name}")

    version = (ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").is_file() else ""
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION must contain a semantic version")
    readme = (ROOT / "README.md").read_text() if (ROOT / "README.md").is_file() else ""
    if version and f"newsletter-icm-workbook:v{version}" not in readme:
        errors.append("README live marker does not match VERSION")

    edition = ROOT / "_templates" / "edition"
    for stage in STAGES:
        base = edition / stage
        for relative in [
            "CONTEXT.md",
            "references/CONTEXT.md",
            "references/output-contract.md",
            "output/.gitkeep",
        ]:
            if not (base / relative).is_file():
                errors.append(f"missing edition factory file: {stage}/{relative}")

    publication = ROOT / "_templates" / "publication"
    for name in PUBLICATION_FILES:
        if not (publication / name).is_file():
            errors.append(f"missing publication factory file: {name}")

    for relative in SCRIPTS:
        script = ROOT / relative
        if not script.is_file():
            errors.append(f"missing script: {relative}")
            continue
        try:
            compile(script.read_text(), str(script), "exec")
        except SyntaxError as exc:
            errors.append(f"invalid script {relative}: {exc}")
        if "SPDX-License-Identifier: MIT" not in script.read_text():
            errors.append(f"script lacks MIT SPDX marker: {relative}")

    scan_skip = {Path(__file__).resolve()}
    for path in public_files():
        if path.resolve() in scan_skip:
            continue
        text = path.read_text(errors="ignore")
        lowered = text.lower()
        for token in FORBIDDEN_PUBLIC_TERMS:
            if token in lowered:
                errors.append(
                    f"private or production-specific token in {path.relative_to(ROOT)}: {token}"
                )
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(
                    f"credential-like value in {path.relative_to(ROOT)}: {pattern.pattern}"
                )
        if "—" in text or "&mdash;" in lowered or "&#8212;" in lowered or "&#x2014;" in lowered:
            errors.append(f"em dash found in {path.relative_to(ROOT)}")

    generic_paths = [
        ROOT / "_shared",
        ROOT / "_templates",
        ROOT / "README.md",
        ROOT / "START-HERE.md",
        ROOT / "SETUP.md",
        ROOT / "NEW-NEWSLETTER-DISCOVERY.md",
        ROOT / "CONTEXT.md",
        ROOT / "AGENTS.md",
        ROOT / "CLAUDE.md",
    ]
    for base in generic_paths:
        candidates = [base] if base.is_file() else list(base.rglob("*"))
        for path in candidates:
            if not path.is_file():
                continue
            lowered = path.read_text(errors="ignore").lower()
            for token in FORBIDDEN_GENERIC_ASSUMPTIONS:
                if token in lowered:
                    errors.append(
                        f"generic workflow inherits publication assumption in "
                        f"{path.relative_to(ROOT)}: {token}"
                    )

    verify_map_coverage(errors)

    example = ROOT / "examples" / "beyond-banks" / "publications" / "beyond-banks"
    if example.is_dir():
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "verify-publication.py"),
                str(example),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if result.returncode:
            errors.append("sanitized Beyond Banks example fails publication verification")
            errors.extend(
                f"example verifier: {line}"
                for line in result.stdout.splitlines()
                if line.startswith("-")
            )
    else:
        errors.append("missing sanitized Beyond Banks example profile")

    example_root = ROOT / "examples" / "beyond-banks"
    if any(path.is_dir() and path.name == "editions" for path in example_root.rglob("*")):
        errors.append("sanitized example must not contain edition records")

    if errors:
        print("TEMPLATE VERIFICATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("TEMPLATE VERIFICATION PASSED")
    print(f"- reusable edition stages: {len(STAGES)}")
    print("- publication factory: seven files")
    print("- entry maps: identical and setup-first")
    print("- file build map: complete and classified")
    print("- scripts: syntax and MIT markers valid")
    print("- private data, credential, style, and assumption scans: clean")
    print("- sanitized example: publication verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
