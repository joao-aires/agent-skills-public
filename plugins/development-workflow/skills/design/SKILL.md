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

Read [task guidance](../../TASKS.md). Use [system-design](../system-design/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent planning/implementation. When data or authority boundaries change, read [security-and-privacy-design](../security-and-privacy-design/SKILL.md). Load the optional stack/domain guidance selected by task guidance only when relevant and available.

Establish the audience, intended outcome, accepted decisions and affected boundaries from supplied references and repository evidence. Choose the supporting methods through task guidance; keep the result proportionate to the uncertainty.

For UI work establish contextual visual direction, flows, state and affected-surface coverage. Use installed visual-design and interaction-design when available for those decisions. Stack conventions map those decisions to the selected implementation without choosing the product direction. Use interface-quality for rendered assessment, ux-writing for consequential language and usability-research for questions needing participant evidence. Establish a representative design before propagating it. Choose text, wireframes, Figma or local prototypes according to the question and available tools. Connect agreed design decisions to tokens/components and the implementation handoff; Storybook can verify implemented component states later.

For backend behavior establish public contracts, actor authority, invariants, state/failure and compatibility, using installed backend-design when available; use system-design for architectural boundaries. Establish these decisions before choosing implementation layers or framework APIs. Compare consequential alternatives with constraints and tradeoffs; retain existing decisions where suitable. Ask for unresolved high-impact choices, record reversible assumptions and continue when the direction is sufficiently established. Return an agreed/proposed design and acceptance evidence with unknowns explicit. Do not silently implement or impose a design document/approval gate on trivial edits.
