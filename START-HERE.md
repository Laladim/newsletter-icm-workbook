# Start here

You do not need to understand the folder structure before using this workbook.
Choose one path below.

## Guided path with Claude Code or Codex

1. Clone or download this repository.
2. Open the repository folder in Claude Code or Codex.
3. Paste this exact instruction:

```text
Read SETUP.md and guide me through creating my newsletter ICM workspace.
```

The agent will ask a few questions at a time. It will prepare a publication
brief, stop for your approval, generate the tailored profile, and stop again
for your profile review. It may not proceed past either stop on its own.

## Workbook-only path

1. Read `NEW-NEWSLETTER-DISCOVERY.md`.
2. Answer each section using the four evidence labels:
   `Supplied fact`, `Researched evidence`, `Interpretation`, and
   `Human decision`.
3. Turn the answers into `publication-brief.md`.
4. Approve or revise the completed brief before any contracts are generated.
5. Use `SETUP.md` as the generation checklist.

## What you will decide

Only you may decide:

- who the publication serves;
- its recurring editorial promise;
- its positioning and point of view;
- its risk tolerance;
- whether the generated profile is accepted; and
- who may schedule, send, activate, or publish.

An agent may organize answers, research evidence you authorize, identify gaps,
and draft files. It may not invent your history, expertise, sources, tools,
permissions, or decisions.

## Safe first run

Every profile begins in `shadow` mode with local Markdown delivery. A shadow
run can exercise intake, source selection, research, routing, drafting, review,
packaging, and a simulated local delivery surface. It does not connect to or
write to an email platform.

Only consider a platform adapter after the profile and shadow edition pass.
Treat that connection as a separate supervised pilot with an explicit scope,
readback, rollback route, and human publishing boundary.

## How progress works

Each edition follows nine folders in order:

1. Intake
2. Source selection
3. Research
4. Editorial routing
5. Draft
6. Quality review
7. Package
8. Delivery
9. Post-publish records and learning

Each completed stage leaves files and a receipt. If work stops, the next person
or agent runs the verifier and resumes from the first unfinished stage.

## Quick checks

After profile generation:

```bash
python3 scripts/verify-publication.py publications/your-newsletter
```

After stamping or continuing an edition:

```bash
python3 scripts/verify-edition.py editions/YYYY-MM-DD-your-newsletter
```

For the whole workbook:

```bash
python3 _shared/check-rules.py
python3 scripts/verify-template.py
```
