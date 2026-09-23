# Shared contracts

This folder owns rules that apply across publications and editions. A durable
rule gets one canonical home. Necessary duplicates must be registered in
`rule-map.json` and checked with `check-rules.py`.

Read:

- `safety-contract.md` for modes, human authority, and live-write boundaries.
- `approval-contract.md` for the two setup gates and edition receipts.
- `edition-contract.md` for stage anatomy and file-based state.
- `skill-interface.md` for capability slots and verifiable binding forms.

After changing a shared contract, inspect every derived file reported by the
rule checker. Update or bless each dependency deliberately.
