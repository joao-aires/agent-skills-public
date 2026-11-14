---
name: fix
description: Investigate and repair reported incorrect software behavior when the user asks for a fix. Compare observed behavior with intent, reproduce the defect, apply a focused repair, verify it and hand off the evidence. Use for local or authorized engineering repair after an incident.
user-invocable: true
metadata:
  kind: activity
  origin: local
  pack: sdlc
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
  role: task
---

# Fix a defect

Read [activity system](../activity-system/SKILL.md). Confirm the requested stopping point and scope. For an active service incident, use available incident-response expertise for impact, mitigation and recovery. Use this repair method when a source change is authorized.

1. Establish intended behavior from the report, existing contracts, decisions and affected callers. Separate observations from hypotheses. Use [defect diagnosis](../diagnosing-bugs/SKILL.md) to reproduce the failure and test the likely cause. If reproduction is unavailable, record the evidence and limits before proposing a repair.
2. Choose a focused correction. Trace which existing paths use the changed condition or state transition, including what happens after errors, retries or cancellation when applicable. Preserve behavior that the request leaves in scope. Use relevant design expertise when the repair changes a contract, state transition or boundary. Apply [implementation preparation](../activity-system/references/implementation-preparation.md) when ordering work or verification needs care.
3. Use [Git contributions](../git-contributions/SKILL.md) for the authorized source change. Verify the original failure path and the affected existing behavior identified during design with [change verification](../test/SKILL.md). Recheck after repairing failures.
4. Use [artifact system](../artifact-system/SKILL.md) and [engineering workspace](../artifact-system/references/storage/coordination.md) for the handoff. Record the intended behavior, cause or remaining uncertainty, repair, actual verification and next action. Update authorized issue or PR views when applicable. Keep incident recovery and deployment claims tied to their own observed evidence.
