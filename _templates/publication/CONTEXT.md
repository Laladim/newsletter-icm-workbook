---
publication_id: "{{publication_id}}"
title: "{{publication_title}}"
mode: shadow
profile_status: unconfigured
profile_review_status: pending
profile_reviewed_by: ""
profile_reviewed_at: ""
publication_brief_sha256: "{{publication_brief_sha256}}"
canonical_output_home: "local-markdown: editions/{{publication_id}}"
final_review_surface: "local-markdown: stage-08 review package"
routine_run_authority: "human: replace"
final_review_approver: "human: replace"
schedule_send_publish_authority: "human: replace"
post_publish_record_authority: "human: replace"
---

# {{publication_title}}

This profile turns the generic newsletter engine into one publication. It is
not usable until every contract is grounded in the approved
`publication-brief.md`, the brief hash matches, and a human approves the final
profile.

## Business and audience

- Accountable owner: replace from the approved brief.
- Primary audience: replace from the approved brief.
- Reader problem: replace from the approved brief.
- Recurring promise: replace from the approved brief.
- Positioning: replace from the approved brief.
- Intended cadence: replace from the approved brief without granting send
  authority.

## Editorial identity

- Voice and expertise posture: read `editorial-contract.md`.
- Edition anatomy and reader action: read `editorial-contract.md`.
- Source hierarchy and risk rules: read `source-contract.md`.
- Visual requirement: read `visual-contract.md`.

## Operating boundaries

- Mode begins as `shadow`.
- Output and final review remain local Markdown in shadow mode.
- A future platform preference is intent only, not a configured adapter.
- Tool access never changes the named human publishing authority.
- Stage 09 does not run until real publication is observed under an authorized
  live mode.

## Local files

| File | Owns |
|---|---|
| `publication-brief.md` | approved source decisions and evidence categories |
| `editorial-contract.md` | audience, promise, voice, structure, and content standards |
| `source-contract.md` | sources, freshness, credibility, evidence, citation, and risk rules |
| `visual-contract.md` | whether visuals are needed and how they are judged |
| `delivery-contract.md` | output format, review surface, authority, platform intent, and rollback |
| `skill-bindings.md` | verified capability used at each stage |

## Activation checklist

Set `profile_status: configured` only when every contract has no unresolved
placeholder, all required capability bindings verify, authority is explicit,
and the profile matches the approved brief hash.

Set `profile_review_status: approved` only after the named human reviews this
complete profile. The edition stamper must reject any other state.
