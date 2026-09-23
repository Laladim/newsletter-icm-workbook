#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Verify an approved publication brief or a complete publication profile."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_PROFILE_FILES = [
    "publication-brief.md",
    "CONTEXT.md",
    "editorial-contract.md",
    "source-contract.md",
    "visual-contract.md",
    "delivery-contract.md",
    "skill-bindings.md",
]
REQUIRED_BRIEF_FIELDS = [
    "publication_id",
    "publication_title",
    "brief_status",
    "approved_by",
    "approved_at",
    "audience_decision_by",
    "editorial_promise_decision_by",
    "positioning_decision_by",
    "risk_tolerance_decision_by",
    "publishing_authority_decision_by",
]
HUMAN_BRIEF_FIELDS = [
    "approved_by",
    "audience_decision_by",
    "editorial_promise_decision_by",
    "positioning_decision_by",
    "risk_tolerance_decision_by",
    "publishing_authority_decision_by",
]
REQUIRED_BRIEF_HEADINGS = [
    "## Supplied facts",
    "## Researched evidence",
    "## Interpretations",
    "## Human decisions",
    "## Audience and recurring problem",
    "## Editorial thesis, promise, and positioning",
    "## Topic boundaries and edition shape",
    "## Evidence and risk",
    "## Voice, expertise, and visuals",
    "## Cadence, ownership, delivery, and metrics",
    "## Open questions and unresolved evidence",
    "## Approval record",
]
REQUIRED_DECISIONS = [
    "Audience choice",
    "Reader problem",
    "Editorial thesis",
    "Recurring promise",
    "Positioning",
    "Topic boundaries and point of view",
    "Risk tolerance",
    "Final profile reviewer",
    "Schedule, send, activate, and publish authority",
]
REQUIRED_CONTEXT_FIELDS = [
    "publication_id",
    "title",
    "mode",
    "profile_status",
    "profile_review_status",
    "profile_reviewed_by",
    "profile_reviewed_at",
    "publication_brief_sha256",
    "canonical_output_home",
    "final_review_surface",
    "routine_run_authority",
    "final_review_approver",
    "schedule_send_publish_authority",
    "post_publish_record_authority",
]
HUMAN_CONTEXT_FIELDS = [
    "routine_run_authority",
    "final_review_approver",
    "schedule_send_publish_authority",
    "post_publish_record_authority",
]
CAPABILITIES = [
    "candidate discovery",
    "research and source verification",
    "editorial judgment",
    "newsletter writing",
    "factual and risk review",
    "visual production",
    "subject and packaging",
    "delivery adapter",
    "analytics and records",
]
PLACEHOLDER_PATTERNS = [
    re.compile(r"\{\{"),
    re.compile(r"\}\}"),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\breplace\b", re.IGNORECASE),
    re.compile(r"configure-after-brief", re.IGNORECASE),
    re.compile(r"yes or no", re.IGNORECASE),
]
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"\b(?:sk|ghp|github_pat)_[A-Za-z0-9_-]{16,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b"),
    re.compile(r"\bya29\.[0-9A-Za-z_-]{20,}\b"),
    re.compile(
        r"(?i)\b(?:api[_-]?key|client[_-]?secret|access[_-]?token|password)"
        r"\s*[:=]\s*['\"]?[A-Za-z0-9_./+-]{12,}"
    ),
]
PRIVATE_PATH_PREFIXES = ("/" + "Users/", "C:" + "\\Users\\", "~" + "/")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    values: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def valid_date(value: str) -> bool:
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def is_human(value: str) -> bool:
    return value.lower().startswith("human:") and len(value.split(":", 1)[1].strip()) >= 2


def placeholder_hits(path: Path) -> list[str]:
    text = path.read_text(errors="ignore")
    return [pattern.pattern for pattern in PLACEHOLDER_PATTERNS if pattern.search(text)]


def secret_hits(path: Path) -> list[str]:
    text = path.read_text(errors="ignore")
    return [pattern.pattern for pattern in SECRET_PATTERNS if pattern.search(text)]


