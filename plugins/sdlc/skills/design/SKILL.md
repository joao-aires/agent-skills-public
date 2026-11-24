---
name: design
description: Design UI interactions, backend contracts, AI behavior or architecture for a requested
  change before implementation. Use when the user wants to settle a solution, compare directions or
  review a proposal, including a continuation of an exploratory conversation. Use for consequential
  design alternatives; produce options, type-appropriate linked artifacts and a recorded decision.
user-invocable: true
metadata:
  kind: activity
  domain: development
  phase: design
  scope: generic
  invocation: both
---

# Design

Design settles a proposed solution before dependent implementation, and stops at a recorded decision others can judge. It does not implement.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. Design produces the question, affected components, materially different options, the linked artifacts a reviewer needs, the tradeoffs and the chosen direction.

Use the [artifact system](../artifact-system/SKILL.md) for the handoff and [artifact homes](../artifact-system/references/homes.md) for persistence. Read [software types](../artifact-system/references/software-types.md) to decide what evidence the affected components need. Use the [design proposal contract](../artifact-system/references/contracts/design-proposal.md) for the record.

## Reading path

| Need | Read |
| --- | --- |
| What evidence does this kind of component need? | [Software types](../artifact-system/references/software-types.md) |
| Which guide applies to this artifact? | [Design specification](../guide-design-spec/SKILL.md), [data model](../guide-data-model/SKILL.md), [C4](../guide-architecture-views/SKILL.md), [sequence](../guide-architecture-views/SKILL.md), [state machine](../guide-state-machine/SKILL.md), [compatibility matrix](../guide-compatibility-matrix/SKILL.md) |
| How to generate and compare directions | [Option set](references/option-set.md) |
| How to test the direction before building | [Design validation](references/design-validation.md) |
| Is the proposal ready to hand off? | [Design review](references/design-review.md) |
| What must the record contain? | [Design proposal contract](../artifact-system/references/contracts/design-proposal.md) |
| Recovery or operating procedure the design establishes | [Runbook guide](../guide-runbook/SKILL.md) |
| Architecture decisions and boundaries | [design-system](../design-system/SKILL.md) |
| Proposed versus current C4 and sequence views | [Diagram lifecycle](../artifact-system/references/diagram-lifecycle.md) |
| Parallel design threads and reopens | [Engagement state](../activity-system/references/engagement-state.md) |
| Consistency across artifacts | [Artifact assurance](../artifact-system/references/assurance.md) |

## Frame the decision

Establish the question, the accepted outcome and the constraints from supplied references and repository evidence. Identify the components the change touches and their software types:

- `frontend`, `backend`, `ai` or `library-cli`;
- `assumed` or `undecided` when the work is still at the brainstorm stage;
- `not affected` with a reason for components that are out of scope.

A type is a lookup for evidence, not a gate. If the design record would be the same whichever type it is, do not classify it. If the type changes the evidence, say so.

State what exists today at a named revision, or "greenfield; no implementation exists." Distinguish the current system from the proposed target.

Read the requirement IDs from the ECR and record how the proposed design satisfies them. Resolve the design requirements (`DR-`) for any user-facing or contract surface and link the design proposal or specification that evidences the resolution. A requirement the design leaves unanswered is a visible gap, not an implicit acceptance.

## Generate and represent options

For a consequential choice, produce at least three **materially different** options, each from a different lens. Read [option set](references/option-set.md) for triggers, lenses by type, artifact fidelity and anti-patterns.

Consequential means the choice affects responsibility, behavior, ownership, failure, cost, compatibility or a boundary, or is expensive to reverse. Do not turn a local fix into an option exercise.

Link the artifacts that let a reviewer judge each option at comparable fidelity:

| Type | Guide |
| --- | --- |
| Frontend | [Design specification](../guide-design-spec/SKILL.md) |
| Backend | [Data model](../guide-data-model/SKILL.md), [C4](../guide-architecture-views/SKILL.md), [sequence](../guide-architecture-views/SKILL.md), [state machine](../guide-state-machine/SKILL.md) |
| AI | Use the available AI testing method for the evaluation plan |
| Library/CLI | [Compatibility matrix](../guide-compatibility-matrix/SKILL.md) |

Read [software types](../artifact-system/references/software-types.md) for the typical artifacts and evidence for each component type. A text description alone is not enough when layout, interaction, contract shape, failure behavior or model quality is the question. Link the artifacts the decision needs. The guide owns structure, notation, fidelity and common failures. Use realistic content and the states that matter: empty, loading, busy, error, denied, stale, conflict.

