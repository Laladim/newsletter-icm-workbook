# 06_quality-review output contract

Create `output/quality-report.md` with:

```text
# Quality report

- Edition ID:
- Draft reviewed:
- Draft identifier or hash:
- Full artifact inspected: yes | no
- Rendered visual inspected: yes | no | not applicable
- Deterministic checks run:
- Specialist reviews run:

## Findings

| ID | Severity | Owner stage | Finding | Evidence | Correction | Recheck result |

## Claim and citation integrity
## Defamation and liability result
## Product-claim result
## Editorial and audience result
## Structure, repetition, and style result
## Visual result
## Technical and link result
## Remaining blockers
## Release result: pass | revise | stop
```

Create `output/verified-artifact-pointer.md` with the corrected artifact path or
URL, immutable identifier or hash, verification time, rendered or actual
surface inspected, and final result.

`output/stage-receipt.md` may record `Exit result: pass` only when
`Release result: pass` and no release blocker remains. It uses
`_shared/approval-contract.md`. A score or successful script alone is not a
pass.
