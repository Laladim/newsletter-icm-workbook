# 02_source-selection output contract

Create `output/candidate-set.md` with:

```text
# Candidate set

- Edition ID:
- Starting route: supplied rows | auto-discovery | supplied topic or source
- Discovery window or supplied scope:
- Canonical sources checked:
- Prior-coverage records checked:
- Performance evidence checked:

## Ranked candidates

For every candidate record:
- rank
- exact title
- source date
- canonical source URL or file
- News List row when applicable
- News Analysis row when applicable
- source credibility tier
- audience-fit score and reason
- freshness and duplication result
- prior-coverage result
- legal or reputational flag
- recommended next action

## Rejected or deferred candidates

Record the item, destination, and reason.

## Thin-edition finding

State `not applicable` or explain why no candidate cleared the threshold and
which profile-approved fallback may be used.
```

When a publication uses a spreadsheet or database, an identifier is not trusted
until the exact record has been read back. Select the strongest qualifying
research set using the configured criteria, then create
`output/stage-receipt.md` using
`_shared/approval-contract.md`. Pause only if the thin-edition exception cannot
be resolved by the documented fallback.
