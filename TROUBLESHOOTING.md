# Troubleshooting

Start every diagnosis from the files, not from a remembered chat. Run the
check named below, read its exact message, and fix the cause in the file that
owns it. Then rerun the same check.

## First, find where you are

```bash
python3 scripts/preflight.py
python3 scripts/verify-publication.py publications/<publication-id>
python3 scripts/verify-edition.py editions/<edition-id>
```

`verify-edition.py` prints `Pickup:` with the first stage that has not passed.
Open that stage's `CONTEXT.md` and continue there. A new chat, a new operator,
or a new computer all resume the same way.

## Preflight

| Message | Cause | Fix |
|---|---|---|
| `FAIL Python` | Python is older than 3.9 | Install Python 3.9 or newer |
| `FAIL Workbook files` | Incomplete download | Clone or download the full repository again |
| `WARN AI coding agent` | Claude Code or Codex is not on the command path | Install one, or use the workbook-only path. For Claude Code install errors see the official [troubleshooting page](https://code.claude.com/docs/en/troubleshoot-install) |
| `WARN Git` | Git is not installed | Download updates as a zip, or install Git |
| `FAIL End-to-end run` | The smoke test failed on this computer | Run `python3 scripts/smoke-test.py` and read its last lines |

## Publication verifier

| Message contains | Cause | Fix |
|---|---|---|
| `contains unresolved placeholder` | A template field was never filled | Fill it from the approved brief |
| `must begin with human:` | An authority field names an agent or nobody | Name the human, for example `human: Your Name` |
| `binding must use an allowed prefix`, `bound path does not exist` | A capability names a tool that is not real | Use `manual:`, `local:`, `command:`, or `none:` from `_shared/skill-interface.md` |
| `may expose a secret` | A credential-like value is in a file | Remove it and rotate the credential |
| `contains a private local path` | A file names a path on your own computer | Use a repository-relative path |
| Brief or profile gate not open | Approval missing | The owner reads and approves the brief, then the profile |

## Edition verifier

| Message contains | Cause | Fix |
|---|---|---|
| `output exists before every earlier stage has a passing receipt` | Work was done out of order, or an earlier receipt is missing | Finish and verify the earlier stage first |
| `stage receipt exists before required outputs are complete` | A receipt was written too early | Complete the outputs named in the stage's output contract |
| `stage receipt names a different edition` or `stage` | A receipt was copied from elsewhere | Rewrite the receipt for this edition and stage |
| `edition root contains unresolved template placeholders` | The edition `CONTEXT.md` was not filled | Fill the assignment fields in Stage 01 |

## Rule checker

| Message | Cause | Fix |
|---|---|---|
| `STALE` | A shared rule changed after a file that depends on it was last reviewed | Open each listed file and update it, or run `python3 _shared/check-rules.py --bless <file> --reason "why no change was needed"` |
| `UNREGISTERED` | A factory file is not in the rule map | `python3 _shared/check-rules.py --register <file> --derives-from a.md,b.md` or `--independent` |
| Many `STALE` files right after cloning on Windows | Git changed line endings | The repository's `.gitattributes` prevents this; reclone, or run `git add --renormalize .` |

## Template verifier (maintainers)

| Message contains | Fix |
|---|---|
| `unclassified repository artifact` | Add the new file to `FILE-BUILD-MAP.csv` with all eleven columns |
| `shared Claude Code settings lost required` | Restore the ask or deny rule in `.claude/settings.json` |
| `em dash found` | Replace it with a comma, colon, or period |

## Agent behavior

| Symptom | Fix |
|---|---|
| Claude Code keeps asking before stamping or verifying | Accept the folder's trust prompt so the shared allow rules apply |
| The agent moved past the brief or profile gate without your approval | Stop it, rerun `verify-publication.py`, and approve only the exact brief or profile you read |
| The agent says it is done but the verifier fails | The verifier wins. Return to the reported stage |
| You only have a chat app (for example Claude Cowork) | Use the workbook-only path in `START-HERE.md` |

## See a finished sample

To see what a complete shadow edition looks like, keep the smoke test's
fictional edition:

```bash
python3 scripts/smoke-test.py --keep sample-edition
```

Open `sample-edition/` to read every stage output and receipt. Delete the
folder when you are done.
