# Handoff and 30-day rollout

This is the plan for handing the workbook to a new newsletter owner and
leaving them able to run it alone. It follows the workbook's own safety
contract (`_shared/safety-contract.md`) and records evidence in
`deploy/PILOT-SCORECARD.md`.

## Is the workbook the right fit?

Use it when all four are true:

1. The owner publishes, or plans to publish, on a regular cadence.
2. The owner can name the audience, the recurring promise, and who alone may
   publish, or is willing to decide them in the setup interview.
3. Quality can be checked: sources, links, claims, and package completeness.
4. The operator passes `scripts/preflight.py` or will use the workbook-only
   path.

What changes when it works: decisions and evidence live in files, any operator
can resume from the verifier's pickup stage without the original chat, and the
two human gates are explicit. A faster draft alone is not the goal.

## Pilot design

| Item | Plan |
|---|---|
| Cohort | One owner and one operator (often the same person) |
| Unit of work | One approved publication brief, then one shadow edition through Stage 08 |
| Duration | 30 days |
| Success | The owner accepts the edition, every gate passed, and the operator can name the next step without help |
| Protected scope | Shadow mode only. No platform connection during the pilot |
| Feedback | Agree at the start what notes may be kept and whether anything may be quoted. Quote or name a person publicly only with their written yes |
| Measures | `deploy/PILOT-SCORECARD.md`, baseline recorded before Day 1 |

## 30-day rollout

| Week | Work | Exit condition |
|---|---|---|
| Before Day 1 | Access check, preflight, baseline | Preflight passes and the baseline table is filled |
| Week 1 | Setup interview, brief approval, profile review | `verify-publication.py <id>` passes and the owner approved both gates |
| Week 2 | First shadow edition | `verify-edition.py editions/<id> --require-through 08_delivery` passes and the owner reviewed the local preview |
| Week 3 | Second and third shadow editions, measured | Each run recorded in the scorecard |
| Week 4 | Readout and handoff | Day 30 readout filled; the operator runs the next pickup alone; the owner decides continue, adjust, or stop |

## Moving toward a live platform

Go one step at a time, and only on evidence:

1. **Shadow**: local outputs only. Stay here until editions pass the verifier
   on the first try and the owner accepts them.
2. **Supervised pilot**: one precisely approved live scope, such as creating
   one unsent draft on the platform, with readback and a rollback route. The
   named human still schedules and sends.
3. **Production**: only after a successful shadow comparison, a supervised
   pilot with verified delivery and post-publish readbacks, a rollback route,
   and a written owner decision naming the exact scope.

A verified shadow profile never grants live access or publishing authority by
itself.

## The maintainer

Name one maintainer for each deployment, usually the operator.

- Keeps the publication's `CONTEXT.md` and contracts accurate when the owner
  changes a decision.
- Runs `scripts/preflight.py` after pulling workbook updates and the
  verifiers before each edition.
- Notices repeated corrections and proposes a contract change to the owner.
- Does not inherit the owner's approval or publishing authority.

Escalation: first `TROUBLESHOOTING.md`, then a GitHub issue on this
repository (never paste private content, credentials, or unpublished drafts
into an issue), then the publication owner for any decision.

## Closeout checklist

A pilot can be evaluated later only if these exist:

- [ ] Approved `publication-brief.md` and the approved profile
- [ ] Each edition's stage outputs and passing receipts
- [ ] Stage 06 quality reports showing what was corrected
- [ ] The filled `deploy/PILOT-SCORECARD.md`, including the baseline
- [ ] Current entry instructions that still match how the operator works
- [ ] The receiver's own words: what they will do next, and what "done" means
      to them

A folder that exists is not proof that the workflow ran. Run the verifiers.

## Common failure modes

| Failure | Prevention |
|---|---|
| No baseline | Fill the baseline table before Day 1 |
| Nobody owns decisions | The brief names the owner for audience, promise, risk, and publishing |
| The operator relies on the builder's chat | Pickup always starts from `verify-edition.py` output |
| Gates skipped to save time | The verifiers fail; a faster unaccepted run counts as a failure |
| Live platform connected too early | Stay in shadow until the supervised-pilot step above |