When the change touches more than one type, the seam is part of the option set. Decide the contract or data shape, error and denial mapping, loading/empty distinctions, pagination, authority boundaries, retry/idempotency and compatibility once. Do not let each type section invent its own seam.

## Design the affected behavior

Choose the supporting method that matches the component. Do not force one discipline onto every type.

### Frontend

Work through the main user task before polishing a screen. Determine what the user must understand, which action should be easiest to find and what feedback explains the result. Cover the important empty, busy, error, denied and stale states.

Incorporate material domain/archetype guidance and the accepted platform constraints early. Reuse the existing design system, tokens and components. Do not invent a parallel one. Seek available interface-design, UX-writing and usability-research capability by description. If a specialist is absent, use the generic method, project evidence and primary sources. Do not lower the evidence standard.

Develop a representative part far enough to judge the direction. A wireframe may answer navigation. A rendered design may answer typography, density or visual identity. Carry the accepted layout, tokens and component behavior into the other affected surfaces.

### Backend

Start with an operation the service must support. Identify its caller, the data it may access, the checks that permit the action and the stored changes that make the result true. Decide which changes must succeed together and which work can complete later. Explain what the caller can safely infer from success, rejection or timeout.

Follow the operation through repeated requests, partial failure and concurrent changes where they matter. An API shape alone does not settle whether a retry duplicates work or whether an old client still works. Resolve those choices before organizing framework layers. When the change alters durable facts, ownership or their rules, record the logical model with [data model](../guide-data-model/SKILL.md). Physical schema detail stays with database guidance. Use [design-system](../design-system/SKILL.md) for choices that change architectural boundaries.

### AI

Establish the task, the quality bar and the context the model may use. Decide the provider/model boundary, the tools and authority each tool has, and the output contract consumed by the UI or service. Define the evaluation set, regression bar, failure and refusal behavior, cost/latency limits and human control. A demo response is not evaluation evidence.

### Library/CLI

Define the public surface and the consumer task. Cover compatibility, dependency surface, packaging, errors and exit codes, and usage examples for the main path and one failure path. A successful local build is not proof that a clean consumer can install or invoke it.

### Architecture

Use [design-system](../design-system/SKILL.md) when the change affects boundaries, ownership, persistence, identity, integrations or quality attributes. For new applications and boundary-changing work, inspect the current C4/sequence baseline at an explicit revision and create relevant **proposed target** views in the design record or RFC. For a local change, state why the diagrams are unaffected.

## Decide and record

Use the [design proposal contract](../artifact-system/references/contracts/design-proposal.md). For a normal change, the ECR solution-design section can hold the proposal. Use an RFC when the proposal needs its own audience or decision process, or a linked design record when the linked artifacts or review justify it.

Record:

- the affected types and what is not affected;
- the requirement IDs the design satisfies or leaves open, including resolved `DR-` items;
- the options, lenses, tradeoffs and failure behavior;
- the seam decision when several types meet;
- the recommended option, the decision owner and the status;
- the revisit trigger and the evidence still missing;
- the first implementation slice and the key assumptions.

Do not create one proposal per software type. Create one record with a section per affected type and one seam.

## Validate when uncertainty is material

Read [design validation](references/design-validation.md). Use the mode that matches the question: expert critique, rendered slice, prototype, usability observation, contract probe, bench/device observation, consumer test or AI evaluation set.

Record the target, revision, environment, observed result and limits. Validation ends at validated, limited or blocked. A validated design is still proposed relative to implementation and does not authorize building beyond the design request.

## Hand off

Before handing the design to implementation, apply [design review](references/design-review.md) and [artifact assurance](../artifact-system/references/assurance.md) against the accepted requirements:

- are the options real and the linked artifact sufficient;
- are error, denial, concurrency, migration and recovery paths covered;
- is the seam consistent across the type sections;
- are reuse, changed responsibilities and integration points named;
- are open decisions and owners explicit.

Return the accepted or proposed design, the evidence and the unknowns. Name what implementation may start and what is blocked. A design request does not silently authorize implementation or impose a design-document approval gate on trivial edits.

## Proportionality

A small local change may need only a short explanation beside its acceptance criteria. A cross-component or expensive-to-reverse change benefits from an option set, linked artifacts, a seam decision and a recorded owner. Invoke only the design modes whose evidence the decision needs. Do not invoke every mode for every change.

If new evidence invalidates the chosen direction, reopen the design decision, update the proposal and recheck dependents. Do not keep implementing on a contradicted design.
