# Postmortem contract: durable learning from an incident

A **postmortem** is the durable, blameless explanation of an incident and the learning actions that follow. It is system/operations knowledge, not a status update, a blame record or a second incident log.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the operations/documentation home or the incident tool; link the source incident and action tracker.

## Reader questions

A future maintainer must be able to answer:

1. What happened, to whom, and how was recovery established?
2. Which trigger, contributing conditions and barriers produced the impact?
3. What did responders know and decide at the time?
4. What remains unknown or contested?
5. Which actions address the failure pathway, with what owner and verification?
6. What evidence shows the actions worked?

## Contract

```markdown
# <Incident title> — postmortem

## Summary
Impact, duration, severity, recovery and the current status of actions.

## Timeline
Timestamped facts, decisions, actions and recovery evidence; separate customer impact from response duration.

## Analysis
Trigger, contributing conditions, propagation, detection, response and recovery. Distinguish confirmed fact, hypothesis and unknown.

## What worked / what did not
Useful controls, barriers, detection and response gaps; avoid individual blame.

## Actions
Action, causal rationale, owner, target, due/review date, verification criterion and status.

## Open questions
Unresolved evidence, decisions or ownership.

## References
Incident record, evidence, runbooks, SLOs, related incidents and the action tracker.
```

## Maturity

Use **draft**, **reviewed**, **accepted** and **superseded**. A postmortem may establish recovery while leaving the cause unknown. Action states are separate: proposed, accepted, implementing, locally validated, deployed, outcome verified, deferred or superseded.

## Review

Can a reader understand the failure pathway and tell whether each action actually changes it? A chronological narrative without causal analysis is not a postmortem. Do not invent a single root cause or individual accountability.
