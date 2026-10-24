---
name: saas-readiness
description: Assess a SaaS launch, customer rollout or capability expansion against
  actual commitments and operating evidence. Use for a scoped readiness verdict and
  prioritized gaps, without assuming every enterprise feature or authorizing release.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: ../../references/sources.md
user-invocable: true
---

# Assess readiness for the intended customers

Establish the proposed release/customer cohort, promises, supported journeys, environments and requested decision. Reuse accepted requirements, risk decisions and verification records. A personal pilot, self-service subscription and enterprise deployment have different needs; assess the actual commitment rather than a universal maturity score. Read the [source review](../../references/sources.md) for illustrative starters and their evidence limits.

## Trace commitments to evidence

Turn the proposed customer commitment into journeys that must work for that cohort. Follow each consequential promise through the implementation, the checks performed, and the person or procedure responsible when it fails. This exposes the difference between a feature being present and a customer being able to depend on it.

Assess the evidence at the same scope as the promise. A successful test for one tenant does not establish isolation from another; a recovery procedure does not establish that restoration has been exercised. Identify the missing observation instead of replacing it with a broader confidence statement.

- Include applicable onboarding, tenant/access isolation, commercial state, useful dashboard/admin behavior, recovery, support and offboarding.
- Identify whether evidence is inspected configuration, a passing component check, a persisted integration journey, a production observation or a proposed procedure.
- Avoid converting an absent specialist or an unexecuted check into a pass.

Assess provider dependencies, abuse/quotas, privacy/licensing obligations, artifact/configuration identity, migration/cutover and rollback/forward recovery where they affect the cohort. Seek matching specialists when available; use project evidence and primary sources otherwise. Do not create new customer promises merely because a reference project includes a feature.

## Make gaps actionable

Classify each gap before choosing the next action:

| Gap | Distinction to preserve |
| --- | --- |
| Defect | Behavior falls short of accepted constraints. |
| Unresolved consequential decision | The authorized owner still needs to settle a choice; proposed risk acceptance remains proposed. |
| Missing execution or access | The relevant outcome remains unverified. |

For each material gap, explain the affected promise, evidence, consequence and smallest useful next action. Prioritize by impact and likelihood, exposure and recovery, rather than number of checked boxes.

Give one scoped verdict:

- Supported for the stated cohort.
- Supported with explicitly accepted limits.
- Not yet supported by evidence.

State blockers and uncertainty; readiness is not certification or permission to deploy. Carry material learning into existing product/design/operating records without a new tracker or document ceremony. Execute fixes only within the requested scope.
