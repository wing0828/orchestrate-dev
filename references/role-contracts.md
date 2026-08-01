# Role Contracts

Use only the roles that add independent value. One person or agent may perform multiple roles in compact mode.

## Delivery lead

- Own outcome, scope, plan, integration, and user communication.
- Resolve cross-role assumptions and prevent duplicate or conflicting work.
- Accept or reject role outputs based on evidence.

## Product analyst

- Translate the request into user-visible behavior, acceptance criteria, edge cases, and non-goals.
- Return a concise behavior contract; do not design implementation details unless necessary.

## Explorer

- Perform read-only repository discovery.
- Return relevant paths, symbols, current behavior, tests, constraints, and evidence.
- Avoid edits and avoid proposing broad redesigns without codebase support.

## Architect

- Define the smallest compatible design, interfaces, data flow, failure behavior, and migration or rollback needs.
- Identify risks and decisions the implementer must not improvise.
- Return a startable design, not a conceptual essay.

## Implementer

- Own explicitly named files or modules.
- Implement the smallest correct change and relevant tests.
- Preserve unrelated edits, follow repository conventions, and record executed verification.

## Reviewer

- Review the actual diff and test evidence independently.
- Rank findings by severity and cite exact files or behavior.
- Report only actionable correctness, security, regression, or maintainability issues.

## QA

- Execute realistic user scenarios on the changed surface.
- Record expected versus observed behavior and reproducible failures.
- Avoid duplicating unit tests when manual or integration evidence is the missing layer.

## Delegation contract

Include the following in every delegated task:

1. Objective and acceptance criteria.
2. Exact file, module, or read-only responsibility.
3. Relevant context and constraints.
4. Expected artifact or response format.
5. Verification command or scenario.
6. Reminder that other collaborators may edit the codebase and their changes must not be reverted.
