# 09_post-publish: record the observed result

Room: `rooms/03-distribution/`

## One job

Record verified publication state, update only approved downstream records, and
capture the performance evidence the next edition is allowed to use.

## Inputs

### Run-specific working inputs

- `../08_delivery/output/delivery-receipt.md`
- observed live URL or platform publication record

### Stable references

- `publications/{{publication_id}}/delivery-contract.md`
- analytics-and-records binding from `skill-bindings.md`
- `references/output-contract.md`
- `_shared/approval-contract.md`
- any stage-specific rule or pointer explicitly added under `references/`

## Do not load

Do not run this stage because a draft exists. Do not write to downstream records
without observed publication and the configured authority. In shadow mode,
compare historical records without modifying them.

## Process

1. Verify publication status on the actual platform or live surface.
2. Record the canonical live identifier, URL, date, and responsible human.
3. Run only the approved downstream update in dry-run mode first when supported.
4. Perform authorized writes and read back each exact destination.
5. Capture the performance baseline and any learning that belongs in the
   publication profile or future candidate selection.

## Outputs

- `output/publication-receipt.md`
- `output/downstream-readback.md`
- `output/performance-snapshot.md`
- `output/stage-receipt.md` after the exit gate passes

Follow `references/output-contract.md` for the exact receipt and readback
fields. Do not create the stage receipt until the exit gate passes.

## Exit gate

The observed publication and every declared downstream record agree with this
edition folder. If publication has not happened, record `wait for publication`
and stop without treating the edition as published.

## Failure and fallback

Report partial updates precisely and rerun only the failed authorized step.
Never treat a successful script start or partial response as a completed
post-publish update.
