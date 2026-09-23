#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Run a fictional cold-start publication and local shadow edition."""

from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DATE = "2026-09-23"
PUBLICATION_ID = "harbor-notes"
EDITION_ID = f"{DATE}-{PUBLICATION_ID}"


def run(root: Path, *args: str, expect_success: bool = True) -> str:
    result = subprocess.run(
        [sys.executable, *args], cwd=root, text=True, capture_output=True
    )
    if expect_success and result.returncode:
        raise AssertionError(
            f"command failed: {' '.join(args)}\n{result.stdout}\n{result.stderr}"
        )
    if not expect_success and result.returncode == 0:
        raise AssertionError(f"command unexpectedly passed: {' '.join(args)}")
    return result.stdout + result.stderr


def write(root: Path, relative: str, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip())


def approved_brief() -> str:
    return f"""
    ---
    publication_id: "{PUBLICATION_ID}"
    publication_title: "Harbor Notes"
    brief_status: approved
    approved_by: "human: Morgan Lee"
    approved_at: "{DATE}"
    audience_decision_by: "human: Morgan Lee"
    editorial_promise_decision_by: "human: Morgan Lee"
    positioning_decision_by: "human: Morgan Lee"
    risk_tolerance_decision_by: "human: Morgan Lee"
    publishing_authority_decision_by: "human: Morgan Lee"
    ---

    # Publication brief for Harbor Notes

    ## Supplied facts

    - Supplied fact: Morgan maintains a small sailboat on weekends.
    - Supplied fact: the publication is a fictional test fixture.

    ## Researched evidence

    | Claim supported | Source title | URL or file | Accessed | Limits |
    |---|---|---|---|---|
    | No external factual claim is used in this fictional run | none requested | not applicable | {DATE} | Real editions require opened sources |

    ## Interpretations

    - Interpretation: one maintenance decision per issue is easier for a busy
      weekend sailor to use than a broad roundup.

    ## Human decisions

    | Decision | Approved choice | Decided by | Date | Reason or constraint |
    |---|---|---|---|---|
    | Audience choice | Weekend sailors maintaining one small boat | human: Morgan Lee | {DATE} | One clear primary reader |
    | Reader problem | Maintenance notes are scattered and hard to act on | human: Morgan Lee | {DATE} | Reduce preparation time |
    | Editorial thesis | A short verified checklist can prevent avoidable maintenance mistakes | human: Morgan Lee | {DATE} | Practical and bounded |
    | Recurring promise | One source-backed maintenance decision and checklist | human: Morgan Lee | {DATE} | Repeatable reader value |
    | Positioning | Owner-to-owner learning notes rather than professional advice | human: Morgan Lee | {DATE} | Honest expertise boundary |
    | Topic boundaries and point of view | Routine small-boat upkeep only | human: Morgan Lee | {DATE} | Exclude emergencies and regulated advice |
    | Risk tolerance | Omit any safety claim not supported by an authoritative source | human: Morgan Lee | {DATE} | Low risk tolerance |
    | Final profile reviewer | Morgan Lee | human: Morgan Lee | {DATE} | Human profile gate |
    | Schedule, send, activate, and publish authority | Morgan Lee only | human: Morgan Lee | {DATE} | No agent authority |

    ## Audience and recurring problem

    - Primary audience: weekend sailors maintaining one small boat.
    - Secondary audience: none.
    - Out-of-scope audience: commercial operators and emergency responders.
    - Recurring reader problem: maintenance notes are scattered.
    - Reader knowledge and constraints: basic boating knowledge and little time.

    ## Editorial thesis, promise, and positioning

    - Editorial thesis: a short verified checklist can prevent avoidable errors.
    - Recurring promise: one source-backed maintenance decision and checklist.
    - Positioning: owner-to-owner learning notes, not professional advice.
    - Point of view: uncertainty and safety limits remain visible.
    - What the publication must never imply: certification or emergency advice.

    ## Topic boundaries and edition shape

    - Always in scope: routine inspection and upkeep.
    - Conditionally in scope: product selection with authoritative support.
    - Out of scope: navigation emergencies, weather warnings, and repairs that
      require a licensed professional.
    - Required sections: decision, checklist, limits, and sources.
    - Optional sections: one observation from the owner log.
    - Target length or reading time: four minutes.
    - Intended reader action: prepare one routine maintenance task safely.

    ## Evidence and risk

    - Candidate sources: owner-supplied notes and authoritative public manuals.
    - Primary authority: current manufacturer or safety authority guidance.
    - Independent corroboration: required for a disputed safety claim.
    - Weak or prohibited sources: anonymous rumor and unattributed generated text.
    - Freshness and duplication rules: verify version date and prior coverage.
    - Citation standard: every safety claim cites an opened source.
    - Specialist review triggers: emergency, electrical, structural, or legal advice.
    - Approved risk tolerance: omit unsupported safety claims.

    ## Voice, expertise, and visuals

    - Voice: calm, plain, practical, and explicit about limits.
    - Truthful expertise posture: an owner sharing organized learning notes.
    - Expertise the publication must not imply: licensed marine technician.
    - Visual requirement: none.
    - Visual purpose and inspection standard: not applicable.

    ## Cadence, ownership, delivery, and metrics

    - Intended cadence: monthly.
    - Routine shadow-run authorization: direct request from Morgan Lee.
    - Local Markdown output home: Stage 07 delivery package.
    - Local final review surface: Stage 08 Markdown preview.
    - Future platform intent: none.
    - Profile reviewer: Morgan Lee.
    - Schedule, send, activate, and publish authority: Morgan Lee only.
    - Metrics and capture windows: reader replies after each future issue.
    - Post-publish record authority: Morgan Lee only.
    - Supervised-pilot proof and rollback: not yet defined.

    ## Open questions and unresolved evidence

    - The first real topic and its authoritative sources remain undecided.

    ## Approval record

    Morgan Lee approved this fictional brief on {DATE} for a local smoke test.
    """


