---
name: orchestrate-dev
description: Orchestrate complex software delivery through explicit product, architecture, implementation, review, and QA roles without invoking an external agent framework. Use when a build, feature, refactor, integration, migration, or bug fix spans multiple components or disciplines, contains material uncertainty or risk, or is explicitly requested as a coordinated multi-agent workflow. Do not use for explanations, read-only reports, or tiny isolated edits.
---

# Software Delivery Orchestrator

Deliver software through one accountable lead and a right-sized virtual team. Use the host's own capabilities and optional sub-agent mechanism. Do not invoke MetaGPT or another model API.

## Route the task

Read [references/task-router.md](references/task-router.md) after initial discovery and select exactly one mode:

- **Compact:** Keep one agent and apply the role lenses sequentially.
- **Coordinated:** Delegate only independent, non-overlapping work with explicit ownership.
- **Critical:** Separate implementation, review, and QA responsibilities and require risk-specific evidence.

Treat the selected mode as a budget, not a target. Collapse roles whenever separation adds no independent value.

## Load only the needed guidance

- Read [references/role-contracts.md](references/role-contracts.md) and [references/role-output-schemas.md](references/role-output-schemas.md) before assigning roles.
- Read [references/host-adapters.md](references/host-adapters.md) only when delegation is permitted and useful.
- Read [references/verification-recipes.md](references/verification-recipes.md) before defining the verification plan.
- Read [references/quality-gates.md](references/quality-gates.md) before claiming completion.

## Run the delivery loop

### 1. Frame

- Restate the requested outcome, scope, constraints, and non-goals.
- Distinguish explanation, diagnosis, and implementation authority. Do not implement when only diagnosis was requested.
- Derive observable acceptance criteria. Ask only for choices that materially alter the result or require new authority.
- Inspect repository instructions and preserve unrelated user changes.

### 2. Discover

- Locate relevant code, tests, configuration, owners, and established patterns.
- Establish current behavior with direct evidence before designing a change.
- Verify unstable technical facts against primary documentation when research is needed.
- Identify dependencies, unknowns, and risk boundaries, then route the task.

### 3. Design

- Define affected interfaces, data flow, failure behavior, compatibility, and verification strategy.
- Prefer existing abstractions and conventions over parallel systems.
- Split work only at independently verifiable boundaries. Assign one owner per file or module.
- Use a lightweight task plan. Create persistent planning documents only when requested or required by repository convention.

### 4. Execute

- Keep the lead responsible for scope, integration, and user communication.
- Give each delegated role a bounded objective, exact ownership, inputs, output schema, and verification command.
- Tell collaborators they are not alone in the codebase and must preserve others' edits.
- Parallelize read-only discovery and non-overlapping implementation only when host policy permits it.
- Integrate continuously and resolve interface disagreements before additional implementation.

### 5. Review and verify

- Review the actual diff for correctness, regressions, security, maintainability, and scope creep.
- Run the narrowest relevant checks first, then broader checks proportional to risk.
- Exercise real user scenarios for UI, CLI, API, persistence, integration, or migration changes.
- Fix material findings and rerun affected checks. Never report a check as passing unless it ran successfully.
- If the same blocker survives two review cycles, reassess the design or request the smallest missing decision.

### 6. Gate and hand off

- Map each acceptance criterion to an implementation artifact and direct verification evidence.
- Confirm no required work remains and disclose every unverified area or residual risk.
- Lead with the delivered outcome, then summarize verification and the minimum useful next step.
- Do not commit, push, deploy, message third parties, or perform destructive operations unless authorized.

## Keep coordination real

- Produce decisions, artifacts, diffs, and test evidence, not fictional role dialogue.
- Prefer one implementer plus one independent reviewer over many agents touching the same surface.
- Stop delegation when coordination cost exceeds its expected benefit.
- Use `scripts/validate_evidence.py` when a machine-checkable completion record is useful.
- Use `scripts/sync_install.py --check` to detect drift between the source skill and host installations.

## Handle blockers

- Exhaust safe, in-scope diagnostics and alternatives first.
- Stop for credentials, destructive authority, an external decision, or a material scope expansion.
- Report the exact blocker, evidence, completed work, and smallest decision needed to continue.
