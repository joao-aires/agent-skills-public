---
name: architecture-patterns
description: >-
  Expertise and methods for backend architecture patterns. Select and compare backend
  architecture patterns — modular monolith, layered, hexagonal/ports-and-adapters,
  clean/onion, CQRS, event sourcing, microservices and serverless — by the forces that justify
  them, their costs and migration path. Use when an architecture proposal or option comparison
  needs pattern candidates, a fit check or a tradeoff review; the architecture decision,
  service behavior, event contracts and cross-service failure reasoning stay with their owning
  capabilities. It informs the activity that composes it; that activity owns the decision and
  stopping point.
user-invocable: true
metadata:
  kind: method
  domain: backend
  phase: design
  scope: generic
  invocation: both
---

# Select patterns from forces, not familiarity

An architecture pattern is a reusable answer to recurring forces. The name is shorthand for a set of boundaries, dependencies and operational obligations; it is not evidence that those obligations fit this system. Pattern selection is the work of matching candidate structures to accepted constraints and naming what each one costs.

This skill owns the pattern vocabulary, fit conditions, tradeoffs, operational consequences and the shape of a migration. It does not own the architecture decision: `design-system` establishes constraints, compares options, selects boundaries and records the decision. `backend-design` owns service behavior, authority, transactions and recovery inside those boundaries. `event-driven-design` owns event and message contracts, including how a projection consumes and evolves them. `distributed-systems` owns cross-service consistency, failure and capacity reasoning. Use this skill to supply and test candidates inside those activities; it does not authorize a pattern.

Pattern-first design reverses the burden of proof: it chooses a familiar name and then invents requirements that justify it. Start with the forces. A pattern that answers no force is decoration, and a pattern whose operational cost exceeds the force it answers is a liability.

## Establish the forces

Read the accepted outcome, current system evidence and operating constraints before naming a candidate. Distinguish measured facts from estimates.

| Force | What to establish |
| --- | --- |
| Ownership and team topology | Which capability and data one team owns, and whether it must deploy and operate independently. |
| Transaction boundaries | Which state changes must commit together, and which may complete later. |
| Consistency | What a read may see after a write, and how much staleness the journey permits. |
| Change cadence | Which parts change or deploy on different schedules, and which must stay in lockstep. |
| Load and latency | Which parts scale independently, and what the end-to-end budget is. |
| Operational capacity | Who runs the system, with what platform, observability, on-call and recovery skills. |
| Cost | The cost curve at expected and peak load, including idle time and recovery capacity. |
| Migration risk | What must remain compatible, and which changes are expensive or impossible to reverse. |

A candidate is worth comparing only if it changes at least one of these forces in a way the journey can observe. Prefer the least structure that satisfies the binding forces. Retaining a modular monolith is a legitimate outcome, not a failure to reach microservices.

## Compare candidates by what they change

For each candidate, state the forces it answers, the transaction and consistency boundary it creates, the ownership and deployment unit it creates, the operational burden it adds, its compatibility and rollback path, and the evidence that would confirm or reopen the choice.

| Pattern family | Patterns | Primary question |
| --- | --- | --- |
| Runtime boundaries | Modular monolith, microservices, serverless | Does independent ownership, deployment, scaling or cost justify a new runtime and failure boundary? |
| Dependency direction | Layered, hexagonal/ports-and-adapters, clean/onion | Does the core need to outlive a framework, replace infrastructure or support multiple adapters? |
| Model separation | CQRS, event sourcing | Is there measured read/write asymmetry, or a concrete replay/rebuild/temporal requirement? |

Read [pattern selection](references/pattern-selection.md) for the full fits/costs matrix, force checklist, coherent combinations, per-pattern evidence and migration consequences.

Patterns combine. A modular monolith can use hexagonal or clean structure inside each module; microservices can use CQRS, event sourcing or serverless per service. Evaluate the combination and its total cost, not the label alone.

## Test the expensive claims

These patterns fail most often because their obligations are discovered after selection.

- **CQRS** can be an in-process read model; a separate broker and store are additional decisions. Add them only when load, shape or ownership requires it, and then own projection lag, rebuild, backfill and duplicate handling. A read-after-write journey needs an explicit freshness path, not an assumption that projections are current.
- **Event sourcing** is a persistence decision with permanent obligations, not an audit feature. A current-state store plus an audit or history log satisfies most audit needs. Require a concrete replay, rebuild or temporal-query need, a deletion and redaction policy, and a tested restore before events become authoritative. Introduce it for one aggregate or bounded context, not the whole system.
- **Microservices** require independent ownership, deployment and data. Services that share a database, must deploy together, or synchronously chain to complete one transaction form a distributed monolith with more failure modes. Split by business capability and data ownership, not by layer or team count alone.
- **Serverless** is a runtime and cost choice, not a synonym for microservices. Check runtime limits, concurrency, cold start, connection handling, per-invocation cost at peak, and the local and CI path before using it for steady high throughput or long-running work.

## Refuse weak justifications

