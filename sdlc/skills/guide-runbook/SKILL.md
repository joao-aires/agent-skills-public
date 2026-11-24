---
name: guide-runbook
description: Guide to authoring, exercising and auditing operational runbooks. Covers triggers, prerequisites, diagnosis, mitigation, verification, escalation, recovery, artifact craft and exercise evidence; invoke from design, release, incident response, recovery and operations review as well as runbook maintenance.
user-invocable: true
metadata:
  kind: guide
  domain: operations
  phase: maintenance
  scope: generic
  invocation: both
---

# Runbook guide

A runbook is a procedure a responder can follow under pressure. It should reduce the time to a supported action and make the result verifiable, not merely list commands.

The runbook contract is the authority for required content, status and evidence. This guide owns the authoring, exercise and audit practice around that artifact. Use it whenever a runbook is created, changed, exercised or reviewed; a runbook is not an operations-only maintenance task.

## Reader questions

1. What condition does this runbook apply to, and how do I recognize it?
2. What must be true before I start?
3. What should I inspect first, and what does each result mean?
4. What action should I take, against which target, and what should I observe?
5. When should I stop, roll back or escalate?
6. How do I verify recovery independently of the action succeeding?
7. What remains temporary, and what follow-up is required?

## Choose the mode

- **Author:** create or rewrite a procedure for a known condition, alert, failure or planned operation.
- **Exercise:** run the procedure in a safe environment and record what actually happened.
- **Audit:** review an existing runbook for stale signals, broken links, missing branches, unowned steps or untested paths.

A single request may combine modes, for example rewriting a procedure and then exercising its changed branches. Read the mode against the requested stopping point rather than expanding into an incident response or a release.

## Author

1. Establish the service, trigger, observable impact and operating owner. Read the alert, architecture, signal, incident and prior procedure evidence before writing.
2. Write the diagnostic path: what to inspect, what each result means and what to do next. A command without an interpretation is not a diagnostic.
3. Put the exact target, prerequisites, expected effect, stop/rollback condition and independent recovery verification beside each consequential action.
4. Add escalation, the evidence to preserve and the follow-up that remains after the procedure.
5. Publish to the established operations home and link the alert, dashboard, architecture view and related incident. Do not copy those authorities into the runbook.
6. Mark the artifact draft, active or retired according to the contract, and name the branches that have not been exercised.

## Exercise

1. Select the branches that can be exercised safely and the environment that can represent them without touching production or sending real external effects.
2. Run the procedure as written, including the diagnostic interpretation, not only the successful commands.
3. Record the date, environment, target revision, branch exercised, observed result and any point where the procedure was ambiguous or wrong.
4. Update the procedure and its exercise evidence in the same change. Mark every branch that was not exercised.
5. Do not claim production recovery from a local or simulated exercise. A successful exercise establishes only what was exercised.

## Audit

1. Check the trigger identity, impact statement, links, owners and prerequisites against the current system.
2. Check that each branch leads to a decision, a safe action and a verification step, and that stop, rollback and escalation are reachable.
3. Check that recovery is verified through a user or system path, not by repeating the mitigation or reading a green status.
4. Check status, last exercise date, known gaps and the replacement link if the runbook is retired.
5. Return precise gaps and the resulting status. Do not silently refresh a stale signal or invent an owner, dashboard, host or contact.

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

## When invoked from another activity

Use this guide at the point where that activity needs a procedure, an exercise or a procedure audit:

| Context | What the guide contributes |
| --- | --- |
| [Design](../design/SKILL.md) | Identify the operating, rollback and recovery procedure the proposed design implies; keep it proposed until implemented. |
| [Release](../release/SKILL.md) | Update the deployment, rollback or recovery procedure and exercise the changed path before claiming readiness. |
| [Run incident response](../run-incident-response/SKILL.md) | Stabilize first, then capture the procedure actually used and the branch that failed under pressure. |
| Recovery design | Write and exercise the restore, cutover and return-to-normal procedure, with independent recovery evidence; continuity design stays in [design-system](../design-system/references/reliability-disaster-recovery.md). |
| [run-operations-review](../run-operations-review/SKILL.md) | Audit runbook ownership, staleness, exercise coverage and retired procedures as part of the recurring review. |

The invoking activity owns its outcome; the runbook contract owns the artifact. Do not turn a design, release or incident request into an unbounded runbook programme.

## Common failures

- a template with no real diagnostic knowledge;
- “check the dashboard” without saying what to look for;
- commands with no target or expected result;
- no stop, abort or escalation condition;
- verification that repeats the mitigation rather than proving recovery;
- stale signal identities, links or owners;
- secret values or sensitive payloads in examples;
- presenting an unexercised procedure as verified;
- one runbook that tries to cover unrelated failures;
- an exercise that runs the happy path only and leaves the branches unexamined;
- an audit that updates prose without checking the live signal or owner.

## Review

Read the runbook as a responder who is paged at night:

- Can you recognize the condition and decide the first check?
- Does each branch lead to a next decision?
- Do you know the target, expected result and stop condition?
- Can you verify recovery independently?
- Is escalation reachable and owned?
- Is the procedure exercised, and are the gaps named?

When reviewing an exercise or audit, add: is the recorded evidence from the stated environment and revision, and does the status match what was actually established?

## Handoff

The next responder needs the trigger, prerequisites, diagnosis, mitigation, verification, escalation and follow-up. Record the last exercise and the unresolved branches so the next person does not mistake an untested step for a known procedure. When handing to design, release, incident response, recovery or an operations review, state which mode was performed and what remains for that activity.
