---
name: test-end-to-end
description: Plan, write, run or debug Playwright end-to-end tests for important user journeys. Use for changes spanning UI/API/database behavior, persistence, authentication, authorization or critical browser interactions, and to investigate failing journey tests.
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Test what users depend on

## Define the claim and boundary

Read acceptance criteria and existing tests. Select the main affected journey and meaningful failure cases; allocate focused logic and combinatorial edge cases to unit/integration tests. Use Playwright for browser behavior. Select available `playwright-cli` expertise for exploration and debugging; keep repeatable tests in the application. An MCP server is optional.

For a full-stack claim, exercise the real frontend, API and migrated PostgreSQL database. Keep external providers replaceable with controlled fixtures in routine CI; report that boundary. A mock API or browser-only demo proves a narrower claim and must be named as such.

## Make outcomes observable

- Assert user-visible results and relevant persisted state, not merely successful clicks, HTTP 200 or the absence of errors.
- Check data survives reload or a new session. Verify update/delete effects rather than trusting an optimistic UI.
- For private resources, use distinct users and test direct access by another user's resource ID, including mutation paths. Hiding a button does not establish authorization.
- Exercise the real authentication path in dedicated auth coverage; reuse authenticated sessions where appropriate for other journeys. Never bypass the behavior the test claims to establish.
- Inspect affected mobile/desktop layouts and keyboard/focus behavior. Include relevant loading, empty, error, validation and permission states; do not rely only on screenshots.

For saved searches, create a named filter as user A, reopen it after reload and assert the restored values, delete it and confirm it remains absent. Use user B to attempt direct read/delete of A's resource; confirm denial and unchanged data. Keep narrower API tests for additional authorization permutations.

## Keep tests trustworthy

Isolate users and data per test or worker and use an explicit test database. Apply migrations, establish service readiness and clean up only owned test data; do not reset an unspecified database. Use semantic locators and observable-state waits instead of fixed sleeps. Keep credentials out of committed fixtures and traces.

Match local and CI configuration. Capture failure traces/screenshots and useful service logs. Reproduce a flaky failure and diagnose state, timing or environment before changing waits; do not weaken assertions or inflate retries to hide it. Keep a small critical journey set fast enough to run routinely.

Report commands, environment, journeys and actual results, plus mocked boundaries and important gaps. If the browser/database environment is unavailable, supply the tests or plan and say execution is blocked; do not claim full-stack verification. Expand coverage when changed risk warrants it rather than duplicating every unit test in the browser.
