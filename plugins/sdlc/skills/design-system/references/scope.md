# Scope: architecture design and tactical system design

This skill is one design method at two depths. It decides how a system is structured, how its parts behave together and what the structure commits us to. It is not a UI component library, a design-token set or a product design system: components, themes and interaction patterns are interface and visual design work.

The two layers below are not phases or maturity levels. They answer different questions, have different primary readers and produce evidence at different resolution.

## The two layers

| Layer | Question | Decides | Primary readers |
| --- | --- | --- | --- |
| **Architecture design** ("what", strategic) | What must exist, who owns which responsibility, and which commitments constrain future change? | Macro and ecosystem scope; hard-to-change structural decisions; major components and their relationships; boundaries; non-functional requirements; business alignment; monolith or microservices; system-to-system interaction. | Architects, tech leads |
| **System design** ("how", tactical) | How do the accepted components behave and fit together closely enough to build, operate and verify? | The concrete blueprint: component behavior, data flows, schema ownership, API interfaces, caching, load balancing, queues, infrastructure shape, resource allocation and deployment topology. | Backend/system engineers, DevOps |

Both layers use the same decision principles, the same evidence standard and the same design record. The difference is the resolution of the question, not the ceremony around it.

## Choose depth by decision

- A choice that changes ownership, an external boundary, a failure domain, a tenancy or identity model, a provider commitment or another expensive-to-reverse structure belongs to **architecture design**.
- A choice about how accepted components exchange data, where a cache sits, how work is queued, how traffic is balanced, how resources are sized or how the deployment is shaped belongs to **system design**.
- A change with one evident local answer and no boundary movement needs neither layer in full; state the affected contract and proceed. Do not produce a strategic section to satisfy a template.
- Start at the layer where the decision lives and descend only when the blueprint is needed to judge or implement it. Do not write both by default.
- Tactical evidence can invalidate an architectural assumption. When it does, reopen the architectural decision instead of patching the blueprint around it.

Architecture sets constraints; system design realizes them; technical owners implement the result. A project may legitimately stop after either layer when that is the requested decision.

## Technical-owner boundary

Design-system owns cross-system decisions and the blueprint. It does not own every implementation detail inside a selected boundary. The split is about decision ownership, not importance: an authoritative-record choice can be architectural while the table that stores it is database design.

| Area | Design-system decides | Technical owner owns |
| --- | --- | --- |
| Service authority, state, transactions and failure inside a boundary | Where the boundary is, what the service is responsible for and what it promises other systems | Service-contract design (`backend-design` when installed): authority, invariants, idempotency, transaction and recovery behavior |
| Protocol contracts | Which system exposes what, to which consumers, and the semantic seam | REST or GraphQL design (`rest-api-design` and `graphql-design` when installed): media types, schemas, status and error mapping, pagination, rate-limit semantics |
| Data and schema | Which fact is authoritative, schema ownership, compatibility window and rebuild path | Database design (`database-design` when installed): logical and physical schema, constraints, indexes, migrations and engine mechanics |
| Infrastructure and delivery | Infrastructure shape, topology, isolation, environments and operational boundary | Infrastructure delivery (`infra-delivery` when installed): IaC, GitOps, drift and delivery recovery; provider guidance for concrete services |
| Provider and platform mechanics | The dependency choice and its failure, cost and exit consequences | Installed provider/platform guidance: service limits, quotas, configuration and pricing mechanics |
| User-facing surfaces | Which user capability the system must serve and the contract behind it | Interface and visual design (`interface-design` when installed): layout, components, tokens and content |

Rules that keep the seam honest:

- Design-system may constrain an implementation detail — "orders are authoritative in the billing service", "consumers may retry", "the cache must tolerate stale entries" — but it does not choose tables, indexes, framework APIs, manifests or provider configuration.
- If a decision cannot be stated without a specific framework mechanism, file or provider API, it is probably implementation detail.
- When a technical owner is unavailable, use project evidence and general expertise, and record the missing depth as a limit rather than inventing the owner's decision.
- The product's own design system (components, tokens, themes) is out of scope even though the words collide. Route that request to interface and visual design expertise.

## Decision table

| Question | Layer | Evidence that settles it |
| --- | --- | --- |
| Does this capability need a separate service, or can it stay inside the existing one? | Architecture | Responsibility and ownership map; independent change, operation or failure argument; rejected alternatives; ADR |
| Which system is authoritative for this record, and what may be derived or rebuilt? | Architecture, then system design for the flow | C4 context/container plus data-flow or sequence; authority and rebuild path; behavior for incomplete work |
| What happens when a region, provider, identity service or primary datastore is lost? | Architecture | Named failure domains, RTO/RPO, dependency order, continuity strategy and exercise plan; ADR |
| How does a request or event move through components, queues and stores? | System design | Sequence and data-flow views with ordering, retries, idempotency and the completion point |
| What is cached, keyed how, for how long, and what happens on a miss, stale entry or cache loss? | System design | Cache policy, freshness and invalidation rule, failure behavior, measurement point |
| Can the accepted peak be served within the latency and reliability targets? | System design, with capacity planning | Demand model, bottleneck and saturation point, headroom, scaling lag; load evidence at the real target |
| What interface do consumers see, and how does it change over time? | System design, then protocol owner | Consumer list, compatibility window, error and denial mapping; contract test |
| What does this cost per tenant or unit of work, and which part is fixed? | Architecture when it changes structure; system design when sizing | Cost driver, attribution key, fixed/variable split, exit cost, measured rate or labelled estimate |
| Where is the signal that this outcome happened, and what does absence mean? | System design | SLI definition, measurement point, population and coverage, missing-data rule; query or test against real telemetry |
| Is a component, token or visual pattern needed? | Out of scope | Interface and visual design expertise; the product's own design system |
