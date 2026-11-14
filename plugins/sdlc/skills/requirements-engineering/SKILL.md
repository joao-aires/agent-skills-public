---
name: requirements-engineering
description: Elicit, analyze, validate and maintain verifiable functional and quality
  requirements for features, refactors, new systems and architecture changes.
  Use as supporting expertise during refine when stakeholder needs, behavior,
  cross-system constraints or acceptance are materially uncertain.
user-invocable: false
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: development
  phase: requirements
  scope: generic
  invocation: agent
  role: support
---

# Engineer requirements from evidence to acceptance

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

Support the user-facing [refine](../refine/SKILL.md) activity. This skill owns the **quality of requirements analysis**, not product prioritization, solution architecture, implementation planning or a separate mandatory approval process. For a narrow, already-defined correction, use only the applicable checks rather than generating a specification.

## Establish purpose, authorities and what is already known

Read the accepted product outcome, request, current behavior, repository contracts, operational constraints and existing requirements before inventing new ones. For a new system, identify the relevant actors, external systems and intended operating environment instead of pretending there is an implementation to inspect. A company ticket, product brief, user conversation, incident review or migration objective can all be starting evidence; they are not automatically complete requirements.

Identify **stakeholders and decision ownership** in proportion to the change: direct users, operators, maintainers, downstream consumers, security/privacy owners and affected external parties where relevant. Distinguish their observed needs from proposed solutions, opinions and assumptions. Use existing research and decisions first. If stakeholder needs conflict, expose the choice, consequences and decision owner; do not silently optimize for the loudest request or invent approval.

Ask questions that materially change promised behavior, boundaries or acceptable risk. Investigate technical facts from code, contracts and available evidence rather than treating all uncertainty as a user question. Mark unverified assumptions explicitly; an absent stakeholder does not authorize a consequential choice.

## Model required behavior before prescribing a design

Describe the desired outcome as **actor, trigger, allowed preconditions, observable result and durable effects**. For affected journeys, check:

- Identity, authority, ownership, inputs, state transitions and data invariants, including denied or invalid actions.
- Success, partial completion, timeouts, cancellation, retries, duplicate requests, concurrent changes and recovery where consequential.
- External consumers, compatibility, migration boundaries, integrations and the behavior that must remain unchanged.
- Important data lifecycle rules: creation, access, retention, deletion, export and provenance as applicable.

Separate **requirements** (what must hold) from **acceptance evidence** (how we will know) and **design choices** (how it will be implemented). Derive cases from realistic journeys and risks, not a universal error-state checklist. A concise flow or small state table is useful when prose would hide important alternatives.

For refactors, preserve the observable behavioral contract and state explicitly what is allowed to change internally. For rearchitecture or migration, identify interoperability periods, cutover/rollback constraints and the outcomes that prove compatibility; do not confuse an implementation migration plan with a requirement. Incidents can reveal missing recovery, detection or reliability requirements without automatically authorizing a fix.

## Establish measurable quality and operating constraints

In addition to functional behavior, evaluate which **quality attributes** matter for this specific change: performance, availability/reliability, durability, security/privacy, accessibility, usability, observability, resilience/recovery, data correctness, scalability, interoperability, maintainability, deployment and cost. Omit irrelevant dimensions rather than filling a template.

Express an applicable constraint in terms of the affected user/system operation, relevant population/environment, failure or workload conditions and **observable verification**. For latency and availability, distinguish the user-facing operation from a process-level HTTP success and identify denominator, observation point and time window when setting targets. Seek reliability and security specialists where their actual methods matter.

Never invent numeric SLOs, regulatory commitments, owners, workloads or customer promises. State an unresolved target or operating assumption and the evidence/decision required to accept it. Record trade-offs: faster responses may compete with cost; retention with privacy; stronger durability with availability under failure. Do not resolve conflicting quality objectives through a convenient technical choice.

## Analyze, reconcile and validate

Before calling work ready, assess the important requirements for:

| Question | What good evidence looks like |
| --- | --- |
| Need | Each significant requirement traces to an accepted product goal, stakeholder need, operating constraint or verified defect. |
| Clarity | Terms, actors, conditions and states have one usable interpretation; examples expose ambiguity. |
| Consistency | Requirements do not contradict existing policy, data ownership, interfaces, current baselines or each other. |
| Feasibility | Known platform, integration and operational limits are investigated; consequential impossibilities remain visible. |
| Verifiability | A concrete observation/test can distinguish satisfaction from failure, including negative and recovery cases. |
| Coverage | The meaningful journeys, changed boundaries, quality risks and critical unchanged behavior are represented. |

Use examples, counterexamples, boundary conditions and a lightweight walkthrough with relevant stakeholders when the stakes justify validation. Validation checks that the requirements represent the right need; verification checks that the implementation meets them. Passing a unit test cannot by itself confirm stakeholder intent. If a design/feasibility question changes a requirement, return that question and the dependent work; otherwise leave the solution to design.

Maintain a **lightweight relationship** from goals to affected requirements, decisions and acceptance checks. Reuse existing IDs and canonical documents; introduce identifiers or a traceability matrix only when multiple requirements, releases, external obligations or teams need them. When a requirement changes, identify affected design, tests, rollout and operational contracts. Preserve superseded commitments and decision history through the project's existing mechanism.

## Deliver the smallest useful requirements contract

Return enough for `refine` to hand off:

- Intended actors, problem/outcome, scope and notable non-goals.
- Explicit functional and relevant quality/operating requirements with conditions and negative cases.
- Acceptance observations, verification gaps and protected existing behavior.
- Evidence, material assumptions, conflicts, open decisions and the next dependency (design, investigation or implementation).

Distinguish **accepted**, **proposed** and **unknown** requirements. Declare readiness for design or implementation separately: a feature may have clear user behavior and still need an architectural choice before implementation. A short inline issue or conversation can be sufficient for a small change; a longer-lived cross-team contract belongs in an existing authoritative document. Write the requirements contract in the ECR's required requirements section using [artifact-system](../artifact-system/SKILL.md) and authorized [coordination storage](../artifact-system/references/storage/coordination.md). A separate PRD, traceability ledger, ADR or test matrix remains conditional; the standard ECR requirements outcome is not.

### Worked example: data export

Request: "Users can export their data." Clarify which user can request whose data, which records are included, how a permission change affects a pending export, what completion means and how the result is retrieved or expires. A functional requirement might state: *an authorized account member can request an export of their permitted records; a completed export contains only records authorized under the accepted permission policy*. Acceptance checks can exercise allowed and denied membership, content filtering and the observed result. A quality requirement might constrain completion time for an agreed dataset size or define recovery after interruption, but its target is **unresolved until supported by business/operational evidence**. "Use a queue and object storage" is a candidate design, not a requirement.
