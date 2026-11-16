---
name: system-design
description: Choose and evolve application architecture from product outcomes, existing
  system evidence and operating constraints. Use after product refinement for a new
  system or before planning a feature that changes service, data, client or integration
  boundaries; avoid architecture ceremony for small local edits.
user-invocable: false
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: development
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Design the system around the outcome

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

For writing the artifact this activity produces, read [guide-design-proposal](../guide-design-proposal/SKILL.md), [guide-c4-view](../guide-c4-view/SKILL.md), [guide-sequence-view](../guide-sequence-view/SKILL.md), [guide-state-machine](../guide-state-machine/SKILL.md) for structure, conventions and review.

Read [quality attributes](references/quality-attributes.md) to find the dimensions a change actually touches, who owns or delegates each, and what evidence would settle it. Then read the applicable dimension reference:

| Dimension | Read |
| --- | --- |
| Reliability, recovery and continuity | [Reliability](references/reliability.md); [disaster recovery](references/reliability-disaster-recovery.md) when a site, region or provider can be lost |
| Latency, throughput, tail behavior, capacity | [Performance](references/performance.md) |
| Security and privacy | [Security](references/security.md), a route to the installed methods |
| Modifiability, testability, operability | [Maintainability](references/maintainability.md) |
| Cost consequence of the design | [Cost](references/cost.md) |
| Compatibility, accessibility, compliance, portability | [Contextual attributes](references/contextual-attributes.md) |

Requirements own the targets. Design owns the tactics, tradeoffs, delegation and evidence plan; return unresolved targets instead of inventing them.

Use this phase after business/product refinement and before dependent implementation planning. Revisit it when a new feature changes boundaries, persistence, identity, integrations, deployment or important quality attributes. For a small change, a brief assessment of the affected contract can be sufficient. Preserve accepted architecture in existing projects.

Read the product context and repository evidence. Use [system-documentation](../system-documentation/SKILL.md) for the current system and seek available security/privacy expertise for authority and data flows. Distinguish the current architecture, proposed changes and unresolved assumptions. Ask about missing product/authority decisions; investigate technical facts and make reversible choices within scope.

## Make decisions the user can assess

### Establish constraints

Start with the journey the system must support and follow the information needed to complete it. Identify who supplies that information, which component owns the durable record, which consumers use it, and which external systems can affect completion. This reveals where trust, consistency and failure need explicit treatment.

Translate quality goals into conditions that influence the design:

- What must remain available when a dependency fails?
- Which data may be lost?
- How quickly does the user need a response?
- Does work continue after the client disconnects?

Include supported clients, offline behavior, synchronization, expected concurrency, budget, deployment environment and the team's operating capabilities where relevant. Distinguish accepted requirements from provisional estimates; unmeasured demand and unknown platform support remain open inputs. For each applicable dimension, note whether the outcome is owned, shared, delegated to a platform/provider or external; a provider SLA does not become our SLO.

### Compare plausible options

Compare options that differ in a consequential responsibility, such as where state is owned, when work completes, or who operates a dependency. Explain how each option serves the journey under normal operation and under the failures that matter. Include the cost of deployment, diagnosis and recovery, not only implementation convenience.

For a consequential choice, use the [option set](../design/references/option-set.md): at least three materially different options from different lenses, with a linked artifact appropriate to the affected [software type](../artifact-system/references/software-types.md). Record the recommendation and the rejected alternatives in the [design proposal](../artifact-system/references/contracts/design-proposal.md).

Recommend the simplest option that satisfies the accepted constraints. A service split should clarify independent ownership or operation; a queue should have a reason for deferring work and a policy for unfinished work; a cache should have an acceptable freshness and failure behavior. Describe what the chosen option makes easier, what it makes harder, and what evidence would cause the decision to be revisited. A named pattern or popular framework does not establish suitability.

Use installed codebase-design for interfaces/test seams and domain-modeling for complex domain concepts.

### Describe the selected boundaries

Cover the affected design:

- System context, service/client responsibilities, deployment boundaries and critical request/event sequence.
- Contracts, authority checks, persistence/transaction ownership, retries/idempotency, failure/cancellation, compatibility and configuration.
- Test seams, diagnostic signals, artifact/release strategy and recovery.

