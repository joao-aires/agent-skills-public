---
name: postmortem
description: >-
  Facilitate and follow up an incident postmortem: reconstruct evidence, analyse causes and response, derive testable learning actions, and verify that the controls actually work.
metadata:
  kind: activity
  origin: local
  scope: generic
  invocation: both
  role: task
  phase: maintenance
  pack: sdlc
  domain: operations
---

# Postmortem

Use one learning loop for facilitation and follow-up. Reconstruct what happened from evidence, explain the conditions that allowed impact, derive specific actions, and verify the actions on the real target. The review can establish recovery while leaving part of the cause unknown.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

## Choose the mode

- **Facilitation:** build the timeline and evidence ledger, interview only where a gap matters, and draft the review. Read [facilitation](references/facilitation.md) and the [facilitation guide](references/facilitation-guide.md). For proxy/security or detection-gap incidents, use the [worked review](references/proxy-security-review.md) when useful.
- **Follow-up:** turn the supported failure pathway into actions, owners and verification criteria, then track implementation and effect. Read [follow-up](references/followup.md) and the [follow-up guide](references/followup-guide.md).
- **Recurring review:** compare incident histories, action states, overdue controls and recurring patterns. Do not auto-close an action from a ticket status.

## Working rules

- Separate trigger, contributing conditions, propagation, detection, response and recovery. Do not force a single root cause or a fixed five-whys chain.
- Separate confirmed impact from plausible exposure; preserve unknowns and conflicting evidence.
- Keep the review blameless: explain the information and controls available at the time, not individual failure.
- Define actions with a causal rationale, owner, target and observable completion criterion.
- Verify the control on the deployed or intended target: regression/fault test, alert delivery, restore exercise, runbook execution or observed invariant.
- Distinguish proposed, accepted, implementing, locally validated, deployed, outcome-verified, deferred and superseded states.
- Use the [postmortem contract](../artifact-system/references/contracts/postmortem.md) for the durable review and the incident/issue tracker for action tracking.

## Completion evidence

Deliver the postmortem, evidence ledger, unanswered questions, action register, owner states and verification results. Link the source incident and preserve original action age when work moves between tickets. A written or merged action is not proof that the failure mode is controlled.
