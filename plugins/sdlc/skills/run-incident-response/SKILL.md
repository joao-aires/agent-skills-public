---
name: run-incident-response
description: Coordinate and investigate active service incidents using impact-led
  triage, reversible stabilization, causal evidence, escalation, communication and
  independent recovery verification. Use for live or authorized unattended response,
  not readiness exercises, recurring review or durable repair.
metadata:
  kind: activity
  domain: operations
  phase: maintenance
  scope: generic
  invocation: both
  version: '1.0'
---

# Run incident response

Reduce current user harm and preserve enough evidence to make the next decision, and stop at a supported mitigation or an explicit handoff.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. Use the [incident record contract](../artifact-system/references/contracts/incident-record.md) for the durable record. For writing the artifact this activity produces, read [guide-incident-record](../guide-incident-record/SKILL.md) for structure, conventions and review.

Establish what is failing now, who is affected, and which parts still work. Compare that impact with available signals so an old alert or a broken telemetry path does not define the incident by itself.

Run stabilization and investigation together. Choose a mitigation for the effect it is expected to have, observe whether that effect occurred, and revise the hypothesis when it did not. Record the target, time and result so another responder can understand what changed. Do not delay a supported mitigation to finish a perfect diagnosis.

When the affected stack, architecture or domain has installed guidance, read it and carry its conclusions. If none exists, use project evidence and primary sources; this activity keeps the outcome, acceptance and stopping point.

## Response authority

- **Live interactive response:** establish impact, current state and response ownership promptly. Ask only questions needed for the next decision; investigate available sources meanwhile.
- **Authorized unattended response:** execute only mitigations explicitly allowed by the incident or job policy. Missing authority becomes a concrete handoff; never treat an old alert as a new incident without current impact evidence.

This activity is for active impact. A readiness exercise, procedure rehearsal or recurring signal review belongs to the owners in the boundary table. Stop and hand off rather than presenting simulated actions as live operations.

## Boundaries

| Request | Owner |
| --- | --- |
| Is this service ready to depend on? | [run-production-readiness-review](../run-production-readiness-review/SKILL.md) |
| Author, exercise or audit a procedure or runbook | [guide-runbook](../guide-runbook/SKILL.md) |
| Controlled failure experiment or game day | [testing-resilience](../testing-resilience/SKILL.md) |
| Recovery design, RTO/RPO, failover and failback | [design-system continuity and DR](../design-system/references/reliability-disaster-recovery.md) |
| Durable source repair | [fix](../fix/SKILL.md), [harden](../harden/SKILL.md) or [improve](../improve/SKILL.md) |
| Learning and action follow-up | [run-postmortem](../run-postmortem/SKILL.md) |
| Recurring operational drift | [run-operations-review](../run-operations-review/SKILL.md) |
| Credential or vulnerability operations | [run-security-maintenance](../run-security-maintenance/SKILL.md) |

Consult [references/response-guide.md](references/response-guide.md) for deeper implementation details when needed.

## Response loop

1. Read the exact alert/ticket/context and its UTC window. Also recheck a window ending now. Corroborate customer/business outcomes and telemetry health. Identify scope, trend and evidence of unaffected segments.
2. Apply local severity/major-incident criteria and name an incident lead. Separate operations, investigation, communication and timeline roles as staffing permits. Explicit role ownership matters more than titles.
3. Select the quickest defensible reversible mitigation: rollback/config revert, flag, load control, failover, compatible scale change or scoped maintenance. Preserve volatile evidence first when practical without materially delaying restoration.
4. Record hypothesis, expected effect, actual target, action authority, stop/rollback condition and UTC execution/result. Avoid conflicting simultaneous changes. Re-evaluate when impact grows or actions fail.
5. Investigate: align changes in code/config/platform/credentials/data/load with onset. Inspect diffs and scope. Compare working/failing variants. Test the strongest hypotheses with discriminating evidence. A recent change is not causal proof.
6. Escalate ownership/access/provider boundaries with facts, scope, window, actions/results and specific assistance needed. Keep impact updates on the local cadence and immediately on material changes. Use an absolute next-update time rather than an unsupported fix ETA.
7. Verify recovery through the original user/business path and independent signals, including served version/cache/async completion. Observe stability and track temporary controls.
8. Handover or close: current impact, timeline, proven/unknown cause, rejected hypotheses, pending jobs/controls, next action and owner. Feed evidence to postmortem facilitation after stabilization.

## Carry a durable repair forward

When a source repair is warranted, hand off the intended behavior, observed failure, affected scope, supporting signals and verification targets. Use available engineering defect-repair expertise for reproduction, design, implementation and regression checks within its authorized scope. The repair itself is not part of this activity. Keep incident mitigation, live recovery verification and communications with the incident response. Link the durable repair and its evidence from the incident record.

## Evidence discipline

Classify fact, hypothesis and unavailable information. Missing/sampled telemetry is unknown, not healthy. Compare numerator and denominator semantics before interpreting error/availability. Include silent failure, authentication/expiry, routing/cache and event-subscription changes in the investigation. Avoid overfitting everything to deployments.

## Completion evidence

Deliver impact/severity with policy source, response ownership, current status, timestamped evidence/action ledger, recovery verification or explicit blocker, next update and handover. Report a temporary mitigation as such and retain required follow-up work. Do not claim that a mitigation or recovery proves a durable fix.
