# Role Output Schemas

Require concise outputs in these shapes. Omit fields only when they are genuinely inapplicable.

## Product analyst

```text
Outcome:
Users and use cases:
Acceptance criteria:
Edge cases:
Non-goals:
Open decisions:
```

## Explorer

```text
Relevant paths and symbols:
Current behavior and evidence:
Existing tests and commands:
Constraints and conventions:
Unknowns:
Recommended next boundary:
```

## Architect

```text
Proposed change:
Interfaces and data flow:
Failure behavior:
Compatibility or migration:
Implementation boundaries:
Verification strategy:
Risks requiring lead decisions:
```

## Implementer

```text
Owned files or modules:
Implemented behavior:
Tests added or changed:
Commands executed and results:
Scope deliberately unchanged:
Residual risks or blockers:
```

## Reviewer

```text
Findings by severity with exact evidence:
Acceptance criteria not proven:
Regression or security risks:
Required fixes:
Review verdict: pass | revise | blocked
```

## QA

```text
Environment and surface:
Scenario:
Expected result:
Observed result:
Artifacts or logs:
Verdict: pass | fail | blocked
```

## Lead completion record

```text
Outcome delivered:
Acceptance criterion -> artifact -> verification:
Checks executed:
Review and QA verdicts:
Residual risks:
Required work remaining: yes | no
```
