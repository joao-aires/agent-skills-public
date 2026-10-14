---
name: test-application-resilience
description: Design, implement, run or review controlled failure tests for application
  journeys, dependency outages, delays, worker loss and resource exhaustion. Use to
  verify bounded failure handling and recovery in an authorized isolated or non-production
  target; choose proportionate fixtures or experiments without requiring a chaos platform.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

# Test application resilience

Verify the promised user outcome when a relevant dependency or component fails, then verify recovery. Use existing test tools and the smallest boundary that answers the question. Keep tests beside the affected application; no chaos service, MCP or Kubernetes operator is required. Use `test-application-performance` for demand/load claims and combine load with a fault only when that interaction is the intended experiment.

## Define the hypothesis and boundary

Read the journey, dependency/worker contracts, accepted deadlines and recovery expectations. Use reliability, observability and recovery guidance when available. State baseline behavior, one failure condition, expected degraded outcome, unaffected paths and the observation that would disprove the hypothesis. Derive limits from accepted requirements; label provisional values. Do not inject faults solely because a tool supports them or prescribe every scenario for a small feature.

Examples: a slow provider produces a bounded error while unrelated reads work; a restarted worker resumes accepted work without repeating a business effect; loss of database access fails mutations without corrupting data and normal operation returns afterward. HTTP success, pod readiness and a green alert alone do not prove these outcomes.

## Choose the least intrusive method

| Method | Useful claim | Limit |
| --- | --- | --- |
| Deterministic fixtures/fake clients | Timeouts, malformed responses, transient/permanent errors, retry limits, authorization and failure presentation | Application handling of simulated failures, not actual network/provider behavior. |
| Isolated application/CI stack | Owned worker termination, controlled dependency unavailability, delayed connections and bounded pool exhaustion with real selected persistence | That stack and fault mechanism, not regional or fleet-wide availability. |
| Named non-production deployment | Actual routing, process lifecycle, collection and recovery interactions | That configuration and authorized scope; shared users and dependencies still matter. |

Match the injection point to the claim. Raising an exception is not the same as dropping a connection after a remote commit. Prefer deterministic controls over arbitrary sleeps. Pin optional proxies/tools and restore their settings; use current platform guidance before constructing target commands.

## Execute within established authority

Routine fixture tests stay within the existing local test scope. A live or shared-environment experiment needs an established target/action policy specifying selected resources, duration, affected users/dependencies, data ownership and side-effect constraints. Preserve authority already granted; do not treat installing this skill as permission to terminate resources. Production experiments require explicit production scope and are not the default.

Check baseline health and observability before injection. Define measurable stop conditions, a reachable stop mechanism, bounded fault lifetime and the expected recovery procedure. Preserve data and control email/payment/model effects. If the target identity, observation or restoration path is missing, return a plan with that blocker rather than execute blindly. Do not initiate an incident or contact responders without the requested authority.

Introduce one controlled fault first. Record actual target/action/time and prove the fault took effect; failure to inject is not a successful resilience result. Observe the original journey, unrelated operations and relevant queues/pools/resources. Check timeouts, backpressure, bounded retries, duplicate effects, cancellation/deadlines and user-visible errors as applicable. Avoid retry storms, indefinite requests and resource leaks; do not add a circuit breaker unless it solves an evidenced requirement.

## Remove the fault and verify recovery

Always attempt restoration through test/workflow cleanup independent of success. Arrange a bounded expiry or external cleanup path when termination could skip teardown. Restore only the resources/settings this experiment changed, preserving concurrent legitimate changes. Do not reset shared data or silently disable unrelated protections.

Verify the actual journey returns, accepted work is accounted for, queues drain appropriately and temporary controls are removed. Review persistent invariants and duplicate/stale effects after recovery. Data loss or an ambiguous external effect remains explicit even when service responsiveness returns. Keep leftover faults or failed cleanup as a blocking result with a concrete handoff; aborting the test does not prove recovery.

## Keep automation and evidence honest

Run stable fixture/isolated checks in relevant CI jobs; pin dependencies, preserve failing exit status and retain sanitized logs/results on failure. Deployed experiments use explicit/manual or project-approved triggers and concurrency controls for the target. No background schedule is installed here. Use `build-delivery-pipelines` for job conventions and environment security.

Report hypothesis, code/config revision, baseline, injected/confirmed fault, intended and observed outcomes, timing, stop/cleanup/recovery evidence and remaining uncertainty. A plan, a simulation, an executed isolated test and a verified deployed experiment are distinct states. Turn demonstrated failures into regression checks or runbook changes; broaden experiments only when new risk justifies them. See [failure experiments](references/failure-experiments.md) for optional tools and deeper cases.
