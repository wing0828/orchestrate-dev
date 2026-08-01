# Host Adapters

Detect available capabilities from the current host. Never assume a named tool exists.

## Codex

- Use the collaboration mechanism only when the user request and active policy permit sub-agents.
- Assign a concrete bounded task, exact ownership, output schema, and verification command.
- Use read-only explorers for parallel repository discovery.
- Use implementation workers only for non-overlapping files or modules.
- Keep the root agent as delivery lead and final integrator.
- Wait for terminal results before accepting delegated work; do not duplicate a still-running task.

## Claude Code

- Invoke this skill with `/orchestrate-dev` when explicit use is desired.
- Use the current Agent, Task, or background-agent capability only when exposed by the host and allowed by its permission mode.
- Keep one foreground lead responsible for integration and user communication.
- Give background agents non-overlapping ownership and require structured return artifacts.
- Do not bypass Claude Code permissions or broaden allowed tools merely to enable delegation.

## Sequential fallback

When no sub-agent mechanism is available or permitted:

1. Run product and discovery lenses.
2. Freeze acceptance criteria and design boundaries.
3. Implement the smallest slice.
4. Clear implementation assumptions before applying the reviewer lens.
5. Run QA through the real surface.
6. Apply the same quality gates as a delegated workflow.

Sequential role separation is valid; fictional multi-agent dialogue is not.
