# 04_routing: make the editorial decision

Room: `rooms/01-editorial/`

## One job

Choose what this edition will do and persist where every unused item goes.

## Inputs

### Run-specific working inputs

- verified `../03_research/output/research-packet.md`
- verified `../03_research/output/source-ledger.md`
- performance evidence only when the profile says it informs selection

### Stable references

- `publications/{{publication_id}}/editorial-contract.md`
- editorial-judgment binding from `skill-bindings.md`
- `references/output-contract.md`
- `_shared/approval-contract.md`
- any stage-specific rule or pointer explicitly added under `references/`

## Do not load

Do not draft the edition or select a visual before the lead, thesis, supporting
items, and evidence limits pass the routing gate.

## Process

1. Select the lead and state why it best serves the audience now.
2. State the thesis, reader consequence, evidence limits, and required nuance.
3. Select supporting items or recurring modules.
4. Route every unused candidate to its declared destination or close it with a
   reason.
5. Record any decision that a later stage must not relitigate.

## Outputs

- `output/editorial-plan.md`
- `output/routing-receipt.md`
- `output/stage-receipt.md` after the exit gate passes

Follow `references/output-contract.md` for the exact file fields. Do not create
the stage receipt until the exit gate passes.

## Exit gate

The highest-supported lead and thesis fulfill the publication promise, every
unused item has a destination, and no downstream write has been simulated as a
real write. Routine editorial routing proceeds automatically.

## Failure and fallback

If the best candidate still cannot fulfill the publication promise, return to
research or produce the profile's configured thin-edition response. Do not choose
a lead only because it is easiest to write.
