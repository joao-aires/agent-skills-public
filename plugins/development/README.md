# Development plugin: the artifact system and the work that changes it

The `development` plugin is the default bundle for SDLC work. It carries the activity entry points, project foundations, contribution flow, verification methods and the **artifact system** that gives every durable engineering output a shared model.

This README explains the reasoning behind that structure. It is the design note for the plugin, not a replacement for the skills.

## The core insight

Every durable engineering output is an **artifact**: an ECR, PRD, roadmap, RFC, ADR, issue, PR, architecture view, runbook, README, guide, code module, test suite or release note. Each has a type, a primary role, a home, an authority, a maturity and relations to other artifacts. The ECR is the coordination spine for one change, not the center of the system.

This insight came from a concrete problem: the earlier skills were split on different axes.

- The former engineering artifacts skill was split by artifact type and lifecycle.
- `architecture-documentation` was split by subject matter (architecture).
- `documentation-writing` was split by craft (how to write).
- The former documentation conventions skill was split by placement (where documents live).

Those are orthogonal dimensions, so the skills overlapped. `architecture-documentation` felt too narrow for “all documentation,” while `documentation-writing` felt like a separate skill for something every artifact needs.

> The skills were split on different axes: artifact type and lifecycle, subject matter, writing craft and storage placement. Overlap is inevitable because those are orthogonal dimensions. Functional requirements are per artifact type; non-functional requirements are mostly cross-cutting. Writing is not a “dimension inside each artifact” — it is the craft that produces the non-functional outcome.
>
> — Design discussion, preserved as the rationale for this structure.

The correction is to separate the dimensions:

- **Functional requirements** are per artifact type: purpose, authority, lifecycle, status, required content, evidence and link obligations. They belong in the artifact contract.
- **Non-functional requirements** are mostly cross-cutting: reader fit, explanation, structure, examples, style, navigation, links and render fidelity. They belong in a shared quality bar plus a writing-craft skill, not inside every contract.

Writing is not a “dimension inside each artifact.” It is the craft that produces the non-functional outcome. The artifact contract requires the outcome; the craft skill teaches how to achieve it.

## The artifact model

An engineering artifact is a durable, addressable unit of engineering intent, knowledge, implementation or evidence that a reader can inspect and that has an authority, a lifecycle and a home.

| Field | Question |
| --- | --- |
| Identity | What stable name or key identifies it? |
| Type | ECR, PRD, ADR, issue, PR, architecture set, runbook, code module, test suite, release note, README or guide? |
| Plane | What is its primary role: intent, coordination, system knowledge, implementation, delivery or entry? |
| Authority | Is it the source of truth for its concern? |
| Home | Engineering workspace, application repository, tracker, git provider or operations repository? |
| Maturity | Proposed, accepted, implemented, verified, released, superseded, active or retired? |
| Reader | Product, implementer, reviewer, operator or new contributor? |
| Contract | What must it contain? |
| Relations | Derives from, informs, decides, proposes, implements, verifies, documents, projects, supersedes, releases or operates? |
| Evidence | Source revision, command, test, CI run or runtime observation? |
| Freshness | When must it be updated or retired? |
| Access | Public, private, audience-specific? |

Read the full model in [artifact model](skills/artifact-system/references/model.md).

## The plane model

A plane describes the artifact's primary role. It is **not** a storage bucket.

| Plane | Role | Example artifacts | Typical readers |
| --- | --- | --- | --- |
| Intent | Why and what to pursue | PRD, roadmap, product decision record | Product, leadership |
| Coordination | Track a change, its decisions and evidence | ECR, research report, RFC, issue, PR | Change participants, reviewers |
| System knowledge | Explain the implemented system | Architecture set, contracts, API reference, ADRs, runbooks, SLOs | Contributors, operators |
| Implementation | Build and verify the system | Code, tests, migrations, configuration | Engineers, reviewers |
| Delivery and operations | Release and operate | Release notes, changelog, deployment records, incidents, postmortems | Operators, maintainers |
| Entry and knowledge | Help someone start or learn | README, guides, tutorials, glossary, contributor guide | New users, contributors |

