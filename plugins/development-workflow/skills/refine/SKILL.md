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

Read [task guidance](../../TASKS.md). Inspect the request and relevant repository behavior before questioning the user. Identify the user outcome, actors, scope/non-goals, affected contracts and current constraints. Resolve technical facts from code/docs; ask only about material product, authority or design choices. State reversible assumptions with their effect.

Produce concise actionable work: intended behavior, observable acceptance and failure/permission cases, affected surfaces/contracts, dependencies and verification. For UI work identify interaction decisions requiring design-interactions; for backend work identify state, ownership, transactions and recovery decisions. Do not write implementation code merely because the brief is detailed.

Return ready or needs-decisions with concrete unresolved questions and evidence. A tracker item can be input/output when configured and authorized; conversation/Markdown is equally valid. Update labels/status or create tickets only within task policy. Unattended runs return blockers rather than invent product decisions or wait for an absent person. A routine task needs no exhaustive story catalogue or interview.
