# Safety and authority contract

## Modes

- `shadow`: local outputs only, with no live external writes.
- `supervised-pilot`: one precisely approved live scope with readback and
  rollback.
- `production`: configured routine writes after recorded owner cutover.

Every newly stamped publication starts in `shadow` mode. A profile may remain
unconfigured while its brief or contracts are incomplete, but its mode does
not silently change.

## Human boundary

Access is not authority. A human must decide the audience, recurring promise,
positioning, risk tolerance, final profile acceptance, and all schedule, send,
activate, or publish authority.

Every publication profile names who may authorize a routine run, review the
final surface, schedule or publish, and approve post-publish records. An agent
must stop before schedule, send, activate, or publish.

## Data boundary

Never store credentials, account secrets, private source material, customer or
health data, unpublished production content, or private performance records in
this public repository. Refer to a protected source by an authorized route
only inside a private profile.

## Cutover

Platform integrations are optional. Production requires a successful shadow
comparison, a separately authorized supervised live pilot, verified delivery
and post-publish readbacks, a rollback route, and a written owner decision that
names the precise scope. A verified shadow profile alone never grants live
access or publishing authority.