Planes are a navigation view, not an exclusive taxonomy. An artifact has a **primary plane** and may have secondary relations:

- The ECR is coordination-first but links intent, implementation, system knowledge and delivery.
- An ADR is system-knowledge-first but records a change decision.
- A PR is coordination-first but is also delivery evidence.
- A test suite is implementation-first but is also verification evidence.
- A README is entry-first but also describes the system.

The model is deliberately not “one artifact, one plane.” The graph handles cross-plane relations; the plane is the default reading direction.

## Homes are attributes

A home is where the authoritative copy lives. It is separate from the plane. An architecture view is system knowledge and usually lives in the application repository under `docs/architecture/`; a runbook is also system knowledge but may live in `ops/<application>/runbooks/`. An ECR lives in the engineering workspace.

The same artifact type can move homes without changing its contract. The model therefore separates:

- **Plane** — role.
- **Home** — location.
- **Authority** — truth for a concern.
- **Maturity** — what claim the artifact may make.

Read [artifact homes](skills/artifact-system/references/homes.md) for the default homes, alternates, resolution method and repository map template.

### The repository artifact home map

Every project should record where its durable artifacts live. A short pointer belongs in `AGENTS.md`; the full map belongs in `docs/README.md` or `docs/artifact-homes.md`.

The map records, for each artifact type:

- the authoritative home;
- the owner;
- the update trigger;
- the access boundary.

The map is project-specific. The resolution method is generic and lives in the artifact system. `setup` establishes or verifies the map; `project-conventions` maintains the repository placement method; `develop`, implementation and release read or update it. If the map is missing, treat that as a project-foundation gap rather than choosing an arbitrary `docs/` path.

## The artifact graph

Relations use a small, stable vocabulary:

| Relation | Meaning |
| --- | --- |
| `derives_from` | Takes intent or constraints from another artifact |
| `informs` | Provides evidence or context to another |
| `decides` | Records an accepted choice that constrains another |
| `proposes` | Offers a design that another may accept or reject |
| `implements` | Realizes an accepted change |
| `verifies` | Observes or proves accepted behavior |
| `documents` | Explains the implemented system or its operation |
| `projects` | Presents a view of another authority for an audience |
| `supersedes` | Replaces an earlier artifact or decision |
| `releases` | Records delivery to a target |
| `operates` | Governs running-system behavior |

The graph is the real structure. Planes are a view over it.

A typical change looks like this:

```text
PRD ──informs──▶ ECR ──proposes──▶ RFC
                   │                 │
                   ├──decides──────▶ ADR
                   ├──coordinates──▶ issue
                   ├──implements───▶ code / tests / migration
                   ├──verifies─────▶ CI / runtime evidence
                   ├──projects─────▶ PR
                   ├──documents────▶ architecture set / runbook
                   └──releases─────▶ release note
```

The ECR is the coordination spine, but every node is an artifact with its own authority and evidence. Code and tests are not appendices to the ECR; repo documents are not copies of it.

