# Incident record contract: the durable account of live impact and response

An **incident record** is the durable, reader-facing account of an incident: what was affected, what was observed, what was done, how recovery was verified, and what remains. It is operational evidence, not a postmortem and not a second ECR.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the incident tool or operations workspace; link it from the ECR when the incident is part of a change.

## Reader questions

A responder, reviewer or postmortem facilitator must be able to answer:

1. What was the impact, who was affected and when?
2. What was the severity and who had response ownership?
3. What signals, changes and observations supported the diagnosis?
4. What mitigations ran, at which target, with what result?
5. How was recovery verified, and what remains temporary or unresolved?
6. What durable repair or follow-up is linked?

## Contract

```markdown
# <Incident title>

## Impact and severity
Customer/user impact, affected services, start/end (UTC), severity and policy source.

## Response ownership
Incident lead, roles, escalation and communication cadence.

## Timeline and evidence
Timestamped observations, signals, changes, hypotheses and actions with targets/results.

## Mitigation and recovery
Actions, authority, expected effect, actual result, stop/rollback conditions and independent recovery verification.

## Current state
Recovered, mitigated, monitoring or blocked; temporary controls; next update and owner.

## Follow-up
Durable repair, postmortem, runbook/SLO changes and links.
```

Guidance:

- Separate customer impact from response/ticket duration. Use absolute UTC timestamps.
- Classify fact, hypothesis and unavailable information. Missing/sampled telemetry is unknown, not healthy.
- Record the target and result of each consequential action; do not present a simulated action as live.
- Recovery requires the original user/business path and independent signals, not only an alert clearing.
- Keep secret values and sensitive payloads out of the record.

## Maturity

An incident record is **active** while response continues, **recovered** when the user outcome is verified, and **closed** after follow-up is linked or explicitly dispositioned. A closed incident is not proof that the cause or control is resolved.

## Review

Read the record as the next responder or postmortem facilitator. Can they reconstruct impact, decisions, actions and recovery evidence without the chat? If not, the record is a status note, not an incident record.
