---
name: refine
description: Refine a rough idea, brief, conversation or optional tracker item into
  repository-aware actionable work. Use to establish scope, acceptance criteria, affected
  UX/API/data boundaries and material questions before implementation, including unattended
  refinement jobs.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Refine

Read [task guidance](../../TASKS.md). Read [project-conventions](../project-conventions/SKILL.md) for affected project constraints. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

## Establish the change

Read the request alongside the code or documentation for the behavior being changed. Trace how the user reaches that behavior, what the application does today, and where the requested result differs. This gives the refinement a concrete starting point and often answers questions that would otherwise be sent back to the user.

Describe the change in the user's terms: who needs to do what, why the present behavior is insufficient, and what a successful result would let them do. Include the parts of the experience that must remain unchanged. Where the request names a solution, establish which need that solution is intended to satisfy before treating every suggested detail as a requirement.

Resolve implementation facts from the repository. Ask the user about choices only they can settle, such as which users may perform an action or whether an existing behavior should change. For a reversible assumption, say what you are assuming and which part of the result depends on it.

If the problem or product priority is still unresolved, use installed product discovery and prioritization expertise to shape that decision within scope before detailing the change. Accepted product context needs no new discovery cycle.

## Define actionable work

Write requirements that another contributor could implement without reconstructing the conversation. Connect each important requirement to an observable result:

- Describe the action, the conditions in which it is available, and the resulting visible or stored state.
- Explain what happens when the action is denied, cannot finish, or is attempted again, where those cases affect the requested behavior.
- Identify the screens, APIs, stored data and external consumers that need to agree about the change. Name existing behavior that constrains compatibility.
- Describe how the result will be checked. Choose a check that observes the promised result, rather than merely showing that a function was called.

Keep unresolved design choices visible. Requirements can be ready for design while still needing an architecture decision; they are not ready for implementation if that decision changes the behavior being promised.

For a consequential failure, explain what the consumer observes, whether effects may already have occurred and what continuation or recovery is allowed. This can produce both functional behavior and quality constraints: an actionable rejection differs from a deadline, durability or availability requirement. Derive the branches from the affected journey instead of importing an exhaustive error catalogue. A short transition description can be sufficient; use a matrix only when it makes several outcomes easier to compare.

For UI work, identify interaction decisions using available interaction design expertise. For backend work, use available service-contract design expertise for state, ownership, transactions and recovery decisions. A detailed brief does not itself authorize implementation code.


## Return readiness and open decisions

Return ready or needs-decisions and explain what that means for the next activity. Ready work has a clear intended result, sufficient scope and a credible verification approach. When a decision is still needed, identify the exact choice, why implementation depends on it, and which independent work can continue. Include the repository or product evidence that led to the question.

Conversation or Markdown can be sufficient; a tracker item is another input/output when configured and authorized. Labels, status changes and ticket creation stay within task policy. Routine work needs no exhaustive story catalogue or interview.

In unattended runs, return blockers rather than inventing product decisions or waiting for an absent person.
