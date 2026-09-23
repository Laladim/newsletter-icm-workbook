# 05_draft: write the complete edition

Room: `rooms/02-production/`

## One job

Turn the verified editorial plan and evidence into the complete reader-facing
draft in the configured format.

## Inputs

### Run-specific working inputs

- verified `../04_routing/output/editorial-plan.md`
- verified `../03_research/output/research-packet.md`

### Stable references

- `publications/{{publication_id}}/editorial-contract.md`
- `publications/{{publication_id}}/visual-contract.md` when a visual is required
- newsletter-writing and visual bindings from `skill-bindings.md`
- `references/output-contract.md`
- `_shared/approval-contract.md`
- any stage-specific rule or pointer explicitly added under `references/`

## Do not load

Do not load live delivery controls, subscriber data, or post-publish automation.
Do not introduce unused research merely because it is available.

## Process

1. Write the required edition structure for the defined audience and promise.
2. Keep every factual bridge within the verified evidence and citation rules.
3. Distinguish sourced reporting, interpretation, and clearly labeled opinion.
4. Remove repetition and generic filler.
5. Produce required visual work at the point specified by the profile and
   inspect it against the visual contract.
6. Save the draft only to this stage or the canonical output home explicitly
   named by the profile. In shadow mode, use this stage only.

## Outputs

- `output/draft-artifact` using the profile's extension
- `output/visual-brief.md` and an inspected visual pointer when required
- `output/stage-receipt.md` after the exit gate passes

Follow `references/output-contract.md` for the exact artifact and file fields.
Do not create the stage receipt until the exit gate passes.

## Exit gate

The complete draft and required visual exist, render correctly, serve the
intended reader, follow the publication identity, and remain inside the
verified evidence. Failures trigger automatic revision or an exception stop.

## Failure and fallback

If drafting exposes a missing load-bearing fact, return to stage 03. If it
exposes a wrong editorial choice, return to stage 04. Do not silently repair an
upstream decision inside prose.
