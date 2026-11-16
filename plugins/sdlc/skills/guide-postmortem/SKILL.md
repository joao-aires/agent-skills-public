---
name: guide-postmortem
description: Guide to writing a blameless postmortem. Covers timeline, contributing conditions, what worked, actions, owners, verification and open questions.
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

# Postmortem guide

A postmortem explains how an incident happened and what will reduce the chance or impact of a recurrence. It is a learning document, not a blame record, a status update or a second incident log.

## Reader questions

1. What happened, to whom, and how was recovery established?
2. Which trigger, contributing conditions and barriers produced the impact?
3. What did responders know and decide at the time?
4. What remains unknown or contested?
5. Which actions address the failure pathway, with what owner and verification?
6. What evidence shows the actions work?

## Minimum content

- summary and impact;
- timeline of facts, decisions and recovery;
- trigger, contributing conditions, propagation, detection, response and recovery;
- what worked and what did not;
- actions with causal rationale, owner, target, verification and status;
- open questions and conflicting evidence;
- references and related incidents.

## Structure and quality

- Be blameless: explain the information and controls available at the time, not individual failure.
- Do not force a single root cause or a fixed “five whys” chain.
- Separate confirmed impact from plausible exposure.
- Keep customer impact distinct from response duration.
- Define actions with an observable completion criterion.
- Distinguish proposed, accepted, implementing, validated, deployed and outcome-verified actions.
- Keep unknown or disputed evidence visible.
- Link the source incident, timeline and evidence.

## Common failures

- a chronological narrative with no causal analysis;
- naming an individual as the cause;
- a single root cause that hides contributing conditions;
- actions that are “be more careful” or “add a checklist” with no verification;
- closing actions from ticket status;
- rewriting the timeline to fit the conclusion;
- claiming the control works without observing it.

## Review

Read the postmortem as a future maintainer:

- Can you understand the failure pathway and the barriers that did or did not work?
- Are facts, hypotheses and unknowns separated?
- Do actions change the pathway, and can they be verified?
- Are owners and target dates real?
- Is the tone blameless and specific?

## Handoff

The planning and design reader needs the causal analysis, actions, owners, verification and open questions. A written action is not a controlled failure mode; link the verification evidence.
