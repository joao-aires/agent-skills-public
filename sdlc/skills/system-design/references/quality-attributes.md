# Quality attributes in design

Requirements decide which quality attributes matter and what target is acceptable. Design decides how the system will meet those targets, which responsibility it takes on, what it delegates, which tradeoff it accepts and what evidence would show the choice works. Keep those jobs separate: inventing a target in design hides a product decision, and restating a design in requirements hides a technical one.

Use this reference to find the dimensions a change actually touches and to plan the design response. It is a dimension model, not a requirements template: it defines no target, tolerance, owner profile or artifact set. Targets arrive as accepted requirements, or remain explicit unknowns, from [requirements engineering](../../requirements-engineering/SKILL.md) and the [ECR requirements section](../../artifact-system/references/contracts/ecr.md).

## Select dimensions from the change

Start from the affected journey and changed boundary, not from the full list. Ask which dimensions can change the outcome, ownership, failure behavior or operating cost of this change. Two or three usually matter; the rest are genuinely unaffected and need no section in the design.

A dimension is in scope when a plausible design response would differ because of it. "The system should be scalable" is not a selection; "the checkout path must keep its accepted response time when a second payment provider is unavailable" is.

| Dimension | Design question | Where the method lives |
| --- | --- | --- |
| Functionality and correctness | Does the design make the required behavior true, including denial, partial result, duplicate, ordering and state transitions? Where is the authoritative record? | Requirements, [design](../../design/SKILL.md) |
| Reliability | What happens when a dependency fails, returns late or loses recent work? What must remain available for the critical journey? | [Reliability](reliability.md) |
| Performance | How is the response-time target spent across the journey, and what happens at the tail and at saturation? | [Performance](performance.md) |
| Security and privacy | Where is authority enforced, which data crosses which boundary, and what does a provider see? | [Security](security.md) router |
| Maintainability and operability | Where does future change land, and can the system be tested, diagnosed and upgraded without disproportionate risk? | [Maintainability](maintainability.md) |
| Cost | Which resource or provider drives cost per journey or tenant, and what does the chosen design oblige us to keep paying? | [Cost](cost.md) |
| Contextual | Does compatibility, accessibility, compliance or portability apply to this product, contract or environment? | [Contextual attributes](contextual-attributes.md) |

Functionality is not a preliminary to the other dimensions. A design can satisfy a latency target by dropping the confirmation step, or a cost target by weakening a durability guarantee. The other dimensions constrain how functionality is delivered, not whether it is.

## Ownership and delegation

Attribute ownership is a design decision, not an organizational chart. For each in-scope dimension, establish which of these modes applies to each material part of the outcome:

| Mode | What it means | Design must establish | Evidence |
| --- | --- | --- | --- |
| **Owned** | We implement and operate the mechanism and observe the outcome. | Where the responsibility sits, its failure behavior and the operating burden we accept. | Our own measurement of the user outcome, including failure and recovery. |
| **Shared** | Responsibility splits by layer, phase or operation, and no single side controls the outcome. | The seam: who detects, who is paged, who holds the runbook, who may change what, and which failures are attributed to which side. | Evidence from each side of the seam, plus an end-to-end observation that neither side can produce alone. |
| **Delegated to a platform or provider** | We choose, configure and pay for a capability someone else operates. | Contract terms, limits, version and region, failure mapping, credential and data exposure, and the exit path. | Our measurement of the outcome we promise, not the provider's dashboard alone. |
| **External** | Another team, customer, regulator or third party controls it and we cannot change it. | The dependency assumption, the degradation plan and the boundary of what we claim. | The dependency's stated contract or observation, labelled as an assumption. |

- **A provider SLA is not our SLO.** An SLA is the provider's commitment about its own service, usually with credits, exclusions and a monthly window. Our SLO is the outcome our users experience, measured over our population, including the provider's share of failures. Never copy a provider percentage into a user-facing target, and never treat a credit as restored service.
- **Delegation moves mechanism, not accountability.** Using a managed queue, identity service or model provider does not remove our obligation to the user, to the data or to the failure path.
- **Shared needs a seam.** If two sides each assume the other detects the failure, nobody does. Name the signal, the escalation and the authority before accepting a shared split.
- **External dependencies are assumptions, not guarantees.** State what happens when they are slow, unavailable or changed, and what we will tell the user.
- **Unresolved ownership is a finding to return.** Do not assign a provider, team or budget by default to close a design question.

Composition follows from ownership: an end-to-end outcome cannot be healthier than the parts we cannot observe, and it is not the product of the parts' claimed percentages. Reason from the actual dependency graph, correlated failures and the measurement point. Arithmetic belongs to [reliability](reliability.md).

## Design obligations and evidence questions

Each dimension has design work that must be settled before implementation and a question that the planned evidence must be able to answer. The focused references own the depth; these are the obligations this design phase cannot skip.

### Functionality and correctness

