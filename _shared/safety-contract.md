# Safety and authority contract

## Modes

- `template`: unconfigured and cannot execute
- `shadow`: local outputs only; no live external writes
- `supervised-pilot`: one precisely approved live scope
- `production`: configured routine writes after recorded owner cutover

## Human boundary

Access is not authority. Every publication profile must name who may authorize
a routine run, review the final surface, schedule, send or publish, and approve
post-publish records. An agent must stop before schedule, send, activate, or
publish unless a human performs that action.

## Cutover

Production requires a successful shadow comparison, a supervised live pilot,
verified delivery and post-publish readbacks, a rollback route, and a written
owner decision naming the precise scope.
