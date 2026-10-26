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

Read [task guidance](../../TASKS.md). Use [system-design](../system-design/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent planning/implementation. When data or authority boundaries change, seek relevant security/privacy design expertise from available descriptions; retain the affected authority, data-flow and verification reasoning when a specialist is absent. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

Establish the audience, intended outcome, accepted decisions and affected boundaries from supplied references and repository evidence. Choose the supporting methods through task guidance; keep the result proportionate to the uncertainty.

## Design the affected interface

For UI work establish the accepted platform/component system and appearance policy before dependent mockups or implementation. Use existing choices or recommend an appropriate system and theme behavior with their tradeoffs. Carry those decisions through contextual visual direction, flows, state and affected-surface coverage. Choose methods for the unresolved question:

| Question | Relevant expertise or artifact |
| --- | --- |
| Component-system and appearance foundations | Available visual design expertise, accepted application constraints and matching implementation guidance |
| Product-specific visual direction | Available visual design expertise |
| Flow, state and behavior | Available interaction design expertise |
| Layout or navigation uncertainty | Text, wireframes, Figma or local prototypes, according to the question and available tools |
| Rendered quality or consequential language | Available interface assessment or interface-language expertise |
| A question needing participant evidence | Available usability research expertise |

Work through the main user task before polishing a screen. Determine what the user needs to understand, which action should be easiest to find, and what feedback explains the result. Use realistic content and the important empty, busy, error and permission states so the layout is designed for the application people will actually use.

Develop a representative part of the experience far enough to judge the direction. If navigation is uncertain, a wireframe may answer the question; if typography, density or visual identity is uncertain, inspect a rendered design. Explain why the chosen direction suits the product and what an alternative would cost. Once it works, carry its layout, tokens and component behavior into the other affected surfaces.

The handoff should make implementation choices traceable to design choices: which components to reuse, what states they need, how the layout adapts, and which details still need validation. Stack conventions map these decisions to implementation; Storybook can verify implemented component states later.


## Establish service behavior

Start with an operation the service must support. Identify its caller, the data it may access, the checks that permit the action, and the stored changes that make the result true. Decide which changes must succeed together and which work can complete later. Explain what the caller can safely infer from a success, rejection or timeout.

Follow the operation through repeated requests, partial failure and concurrent changes where they matter. An API shape alone does not settle whether a retry creates duplicate work or whether an old client can still use the service. Resolve these behavioral choices before organizing framework layers. Use available service-contract design expertise for this work and system-design for choices that change architectural boundaries.

## Resolve choices and hand off

Compare consequential alternatives against constraints and tradeoffs; retain existing decisions where suitable. Ask about unresolved high-impact choices, record reversible assumptions and continue when the direction is sufficiently established.

Connect the selected design to the application that will implement it. Use the affected behavior trace to identify:

- existing components and conventions to reuse;
- responsibilities that change;
- integration points that must agree.

Explain the intended flow from the caller through decisions and effects to the observed result. Name relevant code locations when known, keep proposed additions distinct from existing files, and leave routine implementation details open.

Carry the behavior, consequential choices and evidence needed to verify them into planning. The handoff should let someone explain where to start and which assumption could change the approach. A small local change may need only a short explanation beside its acceptance criteria; a cross-component change benefits from an implementation map or sequence when that clarifies dependencies.

Return the agreed/proposed design, acceptance evidence and explicit unknowns. A design request does not silently authorize implementation or impose a design-document approval gate on trivial edits.
