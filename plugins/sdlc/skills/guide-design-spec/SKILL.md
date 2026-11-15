---
name: guide-design-spec
description: Guide to producing a design specification that implementation can build and verify from. Covers flows, wireframes, mockups, prototypes, states, content, components, responsiveness, accessibility, motion, assets, handoff and design QA.
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

# Design specification guide

A **design specification** is the handoff package that lets an implementer build the intended experience and lets QA verify it without guessing. It can include wireframes, mockups, interactive prototypes, annotations, component and token mappings, assets, content and acceptance notes. The format matters less than whether the reader can act.

This guide is tool-agnostic. Figma, Penpot, Sketch, code, a written spec or a combination can carry the specification. The guide is about the artifact and the handoff, not about which design tool is fashionable.

## Reader questions

An implementer or reviewer should be able to answer:

1. What is the user trying to do, and what is the intended flow?
2. What should each screen or state look like and do?
3. What happens at empty, loading, error, denied, long-content, partial and permission states?
4. Which components, tokens, assets and content are required?
5. How does it adapt across viewport, platform, theme, locale and input method?
6. What is accessible and keyboard-operable, and what should assistive technology announce?
7. What motion, feedback and validation behavior is expected?
8. What is fixed, what is still open, and what must not change?
9. How will implementation and QA know the result is done?

## The three layers of a handoff

| Layer | What it contains | What it prevents |
| --- | --- | --- |
| **The what** | Screens, measurements, type, color, spacing, assets, tokens, component references, copy | Guessing the visual result |
| **The rules** | States, transitions, breakpoints, edge cases, validation, focus, motion, permissions, data behavior | Building only the happy path |
| **The rationale** | Constraints, non-negotiables, rejected options, open questions, acceptance | Re-litigating the design during implementation |

The tool can generate much of “the what.” The rules and rationale are the part that most often goes missing.

## Minimum content

- the user task, intended outcome and affected flow;
- the screens or steps and how the user moves between them;
- fidelity: which parts are wireframe, mockup, prototype or final visual;
- all consequential states: default, hover, focus, active, disabled, empty, loading, error, denied, partial, long-content and success;
- real content and representative data, including long labels and localization stress;
- component, token and design-system references; which are reused and which are new;
- responsive and adaptive behavior across the supported viewports or platforms;
- accessibility: semantics, focus order, keyboard path, labels, contrast, announcements and reduced motion;
- interaction behavior: validation timing, feedback, confirmation, undo, retry and recovery;
- motion and transitions where they affect comprehension or feedback;
- assets and export requirements: icons, images, illustrations, fonts, formats and naming;
- data and permission requirements that change the experience;
- acceptance criteria and design-QA checks;
- revision, source-of-truth link, open questions and the decision owner.

## Structure and fidelity

- Start with the user task and flow, not the first screen.
- Use a wireframe for structure and hierarchy, a mockup for visual direction, and a prototype for behavior. Do not use one for the question another answers.
- Compare options at comparable fidelity.
- Use realistic content, including the longest and shortest plausible values.
- Annotate behavior, data rules and unresolved questions; do not rely on the frame alone.
- Reuse the accepted component and token system; mark any intentional departure.
- Name layers, frames and components by meaning so an implementer can find them.
- Separate current, proposed and archived work; never present a proposal as the accepted design.
- Link the prototype and, where useful, a short screen recording of the intended path.
- Version the specification and link the exact revision used for handoff.

## Handoff checklist

| Category | Check |
| --- | --- |
| Intent | Task, outcome, flow and affected users are clear |
| Screens | Every affected screen or step is present and named |
| States | Default, hover, focus, active, disabled, empty, loading, error, denied, partial, long-content and success |
| Content | Real copy, labels, validation messages, empty/error text and localization stress |
| Components | Existing components and tokens identified; new ones justified |
| Responsive | Breakpoints, layout changes, overflow, orientation and platform differences |
| Accessibility | Semantics, focus order, keyboard path, labels, contrast, announcements and reduced motion |
| Motion | Transitions, feedback, loading indicators and reduced-motion alternative |
| Assets | Icons, images, fonts, formats, export settings and naming |
| Data | Required fields, permissions, roles, limits and failure behavior |
| Platform | Theme, density, locale, input method and platform conventions |
| QA | Acceptance criteria and a design-QA pass against the implemented result |
| Open items | Unresolved decisions, owners and what implementation may start or must wait |

## Common failures

- polished mockups with only the happy path;
- no empty, loading, error, denied or permission states;
- missing focus, keyboard, contrast or assistive-technology behavior;
- no responsive or adaptive rules;
- no component or token mapping, or a parallel design-system fork;
- placeholder copy that hides hierarchy, length or validation problems;
- ambiguous interaction left to “the developer will decide”;
- no prototype or demonstration of the intended behavior;
- an unversioned link that changes after review;
- no acceptance criteria or design QA;
- hidden non-negotiables and rejected options that resurface during implementation.

## Review

Read the specification as the implementer and as QA:

- Can someone build the flow without asking what happens next?
- Can QA verify the states, accessibility, responsive behavior and content?
- Is the design system respected, and are departures explained?
- Are the non-negotiables, open questions and revision explicit?
- Is the fidelity appropriate to the decision, and comparable across options?

A clean set of screens without rules and rationale is a mood board, not a design specification.

## Handoff

A specification is ready to hand off when the implementer can build the flow without asking what happens next, QA can verify the states and accessibility, and the open questions and revision are explicit. The handoff can be a design file, a written specification, a prototype and a short walkthrough; the reader should not need all four to start, but they should know where each lives.

## Example handoff package

```markdown
# Saved searches — design specification

## Intent
Let a signed-in user save, reopen and delete a search without losing context.

## Flow
Search results → save action → saved confirmation → saved-searches list → reopen.

## Fidelity
- Wireframes: navigation and list structure.
- Mockups: saved-searches panel and empty/error states.
- Prototype: save, duplicate-save and delete path.

## States
Empty, loading, saving, saved, duplicate, error, denied, long label, deleted.

## Components and tokens
Reuse the existing list, button, toast and empty-state components.
Use the accepted surface, border and text tokens; no new palette.

## Responsive
Narrow: full-screen panel; wide: side panel. Long labels wrap; no truncation
without an accessible full label.

## Accessibility
Focus moves to the saved item after save; delete requires confirmation;
icon-only controls have labels; status changes are announced politely.

## Content
Real labels, duplicate-name message, empty-state copy and error copy supplied.

## Motion
Panel slide-in with a reduced-motion alternative; no animation on save failure.

## Open questions
Whether to allow renaming in this slice. Owner: product.

## Acceptance
All states implemented; keyboard and focus path verified; design QA against the
approved frames at the linked revision.
```
