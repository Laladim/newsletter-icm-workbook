#!/usr/bin/env python3
"""Verify one newsletter edition and derive its pickup point from files."""

from __future__ import annotations

import argparse
import re
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
REQUIRED_FILES = {
    "01_intake": ["assignment.md"],
    "02_source-selection": ["candidate-set.md"],
    "03_research": ["research-packet.md", "source-ledger.md"],
    "04_routing": ["editorial-plan.md", "routing-receipt.md"],
    "05_draft": ["visual-brief.md"],
    "06_quality-review": ["quality-report.md", "verified-artifact-pointer.md"],
    "07_package": ["package-manifest.md"],
    "08_delivery": ["artifact-pointer.md", "delivery-receipt.md"],
    "09_post-publish": [
        "publication-receipt.md",
        "downstream-readback.md",
        "performance-snapshot.md",
    ],
}
RECEIPT_FIELDS = [
    "Edition ID",
    "Stage",
    "Run authorization",
    "Completed by",
    "Completed at",
    "Inputs opened",
    "Outputs written",
    "Verifiers and specialist checks",
    "Readback or inspection evidence",
    "Exit result",
    "Exception status",
    "Next action",
    "External writes",
]


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    block = text.split("---\n", 2)[1]
    values: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def receipt_fields(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text().splitlines():
        match = re.match(r"^-\s+([^:]+):\s*(.*)$", line)
        if match:
            values[match.group(1).strip()] = match.group(2).strip()
    return values


def produced_files(output: Path) -> list[Path]:
    if not output.is_dir():
        return []
    return sorted(
        path
        for path in output.rglob("*")
        if path.is_file() and path.name != ".gitkeep"
    )


def has_draft(output: Path) -> bool:
    return any(path.is_file() for path in output.glob("draft-artifact.*")) or (
        output / "artifact-pointer.md"
    ).is_file()


def has_package(output: Path) -> bool:
    package = output / "delivery-package"
    package_files = produced_files(package)
    return bool(package_files) or (output / "package-pointer.md").is_file()


def required_missing(stage: str, output: Path) -> list[str]:
    missing = [name for name in REQUIRED_FILES[stage] if not (output / name).is_file()]
    if stage == "05_draft" and not has_draft(output):
        missing.append("draft-artifact.<extension> or artifact-pointer.md")
    if stage == "07_package" and not has_package(output):
        missing.append("populated delivery-package/ or package-pointer.md")
    return missing


def normalize_stage(value: str) -> str:
    if value in STAGES:
        return value
    if value.isdigit():
        number = int(value)
        if 1 <= number <= len(STAGES):
            return STAGES[number - 1]
    raise argparse.ArgumentTypeError(
        "stage must be 1-9 or one of: " + ", ".join(STAGES)
    )


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument("edition", help="edition folder or edition ID under editions/")
    command.add_argument(
        "--require-through",
        type=normalize_stage,
        help="fail unless this stage and every earlier stage have passing receipts",
    )
    return command


def resolve_edition(value: str) -> Path:
    candidate = Path(value).expanduser()
    if not candidate.is_absolute():
        direct = (Path.cwd() / candidate).resolve()
        candidate = direct if direct.is_dir() else ROOT / "editions" / value
    return candidate.resolve()


def main() -> int:
    args = parser().parse_args()
    edition = resolve_edition(args.edition)
    errors: list[str] = []
    rows: list[tuple[str, str, str]] = []
    external_writes: list[str] = []

    context = edition / "CONTEXT.md"
    if not context.is_file():
        print(f"EDITION VERIFICATION FAILED\n- missing edition CONTEXT.md: {context}")
        return 1

    identity = frontmatter(context)
    if identity.get("edition_id") != edition.name:
        errors.append(
            f"edition folder and edition_id disagree: {edition.name} vs "
            f"{identity.get('edition_id', 'missing')}"
        )
    for field in ["publication_id", "edition_date", "mode"]:
        if not identity.get(field):
            errors.append(f"edition identity is missing: {field}")
    if "{{" in context.read_text():
        errors.append("edition root contains unresolved template placeholders")

    publication_id = identity.get("publication_id", "")
    profile = ROOT / "publications" / publication_id / "CONTEXT.md"
    if publication_id and not profile.is_file():
        errors.append(f"publication profile is missing: {profile}")
    elif profile.is_file():
        profile_identity = frontmatter(profile)
        edition_mode = identity.get("mode")
        profile_mode = profile_identity.get("mode")
        local_shadow_under_pilot = edition_mode == "shadow" and profile_mode == "supervised-pilot"
        completed_pre_cutover_record = (
            edition_mode in {"shadow", "supervised-pilot"}
            and profile_mode == "production"
            and (edition / "09_post-publish" / "output" / "stage-receipt.md").is_file()
        )
        if edition_mode != profile_mode and not local_shadow_under_pilot and not completed_pre_cutover_record:
            errors.append(
                "edition mode no longer matches its publication profile: "
                f"{edition_mode} vs {profile_mode}"
            )
        if edition_mode == "supervised-pilot" and (
            profile_identity.get("supervised_pilot_edition") != identity.get("edition_id")
        ):
            errors.append("edition is not the named supervised pilot in its publication profile")

    prior_passed = True
    first_pickup: str | None = None
    passed_through = 0

    for index, stage in enumerate(STAGES, start=1):
        stage_root = edition / stage
        stage_context = stage_root / "CONTEXT.md"
        reference_contract = stage_root / "references" / "output-contract.md"
        output = stage_root / "output"

        if not stage_context.is_file():
            errors.append(f"missing stage context: {stage}/CONTEXT.md")
        elif "{{" in stage_context.read_text():
            errors.append(f"stage context contains unresolved placeholders: {stage}")
        if not reference_contract.is_file():
            errors.append(f"missing output contract: {stage}/references/output-contract.md")
        if not output.is_dir():
            errors.append(f"missing output boundary: {stage}/output")
            rows.append((stage, "invalid", "output folder missing"))
            prior_passed = False
            first_pickup = first_pickup or stage
            continue

        files = produced_files(output)
        receipt = output / "stage-receipt.md"
        non_receipt = [path for path in files if path != receipt]
        missing = required_missing(stage, output)

        exit_result = ""
        receipt_problem = ""
        if receipt.is_file():
            fields = receipt_fields(receipt)
            absent_fields = [name for name in RECEIPT_FIELDS if not fields.get(name)]
            if absent_fields:
                receipt_problem = "stage receipt has blank or missing fields: " + ", ".join(absent_fields)
                errors.append(f"{stage}: {receipt_problem}")
            exit_result = fields.get("Exit result", "").lower()
            if exit_result not in {"pass", "revise", "blocked", "failed"}:
                receipt_problem = "stage exit result must be pass, revise, blocked, or failed"
                errors.append(f"{stage}: {receipt_problem}")
            if fields.get("Edition ID") and fields["Edition ID"] != identity.get("edition_id"):
                errors.append(f"{stage}: stage receipt names a different edition")
            receipt_stage = fields.get("Stage", "")
            if receipt_stage and receipt_stage not in {stage, stage[:2], str(index)}:
                errors.append(f"{stage}: stage receipt names a different stage: {receipt_stage}")
            external_write = fields.get("External writes", "")
            if external_write and external_write.lower() != "none":
                external_writes.append(f"{stage}: {external_write}")

        if non_receipt and not prior_passed:
            errors.append(f"{stage}: output exists before every earlier stage has a passing receipt")

        if not files:
            state = "not-started"
            detail = "no stage evidence"
        elif missing:
            state = "incomplete"
            detail = "missing: " + ", ".join(missing)
            if receipt.is_file():
                errors.append(f"{stage}: stage receipt exists before required outputs are complete")
        elif not receipt.is_file():
            state = "awaiting-stage-receipt"
            detail = "required outputs exist; no stage receipt"
        elif receipt_problem:
            state = "invalid-receipt"
            detail = receipt_problem
        else:
            state = exit_result
            detail = "stage exit evidence recorded"

        rows.append((stage, state, detail))

        if state == "pass" and prior_passed:
            passed_through = index
        else:
            prior_passed = False
            first_pickup = first_pickup or stage

    if args.require_through:
        required_index = STAGES.index(args.require_through) + 1
        if passed_through < required_index:
            errors.append(
                f"required pass through {args.require_through}, but passing receipts stop after "
                f"stage {passed_through:02d}"
            )

    print(f"Edition: {identity.get('edition_id', edition.name)}")
    print(f"Publication: {publication_id or 'missing'}")
    print(f"Mode: {identity.get('mode', 'missing')}")
    print("\nStage state")
    for stage, state, detail in rows:
        print(f"- {stage}: {state} ({detail})")
    if first_pickup:
        print(f"\nPickup: {first_pickup}")
    else:
        print("\nPickup: complete, no next numbered stage")

    if errors:
        print("\nEDITION VERIFICATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nEDITION VERIFICATION PASSED")
    print(f"- passed through stage: {passed_through:02d}")
    print("- state derived from local output files and stage receipts")
    if external_writes:
        print("- recorded external writes:")
        for external_write in external_writes:
            print(f"  - {external_write}")
    else:
        print("- recorded external writes: none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
