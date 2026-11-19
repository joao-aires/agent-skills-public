# Tactical design: the concrete blueprint

System design turns accepted boundaries into a blueprint that is concrete enough to build, operate and verify. It answers "how do these components behave and fit together?" without taking ownership of the code, schema, manifest or provider configuration that implements the answer.

Read [scope](scope.md) for the technical-owner boundary before deciding how far to go. If the decision changes ownership, a failure domain or another expensive-to-reverse commitment, return to [architecture design](architecture-design.md).

## When this layer is the decision

Use system design when:

- architecture is accepted, or the current boundary is explicitly unchanged;
- a feature introduces a new runtime path: a request, job, event, integration or deployment step;
- behavior depends on ordering, retries, caching, queueing, load balancing or resource limits;
- a new store, queue, cache or infrastructure shape is added inside existing boundaries;
- the team needs the data flow, schema ownership, interface seam or deployment shape settled before implementation.

Do not produce the full blueprint for a local change. Name the affected flow, state or contract, and the one or two views that let a reviewer judge it.

## Build the blueprint

For each element, the design decides the policy, boundary or shape. The technical owner decides the mechanism and writes it. Evidence is the smallest artifact that lets someone else check the decision.

| Blueprint element | Design-level decision | Evidence | Implementation owner |
| --- | --- | --- | --- |
| Component behavior | Operations and state transitions; the completion point; what a caller may assume after success, rejection or timeout; retry, idempotency and concurrency behavior | Sequence view for the critical path; state machine where states and transitions matter | Service-contract design (`backend-design` when installed) |
| Data flow | Producers and consumers; the authoritative record; derived state and its rebuild path; ordering, freshness and retention across the flow | Data-flow or sequence view; ownership list; incomplete-work behavior | Service-contract and database design |
| Schema ownership | Which store owns which fact; identity and keys; migration and compatibility window; what may be reconstructed | Data ownership map; compatibility statement; rebuild path | Database design |
| API boundary | Which operations are exposed, to which consumers, under which authority; error and denial mapping; idempotency; pagination and versioning expectations | Contract view and consumer list; contract test or bounded probe | REST or GraphQL design |
| Caching | What is cached and why; key and scope; freshness and invalidation rule; stampede and cold-start behavior; stale or cache-loss behavior | Cache policy beside the flow; measurement point and failure walkthrough | Backend/runtime and platform guidance |
| Load balancing | Where balancing happens; health check and draining behavior; session affinity; zone or region topology; failure detection | Deployment or topology view; failure walkthrough | Infrastructure and platform guidance |
| Queues and asynchronous work | Purpose of deferral; delivery and ordering expectations; retry, backoff and dead-letter policy; duplicate handling; backpressure; completion and reconciliation | Sequence plus state view; unfinished-work policy | Event or message-contract design, service-contract design |
| Infrastructure shape | Compute, storage, network and managed services; isolation and environments; quota and provider boundaries; stateful versus stateless placement | Deployment view; dependency and quota list | Infrastructure delivery and provider guidance |
| Resource allocation | Replica and pool counts; concurrency; CPU/memory classes; connection and storage limits; what is reserved for peak and recovery | Capacity model with demand assumptions; saturation point | Capacity analysis and platform guidance |
| Deployment topology | Regions and zones; blast radius; rollout and migration order; rollback and roll-forward; stateful migration boundary | Deployment view; migration and rollback sequence | Infrastructure delivery and delivery pipelines |
| Instrumentation points | Which signal is emitted at which stage; population and identity; what absence means; where correlation crosses a boundary | Signal contract per stage; query or export-boundary check | Instrumentation implementation with [observability and monitoring](observability-and-monitoring.md) |

A blueprint usually needs three or four of these, not all eleven. Choose the rows the change actually touches.

## Keep decisions at design level

The boundary is decision ownership, not abstraction for its own sake. State the consequence the rest of the system depends on; leave the mechanism to its owner.

| Design-level statement | Implementation detail for the owner |
| --- | --- |
| "The order service owns the order record; completion is recorded after the durable commit." | Table shape, indexes, isolation level and transaction API. |
| "Consumers may retry; the operation is idempotent by a caller-supplied request key." | Header, field or endpoint mechanics and framework middleware. |
| "Product metadata may be cached for a short interval and served stale during a dependency failure." | Cache product, key format, TTL syntax and client configuration. |
| "Two replicas across zones, drained before termination, with a recovery path when one zone is lost." | Manifest, autoscaling policy, probe timings and provider configuration. |
| "The queue exists to defer non-interactive work; failed work reaches an inspectable dead-letter state." | Broker choice, queue declaration, retry count and monitoring configuration. |

If a decision cannot be stated without a framework mechanism, file or provider API, it is probably implementation detail. Route it to the owner named in [scope](scope.md), and keep the design statement that constrains it.

## Preserve the accepted architecture

Before adding a store, queue, cache, service or region, check that it fits the accepted boundary and ownership. A tactical convenience that quietly changes the authoritative record, introduces a second writer or creates a new cross-system dependency is an architectural change in disguise; reopen the decision instead of hiding it in the blueprint.

When several components meet, decide the seam once: contract or data shape, error and denial mapping, authority and tenant boundary, retry and idempotency, versioning and compatibility. Do not let each component section invent its own version.

If a tactical choice is itself consequential — a cache that can serve another tenant's data, a queue whose duplicate delivery changes billing, a deployment topology that cannot meet the recovery objective — use the [option set](../../design/references/option-set.md) for that choice. It owns the method; this reference owns the blueprint around it.

## Evidence

Match the artifact to the question:

| Question | Evidence that can settle it |
| --- | --- |
| Does the behavior complete, fail and retry as promised? | Sequence view plus a state machine for the states that matter; a contract test or bounded probe where uncertain. |
| Is the authoritative record unambiguous? | Data-flow view and ownership list; a walkthrough of concurrent or partial failure. |
| Can consumers keep working across a change? | Consumer list, compatibility window and an error/denial mapping; contract test. |
| Does the cache, queue or load balancer degrade safely? | Written policy plus a failure walkthrough; measurement point that would show the behavior. |
| Can the deployment meet its recovery and capacity objectives? | Deployment view, capacity model, dependency and quota check; load evidence at the real target where required. |
| Can an operator tell success from failure? | Signal contract and a test against real telemetry; read [observability and monitoring](observability-and-monitoring.md). |

Read [performance](performance.md) for the latency budget and tail behavior, [capacity planning](capacity-planning.md) for demand, headroom and scaling, and [reliability](reliability.md) for outcome targets and error budgets. This reference decides the blueprint that those targets imply; the measured study and its arithmetic belong to the capacity and cost method.

A drawing alone is not a design. A passing contract probe does not establish production behavior, and a deployed component is not evidence that the blueprint was understood.

## Completion evidence

The tactical blueprint is ready when:

- the affected flows, components and stores are named, and unaffected ones are stated or excluded;
- component behavior has a completion point, failure behavior and retry or idempotency expectation;
- each durable fact has one owner, and derived state has a rebuild path;
- the interface seam, cache, queue and load-balancing policies are explicit enough to implement without guessing;
- infrastructure shape, resource allocation and deployment topology match the accepted capacity and recovery objectives;
- the signal contract covers the outcomes an operator must distinguish;
- every remaining implementation detail has a named owner, and unresolved decisions are returned rather than invented.

Record the blueprint in the existing design proposal or architecture note, with proposed target views where the structure is hard to judge from text. Do not create a parallel document per element. Hand implementation to the technical owners and keep the design statement they must preserve; update the blueprint when verified implementation or new evidence changes a decision.
