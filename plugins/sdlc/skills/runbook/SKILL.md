---
name: runbook
description: Create, exercise or audit an operational runbook. Use for alert response, recovery procedures, planned operations and recurring runbook maintenance; stop at a published and exercised procedure or a precise gap.
user-invocable: true
metadata:
  kind: activity
  origin: local
  pack: sdlc
  domain: operations
  phase: maintenance
  scope: generic
  invocation: both
  role: task
---

# Runbook

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. Use the [runbook contract](../artifact-system/references/contracts/runbook.md) for the artifact and [guide-runbook](../guide-runbook/SKILL.md) for writing conventions.

A runbook is an operational procedure a responder can follow under pressure. The activity owns the procedure and its evidence; the contract owns what the artifact must contain; the guide owns how to write it well.

## Choose the mode

- **Author:** create or rewrite a procedure for a known alert, failure or planned operation.
- **Exercise:** run the procedure in a safe environment and record what actually happened.
- **Audit:** review an existing runbook for stale signals, broken links, missing branches or untested steps.

## Work the procedure

1. Establish the service, trigger, observable impact and operating owner.
2. Read the alert, architecture, signal, incident and prior procedure evidence.
3. Write the diagnostic path: what to inspect, what each result means and what to do next.
4. Put exact targets, prerequisites, expected effects, stop/rollback conditions and independent recovery verification beside each action.
5. Add escalation and the evidence to preserve.
6. Exercise the branches that can be exercised; mark the rest as untested.
7. Publish to the established operations home and link the alert, dashboard and related incident.

## Stopping point

Stop at a published, discoverable and exercised procedure, or at the precise missing evidence, access or owner that prevents publication. A template with no established diagnostic knowledge is not a completed runbook.

## Completion evidence

Report the trigger, target, branches exercised, observed results, untested branches and remaining gaps. Do not claim production recovery from a local exercise.

## Handoff

The responder needs the trigger, prerequisites, diagnosis, mitigation, verification, escalation and follow-up. The next maintainer needs the exercise date and the branches that remain untested.
