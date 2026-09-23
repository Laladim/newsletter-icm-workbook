# Newsletter ICM workbook

One approved publication profile and one evidence-backed request go in. One
verified newsletter edition record comes out, delivered only to the local or
live surface and authority named by that profile.

## Routes

| Request | Read first | Stop condition |
|---|---|---|
| Set up a new publication | `SETUP.md` | approved publication brief, then approved profile |
| Answer the discovery workbook manually | `NEW-NEWSLETTER-DISCOVERY.md` | all required human decisions are explicit |
| Generate contracts from an approved brief | `SETUP.md`, Phase 2 | publication verifier passes, then human profile review |
| Create the first edition | selected publication `CONTEXT.md` | local shadow delivery passes through Stage 08 |
| Continue an edition | `scripts/verify-edition.py` output | reported pickup stage passes |
| Change shared rules or templates | `_shared/CONTEXT.md` | drift and template verifiers pass |

## Architecture

- `_templates/publication/` owns the seven publication-file shapes.
- `_templates/edition/` owns the fixed nine-stage edition path.
- `publications/` contains one configured profile per newsletter and is ignored
  by Git except for its placeholder.
- `editions/` contains one evidence-backed record per edition and is ignored by
  Git except for its placeholder.
- `_shared/` owns safety, movement, capability, and state contracts.
- `scripts/` stamps and verifies publication and edition records.
- `examples/` is explanatory only and grants no production authority.

Folders carry sequence. Each folder's `CONTEXT.md` carries local instructions.
Files in `output/` carry state. Do not create a separate status tracker.

## Weight-bearing decisions and stage

Audience, recurring promise, positioning, risk tolerance, profile acceptance,
and publishing authority are human decisions. They must be settled before the
first edition.

Within an edition, research carries the most weight. A polished draft cannot
repair weak, stale, duplicated, or misunderstood evidence.

## Modes and authority

`shadow` is local-only. `supervised-pilot` permits one explicitly approved live
scope. `production` permits only configured routine writes after a recorded
owner cutover. The publication profile must name the human who alone may
schedule, send, activate, or publish.

## Rule changes

When a shared rule or factory contract changes, inspect every file that derives
from it and run:

```bash
python3 _shared/check-rules.py
python3 scripts/verify-template.py
python3 scripts/smoke-test.py
```
