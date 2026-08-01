# Quality Gates

Apply gates proportionally to risk. A gate passes only with direct evidence.

## Ready gate

- Outcome and scope are explicit.
- Acceptance criteria are observable.
- Existing behavior and relevant code are located.
- Required authority, credentials, and user choices are available.
- Risks and non-goals are recorded.

## Design gate

- The change follows existing architecture or explains why deviation is necessary.
- Interfaces, data flow, error handling, and compatibility are defined.
- Data or infrastructure changes include migration and rollback considerations.
- Work boundaries are non-overlapping and independently verifiable.

## Implementation gate

- The diff is limited to the requested outcome.
- Error paths and boundary cases are handled.
- Tests cover the behavior at the appropriate layer.
- Secrets, generated files, and unrelated user edits are not introduced or overwritten.

## Review gate

- A reviewer inspected the actual diff, not a summary of it.
- Critical and high-severity findings are resolved.
- Remaining findings are explicitly justified or disclosed.
- Security-sensitive input, authorization, persistence, and external calls received focused review when applicable.

## Verification gate

- Relevant formatting, linting, type checks, and tests were executed where available.
- User-facing changes were exercised through the real surface when practical.
- Failures were diagnosed rather than hidden or waived silently.
- Exact commands and meaningful results are recorded.

## Completion gate

Create a compact evidence map:

| Acceptance criterion | Implementation or artifact | Verification |
|---|---|---|
| Expected behavior | File, component, or output | Test command or observed scenario |

Claim completion only when every required criterion has evidence and no required work remains. If a check cannot run, state why, what was checked instead, and the residual risk.
