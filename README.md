# orchestrate-dev

`orchestrate-dev` is a portable development-workflow skill for Codex and Claude Code. It coordinates complex software work through explicit product, architecture, implementation, review, and QA roles while using the host agent's native capabilities; no MetaGPT runtime or separate model API is required.

## What it does

- Routes work into compact, coordinated, or critical delivery modes.
- Defines clear ownership and output contracts for each role.
- Separates implementation, review, and QA when risk warrants it.
- Requires acceptance criteria, direct verification evidence, and a completion gate.
- Includes scripts for evidence validation and installation drift checks.

## Install

Clone the repository, then copy or link the whole directory into your host's skills folder.

### Codex

```powershell
git clone https://github.com/wing0828/orchestrate-dev.git "$HOME\.codex\skills\orchestrate-dev"
```

### Claude Code

```powershell
git clone https://github.com/wing0828/orchestrate-dev.git "$HOME\.claude\skills\orchestrate-dev"
```

Restart the host after installation if the skill is not detected immediately.

## Use

Ask the host to use the skill for a substantial software task. For example:

```text
Use $orchestrate-dev to implement this feature, review the diff, and verify the user flow.
```

The skill deliberately avoids external agent frameworks. Delegation happens only through the capabilities supplied by Codex or Claude Code.

## Included tooling

Validate a completion-evidence record:

```powershell
python scripts/validate_evidence.py evals/sample-evidence.json
```

Check whether installed copies match the source directory:

```powershell
python scripts/sync_install.py --check
```

Run `python scripts/sync_install.py --help` for installation and synchronization options.

## Repository layout

```text
SKILL.md                 Main workflow instructions
agents/openai.yaml       Codex-facing metadata
references/              Routing, role, verification, and gate guidance
scripts/                 Evidence validation and installation sync utilities
evals/                   Example scenarios and evidence
```

## License

[MIT](LICENSE)
