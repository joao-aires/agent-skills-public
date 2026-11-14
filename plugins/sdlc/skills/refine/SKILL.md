---
name: refine
description: Refine a rough idea, brief, conversation or optional tracker item into
  repository-aware actionable work. Use to establish scope, acceptance criteria, affected
  UX/API/data boundaries and material questions before implementation, including when a conversation moves from ideation to defining an actionable feature without authorizing code.
user-invocable: true
metadata:
  kind: activity
  origin: local
  pack: sdlc
  domain: development
  phase: requirements
  scope: generic
  invocation: both
  role: task
---

# Refine

Read [activity system](../activity-system/SKILL.md).

Record the agreed behavior, constraints and observable acceptance. When the next contributor needs a ticket, use the issue guidance in the [artifact system](../artifact-system/SKILL.md) for the handoff and [engineering workspace](../artifact-system/references/storage/coordination.md) for persistence. Resolve the artifact home with [artifact homes](../artifact-system/references/homes.md) before writing. Read [project-conventions](../project-conventions/SKILL.md) for affected project constraints. For new systems, substantial features, refactors, migrations, rearchitecture or work with materially uncertain actors, quality constraints or acceptance, read and apply [requirements-engineering](../requirements-engineering/SKILL.md) as supporting expertise. For a small well-defined fix, use only the applicable requirements checks without requiring a fuller analysis. Load other optional stack/domain guidance selected through the development workflow only when relevant and available.

## Establish the change

Read the request alongside the code or documentation for the behavior being changed. Trace how the user reaches that behavior, what the application does today, and where the requested result differs. This gives the refinement a concrete starting point and often answers questions that would otherwise be sent back to the user.

Describe the change in the user's terms: who needs to do what, why the present behavior is insufficient, and what a successful result would let them do. Include the parts of the experience that must remain unchanged. Where the request names a solution, establish which need that solution is intended to satisfy before treating every suggested detail as a requirement.

Resolve implementation facts from the repository. Ask the user about choices only they can settle, such as which users may perform an action or whether an existing behavior should change. For a reversible assumption, say what you are assuming and which part of the result depends on it.

If the outcome, scope or product priority is still unresolved, apply the [planning method](../plan/SKILL.md) within scope before detailing dependent requirements. Accepted product context needs no new discovery cycle.

## Define actionable work

Write requirements that another contributor could implement without reconstructing the conversation. Use the supporting requirements-engineering method when the change warrants elicitation, competing stakeholder needs, quality-attribute analysis, validation, compatibility or traceability. Connect each important requirement to an observable result:

- Describe the action, the conditions in which it is available, and the resulting visible or stored state.
- Explain what happens when the action is denied, cannot finish, or is attempted again, where those cases affect the requested behavior.
- Identify the screens, APIs, stored data and external consumers that need to agree about the change. Name existing behavior that constrains compatibility.
- Describe how the result will be checked. Choose a check that observes the promised result, rather than merely showing that a function was called.

Keep unresolved design choices visible. Requirements can be ready for design while still needing an architecture decision; they are not ready for implementation if that decision changes the behavior being promised.

For a consequential failure, establish:

- what the consumer observes;
- whether effects may already have occurred;
- what continuation or recovery is allowed.

These decisions can produce both functional behavior and quality constraints. An actionable rejection differs from a deadline, durability or availability requirement. Derive the branches from the affected journey instead of importing an exhaustive error catalogue. A short transition description can be sufficient; use a matrix only when it makes several outcomes easier to compare.

For UI work, identify interaction decisions using available interaction design expertise. For backend work, use available service-contract design expertise for state, ownership, transactions and recovery decisions. A detailed brief does not itself authorize implementation code.

## Return readiness and open decisions

Apply the requirement-quality boundary from [artifact assurance](../artifact-system/references/assurance.md): confirm each consequential actor, permission, failure/quality constraint and observable acceptance has coherent evidence; do not treat a proposed solution as a requirement. Give a scoped readiness disposition and resolve contradictions with existing accepted decisions before dependent design. Return **ready for design**, **ready for implementation** or **needs decisions** and explain the next dependency. Ready for design means required behavior, relevant quality constraints and acceptance are clear enough to evaluate solutions; ready for implementation also needs the design choices that materially change that behavior to be settled. Ready work has a clear intended result, sufficient scope and a credible verification approach. When a decision is still needed, identify the exact choice, why implementation depends on it, and which independent work can continue. Include the repository or product evidence that led to the question.

Record accepted/proposed requirements, acceptance, evidence and readiness in the ECR requirements section. A PRD owns broader product intent; an issue is an optional audience-specific summary, only published when configured and authorized. Routine work needs no exhaustive story catalogue or interview.

In unattended runs, return blockers rather than inventing product decisions or waiting for an absent person.
