# Visualization plugin: portable diagrams, decks and explorable system views

The `visualization` plugin turns an explanation into a self-contained artifact: a static architecture diagram, a single-file presentation or an explorable system-flow model. It owns the artifact's narrative, rendering and inspection, not the truth of the architecture it depicts.

Evidence about the current system stays with system documentation and the project's records. A diagram can be accurate only to the evidence supplied; a valid file cannot establish that a proposed system exists.

## Purpose

Use this package when an explanation must be delivered as a portable visual artifact rather than prose. It composes with current-system mapping for evidence, the architecture design activity for proposals, and the frontend and documentation methods for visual or wording craft.

## Conceptual model

| Reader's need | Artifact | Owner |
| --- | --- | --- |
| Understand structure, runtime order, data movement or deployment in one static view | Responsive HTML diagram | [architecture-diagramming](skills/architecture-diagramming/SKILL.md) |
| Follow an argument and reach a decision in a presentation setting | Single-file HTML deck | [presentation-building](skills/presentation-building/SKILL.md) |
| Explore one system through scenarios, sequence messages and C4 depth | Standalone explorer with a canonical JSON model | [system-flow-explorer](skills/system-flow-explorer/SKILL.md) |

Each skill separates **meaning** from **layout** and **rendering**. A diagram's connectors, a deck's narrative and an explorer's scenarios must be decided before visual composition, and inspected in the delivered artifact rather than inferred from source or a successful write.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [architecture-diagramming](skills/architecture-diagramming/SKILL.md) | activity | View selection, element and relationship meaning, notation continuity, responsive HTML construction and render inspection | A delivered diagram with evidence scope, assumptions and checks | Current-system discovery, architecture truth or application change |
| [presentation-building](skills/presentation-building/SKILL.md) | activity | Audience and message, argument structure, slide contribution, visual direction, portable construction and slide inspection | A delivered deck with actual checks and remaining gaps | Copy craft for a document, research or approval of the proposal |
| [system-flow-explorer](skills/system-flow-explorer/SKILL.md) | activity | Scenario model, actors, ownership, messages, depth and view separation, JSON schema, rendering and structural validation | A validated model and rendered explorer with cited evidence | Evidence inventory, topology certification or application scaffolding |

## How it materialized

| Model element | Implementation |
| --- | --- |
| Diagram meaning, layout and HTML patterns | [building blocks](skills/architecture-diagramming/references/building-blocks.md), [design system](skills/architecture-diagramming/references/design-system.md), [HTML guide](skills/architecture-diagramming/references/html-guide.md) |
| Deck construction and starting document | [HTML guide](skills/presentation-building/references/html-guide.md), [skeleton](skills/presentation-building/references/presentation-skeleton.html), [timeline addon](skills/presentation-building/references/addons/timeline.html) |
| Explorer analysis and model contract | [analysis](skills/system-flow-explorer/references/analysis.md), [schema](skills/system-flow-explorer/references/schema.md), [minimal model](skills/system-flow-explorer/assets/minimal.json) |
| Explorer renderer, validator and checks | `skills/system-flow-explorer/scripts/` |

## Artifacts

| Artifact | Contract/template | Guide | Home |
| --- | --- | --- | --- |
| Architecture diagram | [HTML guide](skills/architecture-diagramming/references/html-guide.md) | [architecture-diagramming](skills/architecture-diagramming/SKILL.md) | Project documentation location for the depicted system |
| Presentation deck | [presentation skeleton](skills/presentation-building/references/presentation-skeleton.html) | [presentation-building](skills/presentation-building/SKILL.md) | The presentation's owning workspace or repository |
| Explorer model and HTML | [model schema](skills/system-flow-explorer/references/schema.md) | [system-flow-explorer](skills/system-flow-explorer/SKILL.md) | Alongside the source it explains |

The package supplies the artifact shape. The project's artifact home map decides the authoritative location, ownership and freshness rule.

## Reading paths

1. **Explain a system structure** → current-system mapping for evidence → [architecture-diagramming](skills/architecture-diagramming/SKILL.md) for the smallest sufficient view → render and inspect.
2. **Present a proposal or decision** → the accepted decision and evidence → [presentation-building](skills/presentation-building/SKILL.md) for narrative and deck → inspect every delivered slide.
3. **Let readers explore flows** → repository or design evidence → [system-flow-explorer](skills/system-flow-explorer/SKILL.md) → validate the JSON, render, then run browser checks when available.
4. **Refine an existing artifact** → preserve its accepted identity and model → the same owning skill → re-inspect affected views and widths.

## Boundaries

- **System truth.** Discovery, component ownership, deployment observation and semantic coverage belong to current-system mapping and the project's records. These skills consume that evidence and label proposed, implemented and unknown parts.
- **Proposed architecture.** Options and the accepted design decision belong to the architecture design activity. A diagram can illustrate a proposal; it cannot accept one.
- **Interface design.** Application screens, interaction and component systems belong to frontend design. These are explanatory and presentation artifacts, not product UI.
- **Publications.** Hosting, sharing, publishing or installing assets requires scope from the request. The skills install and deploy nothing.
- **Evidence.** Structural validation, a rendered screenshot or a successful script run proves the artifact, not that its architectural claims are correct.

## Authority and optional tools

The package declares no MCP servers. Diagram and deck artifacts need no server or runtime. The explorer's validation and rendering use Python 3.10+ standard library; optional browser verification uses an existing Playwright installation and must be reported as skipped when unavailable. Do not install browser dependencies merely to render.

## Maintenance

Owning sources are `skills/*/SKILL.md`, their references, the presentation skeleton and the explorer's assets and scripts. Update this README when artifact ownership, the evidence boundary or the tool dependency changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests; render and inspect changed diagrams and decks.
