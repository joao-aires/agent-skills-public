# Assurance assessment contract: applicability, controls and evidence

An **assurance assessment** records a scoped security, privacy or compliance readiness judgment: what applies, which boundary and controls are in scope, what evidence exists, what gaps remain, and who owns the next decision. It is not a certification, an audit opinion or a promise that a control operates.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the engineering workspace or the established compliance workspace; link the service and control evidence.

## Reader questions

A service owner, security reviewer or auditor must be able to answer:

1. Which obligation or framework applies, and why?
2. What service, data, provider and organization boundary is in scope?
3. Which controls are assumed, designed, implemented or operating?
4. What evidence supports each control, for which population and period?
5. What gaps, exceptions or unknowns remain, with owner and next action?
6. What is explicitly outside this assessment?

## Contract

```markdown
# <Assessment title>

## Applicability and scope
Obligation/framework, service/data/provider boundary, period, exclusions and authority source.

## Controls
Requirement → control → owner → operating frequency → evidence.

## Evidence
What was inspected, at which revision/target, for which population/period, and what it establishes.

## Gaps and exceptions
Gap, impact, owner, remediation, review date and residual risk.

## Disposition
Ready, ready with limitations or blocked; named decision owner; what is not claimed.

## References
Policies, architecture, data flows, provider commitments, tickets and prior assessments.
```

## Maturity

Use **draft**, **assessed**, **accepted** and **superseded**. Keep design, implemented, operating and independently examined states separate. A policy, screenshot or green dashboard does not establish operating effectiveness.

## Review

Can a reader distinguish an obligation from a safeguard, and evidence from assurance? If the assessment only restates a framework checklist or claims compliance without scoped evidence, it is not an assurance assessment.
