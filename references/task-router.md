# Task Router

Score the task after discovery. Use evidence from the repository, not the wording of the request alone.

## Score dimensions

### Surface area

- 0: One localized file or configuration value.
- 1: A few files in one component.
- 2: Multiple components or layers.
- 3: Cross-system or cross-repository behavior.

### Risk

- 0: Reversible local behavior with no sensitive boundary.
- 1: User-visible behavior or moderate regression potential.
- 2: Authentication, persistence, external calls, or compatibility risk.
- 3: Security boundary, production state, migration, concurrency, or destructive action.

### Uncertainty

- 0: Established pattern and clear acceptance criteria.
- 1: One localized unknown.
- 2: Unclear interfaces or competing designs.
- 3: Unfamiliar system or unresolved product behavior.

### Verification burden

- 0: Static check or focused unit test is sufficient.
- 1: Integration or real-surface scenario is needed.
- 2: Multiple environments, migration, rollback, or security scenarios are needed.

## Select a mode

- Total 0-3: Use compact mode.
- Total 4-7: Use coordinated mode only when at least two work units are independent. Otherwise remain compact and work sequentially.
- Total 8-11: Use critical mode.

Force critical mode for irreversible data changes, authorization boundaries, production mutations, secret handling, or concurrency that can corrupt state.

## Set the coordination budget

- Compact: No implementation delegation. Optional read-only specialist only when it removes a real unknown.
- Coordinated: Use two to four concurrent roles at most. Keep one owner for each file or module.
- Critical: Keep a separate implementer, reviewer, and QA responsibility. Add domain specialists only for a named risk.

If host policy or user intent does not permit delegation, preserve the mode's gates while performing the roles sequentially in the lead agent.
