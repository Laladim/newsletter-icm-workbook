# Capability binding interface

The newsletter engine defines capability slots. A publication profile binds
each required slot to one canonical capability or explicit human procedure.
The engine does not invent or copy implementations.

| Capability slot | Used in | Binding must explain |
|---|---|---|
| candidate discovery | source selection | where candidates come from and how freshness and duplication are checked |
| research and source verification | research | source hierarchy, claim ledger, and URL or file readback |
| editorial judgment | routing | audience fit, thesis selection, and unused-item routing |
| newsletter writing | draft | voice, structure, length, citations, and output format |
| factual and risk review | quality review | claims, specialist risk, prohibited language, and release threshold |
| visual production | draft or package | whether visuals are needed and how they are produced and inspected |
| subject and packaging | package | metadata, links, accessibility, and complete package checks |
| delivery adapter | delivery | local or platform surface, readback, rollback, and human authority |
| analytics and records | post-publish | approved writes, exact readbacks, and performance fields |

## Allowed binding forms

The `Canonical binding` cell in `skill-bindings.md` must start with exactly one
of these forms:

- `manual:<procedure>` for an explicit human or agent procedure that claims no
  installed tool.
- `local:<relative-path>` for a repository file or directory that exists.
- `command:<relative-script>` for a repository script that exists.
- `none:<reason>` for an optional capability that is deliberately unused.

`local:` and `command:` paths are resolved from the repository root. Absolute
paths, home-directory shortcuts, unverified tool names, URLs presented as
installed capabilities, and empty labels are invalid.

A required capability cannot use `none:`. A binding is valid only when its
trigger is specific and its output proof is observable. If a verified external
integration is added later, record it as a local adapter or command whose own
contract proves the connection. Do not use a plausible product name as proof.
