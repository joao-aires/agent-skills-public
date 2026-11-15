---
name: guide-runbook
description: Guide to writing and reviewing operational runbooks. Covers triggers, prerequisites, diagnosis, mitigation, verification, escalation, recovery and exercise evidence.
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

# Runbook guide

A runbook is a procedure a responder can follow under pressure. It should reduce the time to a supported action and make the result verifiable, not merely list commands.

## Reader questions

1. What condition does this runbook apply to, and how do I recognize it?
2. What must be true before I start?
3. What should I inspect first, and what does each result mean?
4. What action should I take, against which target, and what should I observe?
5. When should I stop, roll back or escalate?
6. How do I verify recovery independently of the action succeeding?
7. What remains temporary, and what follow-up is required?

## Minimum content

- trigger and observable impact;
- scope and non-applicability;
- prerequisites, access and safety conditions;
- a diagnostic path with branching observations;
- mitigation actions with exact targets and expected effects;
- stop, abort and rollback conditions;
- independent recovery verification;
- escalation trigger, owner and evidence to preserve;
- follow-up and related links;
- last exercise date and known gaps.

## Structure and quality

- Start from the condition a responder can recognize, not from the service name.
- Explain what a check establishes, so the responder can notice when the evidence does not fit.
- Use ordered steps only where order matters; otherwise use branching choices.
- Name the exact environment, target, command or console.
- Put the expected result beside the action.
- State the point of no return and the rollback.
- Verify recovery with a user or system path, not only a green status.
- Keep secret values out of the runbook.
- Record the last exercise and any branch that has never been tested.
- Link the alert, dashboard, architecture view and related incident rather than copying them.

## Common failures

- a template with no real diagnostic knowledge;
- “check the dashboard” without saying what to look for;
- commands with no target or expected result;
- no stop, abort or escalation condition;
- verification that repeats the mitigation rather than proving recovery;
- stale signal identities, links or owners;
- secret values or sensitive payloads in examples;
- presenting an unexercised procedure as verified;
- one runbook that tries to cover unrelated failures.

## Review

Read the runbook as a responder who is paged at night:

- Can you recognize the condition and decide the first check?
- Does each branch lead to a next decision?
- Do you know the target, expected result and stop condition?
- Can you verify recovery independently?
- Is escalation reachable and owned?
- Is the procedure exercised, and are the gaps named?

## Handoff

The next responder needs the trigger, prerequisites, diagnosis, mitigation, verification, escalation and follow-up. Record the last exercise and the unresolved branches so the next person does not mistake an untested step for a known procedure.
