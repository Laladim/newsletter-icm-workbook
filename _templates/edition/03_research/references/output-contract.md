# 03_research output contract

Create both `output/research-packet.md` and `output/source-ledger.md`.

`research-packet.md` contains:

```text
# Research packet

- Edition ID:
- Approved candidates:
- Research completed at:

## Candidate: exact title

### Detailed analysis
### Specific implications for the publication audience
### Key numbers, names, dates, and domain-specific details
### Broader context and contrary evidence
### What readers should watch for or do differently
### Audience relevance assessment and full rationale
### Recommendation and confidence limits
### Supported claims
### Unsupported, qualified, or unresolved claims
```

`source-ledger.md` contains one row per source:

```text
| ID | Claim supported | Source owner | Source type | Exact title | Date | URL or file | Opened at | Primary or independent | Limits | Live check |
```

When the publication profile names a production research record, write its
complete configured fields and read the exact destination back before Stage 04.
In shadow mode, record the intended destination and simulated values without
writing. After the evidence gate passes, create `output/stage-receipt.md` using
`_shared/approval-contract.md` and continue automatically.
