# Start here

## What this gives you

One newsletter edition moves through nine visible stages:

1. Intake
2. Source selection
3. Research
4. Editorial routing
5. Draft
6. Quality review
7. Package
8. Delivery to a human review surface
9. Post-publish records and performance learning

Every stage has its own instructions, expected outputs, and completion receipt.
If a session stops, the next person or agent reads the files and continues from
the first unfinished stage.

## Set up your publication

From this folder, run:

```bash
python3 scripts/stamp.py publication --id your-newsletter --title "Your Newsletter"
```

Then configure these files under `publications/your-newsletter/`:

- `CONTEXT.md`: owner, audience, promise, cadence, authority, and mode
- `editorial-contract.md`: voice, structure, and quality standard
- `source-contract.md`: approved sources and evidence rules
- `visual-contract.md`: image requirements and review standard
- `delivery-contract.md`: platform, draft surface, readback, and rollback
- `skill-bindings.md`: the actual tools or procedures used at each stage

Start in `shadow` mode. Shadow mode produces local work and proves the process
without changing a live newsletter account.

## Create an edition

```bash
python3 scripts/stamp.py edition --publication your-newsletter --date 2026-09-01
```

Tell your agent:

```text
Create the newsletter. Use the publication profile and continue automatically
while each stage passes. Stop before scheduling, sending, or publishing.
```

Check progress with:

```bash
python3 scripts/verify-edition.py editions/2026-09-01-your-newsletter
```

## Move toward live use safely

Use three modes:

- `shadow`: local-only practice and comparison
- `supervised-pilot`: one precisely approved live test
- `production`: standing permission for configured routine writes

Before production, compare a shadow edition with the current workflow, run one
supervised live edition, verify the final draft and post-publish records, and
record the owner's cutover decision. Tool access never grants schedule, send,
or publish authority.
