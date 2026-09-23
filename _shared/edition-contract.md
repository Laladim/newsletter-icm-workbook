# Edition contract

An edition is one publication-specific run through the newsletter engine.

## Required identity

The edition root must name:

- edition ID and date
- publication profile
- mode
- request and intended reader outcome
- canonical output home
- publishing authority
- any approved deviation from the standard route

## Required stage anatomy

Every stage context contains:

1. Room
2. One job
3. Inputs separated into run-specific working inputs and stable references
4. Do not load
5. Process
6. Outputs
7. Exit gate
8. Failure and fallback

Every stage folder contains:

- `CONTEXT.md`: the Layer 2 execution contract
- `references/`: the Layer 3 boundary for stable rules, readable pointers, and
  the exact `output-contract.md` for this stage
- `output/`: the Layer 4 boundary for files unique to this edition

Publication contracts may remain canonical under `publications/` and be named
as Layer 3 inputs. Do not copy them into every edition. The local `references/`
folder is for additional stage-specific rules or pointers that the parent
`CONTEXT.md` explicitly names.

Every stage writes only to its own `output/` unless the publication profile
explicitly names an external final surface. When the artifact must remain
external, write an `artifact-pointer.md` with the observed path or URL and the
verification receipt instead of copying the artifact.

## Movement rule

The user's `create newsletter` or `continue newsletter` command authorizes the
routine edition run. Every stage writes `stage-receipt.md` following
`_shared/approval-contract.md`. Complete outputs plus `Exit result: pass` open
the next stage automatically. `revise` triggers correction in the same stage;
`blocked` or `failed` stops the run. No stage receipt may grant schedule, send,
activate, or publish authority.

## Status rule

The filesystem is the record. Empty output means not run. Required outputs
without a passing stage receipt mean incomplete. The index summarizes but does
not override the edition folder.

Run `python3 scripts/verify-edition.py <edition-folder>` to derive the pickup
point and detect skipped stages, incomplete outputs, or invalid receipts.
