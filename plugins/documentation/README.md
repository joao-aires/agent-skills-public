# Documentation plugin: technical writing and prose craft

The `documentation` plugin is a focused writing bundle. It supplies the cross-type craft for making product and engineering documents understandable, plus optional prose editing.

It does not own documentation placement, artifact contracts or architecture coverage. Those belong to the artifact system, the activity system and the repository’s artifact home map.

## What it owns

| Skill | Owns |
| --- | --- |
| [Technical writing](skills/technical-writing/SKILL.md) | Reader fit, explanation, structure, examples, precision, navigation and presentation for product and engineering documents |
| [Humanizer](skills/humanizer/SKILL.md) | Optional prose polish that preserves technical meaning, caveats, commands and links |

The plugin is useful when the question is “how should this be written for its reader?” It is not the place to decide what the document must contain, where it lives or what status it carries.

## How it composes

| Need | Use |
| --- | --- |
| What artifact is this, what must it contain, where does it live? | [Artifact system](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/artifact-system/SKILL.md) |
| What activity applies, and where does it stop? | [Activity system](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/activity-system/SKILL.md) |
| How do I explain the current system architecture? | [System mapping](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/system-documentation/SKILL.md) |
| How do I write or revise the document? | [Technical writing](skills/technical-writing/SKILL.md) |
| How do I polish the prose? | [Humanizer](skills/humanizer/SKILL.md) |

The artifact contract supplies the audience, purpose, required sections and status. The domain method supplies the subject explanation. This plugin supplies the craft.

## Technical writing is craft, not a contract system

`technical-writing` is the craft that produces the non-functional outcome. It does not own artifact-specific functional requirements such as required sections, status, evidence or authority. Those belong to the artifact contract and domain method.

A PRD, ADR, runbook and architecture view need different structure, tone and level of detail. The shared craft is reader modeling, explanation, examples, precision and presentation; the contract supplies the parameters.

## Architecture explanation

Current-state architecture explanation lives with [system mapping](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/system-documentation/SKILL.md) in the development plugin. Proposed architecture lives with `system-design`. The artifact system owns the architecture-set contract, status, evidence, home and maintenance triggers.

This plugin does not own an architecture document set, a documentation portfolio or repository placement.

## Migration

The former architecture and writing skills are retired names. Use `system-documentation` for current-state architecture documentation and `technical-writing` for writing craft. The former package composition file is retired; composition guidance lives in the activity system. See the [migration guide](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/migration.md).
