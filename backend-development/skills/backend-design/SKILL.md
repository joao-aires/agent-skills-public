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

Establish the observable service behavior and its failure boundaries. Use system architecture expertise when service, client, data or deployment boundaries need architectural decisions; this discipline owns behavior inside and between the selected boundaries. Technical conventions own concrete framework, driver and runtime APIs.

## Establish authority and invariants

Read the intended journey, existing contracts and accepted decisions.

- Identify actors, resource ownership, allowed operations and invariants that must survive failures or concurrency.
- Distinguish authentication from permission to act on each resource, including related resources and worker/tool execution.
- Client controls and model proposals cannot grant server authority.
- Use authority and data-flow assessment expertise for changed trust/data boundaries.

Describe each consequential operation from the caller's point of view. Establish what input is accepted, which current state permits it, what change becomes durable, and what the response promises. An accepted request may mean only that work has been recorded; completion means the promised effect has occurred. Make that distinction visible to callers when work is asynchronous.

Follow what happens if the caller times out, sends the same request again, cancels, or checks progress later. Decide which identity belongs to the logical operation and which belongs to an individual attempt. This lets retries and status checks refer to the same work. Ask about unresolved product choices that change these consequences; investigate implementation facts and choose reversible details within accepted constraints.

## Preserve state under concurrency and failure

Identify the facts that must remain true when requests overlap. Decide which stored changes form one business operation and protect them with the datastore's transaction and constraint mechanisms. A check performed before a write can become stale before the write occurs; verify that the invariant is still enforced when two callers act together.

Keep slow remote calls outside long local transactions when possible. A remote action can succeed even if the local process fails before recording its result, so a local rollback cannot be treated as proof that no external effect occurred. Specify how the application identifies that operation, detects an uncertain result and reconciles it before repeating a consequential effect.

For work that must survive process loss, retain accepted intent, a stable logical identity, progress and a recovery route.

- Assume retries or duplicate delivery where the transport permits them.
- Prevent repeated business effects through durable idempotency and handle ambiguous remote outcomes by reconciliation.
- Lease expiry does not establish that the old worker stopped; prevent stale owners from committing conflicting effects.
- Acknowledge work only after durable progress under the selected transport contract.
- When domain changes and delivery intent must commit atomically, use an outbox or equivalent supported mechanism; dispatch still needs duplicate handling rather than an exactly-once claim.
- Define cancellation races, compensation and exhausted-work handling where they affect correctness.

Best-effort work need not acquire a durable queue without a requirement.

Bound calls, resource consumption, retries and total deadlines according to the journey. Make failures diagnosable without leaking sensitive data. Use relevant reliability/operations guidance for operating objectives and recovery, without introducing a platform solely to fill a checklist.

## Keep contracts useful to consumers

Identify actual consumers and supported versions before changing an API, event or stored representation.

- Compare meaning as well as schema: authority, omitted/null fields, status, order, pagination and error behavior can break callers even when types compile.
- Keep compatibility, migration and recovery consequences explicit.

A rollback of application code does not necessarily reverse a data change.

Describe the affected flow or state/contract in the existing design note or conversation; add diagrams only when they clarify a real uncertainty. Reuse the project vocabulary and accepted architecture. No layer quota, universal service split or document template is required.

## Carry decisions into implementation and verification

Return the proposed/accepted contract, invariants, changed boundaries, unresolved choices and evidence needed. Load relevant technical guidance from the observed inventory for framework APIs, persistence and packaging; absence of Python guidance does not select Python or block another accepted stack.

Use change-verification expertise to exercise successful, denied, failure and recovery outcomes at the appropriate boundary. Include transaction rollback, duplicate effects or restart behavior where affected. Generated types or a transport success cannot establish semantic compatibility. Design-only work ends with the contract and verification needs; implementation remains within the requested activity.
