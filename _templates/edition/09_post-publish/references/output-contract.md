# 09_post-publish output contract

This stage begins only after publication is observed. Create:

`output/publication-receipt.md`

```text
# Publication receipt

- Platform:
- Publication or account identity:
- Post ID:
- Canonical live URL:
- Published at:
- Published by:
- Live state observed at:
- Live metadata and body match:
```

`output/downstream-readback.md`

```text
# Downstream readback

| Destination | Intended range or record | Dry-run result | Authorized write | Exact readback | Result |
```

`output/performance-snapshot.md`

```text
# Performance snapshot

- Captured at:
- Recipient cohort and configuration:
- Delivered:
- Delivery rate:
- Opens and open rate:
- Clicks and click rate:
- Spam or delivery anomalies:
- Comparison baseline:
- Reusable learning and confidence:
```

In shadow mode, reconstruct these only from an unchanged historical edition and
label them historical. Do not write downstream. After the configured
readbacks pass, create `output/stage-receipt.md` using
`_shared/approval-contract.md`. If publication has not happened, record the
wait state instead of a passing receipt.
