---
name: assurance-assessment-guide
description: Guide to writing a scoped assurance assessment. Covers applicability, service boundary, controls, evidence, gaps, disposition and ownership.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: governance
  phase: cross-phase
  scope: generic
  invocation: both
  role: support
---

# Assurance assessment guide

An assurance assessment records a scoped security, privacy or compliance readiness judgment: what applies, which boundary and controls are in scope, what evidence exists, what gaps remain and who owns the next decision. It is not a certification or an audit opinion.

## Reader questions

1. Which obligation or framework applies, and why?
2. What service, data, provider and organizational boundary is in scope?
3. Which controls are assumed, designed, implemented or operating?
4. What evidence supports each control, for which population and period?
5. What gaps, exceptions or unknowns remain, with owner and next action?
6. What is explicitly outside this assessment?

## Minimum content

- applicability and authority source;
- service, data, provider and organizational scope;
- period, exclusions and assumptions;
- requirements mapped to controls, owners and evidence;
- evidence inspected, population and period;
- gaps, exceptions, residual risk and owner;
- disposition: ready, ready with limitations or blocked;
- what is not claimed.

## Structure and quality

- Establish applicability before mapping controls.
- Separate a legal obligation, a contractual commitment and an engineering safeguard.
- Distinguish design, implemented, operating and independently examined states.
- Check that evidence covers the defined population and period.
- Prefer existing controls and project records; do not create a parallel compliance universe.
- A policy, screenshot or green dashboard does not establish operating effectiveness.
- Name the decision owner and what remains outside the assessment.

## Common failures

- a framework checklist with no service scope;
- claiming compliance without scoped evidence;
- treating a policy as an operating control;
- evidence from the wrong population or period;
- unowned gaps presented as accepted risk;
- conflating readiness with certification;
- no statement of what is not covered.

## Review

Read the assessment as a service owner and a reviewer:

- Do you know what applies and what is in scope?
- Can you trace each requirement to a control and evidence?
- Are gaps and residual risks owned?
- Is the disposition proportionate to the evidence?
- Is the boundary of the claim explicit?

## Handoff

The remediation and decision reader needs applicability, controls, evidence, gaps and disposition. Hand engineering changes to the relevant work; keep certification, legal advice and external submission outside the assessment unless separately authorized.
