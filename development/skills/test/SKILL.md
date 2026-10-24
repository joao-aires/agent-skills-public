---
name: test
description: Select, add where needed and run checks for the current change or named
  journey, component or application. Use for unit/integration/contract/web/desktop/mobile verification
  and relevant performance/resilience checks within the authorized target scope.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Test

Read [task guidance](../../TASKS.md). Read [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) for evidence and suite health, [journey-testing](../journey-testing/SKILL.md) for changed user journeys. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

## Select meaningful coverage

Identify what the requested change promises and what could break that promise. Inspect the existing tests and project commands before adding another test layer. Select checks that can observe the relevant result, including the previously broken condition for a bug fix and important denial or failure paths for changed behavior.

Use deliver-reliable-changes to select meaningful checks and existing required suites. Prefer the narrowest check that exercises the behavior faithfully, then cross a real integration boundary when a substitute would hide the risk. A test of a component with a fake service can establish its response to that service; it cannot establish that the actual service stores the right result.

Add missing coverage where needed. Keep assertions independent enough to catch a plausible faulty implementation. Diagnose a failing test before deciding whether the application, fixture or environment is wrong; do not silently alter production behavior, weaken assertions or inflate retries to pass.

## Execute and report the actual boundary

Select the evidence for the claim:

| Claim | Relevant boundary and guidance |
| --- | --- |
| Component/state behavior | Journey-testing guidance on Storybook when adopted; building the catalogue alone does not establish interaction coverage. |
| Full-stack behavior | Actual persistence and authorization contracts. |
| Web, desktop or mobile journey | Journey-testing and the actual target platform. |
| Load | Implementation expertise matching the selected load-test tool. |
| Bounded failure and recovery | Resilience-testing. |

A bare test request does not authorize deployed load or fault injection. Execute supported checks and diagnose failures, distinguishing application defects, fixture/environment issues and unexecuted checks.

Return results, artifacts, actual boundaries and the next action. A green build alone does not establish behavior.
