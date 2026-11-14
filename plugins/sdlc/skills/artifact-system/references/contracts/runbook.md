# Runbook contract: operating a known failure or task

A **runbook** is an actionable procedure for an operator responding to a known condition or performing a repeatable operational task. It is system-knowledge-first and must be usable under pressure. It is not a design document, a release note or a general operations essay.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is an operations repository such as `ops/<application>/runbooks/`; the application repository `docs/operations/` is an acceptable alternate when the team keeps operations knowledge with the code.

## Reader questions

An operator who was not in the conversation must be able to answer:

1. What condition or task does this runbook cover?
2. How do I know it is the right runbook, and what is the current impact?
3. What access, tools and prerequisites do I need?
4. What do I inspect first, and how do I interpret the result?
5. What actions are safe, and in what order?
6. How do I verify recovery or completion?
7. When do I stop, roll back or escalate?
8. Where is the evidence, owner and related design/decision?

## Contract

```markdown
# <Condition or task>

## Trigger and impact
The observable condition, affected users or systems, and the severity/urgency boundary.

## Prerequisites
Access, tools, environment, approvals and safety conditions.

## Diagnosis
What to inspect, expected signals, and how each result changes the next action.

## Mitigation
Ordered actions, with the safe abort/rollback point and expected effect.

## Verification
How to confirm recovery or completion, including the observable signal and target.

## Escalation
When to stop, who to contact, and what evidence to preserve.

## Follow-up
Related incident, postmortem, decision, SLO, or preventive work.

## References
Architecture view, SLO, dashboard, alert, source revision and evidence.
```

Guidance:

- **Trigger and impact.** Start with the observable condition, not the tool. State the impact and the boundary at which the operator should escalate.
- **Prerequisites.** Name access, permissions, environment and safety conditions. Put secrets and sensitive values in the approved secret store, never in the runbook.
- **Diagnosis.** Explain what to inspect and how to interpret it. A command without an interpretation is not a diagnostic.
- **Mitigation.** Use ordered steps. State the abort/rollback point and what the operator should observe after each consequential action.
- **Verification.** Define the observable signal that means recovered, not merely "command succeeded."
- **Escalation.** Include the trigger, owner/role and evidence to preserve. Do not invent contact details.
- **References.** Link the architecture view, SLO, alert, dashboard, source revision and incident record using the [link rules](../quality-bar.md#4-resolvable-navigation).
- **Status.** Draft, active or retired. Record the last exercise and any known gaps. Do not present an unexercised procedure as verified.

## Maturity and evidence

A runbook can be **draft**, **active** or **retired**.

- **Draft** means the procedure is proposed or untested. Say so.
- **Active** means the owner has accepted it and it is discoverable from the operations index. It may still have untested branches; name them.
- **Retired** means it must not be used; link the replacement.

A successful command, a green dashboard or a stored runbook does not establish that the procedure works under the real failure. Record what was actually exercised, in which environment, and what remains untested.

## Home and maintenance

| Change | Update |
| --- | --- |
| New failure mode or alert | Add or update the runbook and link the alert |
| Changed recovery, rollback or escalation | Update the procedure and verification |
| Boundary, dependency or deployment change | Recheck diagnosis, prerequisites and references |
| Incident or exercise | Record the observed gap, update the runbook and link the postmortem |
| Runbook retired | Mark retired and link the replacement |

## Review

Read the runbook as the on-call operator at the moment of failure. Can they identify the condition, impact, first diagnostic, safe action, verification and escalation without opening a design document? If not, it is a note, not a runbook.

Check commands and paths against the actual system. Do not invent dashboards, SLOs, hosts, owners or escalation contacts. If a prerequisite or target is unknown, mark it as an open gap rather than filling it with a plausible value.
