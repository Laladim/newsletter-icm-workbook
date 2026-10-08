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

## 3. Route decision

Default route: one operator, on their own account, on their own computer, in
`shadow` mode. Nothing is sent or published from the workbook.

The fact that changes the route: if your organization allows only a chat app
and no terminal or coding agent, use the workbook-only path in `START-HERE.md`.
You answer the discovery workbook and write the publication brief by hand, and
someone with a coding agent can generate the profile from your approved brief.

A second fact that changes who decides: if your organization manages Claude
Code centrally (Team or Enterprise with managed settings), your administrator
owns tool permissions. The workbook's gates still apply on top of those
settings.

## 4. Known capability gaps

| Gap | When you notice it | What to do |
|---|---|---|
| Your tool cannot run Python scripts | `scripts/preflight.py` cannot start | Use the workbook-only path; ask someone with a coding agent to run the verifiers |
| No Claude Code or Codex installed | Preflight shows WARN for the AI coding agent | Install one, or use the workbook-only path |
| No Git | Preflight shows WARN for Git | Download the repository as a zip; download it again for updates |
| Native Windows without WSL 2 | You want Claude Code's sandbox | The workbook runs on native Windows (tested in CI). Claude Code's sandbox needs WSL 2; see [sandboxing](https://code.claude.com/docs/en/sandboxing) |
| Codex instead of Claude Code | You open the folder in Codex | Codex does not read `.claude/settings.json`, so the shared permission rules below do not apply. The two human gates and the verifiers still do |
| No live platform delivery | You want the edition in your email platform | Shadow mode delivers local Markdown only. A platform connection is a separate supervised pilot with its own scope, readback, and rollback |

## 5. Network

The workbook's scripts work offline. Your AI coding agent needs internet
access to reach its provider. Behind a corporate proxy or firewall, ask your IT
team to follow the agent's network guide, for example
[Claude Code network configuration](https://code.claude.com/docs/en/network-config).
No gateway or proxy is needed for one operator.

## 6. Where your data lives

- Your real publication and edition folders stay on your computer. The
  repository's `.gitignore` already keeps `publications/` and `editions/` out
  of Git.
- For a backup, use a separate private repository. Never push real
  publications or editions to a public copy of this workbook.
- Never put passwords, API keys, or tokens in any workbook file. The template
  verifier and smoke test reject credential-like values.
- Anything your AI coding agent reads is sent to its provider under your
  account's terms. Do not put customer, health, or other confidential material
  into a publication unless your account's data terms allow it.

## 7. Shared Claude Code settings

The repository ships `.claude/settings.json`, so every operator who opens the
folder in Claude Code gets the same rules. Rule syntax follows the official
[permissions page](https://code.claude.com/docs/en/permissions).

| Rule | Type | Why |
|---|---|---|
| Edit files in `publications/` and `editions/` | allow | Newsletter work belongs there; edits elsewhere ask first |
| Run the workbook's own scripts | allow | Stamping and verifying should not interrupt the operator |
| Any MCP connector tool | ask | Shadow mode needs no connector, so any use gets a human look |
| Read `.env` or `.env.*` | deny | Keeps passwords and keys away from the agent |
| `git push` | deny | Only the human decides what reaches GitHub |

Claude Code applies the deny and ask rules at once. It ignores the allow rules
until you accept the folder's trust prompt, so accept it the first time you
open the workbook.

`/newsletter-setup` is a Claude Code skill in `.claude/skills/`. Only you can
run it; the agent cannot start it on its own. It sends the same kickoff
sentence as `START-HERE.md`.
