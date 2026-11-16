---
name: compliance-readiness
description: Translate applicable legal, contractual and assurance requirements into system boundaries, controls, ownership and evidence. Use for compliance design, GDPR, CCPA/CPRA or SOC 2 readiness, and scoped SaaS assurance assessments including subprocessor, residency, export and deletion evidence.
metadata:
  kind: method
  origin: local
  scope: generic
  invocation: both
  role: support
  phase: cross-phase
  pack: sdlc
  domain: governance
---

# Compliance readiness

Establish applicability before mapping controls. A compliance claim is only useful when the service boundary, obligations, control owner and operating evidence are explicit. This method supports engineering and assessment; it does not certify the service or replace legal or audit judgment.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. Apply the [assurance assessment contract](../artifact-system/references/contracts/assurance-assessment.md) for the durable result.

For writing the artifact this activity produces, read [guide-assurance-assessment](../guide-assurance-assessment/SKILL.md) for structure, conventions and review.

## Establish applicability and boundary

Read the actual service, data flows, contracts, customer commitments, jurisdictions, providers and existing controls. Separate a legal obligation, a contractual commitment and an engineering safeguard. Record unknowns and the owner who can resolve them.

## Reading path

| Need | Read |
| --- | --- |
| General applicability, control derivation and evidence design | [Compliance design](references/compliance.md) |
| GDPR processing, rights, retention and provider consequences | [GDPR](references/gdpr.md) and [applicability notes](references/applicability-and-decisions.md) |
| CCPA/CPRA applicability, consumer rights, sale/share and service-provider terms | [CCPA/CPRA](references/ccpa.md) |
| SOC 2 service commitments, criteria and operating evidence | [SOC 2](references/soc2.md) and [controls and evidence](references/controls-and-evidence.md) |
| SaaS subprocessors, DPAs, residency, export/deletion, audit logs and Type II evidence | [SaaS evidence](references/saas-evidence.md) |

Select only the regimes and evidence types the actual service, cohort and request require. A compliance programme is not the union of every available reference.

## Derive proportionate controls

Map each applicable requirement to the boundary, control, owner, operating frequency and evidence. Distinguish design, implemented, operating and independently examined states. Prefer existing controls and project records; do not create a parallel compliance universe.

## Assess evidence honestly

Check whether the evidence is current, covers the defined population and period, and actually demonstrates the control. Gaps remain gaps; a policy, screenshot or green dashboard does not establish operating effectiveness. Record exceptions, remediation, owner and review date.

For SaaS subprocessor, DPA, residency, export/deletion, audit and Type II questions, use [SaaS evidence](references/saas-evidence.md) rather than treating a trust page or provider report as the service's own control.

## Output

Use the assurance assessment for applicability, scope, controls, evidence, gaps, disposition and owner. Hand engineering changes to the relevant activity and keep certification, legal advice and external submission outside this method unless separately authorized.
