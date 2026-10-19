---
name: incident-response
description: Coordinate and investigate active service incidents using impact-led
  triage, reversible stabilization, causal evidence, escalation, communication and
  independent recovery verification across any application stack.
metadata:
  scope: generic
  invocation: both
  version: '1.0'
  role: task
---

# Incident response

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

Reduce user harm while building a reliable record of decisions and evidence. Do not delay a supported mitigation to finish a perfect diagnosis.

## Modes

- **Live interactive response:** establish impact, current state and response ownership promptly. Ask only questions needed for the next decision; investigate available sources meanwhile.
- **Setup/exercise:** implement local role/escalation/communication contracts, verification checks and rehearsals without presenting simulated actions as live operations.
- **Recurring review:** collect/scoped-correlate signals, draft incident updates and recommended actions. Execute only mitigations explicitly allowed by the incident/job policy; missing authority becomes a concrete handoff. Never reopen an old outage merely because an old alert link exists.

Consult [references/response-guide.md](references/response-guide.md) for deeper implementation details when needed.

## Response loop

1. Read the exact alert/ticket/context and its UTC window; also recheck a window ending now. Corroborate customer/business outcomes and telemetry health. Identify scope, trend and evidence of unaffected segments.
2. Apply local severity/major-incident criteria and name an incident lead. Separate operations, investigation, communication and timeline roles as staffing permits; explicit role ownership matters more than titles.
3. Select the quickest defensible reversible mitigation: rollback/config revert, flag, load control, failover, compatible scale change or scoped maintenance. Preserve volatile evidence first when practical without materially delaying restoration.
4. Record hypothesis, expected effect, actual target, action authority, stop/rollback condition and UTC execution/result. Avoid conflicting simultaneous changes; re-evaluate when impact grows or actions fail.
5. Investigate: align changes in code/config/platform/credentials/data/load with onset; inspect diffs and scope; compare working/failing variants. Test the strongest hypotheses with discriminating evidence. A recent change is not causal proof.
6. Escalate ownership/access/provider boundaries with facts, scope, window, actions/results and specific assistance needed. Keep impact updates on the local cadence and immediately on material changes; use absolute next-update time rather than unsupported fix ETA.
7. Verify recovery through the original user/business path and independent signals, including served version/cache/async completion. Observe stability and track temporary controls.
8. Handover or close: current impact, timeline, proven/unknown cause, rejected hypotheses, pending jobs/controls, next action and owner. Feed evidence to postmortem facilitation after stabilization.

## Evidence discipline

Classify fact, hypothesis and unavailable information. Missing/sampled telemetry is unknown, not healthy. Compare numerator and denominator semantics before interpreting error/availability. Include silent failure, authentication/expiry, routing/cache and event-subscription changes in the investigation; avoid overfitting everything to deployments.

## Completion evidence

Deliver impact/severity with policy source, response ownership, current status, timestamped evidence/action ledger, recovery verification or explicit blocker, next update and handover. Report a temporary mitigation as such and retain required follow-up work.
