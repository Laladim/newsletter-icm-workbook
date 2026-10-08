# Deployment decision

This record tells a new operator what access the workbook needs and which kind
of model to use at each stage. Plans and products change, so each section
names the official page it was checked against and the date. Recheck those
pages before you rely on them.

## 1. Access an operator needs

Checked on 9 October 2026.

| Need | What counts | Official source |
|---|---|---|
| Python | Python 3.9 or newer. `scripts/preflight.py` checks it. | Tested in this repository's CI |
| Claude Code | A Pro, Max, Team, Enterprise, or Console account. The free Claude plan does not include Claude Code. Team and Enterprise users sign in with the account their admin invited. Cloud providers (Amazon Bedrock, Google Cloud, Microsoft Foundry) also work. | [Claude Code setup](https://code.claude.com/docs/en/setup), [authentication](https://code.claude.com/docs/en/authentication) |
| Codex (alternative) | A ChatGPT plan that includes Codex, or an OpenAI API key billed at API pricing. Check the plan card for CLI access. | [Codex pricing](https://learn.chatgpt.com/docs/pricing) |
| API key, connector, or MCP server for the workbook itself | None. The scripts use only the Python standard library. | This repository |

If you only have a chat app and no coding agent, use the workbook-only path in
`START-HERE.md`. You can still answer the discovery workbook and create the
publication brief by hand.

## 2. Model choice by stage

The rule: a stage whose output a script can check may use a lighter, faster
model. A stage that needs judgment uses the strongest model you have. The
verifier is the same either way, so a weaker model cannot pass work the
verifier would reject.

| Stage | Model | Why |
|---|---|---|
| Setup interview and publication brief | Strongest | Elicits the owner's decisions; mistakes reach every later edition |
| 01 Intake | Lighter | Copies fields from the profile; `verify-edition.py` checks them |
| 02 Source selection | Lighter | Dates, duplicates, and source rules are checkable |
| 03 Research | Strongest | Claim-level evidence, contrary evidence, and limits need judgment |
| 04 Routing | Strongest | Chooses the lead and thesis against the promise |
| 05 Draft | Strongest | Writing quality and staying inside the evidence |
| 06 Quality review | Strongest | Factual, legal, and editorial release decisions |
| 07 Package | Lighter | Completeness, links, and lengths are checkable |
| 08 Delivery | Lighter | A local readback compares the surface with the package |
| 09 Post-publish | Lighter | Records observed numbers; runs only after real publication |

Adjust from evidence: if a lighter-model stage fails its verifier twice on the
same edition, move that stage to the strongest model and note it here.
