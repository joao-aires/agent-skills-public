---
name: journey-testing
description: Define, automate, explore and evaluate user journeys across web, desktop
  and mobile applications. Use for UI/API/persistence changes, interaction and visual
  consistency, authentication, authorization, lifecycle behavior and failing journey checks.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

Read [workflow framing](../../WORKFLOW.md) for skill selection and invocation boundaries.


# Test what users depend on

## Define the claim and boundary

Read acceptance criteria and existing tests. Select the main affected journey and meaningful failure cases; allocate focused logic and combinatorial edge cases to unit/integration tests. Select an actual platform driver using the table below. Use installed tools for repeatable checks and exploratory operation; an MCP is optional. Keep regression tests and representative scenarios in the target application.

For a full-stack claim, exercise the real frontend, API and the application's actual persistence layer, with migrations applied where applicable. Use PostgreSQL when that is the selected stack; preserve an existing database choice. Keep external providers replaceable with controlled fixtures in routine CI; report that boundary. A mock API or browser-only demo proves a narrower claim and must be named as such.

## Select the platform and evidence

| Surface | Starting point | Boundary to verify |
| --- | --- | --- |
| Web | Playwright plus installed browser CLI/MCP for exploration | Actual browsers, responsive sizes, keyboard/focus and relevant role variants |
| Electron | Playwright Electron support where compatible (experimental) | Renderer coverage does not prove native dialogs, packaging, updates or filesystem integration |
| Native desktop | Platform-native automation or an appropriate maintained Appium driver | Named supported OS and packaged application; inspect driver maintenance/limitations |
| Android/iOS | Maestro for suitable flows or Appium/platform-native tooling | Actual emulator/device, lifecycle, permissions, keyboard, offline and supported OS behavior |

A mobile viewport is not a native-mobile test. Maestro's desktop authoring app does not automate arbitrary native desktop applications. Compose can supply backend services; desktop clients and simulators normally run on the appropriate host. Record device/OS/browser/build identities. Test the selected application's real platform; supporting these methods does not add those frameworks to this repository.

Combine a small critical journey suite with component/state checks, visual regression, accessibility evaluation and bounded agent exploration. Use a component-state catalogue such as Storybook when the project benefits from it; it is optional. Stabilize data, rendering environment, fonts, time and animations for visual comparisons; compare against the accepted design and reviewed baselines. A changed screenshot is evidence to investigate, not permission to accept a new baseline. Automated accessibility checks complement keyboard, screen-reader and user evaluation where needed; they do not prove accessibility or usability.

For exploration give the agent a user goal, acceptance criteria, target and allowed actions, rather than only a prescribed click sequence. Inspect real UI/accessibility state, relevant requests, console errors, persisted outcomes and telemetry. Screenshots aid layout judgment but cannot establish saved data, permissions or task success. Preserve useful reproductions and convert discovered regressions into checks at the appropriate boundary. Treat model visual/usability judgments as fallible findings, calibrate against accepted references and human examples, and distinguish observations from subjective suggestions. An agent's positive narrative is not a release gate.

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

For suite upkeep, follow deliver-reliable-changes: temporary flaky-test quarantine has accountable repair and explicit coverage implications. Preserve useful traces and fixture ownership, and remove redundant browser checks only when the affected journey remains established at an appropriate boundary.


## Feed implementation with evidence

Before coding, define the affected scenarios, expected outcomes, relevant surface/state coverage and observable checks. After each meaningful increment run fast affected checks, exercise the changed journey and inspect diagnostics; use deliver-reliable-changes for the repair/recheck loop. Before completion reconcile all in-scope surfaces and run broader required regression checks. Do not run every expensive platform/suite after each edit or let an agent silently change acceptance criteria to fit its output.

For deeper driver setup and evaluation methods use [journey references](references/journey-references.md). Core decisions above should suffice for ordinary work.
