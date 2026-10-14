---
name: design
description: Design UI interactions, backend contracts or architecture for a requested
  change before implementation. Use for flows, navigation, shared components, API/data/state
  behavior or consequential design alternatives; produce concise text and useful wireframes/mockups
  when needed.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Design

Read [task guidance](../../TASKS.md). Establish audience, intended outcome and affected boundaries from repository evidence and supplied references. Select only relevant frontend/backend/domain/reliability/security guidance. For UX use design-interactions from web-frontend when available; define flows, states, information hierarchy, shared patterns and all affected surfaces before styling or implementation. Use text for behavior and wireframes/mockups for spatial or visual uncertainty, not as substitutes for each other.

For backend/architecture define public contracts, actor authority, invariants, state transitions, transactions/events, failure/cancellation and compatibility before choosing layers or frameworks. Compare consequential alternatives with constraints and tradeoffs; retain existing decisions where suitable. Ask for unresolved high-impact choices, record reversible assumptions and continue when the direction is sufficiently established. Return an agreed/proposed design and acceptance evidence with unknowns explicit. Do not silently implement or impose a design document/approval gate on trivial edits.
