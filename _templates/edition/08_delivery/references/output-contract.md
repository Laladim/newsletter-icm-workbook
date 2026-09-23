# 08_delivery output contract

Create `output/artifact-pointer.md` with:

```text
# Final review surface pointer

- Edition ID:
- Platform:
- Account or publication identity:
- Draft or post ID:
- Exact editor or preview URL:
- State observed:
- Scheduled time: null | observed value
- Published time: null | observed value
- Observed at:
```

Create `output/delivery-receipt.md` with:

```text
# Delivery receipt

- Verified package identifier:
- Operation performed: local simulation | duplicate | create draft | update draft
- Adapter used:
- API or operation result:
- Metadata readback:
- Body readback:
- Visual readback:
- Audience readback:
- Links checked on final surface:
- Unsent and unscheduled state verified:
- Visible surface inspected by:
- Discrepancies and corrections:
- Final result: match | revise | blocked
- Rollback route:
```

In shadow mode, use a local simulated surface or an unchanged historical
artifact only. Do not write to the delivery platform. In an approved live mode,
create and read back the actual unsent draft automatically, then create
`output/stage-receipt.md` when it matches. Notify the authorized human with the
review surface. The receipt never grants an agent schedule, send, or publish
authority.
