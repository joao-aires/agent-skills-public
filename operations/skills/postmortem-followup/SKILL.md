---
name: postmortem-followup
description: Review incident histories and postmortems to derive, prioritize, implement
  and verify learning actions, track overdue or ineffective fixes, and identify recurring
  failure patterns across incidents.
metadata:
  scope: generic
  invocation: both
  version: '1.1'
  role: task
---

# Postmortem follow-up

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

Start with the supported failure pathway from the incident review. Identify which condition a proposed action changes and why changing it should prevent recurrence, improve detection or reduce harm. This keeps the action tied to the incident's mechanism instead of turning the follow-up into a general backlog of desirable improvements.

Define how the control's effect will be observed before closing the action. Check that it reached the intended target and that the relevant behavior was exercised. If the same failure returns, investigate whether the action was incomplete, undeployed, bypassed, ineffective or based on an assumption that changed. A written, merged or closed action does not settle those questions.

## Modes and inputs

- **Interactive:** help owners choose actions based on the failure pathway and assess whether the proposed control will work.
- **Implementation:** make a scoped fix, telemetry/test/runbook change or rehearsal tied to an action's success criterion.
- **Recurring review:** compare action registers, code/config/runtime evidence and new incidents; update existing IDs, flag overdue/unverified controls and prepare bounded improvements. Do not auto-close actions from issue status alone.

Gather reviewed incident evidence, action history, owners, deadlines and applicable implementation scope. Preserve proposed versus accepted ownership and documented exceptions. Consult [the follow-up guide](references/followup-guide.md) for deeper implementation details when needed.

## Workflow

1. Reconstruct the supported failure and response gaps from the history. Identify unaddressed mechanisms and duplicate/related actions across incidents.
2. Propose correction, prevention, detection, mitigation/recovery, evidence-gathering and temporary-control cleanup actions where justified.
3. Prioritize by expected harm/risk reduction, recurrence likelihood, response cost, dependencies and implementation effort. Do not invent numeric confidence or savings without a method.
4. Define owner, tracking ID, due/review date, affected targets, causal rationale and verification criterion. Replace vague “improve” actions with observable changes/tests.
5. Check existing implementation before adding work. Prepare/apply changes within assigned authority using appropriate tests and delivery validation.
6. Verify the control on the deployed/intended target: regression/fault test, alert delivery, restore exercise, runbook execution, or observed invariant as applicable.
7. Compare new incidents with prior controls: not implemented, not deployed, not exercised, ineffective, bypassed, or changed assumptions are different findings.
8. Publish a follow-up report with stable action states and escalation of overdue material risk under local policy.

Check that action tables/search results actually relate to the incident, especially when items predate it or come from a shared tracking query. Preserve incident -> review -> action relationships and accepted ownership. Closure automation and tracker labels provide navigation, not proof of implementation or effect.

## Completion evidence

Use proposed, accepted, implementing, locally validated, deployed, outcome verified, deferred or superseded states. Keep source incident links and original age when actions move between tickets. Close only with the stated success evidence or an explicit accountable disposition; keep residual risk visible.
