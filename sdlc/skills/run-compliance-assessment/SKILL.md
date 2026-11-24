---
name: run-compliance-assessment
description: Run a scoped assurance assessment of applicable legal, contractual and privacy requirements — establish applicability and boundary, map controls to owners and evidence, and record gaps, disposition and unclaimed scope. Use for GDPR, CCPA/CPRA, SOC 2 or SaaS subprocessor, residency, export and deletion evidence; it does not certify the service or replace legal or audit judgment.
metadata:
  kind: method
  scope: generic
  invocation: both
  phase: cross-phase
  domain: governance
---

# Run compliance assessment

A compliance assessment is a scoped assurance assessment. It records what applies, which boundary and controls are in scope, what evidence exists, what gaps remain and who owns the next decision. It is assurance, named `run-` because it executes a bounded assessment; it does not certify the service, express an audit opinion or replace legal judgment.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. Apply the [assurance assessment contract](../artifact-system/references/contracts/assurance-assessment.md) for the durable result.

For writing the artifact this method produces, read [guide-assurance-assessment](../guide-assurance-assessment/SKILL.md) for structure, conventions and review.

[Design security](../design-security/SKILL.md) owns the engineering protections, [harden](../harden/SKILL.md) owns scoped remediation, and [run-security-maintenance](../run-security-maintenance/SKILL.md) owns credential and vulnerability operations. This skill owns applicability, control and evidence mapping, and the assessment disposition.

## Establish applicability and scope

Read the actual service, data flows, contracts, customer commitments, jurisdictions, providers and existing controls. Separate a legal obligation, a contractual commitment and an engineering safeguard. Record unknowns and the owner who can resolve them.

Fix the period, population, service boundary and exclusions before mapping controls. A framework checklist without that scope is not an assessment.

## Reading path

| Need | Read |
| --- | --- |
| General applicability, control derivation and evidence design | [Compliance design](references/compliance.md) |
| GDPR processing, rights, retention and provider consequences | [GDPR](references/gdpr.md) and [applicability notes](references/applicability-and-decisions.md) |
| CCPA/CPRA applicability, consumer rights, sale/share and service-provider terms | [CCPA/CPRA](references/ccpa.md) |
| SOC 2 service commitments, criteria and operating evidence | [SOC 2](references/soc2.md) and [controls and evidence](references/controls-and-evidence.md) |
| SaaS subprocessors, DPAs, residency, export/deletion, audit logs and Type II evidence | [SaaS evidence](references/saas-evidence.md) |

Select only the regimes and evidence types the actual service, cohort and request require. A compliance programme is not the union of every available reference.

## Assess controls and evidence

Map each applicable requirement to the boundary, control, owner, operating frequency and evidence. Distinguish design, implemented, operating and independently examined states. Prefer existing controls and project records; do not create a parallel compliance universe.

Check whether the evidence is current, covers the defined population and period, and actually demonstrates the control. Gaps remain gaps; a policy, screenshot or green dashboard does not establish operating effectiveness. Record exceptions, remediation, owner and review date.

For SaaS subprocessor, DPA, residency, export/deletion, audit and Type II questions, use [SaaS evidence](references/saas-evidence.md) rather than treating a trust page or provider report as the service's own control.

## Record the disposition

Use the assurance assessment for applicability, scope, controls, evidence, gaps, disposition and owner, including what is not claimed. Hand engineering changes to the relevant activity. Keep certification, legal advice and external submission outside this method unless separately authorized.
