# Architecture design: strategic structure

Architecture is the layer that makes later change cheap or expensive. It decides the structure the outcome requires and the commitments everything downstream must respect. It is not a UI component library, not a full implementation blueprint, and not a reason to draw every box in the system.

Read [scope](scope.md) for the boundary with [tactical system design](tactical-design.md) and with the technical owners. If the question is how accepted components behave and fit together, this is the wrong layer.

## When this layer is the decision

Use architecture design when at least one is true:

- a new product, system or externally visible capability needs a structure;
- a boundary moves: service split or merge, data ownership, tenancy, identity authority, provider or platform dependency;
- the choice is expensive to reverse: a public contract, an authoritative data location, a deployment region, a protocol or a vendor commitment;
- an accepted quality attribute cannot be met inside the current structure — regional loss, isolation, latency, residency, throughput;
- several systems, teams or organizations must interact, and the interaction needs an agreed seam;
- the user is explicitly comparing architectural directions.

Do not invoke it for a local change whose boundary is unchanged. A short note beside the affected contract can be the whole architecture response.

## Establish the boundary

Define what the architecture is responsible for before defining components:

- **System in scope.** Which users, journeys, data, systems and teams it serves, and what is deliberately outside. An unstated exclusion becomes an accidental assumption.
- **Ecosystem position.** Upstream suppliers, downstream consumers, providers, identity services, partners and regulators. State which are dependencies, which are delegated and which are assumptions we cannot change.
- **Ownership boundary.** Which component owns each durable fact, who may change it and which failure is contained by the boundary. A boundary that does not contain a responsibility or a failure is only a diagram edge.
- **Trust and data boundaries.** Where authority is enforced and which data classes cross which edge; read [security](security.md) for the depth.

Name the failure domain precisely when continuity or isolation matters: a region, availability zone, account, cluster, primary datastore, identity provider or network path is not "the cloud".

## Name macro components and relationships

Describe components by responsibility, not by framework layer. A useful component has a reason to change independently, an owner and a clear promise to its consumers.

For each material relationship, state:

- direction of dependency and whether the interaction is synchronous or asynchronous;
- what is exchanged — command, query, event, shared data — and who owns it;
- which failures propagate, which are contained, and what the caller may assume after success, rejection or timeout;
- the compatibility and deprecation expectation between the two sides;
- quotas, identity, network reachability and provider boundaries that constrain the interaction.

For system-to-system interaction, the architectural decision is the purpose, authority and failure contract. Protocol-level shape belongs to the protocol owner once the seam is accepted. Use a proposed C4 context or container view for the macro structure and a sequence view only for the interactions a reviewer cannot judge from text; read [C4](../../guide-c4-view/SKILL.md) and [sequence](../../guide-sequence-view/SKILL.md) for structure.

## Decide what is expensive to reverse

Not every choice deserves architecture treatment. Test reversibility by:

- the time and cost to undo it, including migration, redeployment and consumer change;
- the number of dependents and the length of their release cycles;
- data gravity, contractual commitments and provider exit cost;
- the team and operating model it creates;
- whether it becomes a public or partner-visible contract.

Choices that often qualify: the tenancy model, identity authority, placement of the authoritative record, synchronous versus asynchronous seams, a service split, a deployment region, a protocol visible to third parties, and a provider dependency with high exit cost. Record the reversal cost and the condition that would reopen the choice, not only the expected benefit.

Choices that are cheap to reverse should be delegated downward and decided at the system design or implementation depth. Over-specifying reversible detail at this layer creates ceremony without protection.

## Choose monolith, services or distribution

A monolith is the legitimate default until separation buys something specific. Separate a service when it needs independent ownership, independent change cadence, independent scaling or failure isolation, a distinct security or data boundary, or a genuinely different runtime. Service count is not a maturity signal.

Distribution has a standing cost. Make it explicit:

