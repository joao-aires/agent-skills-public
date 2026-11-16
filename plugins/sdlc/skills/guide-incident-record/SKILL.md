---
name: guide-incident-record
description: Guide to writing an incident record. Covers impact, severity, ownership, timeline, mitigation, recovery verification, current state and follow-up.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: operations
  phase: maintenance
  scope: generic
  invocation: both
  role: support
---

# Incident record guide

An incident record is the durable account of live impact and response: what was affected, what was observed, what was done, how recovery was verified and what remains. It is operational evidence, not a postmortem.

## Reader questions

1. What was the customer or system impact, and when?
2. What severity and response ownership applied?
3. What signals, changes and observations supported the diagnosis?
4. What mitigations ran, against which target, with what result?
5. How was recovery verified independently?
6. What is still temporary, unresolved or at risk?
7. What repair or follow-up is linked?

## Minimum content

- impact and severity;
- response lead, roles and escalation;
- timeline of observations, decisions and actions;
- mitigation and recovery actions with targets and results;
- independent recovery verification;
- current state and next update;
- follow-up, remaining temporary controls and links.

## Structure and quality

- Put customer impact before response activity.
- Use absolute UTC timestamps.
- Separate confirmed facts, hypotheses and unavailable information.
- Record the target, time and result of each consequential action.
- Do not present a simulated or planned action as executed.
- Keep secret values and sensitive payloads out of the record.
- Verify recovery with the original user/business path and independent signals.
- Keep the record live during the incident; it is not written only at the end.

## Common failures

- impact buried under a command log;
- confusing response duration with customer impact;
- a timeline with no timezone or ordering;
- “mitigated” because an alert cleared;
- no independent recovery evidence;
- hypotheses presented as facts;
- secrets copied from logs;
- follow-up promised with no owner.

## Review

Read the record as the next responder or postmortem facilitator:

- Can you reconstruct the impact, decisions and actions?
- Do you know what was actually verified?
- Are facts, hypotheses and unknowns separated?
- Is the current state and next update clear?
- Is the follow-up linked?

## Handoff

The postmortem and repair reader needs impact, timeline, mitigation, recovery evidence, current state and follow-up. A recovered incident does not mean the cause or control is resolved; keep that distinction.
