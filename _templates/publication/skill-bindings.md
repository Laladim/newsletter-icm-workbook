# Capability bindings for {{publication_title}}

Source: the approved `publication-brief.md` and
`_shared/skill-interface.md`. Bind only capabilities that can be verified.

| Capability | Canonical binding | Trigger | Output proof | Required? |
|---|---|---|---|---|
| candidate discovery | configure-after-brief | configure-after-brief | configure-after-brief | yes |
| research and source verification | configure-after-brief | configure-after-brief | configure-after-brief | yes |
| editorial judgment | configure-after-brief | configure-after-brief | configure-after-brief | yes |
| newsletter writing | configure-after-brief | configure-after-brief | configure-after-brief | yes |
| factual and risk review | configure-after-brief | configure-after-brief | configure-after-brief | yes |
| visual production | configure-after-brief | configure-after-brief | configure-after-brief | yes or no |
| subject and packaging | configure-after-brief | configure-after-brief | configure-after-brief | yes |
| delivery adapter | manual: create and inspect the local Markdown review package | Stage 08 in shadow mode | local artifact path and visual readback | yes |
| analytics and records | configure-after-brief | configure-after-brief | configure-after-brief | yes or no |

Allowed binding forms are `manual:`, `local:`, `command:`, and `none:`. Required
rows cannot use `none:`. A `local:` or `command:` path must exist from the
repository root. A plausible tool name, product name, URL, or absolute path is
not a verified binding.
