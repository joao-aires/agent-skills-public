---
name: backend-design
description: Define application-service behavior, authority, state and interface contracts independently of a framework. Use for APIs, durable jobs, stored data or integration changes before dependent implementation; preserve accepted behavior for local fixes.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Define backend behavior before choosing implementation details

Establish the observable service behavior and its failure boundaries. Use [system design](../system-design/SKILL.md) when service, client, data or deployment boundaries need architectural decisions; this discipline owns behavior inside and between the selected boundaries. Technical conventions own concrete framework, driver and runtime APIs.

## Establish authority and invariants

Read the intended journey, existing contracts and accepted decisions. Identify actors, resource ownership, allowed operations and invariants that must survive failures or concurrency. Distinguish authentication from permission to act on each resource, including related resources and worker/tool execution. Client controls and model proposals cannot grant server authority. Use [security and privacy design](../security-and-privacy-design/SKILL.md) for changed trust/data boundaries.

Define relevant state transitions, public inputs/outputs, validation and failure semantics. Separate accepted intent, durable progress and completed effects. Identify what callers can retry, cancel, recover or observe. Ask about unresolved product choices that change these consequences; investigate implementation facts and choose reversible details within accepted constraints.

## Preserve state under concurrency and failure

Choose the atomic business operation and its commit boundary. Related changes must preserve invariants together; enforce durable uniqueness or other constraints where races matter. Keep slow remote calls outside long local transactions when possible. A remote effect and a local commit are separate failure boundaries.

For work that must survive process loss, retain accepted intent, a stable logical identity, progress and a recovery route. Assume retries or duplicate delivery where the transport permits them. Prevent repeated business effects through durable idempotency and handle ambiguous remote outcomes by reconciliation. Lease expiry does not establish that the old worker stopped; prevent stale owners from committing conflicting effects. Acknowledge work only after durable progress under the selected transport contract. When domain changes and delivery intent must commit atomically, use an outbox or equivalent supported mechanism; dispatch still needs duplicate handling rather than an exactly-once claim. Define cancellation races, compensation and exhausted-work handling where they affect correctness. Best-effort work need not acquire a durable queue without a requirement.

Bound calls, resource consumption, retries and total deadlines according to the journey. Make failures diagnosable without leaking sensitive data. Use relevant reliability/operations guidance for operating objectives and recovery, without introducing a platform solely to fill a checklist.

## Keep contracts useful to consumers

Identify actual consumers and supported versions before changing an API, event or stored representation. Compare meaning as well as schema: authority, omitted/null fields, status, order, pagination and error behavior can break callers even when types compile. Keep compatibility, migration and recovery consequences explicit. A rollback of application code does not necessarily reverse a data change.

Describe the affected flow or state/contract in the existing design note or conversation; add diagrams only when they clarify a real uncertainty. Reuse the project vocabulary and accepted architecture. No layer quota, universal service split or document template is required.

## Carry decisions into implementation and verification

Return the proposed/accepted contract, invariants, changed boundaries, unresolved choices and evidence needed. Load relevant technical guidance from the observed inventory for framework APIs, persistence and packaging; absence of Python guidance does not select Python or block another accepted stack.

Use [change verification](../deliver-reliable-changes/SKILL.md) to exercise successful, denied, failure and recovery outcomes at the appropriate boundary. Include transaction rollback, duplicate effects or restart behavior where affected. Generated types or a transport success cannot establish semantic compatibility. Design-only work ends with the contract and verification needs; implementation remains within the requested activity.
