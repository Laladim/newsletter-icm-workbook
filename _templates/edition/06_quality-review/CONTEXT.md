# 06_quality-review: resolve release blockers

Room: `rooms/02-production/`

## One job

Inspect the full draft and resolve every release-blocking factual, editorial,
legal, structural, visual, and technical failure.

## Inputs

### Run-specific working inputs

- complete `../05_draft/output/` artifact and visual
- verified research packet and source ledger

### Stable references

- all publication contracts
- factual and risk-review bindings from `skill-bindings.md`
- `references/output-contract.md`
- `_shared/approval-contract.md`
- any stage-specific rule or pointer explicitly added under `references/`

## Do not load

Do not stage on the delivery platform. Do not grade only an excerpt when the
complete artifact contains recurring or supporting sections.

## Process

1. Verify every material claim, citation, quotation, number, name, date, link,
   and attribution against the opened evidence.
2. Apply the publication's legal, product, brand, structural, and prohibited-
   language checks.
3. Inspect the rendered or actual visual surface when relevant.
4. Run configured deterministic checks and specialist reviews.
5. Resolve findings in the artifact, then rerun the affected checks.
6. Separate observations, inferences, accepted limitations, and remaining
   blockers.

## Outputs

- `output/quality-report.md`
- `output/verified-artifact-pointer.md`
- `output/stage-receipt.md` only after all release blockers are resolved

Follow `references/output-contract.md` for the exact report and pointer fields.
Do not create a passing stage receipt until the exit gate passes.

## Exit gate

All release-blocking findings are resolved in the complete artifact, every
required deterministic and specialist check passes, and rendered content and
visuals have been inspected. Continue automatically when true.

## Failure and fallback

Return failures to the stage that owns the underlying decision. A score, script
pass, or successful render cannot waive factual, legal, authority, or visual
failure.
