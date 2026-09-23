<!-- newsletter-icm-workbook:v1.0.0 -->
# Newsletter ICM Workbook

Build a newsletter workflow whose decisions, evidence, and progress live in
files instead of chat memory.

This public workbook is for a person or small team starting a newsletter. You
can read it on your own, or open the repository in Claude Code or Codex and ask
for a guided interview. The interview produces an approved publication brief,
a tailored publication profile, and a local shadow edition that cannot send or
publish anything.

## What you get

- A guided discovery workbook for audience, promise, scope, evidence, voice,
  cadence, visuals, metrics, ownership, risk, and publishing authority.
- Two deliberate human gates: approve the publication brief, then approve the
  generated profile before the first shadow edition.
- A fixed nine-stage edition engine from intake through post-publish learning.
- Deterministic checks for incomplete profiles, placeholders, invented tool
  bindings, unclear authority, secrets, and skipped edition stages.
- A sanitized Beyond Banks example that shows the answer-to-file transformation
  without exposing private operations, sources, content, records, or results.

## Fastest start

Clone the repository, open it in Claude Code or Codex, and paste:

```text
Read SETUP.md and guide me through creating my newsletter ICM workspace.
```

The agent must ask one small question group at a time. It must keep supplied
facts, researched evidence, interpretations, and your decisions separate. It
cannot choose your audience, promise, positioning, risk tolerance, final
profile, or publishing authority for you.

Prefer a workbook-only path? Start with [START-HERE.md](START-HERE.md) and then
complete [NEW-NEWSLETTER-DISCOVERY.md](NEW-NEWSLETTER-DISCOVERY.md).

## Safety defaults

- Every new publication starts in `shadow` mode.
- Shadow delivery is local Markdown only.
- Platform integrations are optional and require a separate supervised pilot.
- Credentials never belong in this repository.
- Tool access never grants schedule, send, activate, or publish authority.
- The human named in the publication profile keeps all publishing authority.

## Commands

```bash
python3 scripts/stamp.py publication --id your-newsletter --title "Your Newsletter"
python3 scripts/stamp.py contracts --publication your-newsletter
python3 scripts/verify-publication.py publications/your-newsletter
python3 scripts/stamp.py edition --publication your-newsletter --date 2026-09-23
python3 scripts/verify-edition.py editions/2026-09-23-your-newsletter
```

Run `python3 scripts/stamp.py --help` before using command options. The setup
guide explains when each command is allowed.

## Public companion versions

The Google Doc combines the discovery workbook and setup guide. The Google
Sheet mirrors `FILE-BUILD-MAP.csv`. GitHub remains canonical, and each Google
file displays source version `v1.0.0` plus make-a-copy instructions.

- [Discovery and setup guide, view only](https://docs.google.com/document/d/1vF7u3wKQEFoMHsKJEDZEKC0rmmoy-tur4YLxYlIx74Q/edit) ([make a copy](https://docs.google.com/document/d/1vF7u3wKQEFoMHsKJEDZEKC0rmmoy-tur4YLxYlIx74Q/copy))
- [File build map, view only](https://docs.google.com/spreadsheets/d/17ZTncp2vIgivSa0om0b7UjHOYMYDSvdcsErto42PXMc/edit) ([make a copy](https://docs.google.com/spreadsheets/d/17ZTncp2vIgivSa0om0b7UjHOYMYDSvdcsErto42PXMc/copy))

## What is canonical

This GitHub repository is the canonical public source. A private production
workspace may use the same architecture, but its accounts, sources, content,
records, performance data, and operating authority do not belong here.

## Verification

```bash
python3 _shared/check-rules.py
python3 scripts/verify-template.py
python3 scripts/smoke-test.py
```

The smoke test creates a fictional publication in a disposable copy, generates
all seven publication files, verifies the profile, stamps an edition, and
passes a local shadow run through delivery.

## License and credit

Copyright 2026 Laladim.

- Scripts are licensed under the MIT License in `LICENSE-CODE`.
- Guides, templates, workbook material, and the sanitized case study are
  licensed under Creative Commons Attribution 4.0 in `LICENSE-CONTENT`.

When reusing the content, credit `Laladim` and link to this repository.
