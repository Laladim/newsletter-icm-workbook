---
publication_id: "{{publication_id}}"
title: "{{publication_title}}"
mode: template
profile_status: unconfigured
---

# {{publication_title}}

This profile turns the generic newsletter engine into one specific publication.
It is not usable until every field below is grounded and `profile_status` is
changed to `configured`.

## Business and audience

- Owner or business: replace with the accountable organization.
- Primary audience: describe the people this publication serves.
- Reader problem: name the recurring problem the newsletter helps solve.
- Promise: state what a reader consistently receives.
- Cadence: define the intended rhythm without granting send authority.

## Editorial identity

- Voice: point to `editorial-contract.md`.
- Standard structure: point to the publication-specific structure.
- Source hierarchy: point to `source-contract.md`.
- Visual identity: point to `visual-contract.md`.

## Operating boundaries

- Canonical output home: configure the one true production location.
- Final review surface: configure the surface the human actually inspects.
- Routine-run authorization: configure the command that authorizes automatic
  source selection, research, routing, drafting, QA, packaging, and draft staging.
- Final-review approver: configure a person or role.
- Schedule/send/publish authority: configure a person. Never assign this to an
  agent merely because it has tool access.
- Post-publish-write authority: configure a person or approved automation.

## Local files

| File | Owns |
|---|---|
| `editorial-contract.md` | audience, promise, voice, structure, content standards |
| `source-contract.md` | sources, freshness, credibility, evidence and citation rules |
| `visual-contract.md` | whether visuals are required and how they are judged |
| `delivery-contract.md` | output format, platform, readback, human authority and rollback |
| `skill-bindings.md` | canonical capability used at each stage |

## Activation checklist

A publication stays unconfigured until its identity, contracts, skill bindings,
output home, final surface, run authorization, exception stops, and human
authorities are explicit. Start it in
`shadow` mode. Promotion to a live mode requires the cutover contract in the
workspace root.
