# Approval and stage receipt contract

## Publication brief gate

Audience, recurring promise, positioning, risk tolerance, and publishing
authority are human decisions. The agent may organize and draft them, but the
human must approve the complete `publication-brief.md` before profile contracts
are generated.

Approval applies to the exact brief content at that moment. Record the human
approver and date in front matter. After contract generation, bind the profile
to the brief with its SHA-256 digest.

## Profile review gate

The human must review the generated profile before the first edition is
stamped. Record `profile_review_status: approved`, a `human:` reviewer, and a
review date in the publication `CONTEXT.md`. A passing structural verifier does
not replace this decision.

## Edition run authorization

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
