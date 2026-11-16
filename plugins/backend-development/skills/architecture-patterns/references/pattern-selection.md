# Pattern selection matrix

Use this reference inside the architecture decision, after the forces are known. It compares structural tendencies; it does not score a system. A high cost can be correct when a binding force demands it, and a low cost does not make a pattern suitable.

## Force checklist

Fill what matters for the journey. Leave a cell unknown rather than guessing, and carry the unknown into the decision.

| Force | Question | More structure indicated when | Less structure indicated when |
| --- | --- | --- | --- |
| Coupling | Which changes must be made together, and which modules can evolve independently? | Independent change cadence is measured, or a boundary is being protected from a volatile dependency. | Most changes touch one capability, or boundaries are still speculative. |
| Transaction boundaries | Which state changes must commit atomically? | Several capabilities must commit together, or the datastore cannot span them cheaply. | Each capability owns its writes and can complete later. |
| Ownership | Who owns the data, the decision and the on-call page? | Ownership is split by business capability, with data each team can defend. | One team owns most of the system, or ownership is organized by layer. |
| Deployment | Which parts must ship independently, and what breaks if they ship together? | Release cadence or failure isolation is a measured constraint. | One pipeline and one release cadence are acceptable. |
| Consistency | What may a read see after a write, and for how long may it be stale? | Strong read-after-write is limited to specific operations, and other reads tolerate staleness. | The journey needs one current view for most operations. |
| Team topology | How many teams contribute, and what coordination is already painful? | Teams are blocked by shared code, shared releases or shared data ownership. | Communication is cheap and one team can review the whole change. |
| Operational cost | Who runs it, and what does idle, peak and recovery cost? | The platform, observability and on-call capacity already exist and are funded. | Capacity is thin, or the workload does not justify a platform. |
| Migration risk | What must stay compatible, and which step is hard to reverse? | Old and new paths can run together behind a stable contract. | The change is internal, or the system can be rebuilt within the accepted window. |

## Comparison matrix

`Low`, `medium` and `high` are relative tendencies for a typical small-to-medium backend, not measurements.

| Pattern | Coupling | Transaction boundary | Ownership | Deployment | Consistency | Team topology | Operational cost | Migration risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Modular monolith | Module interfaces; runtime coupling remains | One local transaction can span modules | One deployable; modules by capability | Single unit | Strong local consistency is cheap | One or few teams; parallel work needs module discipline | Low to moderate: one runtime and pipeline | Low from a monolith; moderate if later split |
| Layered | Layered dependencies that can cut across features | Application/service layer | By layer, not capability | Single unit | Strong local consistency | Conventional; weak parallel ownership | Low | Low: reorganize in place |
| Hexagonal / ports-and-adapters | Core depends on ports; adapters at the edge | Application service or unit of work | Core by capability; adapters by technology | Usually single unit | Strong local consistency | Needs boundary ownership and test discipline | Low to moderate: more code, same runtime | Moderate: introduce ports incrementally |
| Clean / onion | Inward dependency rule; use cases at the center | Use case or interactor | Domain and use-case owners | Usually single unit | Strong local consistency | High discipline; benefits a complex domain | Moderate: mapping, boilerplate, review | Moderate to high if retrofitted wholesale |
| CQRS | Write model to read projections; asynchronous boundary | Write side local; projections eventually consistent | Write owner; read model may have another owner | Same unit or separate projection services | Eventual reads; read-your-writes needs work | Separate read and write ownership is possible, with more coordination | Moderate to high: lag, rebuild, dual paths | Moderate: reversible while reads can fall back |
| Event sourcing | Events are the model; consumers couple to schema | Append per aggregate; cross-aggregate work needs coordination | Aggregate or stream owner | Same unit or separate projections | Eventual projections; per-aggregate serialization | Needs event versioning and replay skills | High: retention, snapshots, replay, redaction, restore | High: hardest to reverse once events are authoritative |
| Microservices | Network contracts; low runtime coupling only if boundaries are real | Per service; cross-service work uses sagas or compensation | One service and data set per owning team | Independent | Eventual across services; explicit | Multiple teams with real ownership plus a platform team | High: observability, on-call, versioning, infrastructure | High: incremental only through strangling or splitting |
| Serverless | Event or HTTP contracts; managed runtime | Per invocation; longer work needs queues or orchestration | Handler or function by capability | Independent handlers | Depends on the store; eventual for events | Small teams with platform guardrails | Low server operations; high vendor and observability dependency | Moderate: extract stateless handlers first |

Read the matrix by row: a pattern can be cheap on one force and expensive on another. The decision is which costs the accepted constraints permit.

## Heuristics by binding force

Start with the simpler structure and escalate only when the force is measured or accepted.