This is the correction to an ECR-centric diagram. The third SDLC diagram in [the SDLC overview](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/sdlc.md#standard-engineering-artifacts-and-workspace-handoffs) shows the ECR at the center of a change. That is accurate for coordination, but the surrounding code, tests, architecture views, runbooks and release records are first-class artifacts too.

## Functional and non-functional requirements

| Layer | Examples | Owner |
| --- | --- | --- |
| Functional artifact requirements | Purpose, authority, required sections, status, evidence, relations, update rules | Artifact contract + domain method |
| Shared non-functional floor | Self-contained context, readable structure, resolvable links, render fidelity, one authority | Artifact quality bar |
| Writing craft | Reader modeling, explanation, examples, precision, tone, navigation | Writing-craft expertise |
| Artifact-specific non-functional parameters | ADR conciseness and immutability; runbook scannability under pressure; PRD persuasive but evidence-based; architecture-view precision | Contract parameters + domain method |

The contract states the outcome; the craft skill teaches how to achieve it. This is why writing is not a section inside every contract and not a separate artifact system.

## Skills organization

The plugin is organized around the artifact model, not around a universal document template.

### `artifact-system`

The shared core. It owns:

- the artifact model, planes and relations;
- the catalog of artifact types and default homes;
- home resolution and the repository map method;
- the quality bar;
- cross-artifact assurance;
- the artifact contracts.

Start at [artifact system](skills/artifact-system/SKILL.md). Use the [catalog](skills/artifact-system/references/catalog.md) to choose a type, the [homes](skills/artifact-system/references/homes.md) reference to resolve a location, the relevant [contract](skills/artifact-system/references/contracts/README.md) for content, and the [quality bar](skills/artifact-system/references/quality-bar.md) before handoff.

### `engineering-workspace`

The storage mechanics for coordination artifacts: discovery, identity, persistence, revisions, provider limits and access. It owns **how** to publish an ECR or research report; the artifact system owns **what** it contains and **where** it belongs.

### `project-conventions` and `setup`

`project-conventions` owns repository foundations, including the artifact home map. `setup` establishes or verifies the map and records a portable pointer. This is how the phases become aware of placement: setup creates the map, implementation reads it, release updates the mapped records.

### `architecture-documentation`

A domain method for the architecture subject: C4 views, runtime and lifecycle scenarios, interface analysis, deployment boundaries and source-backed verification. It is **not** a generic documentation portfolio. The artifact system owns the architecture-set contract, status, evidence, home and maintenance triggers; this skill owns how to explain and verify the views.

### `documentation-writing`

Cross-type writing craft: reader fit, explanation, structure, examples, precision, navigation and presentation. It takes audience, purpose and required sections from the artifact contract. It does not own placement, status, evidence or content contracts.

### Domain methods

Requirements engineering, system design, system mapping, security, operations, database, frontend, backend and AI skills own their subject methods. The artifact contracts link to them by capability; the artifact system does not duplicate them.

### Retired: the former documentation conventions skill

The former documentation conventions skill has been dissolved. Its content split into:

- **generic home resolution** → [artifact homes](skills/artifact-system/references/homes.md);
- **freshness and synchronization** → [artifact assurance](skills/artifact-system/references/assurance.md) and the map’s update triggers;
- **the project-specific document map** → a repository artifact established by `setup` and maintained by `project-conventions`;
- **document responsibilities** → the artifact contracts and domain methods.

Keeping a separate generic conventions skill would duplicate the artifact system and create a second place to update placement rules. The repository map is the one-stop shop for “where does this live here?” The artifact system is the one-stop shop for “what is it and what must it contain?”

## Composability and reusability rules

1. **One owner per rule.** Link navigation lives in the quality bar, not in every contract. C4 coverage lives in architecture documentation, not in the ECR contract. Prose craft lives in writing, not in the issue template.
2. **Contracts are thin routers, not methods.** A contract says what the artifact must contain and which domain/craft capability to use. It does not re-teach architecture, product strategy or prose.
3. **Progressive disclosure.** The artifact-system `SKILL.md` carries the model and reading path. Contracts and domain skills load only when relevant.
4. **Capability-based composition.** Use available subject and craft expertise by description, not a hardcoded dependency graph.
5. **Stable vocabulary.** Artifact, type, plane, home, authority, maturity, contract, relation, evidence and freshness mean the same thing in every skill.
6. **Separate what / how / where / whether.** What = contract. How = domain method and craft. Where = homes and repository map. Whether = quality bar and assurance.
7. **No universal template.** A PRD, ADR, runbook and ECR have different functional requirements. The shared model is fields and relations, not identical sections.
8. **Evaluate composition, not just individual skills.** A change should be judged by whether the PRD, ECR, RFC/ADR, issue, PR, code, tests, architecture view and runbook agree on scope, status, revision and evidence.

## Reading paths

### For a change

1. Choose the activity in [WORKFLOW.md](WORKFLOW.md).
2. Use the [artifact catalog](skills/artifact-system/references/catalog.md) to select the ECR and any linked types.
3. Resolve the ECR home with [artifact homes](skills/artifact-system/references/homes.md) and [engineering workspace](skills/engineering-workspace/SKILL.md).
4. Read the [ECR contract](skills/artifact-system/references/contracts/ecr.md).
5. Apply the [quality bar](skills/artifact-system/references/quality-bar.md) and [assurance](skills/artifact-system/references/assurance.md).

### For a repository document

1. Read the repository artifact home map.
2. Choose the type: architecture set, ADR, runbook, README, guide, release note or API reference.
3. Read its [contract](skills/artifact-system/references/contracts/README.md).
4. Use the domain method for the subject and [documentation writing](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/documentation/skills/documentation-writing/SKILL.md) for craft.
5. Apply the quality bar and update the map if the type, home or owner changed.

### For a work product

1. Link it to the ECR, issue, requirement or ADR it implements or verifies.
2. Use the language/framework/test guidance for implementation quality.
3. Record the checked revision and evidence.
4. Reconcile affected architecture views, contracts, runbooks and API reference.
5. Do not turn the work product into a second ECR.

## What changed in this revision

- Renamed the former engineering artifacts skill to `artifact-system` and expanded it to cover intent, coordination, system knowledge, implementation, delivery and entry artifacts.
- Added the [artifact model](skills/artifact-system/references/model.md), [artifact homes](skills/artifact-system/references/homes.md), [catalog](skills/artifact-system/references/catalog.md), [quality bar](skills/artifact-system/references/quality-bar.md) and [assurance](skills/artifact-system/references/assurance.md).
- Added contracts for architecture sets, runbooks, work products, release notes, READMEs, guides and roadmaps; retained the ECR, issue, PR, research, RFC, ADR and PRD contracts.
- Dissolved the former documentation conventions skill into artifact homes, assurance, the repository artifact home map, and the setup/project-conventions integration.
- Rescoped `architecture-documentation` as the architecture subject method, with the artifact system owning the architecture-set contract.
- Reframed `documentation-writing` as cross-type writing craft, not a second contract system.
- Wired `setup`, `project-conventions`, `develop`, `plan`, `refine`, `design`, `release` and `WORKFLOW.md` to artifact homes and the repository map.
- Added evaluation cases for cold-reader sufficiency, thin structure, link resolution, issue-only pickup, cross-view consistency and render fidelity.

## Boundaries

This is guidance, not an executable gate. Package checks establish structure, links and packaging; they do not establish agent adherence, application behavior or deployment. The artifact system does not grant permission to create issues, publish documents, merge, deploy or access providers beyond the requested scope.

A compact artifact can pass; a long artifact can fail. The test is whether the reader can decide and act, not whether every heading exists.

## References

| Need | Source |
| --- | --- |
| Artifact model and planes | [artifact model](skills/artifact-system/references/model.md) |
| Type selection and contracts | [artifact catalog](skills/artifact-system/references/catalog.md) |
| Home resolution and repository map | [artifact homes](skills/artifact-system/references/homes.md) |
| Readiness, consistency and convergence | [artifact assurance](skills/artifact-system/references/assurance.md) |
| Activity selection | [development workflow](WORKFLOW.md) |
| Coordination storage | [engineering workspace](skills/engineering-workspace/SKILL.md) |
| Repository foundations | [project conventions](skills/project-conventions/SKILL.md) |
| User-facing guide | [engineering artifacts and workspaces](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/artifact-workflow.md) |
| Migration from old names | [migration guide](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/migration.md) |
