# Pilot scorecard

Copy this file for each new operator or publication and fill it in as you go.
It answers one question at Day 30: did the workbook produce accepted
newsletter editions faster or better than before, and at what cost?

Record the baseline before the first run. A baseline written after the pilot
starts is already shaped by the pilot.

## Before Day 1: baseline

| Measure | Value | How you got it |
|---|---|---|
| How the owner makes an issue today (steps, tools, reviewers) | | Ask the owner to walk through the last issue |
| Hours per issue today | | Owner estimate or calendar |
| Corrections after review per issue today | | Last two or three issues |
| Issues published in the last 30 days | | Platform or archive |

## Access check

| Check | Result |
|---|---|
| Agent and plan match `deploy/DEPLOYMENT-DECISION.md` section 1 | |
| `python3 scripts/preflight.py` result (paste the last line) | |
| Folder trusted in Claude Code, or Codex in use | |

## Each run

Write the start and finish times when they happen. Do not reconstruct them from
stage receipts later: a receipt's completion time changes when a stage is
re-verified, so it can show a later stage finishing before an earlier one.

| Measure | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Setup: kickoff to approved brief (minutes) | | | |
| Setup: approved brief to approved profile (minutes) | | | |
| Edition: Stage 01 start to Stage 08 pass (minutes) | | | |
| `verify-edition.py` passed on the first try (yes or no) | | | |
| Stage 06 findings that needed a correction | | | |
| Times the owner had to step in or redirect | | | |
| Owner accepted the edition (yes or no) | | | |
| Cost (see below) | | | |

## Cost

Follow the official [costs page](https://code.claude.com/docs/en/costs),
checked on 9 October 2026:

- API or Console users: run `/usage` at the end of the run and copy the
  Session block's `Total cost`. It is an estimate; the Console usage page is
  the bill.
- Pro and Max subscribers: usage is included in the plan, so there is no
  per-session dollar figure. Note the plan usage bars before and after the run.
- Team and Enterprise: an admin reads spend per user in the organization's
  analytics.

Cost per accepted edition = total cost of all runs / editions the owner
accepted. Count only accepted editions in the denominator.

## Day 30 readout

| Question | Answer and evidence |
|---|---|
| Accepted editions in 30 days, compared with the baseline | |
| Time per accepted edition, compared with hours per issue today | |
| Corrections per edition, compared with the baseline | |
| Cost per accepted edition | |
| Can the operator run the next edition without help? | |
| What changed in the workbook because of this pilot? | |
| Decision: continue, adjust, or stop | |

A faster run that the owner did not accept, or that skipped a gate, counts as a
failed run, not a faster one.