| Binding force | Start with | Escalate when |
| --- | --- | --- |
| Unknown boundaries, small team, strong local transactions | Modular monolith with explicit modules and data ownership | Module ownership or release cadence becomes a measured blocker. |
| Multiple delivery mechanisms, replaceable infrastructure, IO-free core tests | Hexagonal inside the current deployable | The core also needs an independent deployment or scaling boundary. |
| Complex domain rules with a long-lived model | Clean/onion inside the affected module, with domain-driven modeling where the complexity is real | The complexity crosses capability boundaries or needs independent ownership. |
| Read/write asymmetry with tolerable staleness | In-process CQRS projection | Load, shape or ownership requires separate stores or services. |
| Audit, replay or temporal reconstruction is the requirement | Event sourcing for one aggregate or bounded context, with projections for reads | Replay and rebuild are proven and the obligations are funded. |
| Independent ownership, deployment and scaling by capability | Microservices split by business capability, one data owner each | The split is proven by an actual ownership or deployment conflict, not headcount. |
| Spiky or low-utilization event work | Serverless handlers behind the existing contract | Sustained load, long-running work or portability changes the cost model. |
| Simple CRUD with one team | Layered monolith | A force appears that layering cannot answer. |

## Coherent and contradictory combinations

| Combination | Verdict | Note |
| --- | --- | --- |
| Modular monolith + layered + hexagonal or clean | Coherent | Layer inside a module; put ports at module and infrastructure edges. Avoid two competing boundary systems. |
| Modular monolith + CQRS or event sourcing | Coherent, with cost | Keep projections beside the owning module; the monolith still pays replay and consistency obligations. |
| Microservices + database per service + CQRS or event sourcing | Coherent, highest cost | Start with one capability; independent deployment and data ownership must be real. |
| Microservices + shared database | Contradiction | This is a distributed monolith: shared schema, coupled releases and no independent data ownership. |
| Microservices + lockstep deployment for one transaction | Contradiction | Use one service or accept an explicit saga with visible intermediate state. |
| CQRS + immediate read-after-write on an asynchronous projection | Contradiction unless a fallback exists | Provide a synchronous read path, a version check or a product behavior that tolerates lag. |
| Event sourcing + hard deletion with no policy | Unresolved | Decide retention, redaction or crypto-shredding before events become the record. |
| Serverless + long-running or stateful work | Poor fit unless bounded | Check runtime limits and orchestration; do not hide a durable process in a request handler. |
| Clean/onion + thin CRUD | Not contradictory, usually unjustified | The dependency rule adds cost without a boundary or replacement it protects. |

## Evidence per pattern

Evidence has two jobs: show that the force exists, and show that the chosen structure actually delivers it. A framework scaffold, a diagram or a successful build proves neither.

| Pattern | Evidence it is needed | Evidence it works after adoption | What the evidence does not prove |
| --- | --- | --- | --- |
| Modular monolith | A dependency or ownership map shows entangled modules; one deployable is acceptable; local transactions matter. | Module contract tests, a CI dependency rule, single-command deploy, table ownership recorded. | Future independent scaling or team autonomy. |
| Layered | Flows are simple and the team needs a shared orientation; no independent deployment is required. | Layer tests, no pass-through layer, domain logic outside controllers. | Domain isolation or replaceable infrastructure. |
| Hexagonal | At least two adapters or a plausible infrastructure replacement; core tests need to run without IO. | Adapter contract tests, core tests without network or database, one dependency direction enforced. | Deployment independence or team ownership. |
| Clean / onion | Complex domain rules, multiple entry points, or framework churn that the core must survive. | Use-case tests, dependency-rule check, mapping cost measured against changed behavior. | That the domain model matches persistence or that the ceremony pays for itself. |
| CQRS | Measured read/write asymmetry, divergent read shapes, or multiple projections with accepted staleness. | Projection lag measured, rebuild timed, duplicate handling exercised, read-your-writes path tested. | That write contention or domain complexity disappears. |
| Event sourcing | A concrete audit, replay, rebuild or temporal-query requirement, plus retention and deletion decisions. | Rebuild from events, old-schema replay, restore and export tested, projection lag measured, retention cost estimated. | Business correctness or that consumers understand event meaning. |
| Microservices | A measured ownership, deployment or scaling conflict; data ownership separable; platform and on-call funded. | One service deployed without others, failure isolated, data reconciled, contract versions tested, cost measured. | That the organization will use the independence, or that latency and consistency remain acceptable. |
| Serverless | A spiky or low-utilization load profile, event glue, and runtime limits compatible with the work. | Cold-start and concurrency test, peak-cost model, throttling behavior, local and CI path. | That sustained throughput is cheaper or that portability is preserved. |

## Selection record

Record these in the design proposal or ECR owned by the architecture decision; this reference does not create a separate artifact.

- the binding forces, with measured values where available;
- the candidates that differ materially, and why each rejected one fails a force;
- the transaction, consistency, ownership and deployment consequences accepted;
- the operational owner, cost curve and failure behavior;
- the first reversible migration step, compatibility window and rollback;
- the evidence obtained, the evidence still missing and the trigger that reopens the choice.

## Short example

An existing task service is a single deployable with one database. A small team adds saved searches and a tag filter. Reads and writes are symmetric, deployment is not a bottleneck, and no second team owns a capability.

The decision retains the modular monolith and introduces a saved-search module with its own tables and a public interface. Layered structure remains inside the module. CQRS is rejected because there is no measured read asymmetry; event sourcing because there is no replay or audit requirement; microservices because no independent ownership or deployment exists. The record names the reopen trigger: search load or a second team taking ownership of saved searches. This is a pattern decision with a reason, not a preference for monoliths.