def resolve_profile(value: str) -> Path:
    candidate = Path(value).expanduser()
    if candidate.is_absolute():
        return candidate.resolve()
    direct = (Path.cwd() / candidate).resolve()
    if direct.is_dir():
        return direct
    return (ROOT / "publications" / value).resolve()


def verify_brief(profile: Path) -> list[str]:
    errors: list[str] = []
    brief = profile / "publication-brief.md"
    if not brief.is_file():
        return [f"missing publication brief: {brief}"]
    identity = parse_frontmatter(brief)
    for field in REQUIRED_BRIEF_FIELDS:
        if not identity.get(field):
            errors.append(f"publication brief front matter is missing: {field}")
    if identity.get("publication_id") != profile.name:
        errors.append(
            "publication folder and brief publication_id disagree: "
            f"{profile.name} vs {identity.get('publication_id', 'missing')}"
        )
    if identity.get("brief_status") != "approved":
        errors.append("publication brief status must be approved")
    for field in HUMAN_BRIEF_FIELDS:
        value = identity.get(field, "")
        if value and not is_human(value):
            errors.append(f"publication brief {field} must begin with human:")
    approved_at = identity.get("approved_at", "")
    if approved_at and not valid_date(approved_at):
        errors.append("publication brief approved_at must be YYYY-MM-DD")
    text = brief.read_text()
    for heading in REQUIRED_BRIEF_HEADINGS:
        if heading not in text:
            errors.append(f"publication brief is missing heading: {heading}")
    for decision in REQUIRED_DECISIONS:
        if not re.search(rf"^\|\s*{re.escape(decision)}\s*\|", text, re.MULTILINE):
            errors.append(f"publication brief is missing human decision row: {decision}")
    for hit in placeholder_hits(brief):
        errors.append(f"publication brief contains unresolved placeholder: {hit}")
    for hit in secret_hits(brief):
        errors.append(f"publication brief may expose a secret: {hit}")
    if any(prefix in text for prefix in PRIVATE_PATH_PREFIXES):
        errors.append("publication brief contains a private local path")
    return errors


def markdown_table_rows(path: Path) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in path.read_text().splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 5:
            continue
        if cells[0].lower() == "capability" or all(
            set(cell) <= {"-", ":"} for cell in cells
        ):
            continue
        rows.append(cells)
    return rows


def verify_bindings(profile: Path) -> list[str]:
    errors: list[str] = []
    path = profile / "skill-bindings.md"
    if not path.is_file():
        return [f"missing capability binding file: {path}"]
    rows = markdown_table_rows(path)
    by_name = {row[0].lower(): row for row in rows}
    for capability in CAPABILITIES:
        if capability not in by_name:
            errors.append(f"missing capability binding row: {capability}")
    for name, row in by_name.items():
        if name not in CAPABILITIES:
            errors.append(f"unknown capability binding row: {row[0]}")
            continue
        _, binding, trigger, proof, required = row
        required_lower = required.lower()
        if required_lower not in {"yes", "no"}:
            errors.append(f"{name}: Required? must be yes or no")
        if not trigger or not proof:
            errors.append(f"{name}: trigger and output proof must be explicit")
        if ":" not in binding:
            errors.append(f"{name}: binding must use an allowed prefix")
            continue
        prefix, detail = binding.split(":", 1)
        prefix = prefix.lower().strip()
        detail = detail.strip()
        if prefix not in {"manual", "local", "command", "none"}:
            errors.append(f"{name}: unsupported binding prefix: {prefix}")
            continue
        if len(detail) < 4:
            errors.append(f"{name}: binding detail is too vague")
        if prefix == "none" and required_lower == "yes":
            errors.append(f"{name}: required capability cannot use none:")
        if prefix in {"local", "command"}:
            candidate = Path(detail)
            if candidate.is_absolute() or ".." in candidate.parts:
                errors.append(f"{name}: binding path must be repository-relative")
                continue
            resolved = ROOT / candidate
            if not resolved.exists():
                errors.append(f"{name}: bound path does not exist: {detail}")
            elif prefix == "command" and not resolved.is_file():
                errors.append(f"{name}: command binding is not a file: {detail}")
    return errors


