---
name: test
description: Select, add where needed and run checks for the current change or named
  journey, component or application. Use for unit/integration/contract/browser verification
  and relevant performance/resilience checks within the authorized target scope.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Test

Read [task guidance](../../TASKS.md). Resolve the target from the supplied scope/current change and project instructions. Use deliver-reliable-changes to select meaningful checks and existing required suites. Add missing coverage for requested behavior where needed; do not silently alter production behavior, weaken assertions or inflate retries to pass.

Use actual persistence/authorization contracts for full-stack claims, journey-testing for browser journeys, performance-testing for load and resilience-testing for relevant bounded failures. A bare test request does not authorize deployed load or fault injection. Execute supported checks, diagnose failures and distinguish application defects, fixture/environment issues and unexecuted checks. Return results, artifacts, actual boundaries and next action; a green build alone does not establish behavior.


Use deliver-reliable-changes for a scenario-led feedback loop: establish expected outcomes before code, run affected checks and real-platform journey evaluation after meaningful increments, inspect telemetry/state, repair discrepancies and recheck. Broaden regression coverage before completion. Keep accepted criteria and baselines independent of the generated result, and report repeated failures or unavailable execution as blockers instead of inventing success.
