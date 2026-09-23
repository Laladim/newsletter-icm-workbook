# 03_research: build the evidence packet

Room: `rooms/01-editorial/`

## One job

Create the claim-level evidence needed to make and defend the editorial choice.

## Inputs

### Run-specific working inputs

- verified `../02_source-selection/output/candidate-set.md`

### Stable references

- `publications/{{publication_id}}/source-contract.md`
- research and source-verification binding from `skill-bindings.md`
- `references/output-contract.md`
- `_shared/approval-contract.md`
- any stage-specific rule or pointer explicitly added under `references/`

## Do not load

Do not load a preferred headline, visual metaphor, delivery template, or prior
draft that could bias the evidence search.

## Process

1. Open the controlling sources named by the source hierarchy.
2. Record exact names, dates, numbers, quotations, procedural status, and source
   locations for every possible load-bearing claim.
3. Identify independent corroboration, interested material, contrary evidence,
   material omissions, and unresolved uncertainty.
4. Separate one original source syndicated many times from genuinely independent
   reporting.
5. Record what the evidence supports, what it does not support, and the audience
   consequence that can be stated safely.

## Outputs

- `output/research-packet.md`
- `output/source-ledger.md`
- `output/stage-receipt.md` after the exit gate passes

Follow `references/output-contract.md` for the exact file fields. Do not create
the stage receipt until the exit gate passes.

## Exit gate

The evidence safely carries at least one lead, every load-bearing claim is
traceable, required primary anchors are present, and material uncertainty is
explicit. Otherwise downgrade, revise, or stop under the exception contract.

## Failure and fallback

If evidence is inaccessible, weak, stale, contradictory, or insufficient, mark
the affected claim or candidate clearly. Downgrade, reroute, or stop. Do not let
writing quality disguise an evidence failure.
