# Run authorization and stage receipt contract

A creation or continuation command authorizes routine work allowed by the
publication mode. Passing stage evidence opens the next stage automatically.
Do not ask for approval after every internal stage.

The command never grants schedule, send, activate, or publish authority.

Every completed stage writes `output/stage-receipt.md` with:

```text
# Stage receipt

- Edition ID:
- Stage:
- Run authorization:
- Completed by:
- Completed at:
- Inputs opened:
- Outputs written:
- Verifiers and specialist checks:
- Readback or inspection evidence:
- Exit result: pass | revise | blocked | failed
- Exception status:
- Next action:
- External writes:
```

Only `pass` moves forward. `revise` remains in the stage. `blocked` or `failed`
stops and records the exact issue.