def profile_files(brief_hash: str) -> dict[str, str]:
    return {
        "CONTEXT.md": f"""
        ---
        publication_id: "{PUBLICATION_ID}"
        title: "Harbor Notes"
        mode: shadow
        profile_status: configured
        profile_review_status: pending
        profile_reviewed_by: ""
        profile_reviewed_at: ""
        publication_brief_sha256: "{brief_hash}"
        canonical_output_home: "local-markdown: editions/{PUBLICATION_ID}"
        final_review_surface: "local-markdown: stage-08 Markdown preview"
        routine_run_authority: "human: Morgan Lee"
        final_review_approver: "human: Morgan Lee"
        schedule_send_publish_authority: "human: Morgan Lee"
        post_publish_record_authority: "human: Morgan Lee"
        ---

        # Harbor Notes

        ## Business and audience

        Harbor Notes serves weekend sailors with one verified routine
        maintenance decision and checklist per issue.

        ## Editorial identity

        Read the local editorial, source, and visual contracts.

        ## Operating boundaries

        All outputs are local Markdown. Morgan Lee keeps all publishing
        authority. Stage 09 waits for an authorized real publication.
        """,
        "editorial-contract.md": """
        # Editorial contract for Harbor Notes

        ## Reader and promise

        Serve weekend sailors with one source-backed routine maintenance
        decision and checklist.

        ## Voice and expertise

        Use calm, plain language. Identify as owner-to-owner learning notes and
        never imply licensed marine expertise.

        ## Edition anatomy

        Include the decision, checklist, limits, and opened sources in a
        four-minute read.

        ## Editorial selection

        Select routine upkeep only. Exclude emergencies and professional repair.

        ## Quality bar

        Every safety claim is traceable and every expertise limit is visible.
        """,
        "source-contract.md": """
        # Source contract for Harbor Notes

        ## Approved sources

        Use current authoritative public manuals and clearly labeled
        owner-supplied notes. Store no credential.

        ## Source hierarchy

        Current safety or manufacturer guidance outranks independent explanation,
        owner observation, and unverified community material.

        ## Required checks

        Verify version date, identity, prior coverage, exact safety language,
        and evidence limits. Omit unsupported safety claims.

        ## Citation and evidence record

        Record source, date, location, accessed time, supported claim, and limit.
        """,
        "visual-contract.md": """
        # Visual contract for Harbor Notes

        ## Requirement

        No visual is required for the shadow profile.

        ## Identity and accessibility

        Not applicable.

        ## Concept selection

        Do not add a decorative visual to satisfy a template.

        ## Inspection

        Record the visual decision as not applicable.
        """,
        "delivery-contract.md": """
        # Delivery contract for Harbor Notes

        ## Shadow output

        Use a local Markdown package and local Markdown preview. Make no external
        write.

        ## Future platform intent

        No platform is selected.

        ## Human authority

        Morgan Lee authorizes the shadow run, reviews the profile and preview,
        and alone may schedule, send, activate, or publish.

        ## Verification and rollback

        Compare the local preview with the package manifest and return to Stage
        07 if they differ.

        ## Post-publish records

        Stage 09 waits for real publication under an authorized live mode.
        """,
        "skill-bindings.md": """
        # Capability bindings for Harbor Notes

        | Capability | Canonical binding | Trigger | Output proof | Required? |
        |---|---|---|---|---|
        | candidate discovery | manual: gather only owner-supplied topics for the fictional run | Stage 02 after intake | candidate set | yes |
        | research and source verification | manual: record the absence of external factual claims in this fixture | Stage 03 after selection | research packet and source ledger | yes |
        | editorial judgment | manual: apply the approved audience and promise | Stage 04 after research | editorial plan | yes |
        | newsletter writing | manual: draft a local fictional Markdown issue | Stage 05 after routing | complete draft | yes |
        | factual and risk review | manual: check every claim and expertise limit | Stage 06 on the draft | quality report | yes |
        | visual production | none: the approved profile requires no visual | Stage 05 visual decision | not-applicable visual brief | no |
        | subject and packaging | manual: assemble one local package | Stage 07 after quality review | package manifest | yes |
        | delivery adapter | manual: create and inspect the local Markdown preview | Stage 08 in shadow mode | delivery receipt | yes |
        | analytics and records | none: a fictional shadow run has no post-publish metrics | Stage 09 | unopened stage | no |
        """,
    }


