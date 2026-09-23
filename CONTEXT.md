# Newsletter ICM workspace

One configured publication and one newsletter request go in. One verified
edition record comes out, delivered only to the surface and authority named by
the publication profile.

## Architecture

- `_templates/publication/` defines the publication-profile stamp.
- `_templates/edition/` defines the fixed nine-stage edition path.
- `publications/` contains one configured profile per newsletter.
- `editions/` contains one evidence-backed record per edition.
- `_shared/` contains safety, movement, capability, and state contracts.
- `scripts/` stamps and verifies records.

Folders carry sequence. Each folder's `CONTEXT.md` carries local instructions.
Files in `output/` carry state. Do not create a separate status tracker.

## Weight-bearing stage

Research carries the most weight. A polished draft cannot repair weak, stale,
duplicated, or misunderstood evidence.

## Modes and authority

`shadow` is local-only. `supervised-pilot` permits one explicitly approved live
scope. `production` permits only configured routine writes after an owner has
recorded cutover approval. The publication profile must name the human who
alone may schedule, send, activate, or publish.

## Rule changes

When a shared rule or factory contract changes, inspect every file that derives
from it and run:

```bash
python3 _shared/check-rules.py
python3 scripts/verify-template.py
```
