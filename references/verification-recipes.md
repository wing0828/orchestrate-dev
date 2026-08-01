# Verification Recipes

Select recipes by changed surface. Combine only the relevant checks.

## Shared baseline

- Run focused tests for changed behavior.
- Run formatting, linting, type checks, and broader tests when configured and proportional to risk.
- Inspect the final diff and repository status.
- Record exact commands and meaningful results.

## Web UI

- Exercise the real route in a browser.
- Verify loading, empty, error, and success states.
- Check keyboard use, focus, responsive layout, and console errors when relevant.
- Capture a screenshot or other surface evidence for visual changes.

## API or service

- Verify success, validation failure, authentication, authorization, and dependency failure paths.
- Check response shape, status codes, idempotency, timeouts, and retries where applicable.
- Confirm logs do not expose secrets or sensitive payloads.

## CLI or automation

- Verify exit codes, stdout, stderr, help output, and invalid input.
- Test paths containing spaces and platform-specific behavior when supported.
- Confirm reruns are safe when idempotency is expected.

## Persistence or migration

- Test clean creation and upgrade from a representative prior state.
- Verify existing data remains readable and constraints remain valid.
- Exercise rollback or document why rollback is impossible.
- Back up material data before an authorized destructive migration.

## Authentication or security

- Test anonymous, valid, expired, malformed, and insufficiently privileged identities.
- Verify server-side authorization rather than UI-only restrictions.
- Check input boundaries, secret handling, audit behavior, and abuse controls.

## Concurrency or asynchronous work

- Test duplicate delivery, retries, cancellation, ordering, and partial failure.
- Verify state transitions are atomic or safely recoverable.
- Look for leaked tasks, deadlocks, and unbounded retries.

## External integration

- Use mocks or sandboxes for deterministic checks, then perform a safe real integration check when authorized.
- Verify rate limits, pagination, authentication failure, schema drift, and timeout behavior.
- Avoid sending external messages or mutating production state without explicit authority.
