# Design specification contract: the handoff implementation can build from

A **design specification** is the durable handoff for an interface change: the flows, screens, states, content, components, assets and acceptance that let implementation build the result and QA verify it. It is coordination-first, but it records the accepted design rather than the design decision.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the design workspace or the application repository's design docs; link the design tool file and revision.

Read [design-spec-guide](../../../design-spec-guide/SKILL.md) for drafting, structure, states, accessibility and design-QA conventions.

## Reader questions

An implementer or reviewer must be able to answer:

1. What is the user task, flow and scope?
2. What does each screen or step look like and do?
3. What happens at empty, loading, error, denied, partial, long-content and success states?
4. Which content, components, tokens and assets are required?
5. How does it adapt across viewport, platform, theme, locale and input method?
6. What is accessible, focusable and announced?
7. What motion, feedback and validation behavior is expected?
8. What is fixed, what is open, and what must not change?
9. How will implementation and QA know it is done?

## Contract

```markdown
# <Change or feature> — design specification

## Intent and scope
User task, outcome, affected flow and non-goals.

## Flow and screens
Screens/steps, navigation, entry and exit, links to wireframes/mockups/prototype.

## States and edge cases
Default, hover, focus, active, disabled, empty, loading, error, denied, partial,
long-content, success and recovery.

## Content and data
Real copy, labels, validation and error messages, localization stress, required data.

## Components, tokens and assets
Reused components and tokens, justified new ones, icons/images/fonts, export notes.

## Responsive, platform and theme
Breakpoints, layout changes, platform differences, theme, density, locale and input.

## Accessibility
Semantics, focus order, keyboard path, labels, contrast, announcements and reduced motion.

## Interaction and motion
Validation timing, feedback, confirmation, undo, retry, transitions and loading indicators.

## Acceptance and design QA
Observable acceptance and the design-QA checks against the implemented result.

## Open questions and revision
Unresolved decisions, owners, the tool/file revision and what may start or must wait.
```

## Handoff

The implementer needs the flow, screens, states, content, components, tokens, responsive behavior, accessibility, motion, assets and acceptance criteria. QA needs the same sufficient to verify. The specification may be carried by a design file, a written document, a prototype and a short walkthrough; link each and state the revision. See [handoff](../handoff.md).

## Maturity

Use **draft**, **proposed**, **accepted** and **superseded**. A proposed screen is not an accepted design, and an accepted design is not implemented behavior.

## Review

Read the specification as the implementer and as QA:

- Can someone build the flow without asking what happens next?
- Are the consequential states and edge cases shown?
- Are accessibility, responsive behavior, content and assets covered?
- Is the design system respected, and are departures explained?
- Are open questions, revision and acceptance explicit?
