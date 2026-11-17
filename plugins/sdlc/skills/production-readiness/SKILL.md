---
name: production-readiness
description: Assess whether a service, launch or material capability change is ready
  to be depended on in production. Use for a scoped readiness review of reliability
  and SLOs, observability and alerts, security and authority, capacity and failure
  behavior, recovery and rollback, runbooks, on-call and support, and open limits,
  without authorizing a release or certifying the service.
metadata:
  kind: activity
  origin: local
  pack: sdlc
  domain: operations
  phase: release
  scope: generic
  invocation: both
  role: task
user-invocable: true
---

# Production readiness

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

Readiness is a claim that named consumers can depend on a named service for a bounded launch, change or resumption. Establish the service or capability, consumers and traffic population, environment, launch mode and requested decision before assessing anything. A new internal service, a public launch, a migration or cutover and a material change to an existing service carry different promises; assess the actual commitment rather than a universal maturity score.

This activity answers "is this service ready to be depended on?" It does not answer "may we perform this release?" or "is this SaaS offering ready for this customer cohort?".

## Separate the readiness questions

| Question | Owner |
| --- | --- |
| May we perform this release, deployment or recovery action? | [release](../release/SKILL.md) |
| Is this service ready to be depended on by these consumers, in this environment, for this launch? | production readiness |
| Is this SaaS offering ready for this cohort and its commercial commitments? | `saas-readiness` |

When more than one applies, production readiness supplies the engineering and operating evidence, `saas-readiness` evaluates the customer and commercial promise, and `release` performs an authorized action. None of them grants authority held by another.

## Establish the readiness claim

Identify:

- the service or capability and the journeys consumers depend on;
- cohort, segments or traffic population, and expected demand;
- target environments, regions, tenants and provider boundaries;
- launch mode: new service, expansion, migration or cutover, material change, or resumption after an incident;
- accepted requirements, SLOs, recovery objectives, support commitments, data classification and open risks;
- the requested decision and its decision owner.

Read accepted requirements, design, threat model, test evidence, runbooks and prior incidents. Reuse existing records rather than re-deriving accepted product decisions. State what would make the answer no before collecting evidence; otherwise a checklist tends to confirm the launch.

## Trace each promise to evidence

| Area | Readiness question | Useful composition |
| --- | --- | --- |
| Reliability and SLOs | Do the accepted journeys have outcome-based indicators, targets, windows and an error-budget policy, and is there evidence they are measured? | [reliability design](../system-design/references/reliability.md), [observability](../observability/SKILL.md) |
| Observability and alerts | Can an operator detect, localize and confirm recovery of the likely failures, with routed alerts, no-data behavior, queries and runbook links? | [observability](../observability/SKILL.md) |
| Security and authority | Do authentication, authorization, tenant/data isolation, secret handling, least privilege, administrative/break-glass access and supply-chain controls hold in the target? | security expertise, [compliance-readiness](../compliance-readiness/SKILL.md) for obligations |
| Capacity and failure behavior | Does measured or modeled demand fit headroom, quotas and dependency limits, and is degradation bounded under saturation, dependency failure and rollout surge? | [capacity and cost](../capacity-and-cost/SKILL.md), [resilience testing](../resilience-testing/SKILL.md) |
| Recovery and rollback | Is application rollback separate from data recovery, and have restore, failover and roll-forward paths been exercised against the accepted RPO/RTO? | [data recovery](../data-recovery/SKILL.md), reliability/DR expertise, [release](../release/SKILL.md) |
| Runbooks, on-call and support | Can a responder detect, escalate, mitigate, verify recovery and reach the support path, and is ownership current for this cohort and environment? | [runbook](../runbook/SKILL.md), [incident response](../incident-response/SKILL.md) |
| Limits and open risks | Which limitations are accepted, by whom, for how long, and what remains outside the claim? | [assurance assessment](../artifact-system/references/contracts/assurance-assessment.md) |

Use [readiness evidence](references/readiness-evidence.md) as a prompt for each area, not as a scorecard.

Match evidence to the claim. A declared control, manifest, architecture diagram, passing pipeline, green dashboard or successful backup job establishes only its own boundary. Distinguish designed, implemented, exercised and observed in the target. An existing service needs observation over a stated window and population; a launch can rely on staging, load, fault and recovery exercises for bounded claims when the environment and limits are named. Missing access or evidence is unknown, not a pass.

Check both success and denial/failure paths where consumers depend on them. One tenant, one replica, one region or one dependency version establishes only that scope. A recent change is a correlation, not proof of the cause or the remedy.

## Make gaps actionable

Classify each material gap before choosing the next action:

| Gap | Distinction to preserve |
| --- | --- |
| Defect | Behavior falls short of an accepted constraint. |
| Unresolved consequential decision | The authorized owner has not settled a choice; proposed risk acceptance remains proposed. |
| Missing execution or access | The relevant outcome remains unverified. |
| Accepted limit | A named owner accepts a specific consequence until a stated review condition or expiry. |

Prioritize by impact and likelihood, exposure and recovery, rather than the number of checked boxes. Give one disposition relative to the next bounded action:

- ready to be depended on for the stated scope;
- ready with explicitly accepted limits;
- not yet ready by evidence.

State blockers, decision ownership, excluded populations and the condition that would change the verdict. Readiness is an evidence-backed assessment, not certification, owner approval or permission to deploy.

## Record and hand off

Use the [assurance assessment contract](../artifact-system/references/contracts/assurance-assessment.md) for a durable scoped judgment: applicability and scope, criteria or controls, evidence, gaps and disposition. Reuse an existing launch review or operations-readiness record and preserve those fields; do not create a parallel artifact type. Read [guide-assurance-assessment](../guide-assurance-assessment/SKILL.md) for the writing conventions of that record.

Keep readiness evidence distinct from release authorization. Update an SLO, runbook, alert or release note only through its owning artifact and authority. Do not relax a target, mute an alert or waive a finding to make the verdict pass. Hand remediation to the owning activity and re-assess after a material change, incident, scale or provider change.

Report the verdict, scope, evidence inspected at its revision/target/window, material gaps and owners, accepted limits, what is not claimed and the next action. State inspected, exercised and observed states separately.

## Composition

- Use [release](../release/SKILL.md) for the authorized release, deployment or recovery action; this activity does not grant it.
- Use `saas-readiness` when customer, tenant or commercial commitments define the cohort; this activity supplies the engineering and operating evidence.
- Use [data recovery](../data-recovery/SKILL.md) and reliability/DR expertise for recovery evidence; an active outage belongs to [incident response](../incident-response/SKILL.md).
- Use [capacity and cost](../capacity-and-cost/SKILL.md), [resilience testing](../resilience-testing/SKILL.md), [observability](../observability/SKILL.md), [runbook](../runbook/SKILL.md) and [test](../test/SKILL.md) for the evidence each owns.
- Use [compliance-readiness](../compliance-readiness/SKILL.md) for legal or contractual obligations and the assurance-assessment contract for the record.

These are optional supports, not prerequisites. Without them, apply this activity's scope, evidence and disposition checks using project records and primary sources; do not invent provider behavior or convert an unavailable specialist into a pass.
