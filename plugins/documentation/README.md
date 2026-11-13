# Documentation plugin: architecture subject and writing craft

The `documentation` plugin no longer owns a separate documentation-placement system. It supplies two focused capabilities:

- **Architecture explanation** — the subject method for structural, runtime, interface and deployment views, with source-backed evidence.
- **Writing craft** — the cross-type method for reader fit, explanation, structure, examples, precision, navigation and presentation.

It also includes the optional Humanizer prose-editing skill.

## What moved out

The former documentation conventions skill has been dissolved into the artifact system:

- Generic home resolution and the repository map method → [artifact homes](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/artifact-system/references/homes.md).
- Freshness, synchronization and cross-artifact consistency → [artifact assurance](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/artifact-system/references/assurance.md).
- The project-specific artifact map → a repository artifact established by `setup` and maintained by [project conventions](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/project-conventions/SKILL.md).
- Document responsibilities and required content → the artifact contracts in [artifact system](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/artifact-system/references/contracts/README.md).

Keeping a separate generic conventions skill would duplicate the artifact system and create a second place to update placement rules.

## How the remaining skills compose

| Need | Use |
| --- | --- |
| What artifact is this, what must it contain, where does it live? | [Artifact system](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/artifact-system/SKILL.md) |
| How do I explain the system architecture? | [Architecture documentation](skills/architecture-documentation/SKILL.md) |
| How do I make a document understandable for its reader? | [Documentation writing](skills/documentation-writing/SKILL.md) |
| How do I polish prose without changing technical meaning? | [Humanizer](skills/humanizer/SKILL.md) |

The artifact contract supplies the audience, purpose, required sections and status. The architecture method supplies the subject explanation. The writing skill supplies the craft. None of them should become a second contract or a second placement system.

## Architecture documentation is not “all documentation”

`architecture-documentation` explains the architecture **document set**: context, containers, selected components, critical runtime sequences, data ownership, interfaces, deployment, quality/failure and links to decisions. It does not own READMEs, guides, runbooks, product briefs or the repository's whole documentation portfolio.

The artifact system owns the architecture-set contract, status, evidence, home and maintenance triggers. The architecture skill owns view selection, C4/arc42 reasoning, interface analysis, deployment explanation and source-backed verification.

## Writing craft is not a contract system

`documentation-writing` is the craft that produces the non-functional outcome. It does not own artifact-specific functional requirements such as required sections, status, evidence or authority. Those belong to the artifact contract and domain method.

A PRD, ADR, runbook and architecture view need different structure, tone and level of detail. The shared craft is reader modeling, explanation, examples, precision and presentation; the contract supplies the parameters.

## Migration

The former documentation conventions skill is retired, not renamed. Update saved prompts to use `artifact-system` for contracts, homes and assurance, and the repository artifact home map for placement. See the [migration guide](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/migration.md).

## References

| Need | Source |
| --- | --- |
| User-facing artifact guide | [Engineering artifacts and workspaces](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/artifact-workflow.md) |
| Artifact model and homes | [Artifact system](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/artifact-system/SKILL.md) |
| Repository foundations | [Project conventions](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/development/skills/project-conventions/SKILL.md) |
| Migration | [Migrating existing installations](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/migration.md) |
