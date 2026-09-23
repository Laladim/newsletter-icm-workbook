#!/usr/bin/env python3
"""Verify the shareable newsletter ICM starter is complete and sanitized."""

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
FORBIDDEN = [
    "cobalt",
    "beyond banks",
    "laladimalanta",
    "/users/",
    "pub_a4b9",
    "seg_0a4",
]


def main() -> int:
    errors: list[str] = []

    for name in ["README.md", "START-HERE.md", "DISCUSSION-GUIDE.md", "CONTEXT.md", "AGENTS.md", "CLAUDE.md"]:
        if not (ROOT / name).is_file():
            errors.append(f"missing root file: {name}")

    agents = ROOT / "AGENTS.md"
    claude = ROOT / "CLAUDE.md"
    if agents.is_file() and claude.is_file() and agents.read_bytes() != claude.read_bytes():
        errors.append("AGENTS.md and CLAUDE.md differ")

    edition = ROOT / "_templates" / "edition"
    for stage in STAGES:
        base = edition / stage
        for relative in ["CONTEXT.md", "references/CONTEXT.md", "references/output-contract.md", "output/.gitkeep"]:
            if not (base / relative).is_file():
                errors.append(f"missing edition factory file: {stage}/{relative}")

    publication = ROOT / "_templates" / "publication"
    for name in ["CONTEXT.md", "editorial-contract.md", "source-contract.md", "visual-contract.md", "delivery-contract.md", "skill-bindings.md"]:
        if not (publication / name).is_file():
            errors.append(f"missing publication factory file: {name}")

    for script in [ROOT / "scripts" / "stamp.py", ROOT / "scripts" / "verify-edition.py", Path(__file__)]:
        try:
            compile(script.read_text(), str(script), "exec")
        except (OSError, SyntaxError) as exc:
            errors.append(f"invalid script {script.name}: {exc}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".py", ".json", ".txt"}:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        lowered = path.read_text(errors="ignore").lower()
        for token in FORBIDDEN:
            if token in lowered:
                errors.append(f"private or publication-specific token in {path.relative_to(ROOT)}: {token}")

    if errors:
        print("TEMPLATE VERIFICATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("TEMPLATE VERIFICATION PASSED")
    print(f"- reusable edition stages: {len(STAGES)}")
    print("- publication factory: complete")
    print("- entry maps: identical")
    print("- scripts: syntax valid")
    print("- private and publication-specific token scan: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
