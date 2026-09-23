# Guided newsletter setup contract

This file is the agent-readable route for creating one tailored publication
profile. The human owns the decisions. The agent owns faithful elicitation,
evidence labeling, file generation, and verification.

## Kickoff

The supported kickoff instruction is:

```text
Read SETUP.md and guide me through creating my newsletter ICM workspace.
```

## Non-negotiable behavior

1. Ask one small question group at a time, with no more than three questions.
2. Use plain language and explain unfamiliar terms before asking for a choice.
3. Keep four categories separate in notes and in the publication brief:
   - `Supplied fact`: something the human states about the publication.
   - `Researched evidence`: something opened and traced to a source.
   - `Interpretation`: a conclusion drawn from facts or evidence.
   - `Human decision`: a choice only the publication owner can make.
4. Never convert an interpretation into a fact.
5. Never invent a tool, connector, source, credential, expertise claim,
   audience insight, approval, or publishing authority.
6. Never copy an assumption from the example publication into a new profile.
7. Default to `shadow` mode and local Markdown delivery.
8. Treat every platform integration as optional until a separately authorized
   supervised pilot exists.
9. Never schedule, send, activate, or publish.

## Interview sequence

Use `NEW-NEWSLETTER-DISCOVERY.md` as the canonical question bank. Ask these
groups in order and summarize the answer after each group:

1. Publication identity and intended outcome.
2. Primary audience and recurring reader problem.
3. Editorial thesis, recurring promise, positioning, and point of view.
4. Topic boundaries, exclusions, and recurring sections.
5. Evidence sources, freshness, corroboration, citation, and risk requirements.
6. Voice, expertise posture, format, length, cadence, visuals, and intended
   reader action.
7. Ownership, review surface, metrics, platform intent, rollback, and human
   publishing authority.
8. Open questions, conflicts, and decisions that still require the human.

When a claim would benefit from research, ask whether the human wants research
now. If yes, record the exact source location, access date, supported claim,
and limits. If no, leave the item explicitly unverified.

## Phase 1: create and approve the publication brief

Once the title and lowercase kebab-case publication ID are known, run:

```bash
python3 scripts/stamp.py publication --id <publication-id> --title "<Title>"
```

This creates only `publications/<publication-id>/publication-brief.md`. Fill it
from the interview. Do not create, populate, or pre-decide the six profile
contracts yet.

Before requesting approval:

- resolve contradictions or mark them as open;
- distinguish all supplied facts, evidence, interpretations, and decisions;
- leave no required human decision blank;
- name any missing evidence without filling it with a guess; and
- show the completed brief to the human.

Then stop and ask the human to approve or revise the publication brief. A clear
approval applies only to that exact brief. Record the approver and date in the
brief front matter. Do not infer approval from silence or from approval of an
earlier summary.

Verify the approved brief:

```bash
python3 scripts/verify-publication.py publications/<publication-id> --brief-only
```

## Phase 2: generate the six profile contracts

Only after the approved-brief check passes, run:

```bash
python3 scripts/stamp.py contracts --publication <publication-id>
```

Generate these six files from the approved `publication-brief.md`:

1. `CONTEXT.md`
2. `editorial-contract.md`
3. `source-contract.md`
4. `visual-contract.md`
5. `delivery-contract.md`
6. `skill-bindings.md`

Use `FILE-BUILD-MAP.csv` as the answer-to-file routing map. Preserve the brief
as the approved source. Put its SHA-256 digest in `CONTEXT.md` so later changes
cannot silently detach the profile from the approved decisions.

Capability bindings must use one of the declared forms in
`_shared/skill-interface.md`. A tool or path binding must resolve during
verification. When no verified tool exists, bind an explicit manual procedure
or mark an optional capability `none:<reason>`. Never name a plausible tool and
pretend it exists.

Run:

```bash
python3 scripts/verify-publication.py publications/<publication-id> --pre-review
```

Fix all structural failures before review.

## Profile review stop

Present the human with:

- the approved publication brief hash;
- the audience, promise, positioning, and risk decisions;
- the edition anatomy and source rules;
- the local output and review surfaces;
- every capability binding and its proof;
- the named schedule, send, and publish authority; and
- any limitation or manual step.

Then stop again. Ask the human to approve or revise the generated profile. Only
after explicit approval may `profile_review_status` become `approved`, with the
reviewer and date recorded in `CONTEXT.md`.

Run the publication verifier again. The first edition command must fail until
this review gate passes.

## Phase 3: first shadow edition

After final profile acceptance:

```bash
python3 scripts/stamp.py edition --publication <publication-id> --date YYYY-MM-DD
```

Keep every artifact local. Stage 08 may verify a local Markdown review surface.
Stage 09 remains unopened until real publication is later observed under an
authorized live mode. A complete first shadow run therefore passes through
Stage 08 without external writes:

```bash
python3 scripts/verify-edition.py editions/<edition-id> --require-through 08_delivery
```

Do not propose a platform connection as part of the first shadow run. A live
adapter requires its own supervised-pilot decision, exact scope, dry run,
readback, rollback, and human authority.