- partial failure and retries that do not exist in-process;
- consistency and transaction boundaries that must become contracts;
- network latency, serialization and deployment coordination;
- duplicated or derived data and its rebuild path;
- contract versioning across independent release cycles;
- a larger operational, observability and debugging surface.

When separating, decide the seam once: authoritative data and its owner, transaction or consistency model, contract and compatibility, retry and idempotency expectations, deployment coupling, failure attribution and team ownership. A split without a seam decision is a distributed monolith.

Use installed architecture-pattern vocabulary to supply and test candidates. A pattern name does not authorize a boundary; the responsibility, failure and cost argument does.

## Align with business and operating model

Architecture serves an accepted business outcome. Connect each major component to the journey or capability it supports, and state the cost and time-to-market consequence of the structure.

- Which team can change and operate each component, and who is on call?
- Does the structure match the decision authority the organization actually has?
- Which budget, vendor, contractual, residency or regulatory constraint shapes the structure?
- What is the migration path from the current system, and what must keep working during it?

State accepted business constraints as inputs. Do not invent a budget, an org design or a compliance obligation to close an architectural question; return it with the options.

## Address quality attributes structurally

Read [quality attributes](quality-attributes.md) to select only the dimensions the change touches. At this layer, decide only those that change structure:

- **Reliability and continuity.** Failure domains, RTO/RPO, dependency order, strategy and failover authority; read [reliability](reliability.md) and [disaster recovery](reliability-disaster-recovery.md).
- **Performance.** Structural choices such as synchronous fan-out, data locality, region placement and isolation; the latency budget and tail detail belong to [performance](performance.md) and [capacity planning](capacity-planning.md).
- **Security and privacy.** Trust boundaries, authority placement, data classes and provider exposure; read [security](security.md).
- **Cost.** Structural cost drivers, fixed versus variable shape, attribution and exit cost; read [cost planning](cost-planning.md).
- **Maintainability and operability.** Whether the structure can be changed, diagnosed and operated by its owners; read [maintainability](maintainability.md).
- **Observability.** Whether the structure can produce the outcome signals its operation depends on; read [observability and monitoring](observability-and-monitoring.md).

Targets arrive from accepted requirements. When a target is unknown, state what the structure does under a labelled provisional assumption and return the decision.

## Compare alternatives and record consequences

For a consequential architectural choice, use the [option set](../../design/references/option-set.md). It owns the method: at least three materially different options, lenses, failure behavior and linked artifacts. Do not restate or replace that method here.

For each option, make the architectural consequence visible:

- the responsibility split and resulting boundary;
- what happens under the failures that matter, including partial and regional loss;
- the hard-to-reverse commitment it creates and its exit cost;
- the operating and team burden it implies;
- the evidence that would demonstrate it works, and the evidence still missing.

Record the recommendation, the rejected alternatives and the revisit trigger in the [design proposal](../../artifact-system/references/contracts/design-proposal.md). When the decision needs its own durable memory, use an [ADR](../../guide-adr/SKILL.md) and link it rather than duplicating the same decision in both places.

## Evidence and completion

Architecture is ready to hand off when:

- the scope, exclusions and ecosystem position are explicit;
- macro components, relationships and ownership are named, with proposed target views where structure is hard to judge from text;
- each hard-to-reverse choice has its alternatives, consequences, reversal cost and revisit trigger;
- the in-scope quality attributes have a structural response, an owner and a target or an explicit unknown;
- distribution, if chosen, has a seam decision and a migration path;
- assumptions about external systems are labelled, and evidence limits are visible.

Prefer evidence that can contradict the design: a bounded spike, a contract probe, provider terms and quota checks, a capacity model, a failure walkthrough or a review of the proposed views. Label demonstrated support, vendor claims and assumptions separately. A diagram, a pattern name or a vendor feature does not establish the structural claim.

Hand the accepted boundaries, commitments and open questions to [tactical system design](tactical-design.md). Route implementation detail to the owners named in [scope](scope.md). Reopen the architectural decision when new evidence contradicts a commitment; do not force a complete redesign for every downstream change.
