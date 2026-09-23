# 01_intake: define the assignment

Room: `rooms/01-editorial/`

## One job

Turn the request into an unambiguous, authorized edition assignment.

## Inputs

### Run-specific working inputs

- edition root `CONTEXT.md`
- the user's request and any supplied material

### Stable references

- `publications/{{publication_id}}/CONTEXT.md`
- `references/output-contract.md`
- `_shared/approval-contract.md`
- any stage-specific rule or pointer explicitly added under `references/`

## Do not load

Do not load candidate research, writing procedures, visual rules, or delivery
adapters until the assignment says they are relevant.

## Process

1. Confirm publication ID, mode, edition date, and requested outcome.
2. Confirm audience, output home, final review surface, and human authorities
   from the profile rather than from memory.
3. Record inputs supplied, inputs missing, special constraints, and whether this
   is a new edition, revision, replay, or post-publish task.
4. Stop if the publication profile is missing or unconfigured.

## Outputs

- `output/assignment.md`
- `output/stage-receipt.md` after the exit gate passes

Follow `references/output-contract.md` for the exact file fields. Do not create
the stage receipt until the exit gate passes.

## Exit gate

The publication, audience, mode, output home, final surface, authority, and
starting route are unambiguous and within the user's run authorization.

## Failure and fallback

If identity, target audience, output home, or authority is unclear, stop here.
Do not guess from another publication.