When the boundary joins more than one software type, decide the seam once: contract or data shape, error and denial mapping, auth/tenant boundaries, retry/idempotency, versioning and compatibility. Do not duplicate the seam in each component's design.

Use relevant backend, frontend/native-client, AI and operations guidance when installed. For new apps/services and boundary-changing work, inspect the canonical implemented-state C4 and critical sequences and produce affected **proposed target** C4 and sequence views in the ECR/RFC engineering workspace. An unchanged local boundary warrants an explicit non-impact disposition. Reconcile application current-state docs after verified implementation, not upon design acceptance. A drawing alone is not a design.

### Account for changes between observation and effect

When work depends on mutable external state, establish what can change and which changes invalidate the proposed operation. Compare revalidation/version checks, transactions, serialization or reconciliation according to the platform and required consistency.

Bind resources through identities appropriate to the operation; a mutable label or position may not identify the originally authorized target. Human edits take precedence where the accepted product promises that behavior, rather than through a universal rule that every manual change wins.

Choose recovery from the effects the system can actually observe and reverse. A transaction, resumable operation, compensation, reconciliation or visible partial result can each fit different boundaries. A generated proposal is not evidence that an effect occurred, and a lost response is not evidence that it did not. Define where completion becomes authoritative and what later work may safely assume. Keep the state representation and recovery mechanism proportionate to that responsibility.

### Include application-specific boundaries

| When the application includes | Make these boundaries explicit |
| --- | --- |
| Desktop or mobile clients | Native shell/client responsibilities versus backend services in the accepted stack. |
| AI capabilities | Model/runtime orchestration, AG-UI interaction transport, A2UI rendering and MCP/ACP integrations; verify actual SDK/protocol and harness capabilities before proposing reuse. |
| Existing-session attachment, concurrent edits or voice interruption | The supported contracts for those operations. |

## Verify consequential technical claims

For a critical dependency or integration, verify a coherent version, required capabilities, interoperability, operating limits and usage terms against current primary sources.

- Distinguish demonstrated support, vendor claims, proposed adapters and unavailable behavior.
- Test uncertain contract boundaries with a bounded authorized spike before committing dependent work.
- Examples, starter kits and protocol labels establish only the capabilities/terms they actually cover; verify the component and intended use separately.

Use supported interfaces and the named disposable target for capability checks, following [integration discovery boundaries](../activity-system/references/authority.md#working-boundaries). A proposed adapter or demo cannot establish access to an existing runtime/session. Carry unresolved support into the alternatives comparison.

## Resolve consequential dependency constraints

Use the shared [consequential finding policy](../activity-system/references/authority.md#consequential-findings) to decide when a finding requires the user and which work depends on it. Architecture evidence should connect actual licensing/distribution terms, security/privacy, reliability, cost and platform support to intended personal, internal or commercial use. Keep these checks proportionate to the critical dependency and changed boundary.

- Where a fact or restriction changes an accepted constraint, present supported alternatives and the concrete decision.
- Continue independent work while dependent work waits.
- Preserve the required user capability when reopening architecture; a different technical solution can satisfy it without silently changing the product or accepting new terms/costs.
- Label evaluation spikes separately from production commitments.

Use service-contract design expertise for service state, authority and consumer contracts inside the chosen boundaries. Use installed interaction design expertise and visual design expertise for experience decisions, and AI contract and evaluation expertise for AI/protocol authority and evaluation. Select technical guidance from the accepted stack and actual inventory; an architecture method does not choose a framework by implication.

## Carry the design into delivery

Keep the consequential decisions in the project's existing architecture note or ADRs, with links to evidence and acceptance. Carry them into the implementation plan, interactions, setup, tests and release process. Avoid duplicating the same architecture across documents. Validate uncertain choices with a bounded spike or contract test before committing dependent work; label prototype behavior and untested claims.

Return a recommended/proposed design, meaningful alternatives, material questions and a useful next increment. Design-only authority does not permit feature edits or deployment. Reassess the affected decision when new evidence arrives; do not force a complete redesign for each feature.

For substantive architecture explanations or current/target views, use evidence-backed architecture explanation expertise. Keep architectural decisions separate from explaining structural, runtime, interface and evidence boundaries; a proposed design is not an implemented system.
