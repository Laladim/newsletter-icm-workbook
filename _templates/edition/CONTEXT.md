---
edition_id: "{{edition_id}}"
publication_id: "{{publication_id}}"
edition_date: "{{edition_date}}"
mode: "{{mode}}"
---

# {{edition_id}}

This folder is one edition record. Read the publication profile first, then
walk the numbered stages. The edition inherits the profile's audience,
contracts, bindings, output home, final surface, and authority boundaries.
Inside each stage, `CONTEXT.md` is the active contract, `references/` holds only
named stable rules or pointers including `output-contract.md`, and `output/`
holds edition-specific state. Automatic movement receipts follow
`_shared/approval-contract.md`.

## Assignment

- Request: record the exact request in `01_intake/output/assignment.md`.
- Intended reader outcome: record the decision or benefit this edition should
  create.
- Authorized deviation: none unless the Stage 01 assignment and stage receipt
  name one within the user's run authorization.

## Where this stands

Status is what exists in the stage `output/` folders:

| Stage | Expected evidence before movement |
|---|---|
| `01_intake` | assignment and authority are unambiguous |
| `02_source-selection` | candidate set passes its configured exit gate |
| `03_research` | research packet and source ledger pass the evidence gate |
| `04_routing` | lead, thesis, supporting items, and unused routes pass the routing gate |
| `05_draft` | complete draft passes the draft exit gate |
| `06_quality-review` | all release blockers are resolved |
| `07_package` | complete delivery package passes all package checks |
| `08_delivery` | actual final surface is read back and remains unsent until authorized |
| `09_post-publish` | observed publication and downstream readbacks are recorded |

## Decisions that later stages must not relitigate

Record verified choices and reasons in the relevant stage receipt. Do not use
this summary to replace those receipts.

## Pickup

Run `python3 scripts/verify-edition.py <this-edition-folder>`. Then open the
reported pickup stage, its `CONTEXT.md`, `references/output-contract.md`, and
the last upstream output with a passing receipt. Continue from the first stage
that has not passed. Never infer state from chat memory.