def stage_receipt(stage: str, outputs: str, next_action: str) -> str:
    return f"""
    # Stage receipt

    - Edition ID: {EDITION_ID}
    - Stage: {stage}
    - Run authorization: fictional local smoke test
    - Completed by: deterministic smoke fixture
    - Completed at: {DATE}T12:00:00Z
    - Inputs opened: required upstream outputs and local contracts
    - Outputs written: {outputs}
    - Verifiers and specialist checks: local fixture checks
    - Readback or inspection evidence: files reopened from the disposable copy
    - Exit result: pass
    - Exception status: none
    - Next action: {next_action}
    - External writes: none
    """


def populate_shadow_edition(root: Path) -> None:
    base = f"editions/{EDITION_ID}"
    outputs = {
        "01_intake": {
            "assignment.md": "# Edition assignment\n\nLocal fictional issue for weekend sailors.\n"
        },
        "02_source-selection": {
            "candidate-set.md": "# Candidate set\n\nOne fictional owner-supplied checklist topic qualifies.\n"
        },
        "03_research": {
            "research-packet.md": "# Research packet\n\nNo external factual claim is made in this fixture.\n",
            "source-ledger.md": "# Source ledger\n\n| ID | Claim | Source | Limit |\n|---|---|---|---|\n| F1 | Fixture-only scenario | owner-supplied fictional input | not a real-world claim |\n",
        },
        "04_routing": {
            "editorial-plan.md": "# Editorial plan\n\nLead with one bounded fictional checklist.\n",
            "routing-receipt.md": "# Routing receipt\n\n| Item | Decision | Reason |\n|---|---|---|\n| Fictional checklist | lead | matches the approved promise |\n",
        },
        "05_draft": {
            "draft-artifact.md": "# Harbor Notes\n\nThis fictional shadow issue demonstrates local workflow state.\n",
            "visual-brief.md": "# Visual brief\n\n- Requirement: none\n- Result: pass\n",
        },
        "06_quality-review": {
            "quality-report.md": "# Quality report\n\nNo unsupported real-world claim or external write. Release result: pass.\n",
            "verified-artifact-pointer.md": "# Verified artifact pointer\n\n- Path: ../05_draft/output/draft-artifact.md\n- Result: pass\n",
        },
        "07_package": {
            "package-manifest.md": "# Delivery package manifest\n\n- Format: local Markdown\n- External writes: none\n",
            "delivery-package/edition.md": "# Harbor Notes local preview\n\nFictional shadow package.\n",
        },
        "08_delivery": {
            "artifact-pointer.md": "# Final review surface pointer\n\n- Platform: local Markdown\n- State observed: local shadow preview\n",
            "delivery-receipt.md": "# Delivery receipt\n\n- Operation performed: local simulation\n- External writes: none\n- Final result: match\n",
        },
    }
    stage_names = list(outputs)
    for index, stage in enumerate(stage_names):
        stage_outputs = outputs[stage]
        for relative, content in stage_outputs.items():
            write(root, f"{base}/{stage}/output/{relative}", content)
        next_action = stage_names[index + 1] if index + 1 < len(stage_names) else "wait at Stage 09"
        write(
            root,
            f"{base}/{stage}/output/stage-receipt.md",
            stage_receipt(stage, ", ".join(stage_outputs), next_action),
        )


