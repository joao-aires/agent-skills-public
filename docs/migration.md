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

Choose replacements for the capabilities you use. Plugin-qualified invocations change with their owning package: for example, `/development-workflow:test` becomes `/sdlc:test` where supported. Most skill names remain the same; use [Local skill naming](#local-skill-naming) for renames.

| Previous bundle | Replacement choices |
| --- | --- |
| development-workflow | sdlc; backend-development, documentation and development-tooling for their respective capabilities |
| business-strategy | strategy |
| application-operations | sdlc; operations-platforms for JVM, Kubernetes and AKS expertise |
| web-frontend | frontend-development; frontend-reactjs-development or frontend-native-development for matching implementations |
| python-backend | backend-python-development |
| ai-development with combined methods and implementation | ai-development for generic methods; ai-python-development, ai-adk-development or ai-langchain-development for selected implementations |
| visual-communication | visualization |

The ai-development plugin keeps its package name but contains only generic methods. Replace its complete directory to remove stale technical skills. The default build contains sdlc alone; select additional capabilities explicitly.

## Local skill naming

Update saved references to renamed local skills. Upstream names remain unchanged, and duplicate aliases are not shipped. These are guidance names, not instructions to rename application code or change test frameworks.

| Previous local name | Current name |
| --- | --- |
| `project-bootstrap`, `maintain-project-foundations` | `project-conventions` |
| `build-consistent-frontend` | `frontend-conventions` |
| `build-python-backend` | `backend-conventions` |
| `design-interactions`, `interaction-design` | `interface-design` |
| `interface-craft`, `interface-quality`, `visual-design` | `interface-design` |
| `write-scannable-documentation`, `write-project-documentation` | `technical-writing` |
| `document-software-architecture`, `architecture-documentation`, `system-mapping` | `guide-system-documentation` for current-state architecture documentation and artifact creation; `design-system` for proposed architecture; the artifact system owns the architecture-set contract |
| `documentation-writing` | `technical-writing` |
| `engineering-workspace` | `artifact-system` storage references (`coordination`, `filesystem`, `providers`) |
| `reliability-design` | `design-system` reliability reference |
| `delivery-pipelines` | `ci-cd-pipelines` for pipeline design; `release` for the authorized action |
| `plan-application-capacity`, `optimize-application-cost` | `analyze-capacity-cost` |
| `credential-lifecycle`, `vulnerability-management` | `run-security-maintenance` |
| `postmortem-facilitation`, `postmortem-followup` | `run-postmortem` |
| `compliance-design`, `gdpr-readiness`, `soc2-readiness` | `run-compliance-assessment` |
| `operational-housekeeping` | `run-operations-review` |
| `runbook-engineering` | `guide-runbook` |
| `runbook-authoring` | `guide-runbook` |
| `observability-operations` | `design-system` observability guidance |
| `protect-and-restore-data` | `guide-runbook` plus `design-system` continuity design |
| `deliver-reliable-changes` | `test` (verification and completion evidence) |
| Upstream `implement` | Local `implement` activity; upstream source link in the plugin README, no copied body |
| `workflow-help` | `activity-system` (help mode) |
| `engineering-artifacts` | `artifact-system` |
| `documentation-conventions` | No direct replacement. Placement and home resolution move to `artifact-system`; the project-specific artifact home map is established by `setup` and `project-conventions`. |
| `test-end-to-end` | `testing-journey` |
| `test-application-performance` | `performance-testing` |
| `test-application-resilience` | `testing-resilience` |
| `build-evaluated-ai` | `ai-development` |
| `build-delivery-pipelines` | `ci-cd-pipelines` for pipeline design; `release` for the authorized action |
| `design-secure-features` | `design-security` |
| `contribute-code` | `git-contributions` |
| `architecture-diagraming` | `architecture-diagramming` |
| Standalone `backup-recovery` | `guide-runbook` plus `design-system` continuity design |
| Standalone `cicd-release-management` | `ci-cd-pipelines` for pipeline design; `release` for the authorized action |

The local `review` and `change-review` activities are retired as separate skills. Review is now a composition: `code-review` for the code-diff axes, `test` for verification evidence, artifact assurance for convergence, and the guides and quality bar for artifact checks. Because "review" is an ordinary word used throughout the documentation, it is intentionally not listed as a retired skill identity in the table above.

The artifact-system rename reflects a broader model, not just a new name. The skill now covers artifact types across intent, coordination, system knowledge, implementation, delivery and entry planes. `documentation-conventions` is retired: its generic placement method moved into the artifact system's artifact-homes reference, and its project-specific map is now a repository artifact established by `setup` and `project-conventions`. Update saved prompts to use `artifact-system` and the repository artifact home map.

Activity routing moved into the `activity-system` skill. `WORKFLOW.md`, `TASKS.md`, `workflow-help` and the per-plugin `COMPOSITION.md` files are retired. Use `activity-system` for activity selection, stopping points, composition and authority; use `test` for verification and completion evidence; use the repository artifact home map for placement.

The documentation plugin now carries cross-type technical writing and prose editing only. Architecture documentation moved into `guide-system-documentation` for current-state explanation, artifact creation and review, with `design-system` retaining proposed architecture and the artifact system owning the architecture-set contract.

The separately acquired Anthropic `frontend-design` entry point is also retired from frontend-development. It is replaced by `interface-design` for applicable design work, with [visual craft](../plugins/frontend-development/skills/interface-design/references/visual-craft.md) loaded conditionally when an open creative direction warrants it. This is a migration of the packaged capability, not a rename of the upstream project's original skill.

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
./scripts/sync_skills.py status
./scripts/sync_skills.py sync
```

It repairs managed unchanged-name links, including broken links to old `skills/` or package paths, while preserving unrelated entries. It adds local skills only, requires the checkout to remain in place and does not migrate renamed basenames, copied directories or other checkouts. Inspect and clean up those entries manually. New installations should use complete built plugins.

## Security ownership

Security and privacy design belongs to `sdlc`'s [design-security](../plugins/sdlc/skills/design-security/SKILL.md); recurring security work belongs to [run-security-maintenance](../plugins/sdlc/skills/run-security-maintenance/SKILL.md). Retain optional identity/access and specialist depth by capability. Replace the previous installation rather than overlaying files so a former security skill is removed; otherwise two copies may be discovered. No identity provider, account or live credential configuration is migrated.

## Committed upstream snapshots

Upstream skills are committed inside their owning plugin folders. The build command stays the same and uses those snapshots without fetching repositories; its old `--cache` option is removed. Snapshot acquisition and updates now use Agent Depot, with explicit artifact commits and destinations in `agent-depot.json` and file identities in `agent-depot.lock.json`. These replace `upstream.lock.json`. See [upstream maintenance](maintainers/upstreams.md) before changing a managed folder.

Continue loading complete built bundles, since raw acquired skills do not yet contain the collection’s adaptations or generated notices. The legacy skills-only helper continues to expose authored skills only. Rebuild bundles when updating; avoid overlaying them onto edited client installations.

## Implementation preparation

Ask for an implementation breakdown when work should stop before edits. Implementation and end-to-end development use the same [preparation method](../plugins/sdlc/skills/activity-system/references/implementation-preparation.md) when they need to order tasks and checks. Update saved prompts that used the former `plan` for implementation breakdowns. The current [plan](../plugins/sdlc/skills/plan/SKILL.md) starts earlier and establishes what to pursue, its scope and feasibility.

## Upstream SDLC review

The acquired SDLC set was reviewed against the local activity, artifact and method model.

| Former | Use instead |
| --- | --- |
| `agents-md` | [Project conventions](../plugins/sdlc/skills/project-conventions/references/repository-instructions.md) |
| `implement-spec` | [implement](../plugins/sdlc/skills/implement/SKILL.md) with optional parallel increments in [implementation preparation](../plugins/sdlc/skills/activity-system/references/implementation-preparation.md) |
| `improve-codebase-architecture` | [improve](../plugins/sdlc/skills/improve/SKILL.md) with optional [architecture scan](../plugins/sdlc/skills/improve/references/architecture-scan.md) |
| `to-spec` | [write-spec](../plugins/sdlc/skills/write-spec/SKILL.md) |
| `property-based-testing` | [Property-based testing reference](../plugins/sdlc/skills/test/references/property-based.md) |
| `differential-review` | [Security diff review reference](../plugins/sdlc/skills/harden/references/security-diff-review.md) |
| `research` | Local [research](../plugins/sdlc/skills/research/SKILL.md) |
| `domain-modeling` | Local [domain modeling](../plugins/sdlc/skills/domain-modeling/SKILL.md) |
| `prototype` | Local [prototype](../plugins/sdlc/skills/prototype/SKILL.md) |
| `retro` | Local [retro](../plugins/sdlc/skills/retro/SKILL.md) |
| `handoff` | Moved to [documentation](../plugins/documentation/skills/handoff/SKILL.md) |
| `writing-for-agents` | Moved to [documentation](../plugins/documentation/skills/writing-for-agents/SKILL.md); the documentation bundle now owns agent-instruction craft |

`writing-for-agents` keeps its upstream body, source pin, license and native controls. Its destination, packaging plugin and `pack: craft` labels now follow the documentation package; rebuild both `sdlc` and `documentation` so the old copy is removed and the new owner is discovered.

Structural renames:

| Former | Current |
| --- | --- |
| `system-design` | [design-system](../plugins/sdlc/skills/design-system/SKILL.md) |
| `system-documentation` + `guide-architecture-set` | [guide-system-documentation](../plugins/sdlc/skills/guide-system-documentation/SKILL.md) |
| `guide-c4-view` + `guide-sequence-view` | [guide-architecture-views](../plugins/sdlc/skills/guide-architecture-views/SKILL.md) |
| `runbook` | [guide-runbook](../plugins/sdlc/skills/guide-runbook/SKILL.md) |
| `security-and-privacy-design` + `security-auth-development` | [design-security](../plugins/sdlc/skills/design-security/SKILL.md) |
| `security-maintenance` | [run-security-maintenance](../plugins/sdlc/skills/run-security-maintenance/SKILL.md) |
| `compliance-readiness` | [run-compliance-assessment](../plugins/sdlc/skills/run-compliance-assessment/SKILL.md) |
| `capacity-and-cost` | [analyze-capacity-cost](../plugins/sdlc/skills/analyze-capacity-cost/SKILL.md) |
| `operations-review` | [run-operations-review](../plugins/sdlc/skills/run-operations-review/SKILL.md) |
| `incident-response` | [run-incident-response](../plugins/sdlc/skills/run-incident-response/SKILL.md) |
| `production-readiness` | [run-production-readiness-review](../plugins/sdlc/skills/run-production-readiness-review/SKILL.md) |
| `dependencies` | [run-dependency-maintenance](../plugins/sdlc/skills/run-dependency-maintenance/SKILL.md) |
| `learn-from-product-feedback` | [run-product-feedback-analysis](../plugins/sdlc/skills/run-product-feedback-analysis/SKILL.md) in `sdlc` |
| `product-management` | [product-direction](../plugins/sdlc/skills/product-direction/SKILL.md) in `sdlc`; removed from `strategy` with no alias, so rebuild and reinstall |
| `business-opportunity-analysis` | Retired; use [business-strategy](../plugins/strategy/skills/business-strategy/SKILL.md) |
| `postmortem` | [run-postmortem](../plugins/sdlc/skills/run-postmortem/SKILL.md) |
| `resilience-testing` | [testing-resilience](../plugins/sdlc/skills/testing-resilience/SKILL.md) |
| `journey-testing` | [testing-journey](../plugins/frontend-development/skills/testing-journey/SKILL.md) in `frontend-development` |

`data-recovery` and `observability` are retired. Recovery design lives in `design-system/references/reliability-disaster-recovery.md`, recovery procedures in `guide-runbook`, and readiness evidence in `run-production-readiness-review`. Observability design lives in `design-system/references/observability-and-monitoring.md`; incident response owns response and operations review owns recurring hygiene.

Rebuild bundles rather than overlaying an old installation.

## Repository documentation paths

The repository's own guides moved from `documentation/` to `docs/`. Relative links inside the repository were updated in the same change. External bookmarks or copied links need the new paths:

| Previous path | Current path |
| --- | --- |
| `documentation/` | `docs/` |
| `documentation/start-here.md` | `docs/usage.md#choose-a-path` |
| `documentation/railway-analogy.md` | Removed; `docs/architecture.md` explains composition and fallback |
| `documentation/maintainers/capability-expansion.md` | Removed; `docs/maintainers/sources.md` and the maintainer guide own current decisions |
| `documentation/maintainers/guidance-audit.md` | Removed; `skill-authoring` and the maintainer guide own the authoring rule |

Plugin package names, skill names and project artifact paths are unaffected. A project's own `documentation/` folder remains a valid project convention; this change applies only to this repository.
