# Migrating existing installations

Use this guide to replace an older installation or update saved skill references. Application layout, accepted technology and tracker choices do not need to change.

## Update your installation

1. Preserve custom edits and identify the origin of existing copies or links.
2. [Build the desired plugins](installation.md#select-additional-bundles) into a new destination. Built packages include local and pinned upstream skills, resources and notices; source directories omit acquisitions.
3. Replace complete affected packages through the client's supported route. Remove superseded copies to avoid duplicate names; do not overlay new files onto old directories.
4. Update saved prompts, project instructions, automations and private resource links using the maps below and the [current ownership catalogue](maintainers/sources.md#plugin-ownership).
5. Confirm the selected skills are discoverable in the application workspace. Discovery establishes availability; correct agent behavior needs separate verification.

Building does not install or remove client plugins, configure tools or connect accounts. Preserve unrelated installations and settings. For current selection flags and client setup, use [Installation](installation.md).

## Plugin package split

Choose replacements for the capabilities you use. Plugin-qualified invocations change with their owning package: for example, `/development-workflow:test` becomes `/development:test` where supported. Most skill names remain the same; use [Local skill naming](#local-skill-naming) for renames.

| Previous bundle | Replacement choices |
| --- | --- |
| development-workflow | development; backend-development, delivery, documentation and development-tooling for their respective capabilities |
| business-strategy | strategy |
| application-operations | operations; operations-platforms for JVM, Kubernetes and AKS expertise |
| web-frontend | frontend-development; frontend-reactjs-development or frontend-native-development for matching implementations |
| python-backend | backend-python-development |
| ai-development with combined methods and implementation | ai-development for generic methods; ai-python-development, ai-adk-development or ai-langchain-development for selected implementations |
| visual-communication | visualization |

The ai-development plugin keeps its package name but contains only generic methods. Replace its complete directory to remove stale technical skills. The default build contains development alone; select additional capabilities explicitly.

## Local skill naming

Update saved references to renamed local skills. Upstream names remain unchanged, and duplicate aliases are not shipped. These are guidance names, not instructions to rename application code or change test frameworks.

| Previous local name | Current name |
| --- | --- |
| `project-bootstrap`, `maintain-project-foundations` | `project-conventions` |
| `build-consistent-frontend` | `frontend-conventions` |
| `build-python-backend` | `backend-conventions` |
| `design-interactions` | `interaction-design` |
| `interface-craft` | `interface-quality` |
| `write-scannable-documentation`, `write-project-documentation` | `documentation-writing` |
| `document-software-architecture` | `architecture-documentation` |
| `test-end-to-end` | `journey-testing` |
| `test-application-performance` | `performance-testing` |
| `test-application-resilience` | `resilience-testing` |
| `build-evaluated-ai` | `ai-development` |
| `build-delivery-pipelines` | `delivery-pipelines` |
| `design-secure-features` | `security-and-privacy-design` |
| `contribute-code` | `git-contributions` |
| `architecture-diagraming` | `architecture-diagramming` |
| Standalone `backup-recovery` | `protect-and-restore-data` |
| Standalone `cicd-release-management` | `delivery-pipelines` |

## AI implementation names and resource paths

The generic ai-development package contains ai-development, ai-testing and ai-operations. For the specific implementations, use ai-deepeval-testing and python-ai-observability in ai-python-development. Requests for the generic names select the disciplines rather than a Python SDK integration.

| Previous package/path | Current package/path |
| --- | --- |
| `ai-python-development/skills/ai-testing` | `ai-python-development/skills/ai-deepeval-testing` |
| `ai-python-development/skills/ai-operations` | `ai-python-development/skills/python-ai-observability` |
| `ai-development/skills/build-evaluated-ai/references/evaluation-references.md` or `ai-development/skills/ai-development/references/evaluation-references.md` | `ai-development/skills/ai-testing/references/evaluation-references.md` |

For other moved resources, locate the owning skill in the [catalogue](maintainers/sources.md#plugin-ownership) and update private links to its current package. Selected quality-tool, local-environment, workflow/registry, telemetry-backend and browser-driver references belong to development-tooling; generic methods no longer contain those implementation instructions.

## Legacy links

The legacy helper supports local symlink installations from this checkout:

```bash
./scripts/sync-skills.sh status
./scripts/sync-skills.sh sync
```

It repairs managed unchanged-name links, including broken links to old `skills/` or package paths, while preserving unrelated entries. It adds local skills only, requires the checkout to remain in place and does not migrate renamed basenames, copied directories or other checkouts. Inspect and clean up those entries manually. New installations should use complete built plugins.
