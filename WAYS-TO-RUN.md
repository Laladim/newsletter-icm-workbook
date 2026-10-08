# Ways to run the workbook

People open this workbook in different tools. This page tells you, for each
common one, how to open the folder, how to start the setup interview, and
what is different. The workbook itself is the same everywhere: the same
folders, the same two human gates, and the same checks.

You need three things whatever tool you use:

1. **A copy of this repository on your computer.** Clone it with Git, or on
   GitHub choose **Code**, then **Download ZIP**, and unzip it.
2. **Python 3.9 or newer**, for the readiness check and the verifiers.
3. **An AI coding agent signed in on your own account**, unless you choose the
   workbook-only path. For Claude Code that means a Pro, Max, Team, Enterprise,
   or Console account; the free plan does not include it.

## Which Python command to type

| Computer | Type | Notes |
|---|---|---|
| Mac or Linux | `python3 scripts/preflight.py` | |
| Windows | `python scripts/preflight.py` or `py scripts/preflight.py` | Python's [Windows guide](https://docs.python.org/3/using/windows.html) recommends `python` or `py`. If `python` opens the Microsoft Store, install Python from python.org and check "Manage app execution aliases" as that guide describes |

Everywhere else in the workbook, read `python3` as `python` or `py` on Windows.

## Pick your tool

How to read the status column:

- **Tested**: the maintainer ran the kickoff on a fresh clone of this
  repository on the date shown and reached setup interview group 1.
- **Checked on every push**: GitHub runs the readiness checks and the
  end-to-end test automatically on Ubuntu, macOS, and Windows.
- **Documented**: the tool's official documentation says it works this way;
  nobody has run the workbook in it yet. Please report what happens in a
  GitHub issue, without private content.

| Tool | Open the folder | Start the interview | What is different | Status |
|---|---|---|---|---|
| Claude Code in a terminal | `cd` into the folder, then run `claude` | Type `/newsletter-setup`, or paste the kickoff sentence | Accept the folder's trust prompt so the shared settings apply | Tested 9 Oct 2026, Claude Code 2.1.295 on macOS |
| Claude Code extension in VS Code or Cursor | **File**, **Open Folder**, then open the Claude Code panel | Type `/newsletter-setup`; if it is not in the `/` menu, paste the kickoff sentence | The extension shows a subset of commands. Preflight shows PASS when it finds the extension; the `claude` command itself is only on your path if you also install the CLI ([VS Code guide](https://code.claude.com/docs/en/vs-code)) | Tested 9 Oct 2026 with the extension's own engine, version 2.1.294, on macOS. Clicking through the panel itself: documented |
| Claude desktop app, **Code** tab | Click the **Code** tab, select **Local**, click **Select folder**, and choose this folder | Type `/newsletter-setup` or paste the kickoff sentence | The app includes Claude Code, so no separate install. Choose **Local**, not **Cloud** (see the web row). Needs a paid plan ([desktop quickstart](https://code.claude.com/docs/en/desktop-quickstart)). Preflight shows WARN for the AI agent; that is expected | Documented |
| Claude Code in JetBrains (IntelliJ, PyCharm, and others) | Open the folder as a project | Same as the terminal | The plugin needs the Claude Code CLI installed separately ([JetBrains guide](https://code.claude.com/docs/en/jetbrains)) | Documented |
| Codex CLI | `cd` into the folder, then run `codex` | Paste the kickoff sentence | Codex reads `AGENTS.md`, not `.claude/settings.json`, so the shared Claude Code permission rules do not apply. The two human gates and the verifiers still do | Tested 9 Oct 2026, codex-cli 0.161.0 on macOS |
| Codex extension in VS Code, Cursor, or Windsurf | Open the folder, then the Codex panel | Paste the kickoff sentence | Same as the Codex CLI ([Codex IDE guide](https://learn.chatgpt.com/docs/codex/ide)) | Documented |
| Claude Code on the web | Not recommended for setup | | Your brief, profile, and editions are kept out of Git on purpose (see `.gitignore`), so a cloud session has nowhere safe to keep them. Use a tool that runs on your own computer | Not recommended |
| Claude chat or Claude Cowork only, without Claude Code | Read the files yourself | Follow the workbook-only path in `START-HERE.md` | No agent runs the checks for you. Run the verifiers yourself if Python is installed | Workbook-only path |

The kickoff sentence:

```text
Read SETUP.md and guide me through creating my newsletter ICM workspace.
```

## Operating system notes

- **Windows**: the readiness checks and end-to-end test pass on Windows on
  every push. The repository's `.gitattributes` keeps line endings the same on
  every computer. For Claude Code, the official
  [overview](https://code.claude.com/docs/en/overview) recommends Git for
  Windows; without it, Claude Code uses PowerShell instead.
- **No Git**: download the ZIP. Preflight shows WARN for Git; that only means
  you download updates the same way.
- **Company computer**: if installs or network access are blocked, see
  `deploy/DEPLOYMENT-DECISION.md`, section 5, Network, and ask your IT team.

If something does not match this page, start with `TROUBLESHOOTING.md`.