- Bind each accepted functional requirement to the operation, state transition or invariant that makes it true, including denied and invalid paths.
- Decide where the authoritative record lives and which derived state may be rebuilt. A cache, index or projection is not the record.
- Name the completion point for asynchronous or multi-step work, and what later work may assume about it.
- **Evidence question:** can an observer distinguish success, legitimate rejection, partial completion and a repeated request without reading the implementation?

### Reliability

- Decide what remains available for the critical journey when each material dependency fails, and how unfinished work is accounted for.
- Choose the indicator, the observation point and the owner for the accepted target; do not derive a target from the design.
- For recovery and continuity, establish the failure domain, RTO/RPO, dependency order and failover authority with [reliability](reliability.md) and its [disaster recovery](reliability-disaster-recovery.md) reference.
- **Evidence question:** does the measured user outcome include work that started and never finished, and is absence of signal treated as unknown rather than healthy?

### Performance

- Allocate the accepted response-time target across the journey's stages and identify which stages run concurrently.
- Model demand and the saturation point, then choose headroom, degradation and scaling behavior.
- Examine tail behavior: retries, timeouts, queueing, cold starts and fan-out.
- **Evidence question:** does the planned measurement exercise the real workload, population and environment at the relevant percentile, and can it distinguish application limits from generator or shared-environment limits?

### Security and privacy

- Place trust boundaries and authority enforcement in the design, including jobs, exports, support tools and AI/tool actions.
- Trace data classes, purpose, recipients, residency and retention across the changed boundary; name what a delegated provider receives.
- Define denial, failure-closed and credential-compromise behavior, and the audit evidence that will exist.
- **Evidence question:** can a denied cross-user or cross-tenant operation be distinguished from a broken one, and does the evidence cover stale authorization as well as a fresh sign-in?

### Maintainability and operability

- Decide where the next likely change lands, which seams it crosses and what would have to be rebuilt.
- Establish test seams, diagnostic signals, deploy/rollback and the upgrade path for dependencies and data.
- Keep the operating burden proportionate: a design that needs constant manual repair has moved cost, not removed it.
- **Evidence question:** can someone who did not write the change locate the responsibility, reproduce the failure and verify a fix from the design and its signals?

### Cost

- Identify the cost driver per journey, tenant or unit of work, and whether it is fixed, variable or stepwise.
- Name the attribution key and the cost consequences of the reliability, performance and provider choices already made.
- State the assumption that would reverse the choice and the exit or switching cost.
- **Evidence question:** is the cost claim connected to measured usage and a defensible rate, with shared and idle cost accounted for rather than hidden?

### Contextual attributes

- Decide applicability explicitly. Compatibility, accessibility, compliance and portability are constraints only when a product, contract, platform or regulation makes them so.
- Record the accepted baseline and who owns it; do not invent a conformance level, jurisdiction or support matrix.
- **Evidence question:** can the claim be checked against the named baseline by someone other than the design author?

## Consume requirement IDs, return unresolved targets

Use the requirement identifiers and acceptance statements the ECR already has. Do not create a second identifier scheme or restate the requirement in design language.

1. Read the accepted requirements and quality constraints relevant to the changed journey. Reuse their IDs verbatim.
2. For each in-scope dimension, record the design response, the requirement it serves, the evidence planned and any gap. Keep this beside the affected decision, not as a new register.
3. When a requirement has no target, do not choose one. State the design consequence under a clearly labelled provisional assumption and return the target question with the options and the evidence that would settle it.
4. When the design cannot meet an accepted target within its constraints, return the conflict: the options, the tradeoff, the cost or risk and the decision owner. Do not silently relax the target or redefine the metric.
5. When new evidence invalidates a target or a design response, mark the affected requirement and dependent work, and reopen the decision.
6. Keep **accepted**, **provisional** and **unknown** distinct in both directions. A design decision is not acceptance of a requirement, and a requirement target is not evidence that the design meets it.

The return is a small set of specific questions, each with the affected requirement ID, the design consequence, the alternatives and who can decide. "Performance is TBD" is not a return; "R-14 sets 300 ms for checkout, the chosen provider adds 180 ms at p95 in the tested region, and the accepted fallback would cost one extra step — product must choose target, region or step" is.

## Tradeoffs and proportionality

Quality attributes compete. Make the competition visible instead of resolving it inside a technical choice:

- availability against consistency and cost;
- latency against durability and freshness;
- security and privacy against data minimization ease and provider convenience;
- maintainability against short-term delivery speed and against premature abstraction;
- portability against leverage from a single platform.

A tradeoff is assessable when it names the affected journey, the two attributes, the accepted target or its unresolved status on each side, the option chosen and the evidence that would reverse it.

Match the depth to the change. A local edit may need one dimension and a sentence of evidence; a new integration or recovery commitment needs the ownership split, the failure path and an exercise plan. Do not produce a complete quality profile, a scoring matrix or a checklist of every dimension for ordinary work.

## Completion evidence

A design is ready to assess when it names the in-scope dimensions, the ownership mode for each material part, the design response, the evidence planned, the unresolved targets and the decision owner for each. Missing dimensions that a reviewer would reasonably ask about are a design gap; missing targets are a requirements gap to return, not a reason to fill in a number.
