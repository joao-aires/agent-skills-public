---
name: presentation-building
description: Create or refine portable single-file HTML slide decks, including narrative, visual direction, responsive/fullscreen layout and optional timeline navigation. Use for HTML presentation work; preserve requested formats and existing deck identity.
metadata:
  version: '1.0'
  scope: generic
  invocation: user
  role: task
---

# Build a presentation around its message

Create or refine a portable single-file HTML deck, with local attachments when needed. Establish the audience, purpose, key message, presentation setting and accepted visual identity before choosing slide layouts. Preserve the requested format and scope; this skill's HTML approach is a particular deliverable, not a requirement for all presentation work.

## Shape the narrative and visual direction

Decide what the audience should understand or choose by the end, then arrange the argument that gets them there. Use supplied evidence to establish the situation, explain the consequential choice and support the recommendation. Give each slide a distinct contribution to that argument, with enough context that its main claim is understandable.

Choose the visual form after deciding what the slide needs to explain. A comparison needs common dimensions; a sequence needs meaningful order; a diagram needs relationships; an image needs a reason to carry attention. Preserve the author's voice and distinguish facts, illustrative examples and proposals. Remove repeated claims and divide dense material when doing so improves the explanation, without inventing a fixed slide count or card arrangement.

Derive typography, palette, density and motion from the brief. Reuse an accepted deck's identity during ordinary edits. The original dark scroll-driven profile is available as a starting point; its colors, title patterns and component counts are examples to adapt to the audience and content.

## Construct with the existing resources

| Need | Resource |
| --- | --- |
| HTML construction or repair | [Implementation guide](references/html-guide.md): skeleton conventions, component catalogue, fullscreen behavior and known rendering issues. |
| A suitable starting document | [Presentation skeleton](references/presentation-skeleton.html). |
| Useful chronology or a requested timeline | [Timeline addon](references/addons/timeline.html); preserve its integration contract. |

Load only resources relevant to the actual construction.

Keep the HTML/CSS/JS portable and assets reachable. Reuse tokens and shared components, preserve unique slide identity and navigation, and handle dense content through appropriate grouping or targeted layout changes. Animation should support the message, respect reduced motion and leave all content available.

## Inspect every delivered slide

Render the actual deck in its intended normal/fullscreen settings and relevant narrow layout. Check complete text and images, dense slides, contrast, keyboard/navigation, slide count and optional addons. Diagnose hidden content through DOM, layout and animation state, then verify the repair across affected slides. Example CSS or a successful file write cannot establish visual correctness.

Deliver the HTML/assets paths, actual checks and any remaining presentation or source-evidence gaps. Preserve useful existing resources; install or publish only within the requested scope.
