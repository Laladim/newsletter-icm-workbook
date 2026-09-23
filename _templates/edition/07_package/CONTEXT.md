# 07_package: assemble the delivery package

Room: `rooms/02-production/`

## One job

Assemble one internally consistent package for the configured final review
surface.

## Inputs

### Run-specific working inputs

- passing quality report and verified artifact pointer
- performance evidence when the publication requires it

### Stable references

- `publications/{{publication_id}}/delivery-contract.md`
- subject, packaging, and visual bindings from `skill-bindings.md`
- `references/output-contract.md`
- `_shared/approval-contract.md`
- any stage-specific rule or pointer explicitly added under `references/`

## Do not load

Do not send, schedule, publish, or run post-publish writes. Do not create a menu
of routine options when the publication requires one evidence-supported choice.

## Process

1. Select or confirm subject, preview text, title, subtitle, visual, alt text,
   body, recurring modules, links, audience, tags, and metadata.
2. Verify that each element adds distinct information and matches the same
   verified editorial thesis.
3. Run visibility, length, formatting, link, citation, and completeness checks
   required by the delivery contract.
4. Produce a manifest naming every package element and its source.

## Outputs

- `output/package-manifest.md`
- `output/delivery-package/` or an immutable package pointer
- `output/stage-receipt.md` after the exit gate passes

Follow `references/output-contract.md` for the exact manifest and package
fields. Do not create the stage receipt until the exit gate passes.

## Exit gate

The complete package is internally consistent, verified, and ready for its
configured final review surface. Routine subject, visual, module, and metadata
choices do not require a pause.

## Failure and fallback

Return content failures to quality review. Return unsupported subject or visual
choices to the owning production step. Never compensate for a bad package by
editing directly on a live surface without updating the edition record.
