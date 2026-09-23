#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Stamp a publication brief, publication contracts, or newsletter edition."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
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
            values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def rendered_text(template: Path, replacements: dict[str, str]) -> str:
    text = template.read_text()
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def render_tree(
    template: Path, destination: Path, replacements: dict[str, str]
) -> None:
    if destination.exists():
        fail(f"destination already exists: {destination}")
    shutil.copytree(template, destination)
    for path in destination.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".json", ".txt"}:
            continue
        path.write_text(rendered_text(path, replacements))


def run_publication_verifier(profile_dir: Path, *extra: str) -> None:
    command = [
        sys.executable,
        str(ROOT / "scripts" / "verify-publication.py"),
        str(profile_dir),
        *extra,
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        if result.stdout:
            print(result.stdout.rstrip(), file=sys.stderr)
        if result.stderr:
            print(result.stderr.rstrip(), file=sys.stderr)
        fail("publication verification failed")


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
    title = args.title.strip()
    if not title:
        fail("publication title cannot be blank")
    destination = ROOT / "publications" / publication_id
    if destination.exists():
        fail(f"destination already exists: {destination}")
    destination.mkdir(parents=True)
    brief = destination / "publication-brief.md"
    brief.write_text(
        rendered_text(
            PUBLICATION_TEMPLATE / "publication-brief.md",
            {
                "{{publication_id}}": publication_id,
                "{{publication_title}}": title,
            },
        )
    )
    print(f"Stamped publication brief: {brief}")
    print("Complete the interview and obtain explicit human approval.")
    print("Do not generate contracts before the approved-brief verifier passes.")


def stamp_contracts(args: argparse.Namespace) -> None:
    publication_id = slug(args.publication, "publication id")
    destination = ROOT / "publications" / publication_id
    brief = destination / "publication-brief.md"
    if not brief.is_file():
        fail(f"publication brief not found: {brief}")
    run_publication_verifier(destination, "--brief-only")
    identity = frontmatter(brief)
    if identity.get("publication_id") != publication_id:
        fail("publication brief and folder name disagree")
    title = identity.get("publication_title", "").strip()
    if not title:
        fail("publication brief is missing publication_title")
    brief_hash = hashlib.sha256(brief.read_bytes()).hexdigest()
    replacements = {
        "{{publication_id}}": publication_id,
        "{{publication_title}}": title,
        "{{publication_brief_sha256}}": brief_hash,
    }
    created: list[Path] = []
    for template in sorted(PUBLICATION_TEMPLATE.iterdir()):
        if not template.is_file() or template.name == "publication-brief.md":
            continue
        target = destination / template.name
        if target.exists():
            fail(f"contract already exists; refusing to overwrite: {target}")
        target.write_text(rendered_text(template, replacements))
        created.append(target)
    print(f"Generated publication contracts: {len(created)}")
    for path in created:
        print(f"- {path.relative_to(ROOT)}")
    print("Populate only from the approved brief, then run the pre-review verifier.")


def stamp_edition(args: argparse.Namespace) -> None:
    publication_id = slug(args.publication, "publication id")
    edition_date = iso_date(args.date)
    profile_dir = ROOT / "publications" / publication_id
    profile_path = profile_dir / "CONTEXT.md"
    if not profile_path.is_file():
        fail(f"publication profile not found: {profile_path}")
    run_publication_verifier(profile_dir)
    profile = frontmatter(profile_path)
    mode = profile.get("mode", "")
    if mode not in {"shadow", "supervised-pilot", "production"}:
        fail("publication mode must be shadow, supervised-pilot, or production")
    if mode == "production":
        production_approval(profile, publication_id)

    edition_id = args.edition_id or f"{edition_date}-{publication_id}"
    slug(edition_id, "edition id")
    destination = ROOT / "editions" / edition_id
    render_tree(
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

    publication = subparsers.add_parser(
        "publication", help="create a draft publication brief"
    )
    publication.add_argument("--id", required=True)
    publication.add_argument("--title", required=True)
    publication.set_defaults(func=stamp_publication)

    contracts = subparsers.add_parser(
        "contracts", help="generate six contracts from an approved brief"
    )
    contracts.add_argument("--publication", required=True)
    contracts.set_defaults(func=stamp_contracts)

    edition = subparsers.add_parser(
        "edition", help="create one edition after final profile approval"
    )
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