| Claim | Why it is not enough | Ask instead |
| --- | --- | --- |
| "Use Clean/Hexagonal because it is best practice." | Dependency direction pays where the core must outlive frameworks, infrastructure changes or multiple adapters exist. Thin CRUD gains ceremony without a changed decision. | Which adapter or framework is expected to change, and what test or replacement does the boundary enable? |
| "Every service needs DDD, aggregates and domain events." | Domain-driven design addresses complex domain behavior. Applying it to simple CRUD adds translation, consistency and vocabulary cost without a model anyone needs. | Where is the domain complexity, who uses the model, and what decision changes without it? |
| "Split into microservices because there are several teams." | Team count alone creates coordination cost; without data ownership and platform capacity it produces a distributed monolith. | Which team needs independent deployment, scaling or failure isolation, and who funds the platform and on-call? |
| "Use event sourcing so we have an audit trail." | An audit or history log usually provides audit without making events the source of truth and accepting replay, schema history and deletion obligations. | Is replay, rebuild or temporal reconstruction required, and can deletion and schema evolution be supported? |
| "Use serverless or microservices because they scale." | Scaling is a property of a measured bottleneck and cost curve, not of a pattern name. | What scales independently, what is the load profile, and what does it cost at peak? |
| "It is a modular monolith, so boundaries are optional." | Without enforceable interfaces and data ownership, a modular monolith is a layered big ball of mud. | Which module owns each table and decision, and what prevents a cross-module write? |

A distributed monolith is not a staging step to microservices; it is the cost of both models with the benefits of neither.

## Choose, migrate and record

- Compare two or three materially different candidates. Hexagonal, clean and onion share one dependency-direction decision and count as one option, not three.
- Name the first reversible migration step, the compatibility window and the rollback before committing. A change that requires a big-bang rewrite is not ready to select.
- Record the forces, candidates, rejected options, accepted costs, evidence and reopen trigger in the existing design proposal or ECR owned by `design-system`. Do not create a separate pattern-selection artifact or a pattern ADR series.
- State when no pattern is warranted and the current structure is retained. "No change" is a decision with a reason.
- Require structural and behavioral evidence: dependency rules, module or adapter contract tests, independent deployment, failure isolation, projection lag, cost at peak and a rollback drill. A diagram, framework scaffold or successful build does not prove the pattern works.

Read [pattern selection](references/pattern-selection.md) for the full matrix, coherent and contradictory combinations, and per-pattern evidence. Read [migration paths](references/migration-paths.md) before proposing a structural change.

## Composition

| Need | Use |
| --- | --- |
| Architecture constraints, option set, boundaries and the design record | Installed system architecture and design guidance |
| Service behavior, authority, transactions, idempotency and recovery inside a boundary | `backend-design` |
| Event, command and message contracts, ordering, replay and consumer topology | `event-driven-design` |
| Cross-service consistency, failure, capacity and recovery reasoning | `distributed-systems` |
| Framework layering, dependency injection, module tooling and packaging mechanics | The selected stack conventions |
| Design proposal, C4, sequence and state artifacts | The artifact system's design guidance |

The selection reasoning works when these capabilities are absent: keep the forces, costs, migration and evidence explicit in the existing design record. Do not lower the evidence standard because a specialist is unavailable.

## Sources and fit

- [Martin Fowler: MonolithFirst](https://martinfowler.com/bliki/MonolithFirst.html) and [MicroservicePremium](https://martinfowler.com/bliki/MicroservicePremium.html) inform when a monolith is the cheaper starting point and when distribution earns its premium.
- [Martin Fowler: PresentationDomainDataLayering](https://martinfowler.com/bliki/PresentationDomainDataLayering.html) describes layered separation and its limits; [Alistair Cockburn: Hexagonal Architecture](https://alistair.cockburn.us/hexagonal-architecture/) defines ports and adapters; the [Clean Architecture article](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) and [Onion Architecture](https://jeffreypalermo.com/2008/07/the-onion-architecture-part-1/) are variants of the same inward dependency rule.
- [Martin Fowler: CQRS](https://martinfowler.com/bliki/CQRS.html) and [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html) describe the models and their costs; [Domain-Driven Design](https://martinfowler.com/bliki/DomainDrivenDesign.html) frames when domain modeling is warranted.
- [microservices.io](https://microservices.io/patterns/microservices.html) provides a pattern catalogue covering [monolithic architecture](https://microservices.io/patterns/monolithic.html), [database per service](https://microservices.io/patterns/data/database-per-service.html), [CQRS](https://microservices.io/patterns/data/cqrs.html), [event sourcing](https://microservices.io/patterns/data/event-sourcing.html), [strangler application](https://microservices.io/patterns/refactoring/strangler-application.html) and [serverless deployment](https://microservices.io/patterns/deployment/serverless-deployment.html). It states forces and solutions, not fitness for this system.
- [Martin Fowler: StranglerFigApplication](https://martinfowler.com/bliki/StranglerFigApplication.html) and [Sam Newman: Monolith to Microservices](https://samnewman.io/books/monolith-to-microservices/) inform incremental replacement and the distributed-monolith failure mode.
- [AWS Prescriptive Guidance: Decomposing monoliths into microservices](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-decomposing-monoliths/introduction.html) and [AWS event-driven architecture guidance](https://aws.amazon.com/event-driven-architecture/) describe decomposition and integration approaches from one vendor's practice.
- [AWS Well-Architected Serverless Applications Lens](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html) and [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework) inform operational, reliability and cost review; [Google Cloud: Microservices architecture](https://cloud.google.com/architecture/microservices-architecture-introduction) covers decomposition and service boundaries. Verify current limits and service behavior in the selected platform's documentation.

These sources describe patterns and their consequences. They do not establish this project's constraints, authority model, budget or acceptable operational risk; no text is copied. Checked 2026-11-16.