def verify_profile(profile: Path, pre_review: bool) -> list[str]:
    errors = verify_brief(profile)
    for name in REQUIRED_PROFILE_FILES:
        path = profile / name
        if not path.is_file():
            errors.append(f"missing publication file: {name}")
    if not (profile / "CONTEXT.md").is_file():
        return errors

    for name in REQUIRED_PROFILE_FILES:
        path = profile / name
        if not path.is_file():
            continue
        for hit in placeholder_hits(path):
            errors.append(f"{name} contains unresolved placeholder: {hit}")
        for hit in secret_hits(path):
            errors.append(f"{name} may expose a secret: {hit}")
        text = path.read_text(errors="ignore")
        if any(prefix in text for prefix in PRIVATE_PATH_PREFIXES):
            errors.append(f"{name} contains a private local path")

    context = profile / "CONTEXT.md"
    identity = parse_frontmatter(context)
    for field in REQUIRED_CONTEXT_FIELDS:
        if pre_review and field in {"profile_reviewed_by", "profile_reviewed_at"}:
            continue
        if not identity.get(field):
            errors.append(f"publication CONTEXT.md front matter is missing: {field}")
    if identity.get("publication_id") != profile.name:
        errors.append("publication folder and CONTEXT.md publication_id disagree")
    mode = identity.get("mode", "")
    if mode not in {"shadow", "supervised-pilot", "production"}:
        errors.append("publication mode must be shadow, supervised-pilot, or production")
    if identity.get("profile_status") != "configured":
        errors.append("profile_status must be configured")
    if not pre_review:
        if identity.get("profile_review_status") != "approved":
            errors.append("profile_review_status must be approved")
        if not is_human(identity.get("profile_reviewed_by", "")):
            errors.append("profile_reviewed_by must begin with human:")
        reviewed_at = identity.get("profile_reviewed_at", "")
        if not valid_date(reviewed_at):
            errors.append("profile_reviewed_at must be YYYY-MM-DD")
    for field in HUMAN_CONTEXT_FIELDS:
        if not is_human(identity.get(field, "")):
            errors.append(f"{field} must begin with human:")
    if mode == "shadow":
        for field in ["canonical_output_home", "final_review_surface"]:
            if not identity.get(field, "").startswith("local-markdown:"):
                errors.append(f"shadow profile {field} must begin with local-markdown:")

    brief = profile / "publication-brief.md"
    if brief.is_file():
        expected = hashlib.sha256(brief.read_bytes()).hexdigest()
        actual = identity.get("publication_brief_sha256", "")
        if actual != expected:
            errors.append(
                "publication_brief_sha256 does not match the approved publication brief"
            )
    errors.extend(verify_bindings(profile))
    return errors


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument(
        "publication", help="publication folder or ID under publications/"
    )
    group = command.add_mutually_exclusive_group()
    group.add_argument(
        "--brief-only", action="store_true", help="verify the approved brief gate"
    )
    group.add_argument(
        "--pre-review",
        action="store_true",
        help="verify generated contracts before final human profile review",
    )
    return command


def main() -> int:
    args = parser().parse_args()
    profile = resolve_profile(args.publication)
    if not profile.is_dir():
        print(f"PUBLICATION VERIFICATION FAILED\n- publication folder not found: {profile}")
        return 1
    errors = (
        verify_brief(profile)
        if args.brief_only
        else verify_profile(profile, pre_review=args.pre_review)
    )
    if errors:
        print("PUBLICATION VERIFICATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    if args.brief_only:
        print("PUBLICATION BRIEF VERIFICATION PASSED")
        print("- required human decisions: approved")
        print("- evidence categories: present and separated")
        print("- contract generation gate: open")
    elif args.pre_review:
        print("PUBLICATION PRE-REVIEW VERIFICATION PASSED")
        print("- seven publication files: complete")
        print("- approved brief hash: matched")
        print("- bindings and authority fields: structurally valid")
        print("- next gate: explicit human profile review")
    else:
        print("PUBLICATION VERIFICATION PASSED")
        print("- seven publication files: complete")
        print("- approved brief hash: matched")
        print("- final human profile review: approved")
        print("- first edition gate: open")
    return 0


if __name__ == "__main__":
    sys.exit(main())
