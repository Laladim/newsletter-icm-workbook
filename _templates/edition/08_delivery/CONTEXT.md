# 08_delivery: stage and read back the final surface

Room: `rooms/03-distribution/`

## One job

Place the verified package on the configured final review surface without
exceeding authority, then prove the actual surface matches.

## Inputs

### Run-specific working inputs

- verified `../07_package/output/package-manifest.md`
- verified delivery package or pointer

### Stable references

- `publications/{{publication_id}}/delivery-contract.md`
- delivery-adapter binding from `skill-bindings.md`
- `references/output-contract.md`
- `_shared/approval-contract.md`
- any stage-specific rule or pointer explicitly added under `references/`

## Do not load

Do not load post-publish automation before observed publication. Do not infer
send or publish authority from credentials. In `template` or `shadow` mode, do
not perform any external write.

## Process

1. Check the publication mode and named authority before any external action.
2. In shadow mode, validate only a historical artifact pointer or a local
   simulated package.
3. In an explicitly approved live mode, create or update a draft only according
   to the delivery contract.
4. Read the final surface back. Inspect complete content, visual, metadata,
   audience, links, and unsent or unscheduled state.
5. Give the authorized human the review surface. Stop before scheduling,
   sending, activating, or publishing unless the profile assigns that action
   to a human procedure.

## Outputs

- `output/artifact-pointer.md`
- `output/delivery-receipt.md`
- `output/stage-receipt.md` after the exit gate passes

Follow `references/output-contract.md` for the exact pointer and readback
fields. Do not create the stage receipt until the exit gate passes.

## Exit gate

The actual or simulated final surface matches the verified package and remains
within the authority boundary. In live mode, an unsent draft may be created and
read back automatically. Scheduling and publishing still require the human
named by the publication profile.

## Failure and fallback

Keep the verified package and record the exact failure. Use the publication's
declared rollback route. Do not improvise a manual copy path unless the
authorized human explicitly chooses it.
