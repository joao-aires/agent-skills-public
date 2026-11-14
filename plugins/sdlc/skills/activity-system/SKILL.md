---
name: activity-system
description: Route development work across activities, stopping points and supporting methods. Use to choose what activity applies, what it produces, where it stops, what may follow, and which artifact or method to use.
user-invocable: true
metadata:
  kind: system
  origin: local
  pack: sdlc
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
  role: task
---

# Activity system: route the work

An **activity** is a requested engagement with an intent, entry conditions, an output, a stopping point, an authority boundary, the artifacts it produces or consumes, the supporting methods it may use, and the evidence that shows it is complete.

The [artifact system](../artifact-system/SKILL.md) owns the durable outputs. This skill owns the work: what activity applies, what it produces, where it stops, what may follow and which methods may deepen it.

> **Activity system in one sentence:** every requested engagement is an activity with an intent, entry conditions, output, stopping point, authority, artifacts and evidence; the activity system is the router that keeps work scoped and composable.

## Reading path

| Need | Read |
| --- | --- |
| Choose an activity and see its default result | [Activity catalog](references/catalog.md) |
| Understand transitions, handoffs and stopping points | [Transitions](references/transitions.md) |
| Select supporting methods and handle absent expertise | [Composition](references/composition.md) |
| Check action scope, unattended work and consequential decisions | [Authority](references/authority.md) |
| Keep the work proportionate to the project | [Project fit](references/project-fit.md) |
| Understand an artifact type, home or contract | [Artifact system](../artifact-system/SKILL.md) |
| Persist a coordination artifact | [Coordination storage](../artifact-system/references/storage/coordination.md) |

## Activity model

| Field | Question |
| --- | --- |
| Identity | What activity is this? |
| Intent | What outcome does the requester want? |
| Entry conditions | What must be known or decided before it starts? |
| Output | What does the requester have afterward? |
| Stopping point | Where does this activity deliberately stop? |
| Authority | What may it read, write, publish, merge or deploy? |
| Artifacts | Which artifact types does it produce or consume? |
| Supporting methods | Which disciplines may deepen the work? |
| Evidence | What shows the activity is complete? |
| Transitions | What can follow, and what must not be silently invoked? |
| Invocation | User-facing, agent-support or explicit-only? |

## Route the work

1. **Read the requested outcome**, project instructions and accepted decisions. Treat the request as the scope; do not infer a larger engagement.
2. **Choose the activity** whose stopping point matches the request. Use the [catalog](references/catalog.md). Distinguish an activity from a supporting method.
3. **Check entry conditions.** If a consequential decision, source or authorization is missing, resolve what can be investigated and return the precise decision or blocker. Do not start dependent work on a guess.
4. **State the stopping point.** A planning request stops at planning; a design request stops at design; an implementation request includes the code, checks and commits within the authorized flow. Do not silently invoke explicit-only activities.
5. **Select supporting methods by capability**, not by a hardcoded list. Read the relevant guidance, check its fit and carry useful conclusions into the work. Missing optional guidance does not lower the acceptance standard.
6. **Resolve artifacts and homes** with the [artifact system](../artifact-system/SKILL.md) and [artifact homes](../artifact-system/references/homes.md). The activity decides what is produced; the artifact system decides its type, contract, home and evidence.
7. **Stop at the requested result.** Report the outcome, actual evidence, unresolved decisions and the next activity or owner. Do not continue into a later activity because its skill is available.

## Help mode

When the request is for help, command discovery or “what should I do next,” use the catalog to explain the activity that matches the user's stopping point. Give one or two copyable requests using the client's supported syntax. Explain what the user will have afterward, not a compulsory sequence. Help is read-only: do not start setup, probes, tests, installs or the suggested activity.

## Boundaries

The activity system does not grant permission to create issues, publish documents, send messages, merge, deploy or access providers. The requested activity, existing policy and host controls own authorization. Planning, design, review and assessment do not silently authorize implementation.

Explicit-only upstream workflows remain explicit. Selecting a supporting discipline does not start a full lifecycle. Read [authority](references/authority.md) for unattended execution, consequential findings and working boundaries.

## Composition

Use [composition](references/composition.md) to seek expertise by capability and to preserve the outcome when a specialist is absent. Use [project fit](references/project-fit.md) to scale the work to the project and the requested change. The entry point and [Git contributions](../git-contributions/SKILL.md) own authorized publishing; the artifact system owns contracts, quality and assurance.
