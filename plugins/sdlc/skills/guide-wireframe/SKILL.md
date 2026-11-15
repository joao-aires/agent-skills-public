---
name: guide-wireframe
description: Guide to producing and reviewing wireframes and wireflows. Use for screen structure, navigation, task flow, states and comparable-fidelity design options; not for final visual styling.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: frontend
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Wireframe guide

Read [activity system](../activity-system/SKILL.md) for scope and the [design proposal contract](../artifact-system/references/contracts/design-proposal.md) for authority. Read [software types](../artifact-system/references/software-types.md) for the frontend evidence.

A wireframe is a **view artifact**, not the design decision. It answers a structural question: what the user sees, in what order, and what happens next. It does not settle visual style, final copy or implementation.

## Reader question

Can a reviewer understand the task, hierarchy and state changes without guessing what happens off-screen?

## When to use

- navigation, task flow, information hierarchy or screen structure;
- several design options that differ in structure or behavior;
- a layout that must be judged before visual design;
- a cross-screen change where the relationship between frames matters.

Do not use a wireframe for final visual direction, copy approval or pixel-level specification.

## Minimum content

- the task and its entry point;
- screens or frames and the navigation between them;
- the primary action and the result on each screen;
- empty, loading, busy, error, denied and success states where relevant;
- annotations for behavior, content rules and open questions;
- a link to the design proposal and the option it represents.

## Structure and quality

- Use comparable fidelity across competing options.
- Use shapes, labels and grouping, not final color or typography.
- Use realistic content and labels, not lorem ipsum.
- Show one frame per meaningful state.
- Explain interaction in annotations rather than inventing implementation detail.
- Keep the main task obvious and the secondary actions subordinate.

## Common failures

- final styling or brand direction in a structural artifact;
- only the happy path;
- placeholder content that hides a hierarchy problem;
- no annotation for a consequential interaction;
- comparing a detailed option against a rough sketch;
- treating the wireframe as the accepted decision.

## Authority, home and review

- **Authority:** the design proposal or ECR solution-design decision.
- **Home:** design workspace, Figma/FigJam or an authorized repository path.
- **Evidence:** link the frame and revision; record the states shown.
- **Review:** use the [design review](../design/references/design-review.md).

## Specialist route

Use available `interface-design` for interaction and visual craft, `ux-writing` for consequential copy, and usability research for participant evidence. The wireframe can be produced without those specialists; the evidence standard does not drop.

## Handoff

Record the wireframe link, revision, states and open behavior questions in the design proposal. Do not claim visual approval or implementation.
