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

For substantive UI work, seek the available **integrated interface-design capability** for hierarchy, navigation, interaction states, visual direction and critique; these do not require separate visual, interaction and assessment skill calls. Establish the accepted platform/component system and appearance policy before dependent mockups or implementation. Use existing choices or recommend a compatible system and theme behavior with their tradeoffs. Select other expertise only when the question calls for it:

| Question | Relevant expertise or artifact |
| --- | --- |
| Application structure, objects or data semantics | Relevant domain/archetype expertise and accepted product evidence |
| Component-system feasibility and platform behavior | Matching technical implementation guidance, brought into design early |
| Layout, behavior or visual uncertainty | Integrated interface design with text, wireframes, Figma or a local render as useful |
| Consequential task language | Available UX-writing expertise |
| A question needing participant evidence | Available usability research expertise |

Before choosing an interface structure, incorporate material domain/archetype guidance (what users operate on, what data means, what workflows must be preserved) and the accepted platform's technical constraints (component behavior, lifecycle, design-system conventions). Treat both as inputs to experience design, not as downstream implementation instructions. Relevant specialists may propose a complete domain-appropriate starting structure; general interface methods refine and reconcile it rather than forcing a second design. If constraints disagree, compare alternatives against accepted outcomes, real authority/accessibility rules and supported platform behavior. Keep optional expertise selected by capability, never by a mandatory package dependency.

Work through the main user task before polishing a screen. Determine what the user needs to understand, which action should be easiest to find, and what feedback explains the result. Use realistic content and the important empty, busy, error and permission states so the layout is designed for the application people will actually use.

Develop a representative part of the experience far enough to judge the direction. If navigation is uncertain, a wireframe may answer the question; if typography, density or visual identity is uncertain, inspect a rendered design. Explain why the chosen direction suits the product and what an alternative would cost. Once it works, carry its layout, tokens and component behavior into the other affected surfaces.

The handoff should preserve the **combined** domain, interaction, visual and technical decisions in the existing task/design record: which objects and authority rules matter, chosen flow and states, tokens/components to reuse, how the layout adapts, and what needs verification. Reuse specialist findings rather than asking implementation to reconcile competing drafts or requiring a new document. Stack conventions map the accepted choices to code; Storybook can verify implemented component states later.


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
