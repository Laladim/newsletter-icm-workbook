#!/usr/bin/env python3
"""Stamp a publication profile or newsletter edition from this starter."""

from __future__ import annotations

import argparse
import re
import shutil
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PUBLICATION_TEMPLATE = ROOT / "_templates" / "publication"
EDITION_TEMPLATE = ROOT / "_templates" / "edition"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> "NoReturn":
    raise SystemExit(message)


def slug(value: str, label: str) -> str:
    if not SLUG_RE.fullmatch(value):
        fail(f"{label} must be lowercase kebab-case: {value}")
    return value


def iso_date(value: str) -> str:
    try:
        date.fromisoformat(value)
    except ValueError:
        fail(f"date must be YYYY-MM-DD: {value}")
    return value


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        fail(f"missing front matter: {path}")
    block = text.split("---\n", 2)[1]
    values: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip('"')
    return values


def render(template: Path, destination: Path, replacements: dict[str, str]) -> None:
    if destination.exists():
        fail(f"destination already exists: {destination}")
    shutil.copytree(template, destination)
    for path in destination.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".json", ".txt"}:
            continue
        text = path.read_text()
        for old, new in replacements.items():
            text = text.replace(old, new)
        path.write_text(text)


def production_approval(profile: dict[str, str], publication_id: str) -> None:
    approval_name = profile.get("cutover_approval", "")
    approval = ROOT / approval_name
    if not approval_name or not approval.is_file():
        fail("production mode requires a cutover_approval receipt")
    text = approval.read_text()
    required = [
        f"- Publication ID: {publication_id}",
        "- Decision: approved",
        "- Approved mode: production",
        "- Schedule/send/publish authority:",
    ]
    if any(line not in text for line in required):
        fail("cutover approval is incomplete")


def stamp_publication(args: argparse.Namespace) -> None:
    publication_id = slug(args.id, "publication id")
    destination = ROOT / "publications" / publication_id
    render(
        PUBLICATION_TEMPLATE,
        destination,
        {
            "{{publication_id}}": publication_id,
            "{{publication_title}}": args.title.strip(),
        },
    )
    print(f"Stamped publication profile: {destination}")
    print("Configure every contract and begin in shadow mode.")


def stamp_edition(args: argparse.Namespace) -> None:
    publication_id = slug(args.publication, "publication id")
    edition_date = iso_date(args.date)
    profile_path = ROOT / "publications" / publication_id / "CONTEXT.md"
    if not profile_path.is_file():
        fail(f"publication profile not found: {profile_path}")
    profile = frontmatter(profile_path)
    if profile.get("profile_status") != "configured":
        fail("publication profile is not configured")
    mode = profile.get("mode", "")
    if mode not in {"shadow", "supervised-pilot", "production"}:
        fail("publication mode must be shadow, supervised-pilot, or production")
    if mode == "production":
        production_approval(profile, publication_id)

    edition_id = args.edition_id or f"{edition_date}-{publication_id}"
    slug(edition_id, "edition id")
    destination = ROOT / "editions" / edition_id
    render(
        EDITION_TEMPLATE,
        destination,
        {
            "{{edition_id}}": edition_id,
            "{{publication_id}}": publication_id,
            "{{edition_date}}": edition_date,
            "{{mode}}": mode,
        },
    )
    print(f"Stamped {mode} edition: {destination}")
    print("Begin at 01_intake. The publication profile controls live authority.")


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    subparsers = command.add_subparsers(dest="command", required=True)

    publication = subparsers.add_parser("publication")
    publication.add_argument("--id", required=True)
    publication.add_argument("--title", required=True)
    publication.set_defaults(func=stamp_publication)

    edition = subparsers.add_parser("edition")
    edition.add_argument("--publication", required=True)
    edition.add_argument("--date", required=True)
    edition.add_argument("--edition-id")
    edition.set_defaults(func=stamp_edition)
    return command


def main() -> int:
    args = parser().parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
