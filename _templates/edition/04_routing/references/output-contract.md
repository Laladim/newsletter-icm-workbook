# 04_routing output contract

Create `output/editorial-plan.md` with:

```text
# Editorial plan

- Edition ID:
- Lead story:
- Why this lead serves the audience now:
- Thesis:
- Reader consequence:
- Evidence limits and required nuance:
- Supporting items or recurring modules:
- Required primary-data anchors:
- Required source count or citation rule:
- Product-claim route: required | no product claims
- Defamation or liability route: required | standard review
- Draft format and canonical output home:
- Visual requirement:

## Material the draft must not claim

## Decisions later stages must not relitigate
```

Create `output/routing-receipt.md` with one row for every considered item:

```text
| Item | Decision | Destination | Identifier or row | Reason | Write/readback proof or shadow simulation |
```

Every lead, future-edition item, supporting item, alternate-content route, and
rejected item must have a destination. In production, persist and read back the
configured queue or record updates before drafting. In shadow mode, simulate
them only. Apply the configured editorial ranking automatically, then create
`output/stage-receipt.md` using `_shared/approval-contract.md` when the route
passes its exit gate.
