# Documentation plugin: explanation, technical writing and prose craft

The `documentation` plugin is a focused writing bundle. It supplies the cross-type craft for making product and engineering ideas understandable: live explanation, document-level technical writing and optional prose editing.

It does not own documentation placement, artifact contracts or architecture coverage. Those belong to the artifact system, the activity system and the repository's artifact home map.

## What it owns

| Skill | Owns |
| --- | --- |
| [Explain](skills/explain/SKILL.md) | Reader-specific explanation of one concept: intuition, bounded analogy, mechanism, worked example, edge cases and a comprehension check |
| [Technical writing](skills/technical-writing/SKILL.md) | Reader fit, explanation inside a document, structure, examples, precision, navigation and presentation for product and engineering documents |
| [Humanizer](skills/humanizer/SKILL.md) | Optional prose polish that preserves technical meaning, caveats, commands and links |
| [Skill authoring](skills/skill-authoring/SKILL.md) | Create, revise or review a skill: capability boundary, form, progressive disclosure, knowledge ownership, testing and integration |
| [Handoff](skills/handoff/SKILL.md) | Compact a conversation into a temporary handoff note for another agent, with references, redaction and suggested skills |

The plugin is useful when the question is "how should this be explained or written for its reader?" It is not the place to decide what a document must contain, where it lives or what status it carries.

## How it composes

| Need | Use |
| --- | --- |
| What artifact is this, what must it contain, where does it live? | [Artifact system](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/sdlc/skills/artifact-system/SKILL.md) |
| What activity applies, and where does it stop? | [Activity system](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/sdlc/skills/activity-system/SKILL.md) |
| How do I make this idea click for this reader right now? | [Explain](skills/explain/SKILL.md) |
| How do I write or revise the document? | [Technical writing](skills/technical-writing/SKILL.md) |
| Which document shape and layout should this use? | [Document types](skills/technical-writing/references/document-types.md), [formatting and layout](skills/technical-writing/references/formatting-and-layout.md) |
| How do I explain a concept inside a document? | [Concept explanation](skills/technical-writing/references/concept-explanation.md) |
| How do I review the finished document? | [Review rubric](skills/technical-writing/references/review-rubric.md) |
| How do I polish the prose? | [Humanizer](skills/humanizer/SKILL.md) |
| How do I create or revise a skill? | [Skill authoring](skills/skill-authoring/SKILL.md) |
| How do I hand this session to another agent? | [Handoff](skills/handoff/SKILL.md) |
| How do I explain the current system architecture? | [System mapping](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/sdlc/skills/guide-system-documentation/SKILL.md) |

The artifact contract supplies the audience, purpose, required sections and status. The domain method supplies the subject explanation. This plugin supplies the craft.

## Craft, artifact guide and contract

These layers answer different questions and should not be collapsed:

| Layer | Owns | Examples |
| --- | --- | --- |
| Artifact contract | Required content, status, evidence, authority, relations and home | A README must state quickstart, status and license; an ADR records one accepted decision |
| Artifact guide | Type-specific structure, conventions, examples, common failures and review questions | The README guide's adoption path; an ADR guide's one-page shape |
| Craft | Reader modeling, explanation, examples, precision, tone, navigation and presentation | This plugin's `explain` and `technical-writing` |
| Domain method | The subject being documented and the evidence for claims | Current-state architecture mapping, research, product strategy |

A craft skill can tell you that a decision needs its alternatives and reversal condition. It cannot tell you that this change requires an ADR, which sections the local ADR contract mandates, or that the architecture is verified. Those are artifact, domain or evidence decisions.

## Explanation is not artifact generation

`explain` is a user-facing craft method. It helps one reader understand one idea well enough to predict, apply or decide. It can end in speech, notes, a sketch or a worked example; it does not require a document, a status field or a template.

Its boundaries:

- **Against research:** explanation works from established material. It does not investigate an open question, rank sources or manufacture a mechanism to fill a gap. When the facts are missing, it says so and hands the inquiry to research.
- **Against system documentation:** explanation can make a mapped architecture flow understandable. It does not trace the current system, establish component ownership or claim that a view is complete. That evidence belongs to system documentation.
- **Against technical writing:** explanation is scoped to the act of making a concept click, often in conversation. Technical writing shapes a complete artifact for its reader, including document type, structure, precision, navigation and presentation. When the explanation must persist and be reviewed, hand it to technical writing and the artifact's contract.

## Technical writing is craft, not a contract system

`technical-writing` is the craft that produces the non-functional outcome. It does not own artifact-specific functional requirements such as required sections, status, evidence or authority. Those belong to the artifact contract and domain method.

A PRD, ADR, runbook and architecture view need different structure, tone and level of detail. The shared craft is reader modeling, explanation, examples, precision and presentation; the contract supplies the parameters. The skill's [document types](skills/technical-writing/references/document-types.md) reference describes common shapes for recognition, not mandatory local templates.

## Architecture explanation

Current-state architecture explanation lives with [system mapping](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/sdlc/skills/guide-system-documentation/SKILL.md) in the development plugin. Proposed architecture lives with `design-system`. The artifact system owns the architecture-set contract, status, evidence, home and maintenance triggers.

This plugin does not own an architecture document set, a documentation portfolio or repository placement.

## Migration

The former architecture and writing skills are retired names. Use `guide-system-documentation` for current-state architecture documentation and `technical-writing` for writing craft. `explain` is a separate local skill for reader-specific explanation; it does not replace `technical-writing` or `guide-system-documentation`. The former package composition file is retired; composition guidance lives in the activity system. See the [migration guide](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/migration.md).