def assert_cold_start(root: Path) -> None:
    kickoff = "Read SETUP.md and guide me through creating my newsletter ICM workspace."
    agents = (root / "AGENTS.md").read_text()
    claude = (root / "CLAUDE.md").read_text()
    if agents != claude:
        raise AssertionError("AGENTS.md and CLAUDE.md must be identical")
    for name, text in [("AGENTS.md", agents), ("CLAUDE.md", claude)]:
        if kickoff not in text or "SETUP.md" not in text:
            raise AssertionError(f"{name} does not expose the setup route")


def main() -> int:
    with tempfile.TemporaryDirectory(
        prefix="newsletter-workbook-smoke-", dir="/private/tmp"
    ) as temp:
        sandbox = Path(temp) / "newsletter-icm-workbook"
        shutil.copytree(
            ROOT,
            sandbox,
            ignore=shutil.ignore_patterns(".git", ".artifacts", "__pycache__", "*.pyc"),
        )
        assert_cold_start(sandbox)
        print("Cold start through AGENTS.md: SETUP.md route found")
        print("Cold start through CLAUDE.md: SETUP.md route found")

        run(
            sandbox,
            "scripts/stamp.py",
            "publication",
            "--id",
            PUBLICATION_ID,
            "--title",
            "Harbor Notes",
        )
        run(
            sandbox,
            "scripts/verify-publication.py",
            f"publications/{PUBLICATION_ID}",
            "--brief-only",
            expect_success=False,
        )
        print("Draft brief rejection: passed")

        brief_path = sandbox / "publications" / PUBLICATION_ID / "publication-brief.md"
        brief_path.write_text(textwrap.dedent(approved_brief()).lstrip())
        run(
            sandbox,
            "scripts/verify-publication.py",
            f"publications/{PUBLICATION_ID}",
            "--brief-only",
        )
        print("Fictional interview and approved brief gate: passed")

        run(
            sandbox,
            "scripts/stamp.py",
            "contracts",
            "--publication",
            PUBLICATION_ID,
        )
        run(
            sandbox,
            "scripts/verify-publication.py",
            f"publications/{PUBLICATION_ID}",
            "--pre-review",
            expect_success=False,
        )
        print("Unconfigured contract rejection: passed")

        brief_hash = hashlib.sha256(brief_path.read_bytes()).hexdigest()
        profile_dir = sandbox / "publications" / PUBLICATION_ID
        for name, content in profile_files(brief_hash).items():
            (profile_dir / name).write_text(textwrap.dedent(content).lstrip())
        if len([path for path in profile_dir.iterdir() if path.is_file()]) != 7:
            raise AssertionError("fictional profile must contain seven files")
        run(
            sandbox,
            "scripts/verify-publication.py",
            f"publications/{PUBLICATION_ID}",
            "--pre-review",
        )
        print("Seven generated publication files and pre-review gate: passed")

        context_path = profile_dir / "CONTEXT.md"
        context = context_path.read_text()
        context = context.replace(
            "profile_review_status: pending", "profile_review_status: approved"
        ).replace(
            'profile_reviewed_by: ""', 'profile_reviewed_by: "human: Morgan Lee"'
        ).replace('profile_reviewed_at: ""', f'profile_reviewed_at: "{DATE}"')
        context_path.write_text(context)
        run(
            sandbox,
            "scripts/verify-publication.py",
            f"publications/{PUBLICATION_ID}",
        )
        print("Final human profile review gate: passed")

        bindings_path = profile_dir / "skill-bindings.md"
        bindings = bindings_path.read_text()
        bindings_path.write_text(bindings.replace("manual:", "imaginary:", 1))
        run(
            sandbox,
            "scripts/verify-publication.py",
            f"publications/{PUBLICATION_ID}",
            expect_success=False,
        )
        bindings_path.write_text(bindings)
        print("Invented capability rejection: passed")

        context = context_path.read_text()
        context_path.write_text(
            context.replace(
                'schedule_send_publish_authority: "human: Morgan Lee"',
                'schedule_send_publish_authority: "agent: newsletter bot"',
            )
        )
        run(
            sandbox,
            "scripts/verify-publication.py",
            f"publications/{PUBLICATION_ID}",
            expect_success=False,
        )
        context_path.write_text(context)
        print("Unclear publishing authority rejection: passed")

        editorial_path = profile_dir / "editorial-contract.md"
        editorial = editorial_path.read_text()
        fake_secret = "gh" + "p_" + ("A" * 20)
        editorial_path.write_text(editorial + f"\nCredential sample: {fake_secret}\n")
        run(
            sandbox,
            "scripts/verify-publication.py",
            f"publications/{PUBLICATION_ID}",
            expect_success=False,
        )
        editorial_path.write_text(editorial)
        print("Exposed secret rejection: passed")

        run(
            sandbox,
            "scripts/stamp.py",
            "edition",
            "--publication",
            PUBLICATION_ID,
            "--date",
            DATE,
        )
        populate_shadow_edition(sandbox)
        run(
            sandbox,
            "scripts/verify-edition.py",
            f"editions/{EDITION_ID}",
            "--require-through",
            "08_delivery",
        )
        generated_scope = [
            sandbox / "publications" / PUBLICATION_ID,
            sandbox / "editions" / EDITION_ID,
        ]
        forbidden = ["alt-lender", "news list", "product video", "nonbank credit"]
        for scope in generated_scope:
            for path in scope.rglob("*"):
                if not path.is_file():
                    continue
                lowered = path.read_text(errors="ignore").lower()
                for token in forbidden:
                    if token in lowered:
                        raise AssertionError(
                            f"fictional publication inherited unrelated assumption: {token}"
                        )
        print("Fictional local shadow edition through Stage 08: passed")
        print("Unrelated publication-assumption scan: clean")

    print("SMOKE TEST PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
