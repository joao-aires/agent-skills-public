# Development plugin: activities, artifacts and evidence

The `development` plugin is the default bundle for SDLC work. It carries the activity entry points, project foundations, contribution flow, verification methods and two core models:

- the **activity model**, which routes the work;
- the **artifact model**, which gives every durable output a shared shape.

> **Artifact system in one sentence:** every durable engineering output is an artifact with a type, plane, home, authority, maturity, relations and evidence; the artifact system is the shared model that keeps those artifacts sufficient, navigable and consistent.

> **Activity system in one sentence:** every requested engagement is an activity with an intent, entry conditions, output, stopping point, authority, artifacts and evidence; the activity system is the router that keeps work scoped and composable.

These are the two core models. The activity system decides **what work is being done and where it stops**. The artifact system decides **what durable outputs are produced, where they live, and what evidence they carry**.

## The conceptual model

The rest of the plugin is composed from a small set of concepts. Two are core models; the others are composition layers or dimensions.

| Concept | Question it answers | Status |
| --- | --- | --- |
| **Artifact** | What durable output is produced? | Core model — `artifact-system` |
| **Activity** | What work is requested, and where does it stop? | Core model — `activity-system` |
| **Method** | What reusable expertise deepens the work? | Supporting capability — TDD, code review, requirements engineering |
| **Workflow** | What ordered sequence carries the work out? | Composition pattern — e.g. the contribution workflow |
| **Role** | Who participates? | Dimension — product, implementer, reviewer, operator |
| **Phase** | Where in the SDLC lifecycle? | Dimension — planning, requirements, design, implementation, verification, release, maintenance |
| **Home** | Where does the artifact live? | Dimension — engineering workspace, repo, tracker, provider, operations repo |
| **Evidence** | What supports the claim? | Quality and assurance — quality bar, artifact assurance |

Artifact and activity are the core. Method, workflow, role, phase, home and evidence are not competing top-level systems; they are layers or dimensions applied to those two models.

### Workflow is a composition, not a third core model

A workflow is an **ordered execution path inside or around an activity**. It is not a new core object.

- An **activity** is “implement the agreed change” or “verify this behavior.”
- A **workflow** is “create a worktree → verify → commit → push → open or update the PR.”
- A **method** is “how to review a diff” or “how to design a test.”

`git-contributions` is the clearest workflow-shaped method in the current plugin. It sequences contribution mechanics and produces or updates artifacts, but it does not own the PR artifact. The PR contract owns the reviewer-facing content; the workflow owns the mechanics.

The same distinction applies elsewhere: `release` is an activity, while readiness → promotion → verification → observation is a workflow; `system-documentation` is an activity-shaped method, while trace → evidence → view is its internal sequence.

If the same ordered sequence is reused across several activities, it can become a formal reference under `activity-system/references/workflows/`. Until then, “workflow” remains a useful label for a method’s internal sequence, not a separate system.

## Why the plugin is organized this way

The earlier skills were split on different axes: artifact type and lifecycle, subject matter, writing craft and storage placement. Those are orthogonal dimensions, so the skills overlapped. The former architecture and writing skills felt too narrow for “all documentation,” or too separate from the artifacts that need them.

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

Read the full model in [artifact model](skills/artifact-system/references/model.md). Choose a type in the [artifact catalog](skills/artifact-system/references/catalog.md). Resolve its location with [artifact homes](skills/artifact-system/references/homes.md).

## The activity model

An activity is a requested engagement. It has the same kind of explicit shape as an artifact:

| Field | Question |
| --- | --- |
| Identity | What activity is this? |
| Intent | What outcome does the requester want? |
| Entry conditions | What must be known or decided before it starts? |
| Output | What does the requester have afterward? |
| Stopping point | Where does this activity deliberately stop? |
| Authority | What may it read, write, publish, merge or deploy? |
| Artifacts | Which artifact types does it produce or consume? |
| Supporting methods | Which disciplines may deepen the work? |
| Evidence | What shows the activity is complete? |
| Transitions | What can follow, and what must not be silently invoked? |
| Invocation | User-facing, agent-support or explicit-only? |

Read [activity system](skills/activity-system/SKILL.md) for the routing model. The [activity catalog](skills/activity-system/references/catalog.md) lists the activities, default results and stopping points. [Transitions](skills/activity-system/references/transitions.md) explains handoffs. [Composition](skills/activity-system/references/composition.md) explains how supporting methods are selected. [Authority](skills/activity-system/references/authority.md) explains action scope and unattended work. [Project fit](skills/activity-system/references/project-fit.md) keeps the work proportionate.

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

## Homes are attributes

A home is where the authoritative copy lives. It is separate from the plane. An architecture view is system knowledge and usually lives in the application repository under `docs/architecture/`; a runbook is also system knowledge but may live in `ops/<application>/runbooks/`. An ECR lives in the engineering workspace.

The same artifact type can move homes without changing its contract. The model therefore separates:

- **Plane** — role.
- **Home** — location.
- **Authority** — truth for a concern.
- **Maturity** — what claim the artifact may make.

Read [artifact homes](skills/artifact-system/references/homes.md) for default homes, alternates, the resolution method and the repository map template.

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

## Functional and non-functional requirements

| Layer | Examples | Owner |
| --- | --- | --- |
| Functional artifact requirements | Purpose, authority, required sections, status, evidence, relations, update rules | Artifact contract + domain method |
| Shared non-functional floor | Self-contained context, readable structure, resolvable links, render fidelity, one authority | Artifact quality bar |
| Writing craft | Reader modeling, explanation, examples, precision, tone, navigation | Technical writing craft |
| Artifact-specific non-functional parameters | ADR conciseness and immutability; runbook scannability under pressure; PRD persuasive but evidence-based; architecture-view precision | Contract parameters + domain method |

The contract states the outcome; the craft skill teaches how to achieve it. This is why writing is not a section inside every contract and not a separate artifact system.

## Skills organization

### `artifact-system`

The shared artifact model. It owns:

- the artifact model, planes and relations;
- the catalog of artifact types and default homes;
- home resolution and the repository map method;
- the quality bar;
- cross-artifact assurance;
- the artifact contracts.

Start at [artifact system](skills/artifact-system/SKILL.md). Use the [catalog](skills/artifact-system/references/catalog.md) to choose a type, the [homes](skills/artifact-system/references/homes.md) reference to resolve a location, the relevant [contract](skills/artifact-system/references/contracts/README.md) for content, and the [quality bar](skills/artifact-system/references/quality-bar.md) before handoff.

### `activity-system`

The shared routing model. It owns:

- the activity catalog, default results and stopping points;
- transitions and handoffs;
- composition and fallback;
- action authority and unattended execution;
- project fit and proportionality;
- the user-facing help mode.

Start at [activity system](skills/activity-system/SKILL.md). Use the [catalog](skills/activity-system/references/catalog.md) to choose an activity, [transitions](skills/activity-system/references/transitions.md) for handoffs, [composition](skills/activity-system/references/composition.md) for supporting methods, [authority](skills/activity-system/references/authority.md) for action scope and [project fit](skills/activity-system/references/project-fit.md) for proportionality.

### Coordination storage

The storage mechanics for coordination artifacts now live inside `artifact-system` under `references/storage/`: discovery, identity, persistence, revisions, provider limits and access. The reference owns **how** to publish an ECR or research report; the artifact system owns **what** it contains and **where** it belongs.

### `project-conventions` and `setup`

`project-conventions` owns repository foundations, including the artifact home map. `setup` establishes or verifies the map and records a portable pointer. This is how the phases become aware of placement: setup creates the map, implementation reads it, release updates the mapped records.

### `system-documentation` and `system-design`

`system-documentation` discovers and documents the **current** system: entry points, runtime relations, data journeys, deployment topology and the architecture document set. It absorbed the former architecture documentation method. `system-design` owns **proposed** architecture and consequential choices. The artifact system owns the architecture-set contract, status, evidence and home.

### `test`

`test` is the **verification** activity. It selects and runs checks, observes real behavior, reviews completion evidence and reports coverage gaps. It absorbed the former completion method. It does not merge, deploy or publish.

### Contribution workflow

`git-contributions` is a workflow-shaped support method. It owns the ordered mechanics: establish the objective worktree, verify and commit, push, and create or update the pull request. It does not own the PR artifact’s content; the [PR contract](skills/artifact-system/references/contracts/pr.md) owns the reviewer-facing why, what, design impact, validation at the current head, risk, links and visibility. The workflow produces the artifact; the contract defines it.

### Domain methods

Requirements engineering, system design, system documentation, security, operations, database, frontend, backend and AI skills own their subject methods. The artifact contracts link to them by capability; the activity system composes them without duplicating their content.

### Writing craft

Technical writing lives in the documentation plugin. It owns reader fit, explanation, structure, examples, precision, navigation and presentation. It takes audience, purpose and required sections from the artifact contract. It does not own placement, status, evidence or content contracts.

### Explicit upstream workflows

`grill-me`, `grill-with-docs`, `grilling`, `to-spec`, `to-questionnaire`, `retro`, `handoff` and `improve-codebase-architecture` remain explicit workflows. Their names, bodies and native controls are preserved. The activity catalog lists them separately from default activities.

## Composability and reusability rules

1. **One owner per rule.** Link navigation lives in the quality bar, not in every contract. C4 coverage lives in system documentation, not in the ECR contract. Prose craft lives in technical writing, not in the issue template.
2. **Contracts are thin routers, not methods.** A contract says what the artifact must contain and which domain/craft capability to use. It does not re-teach architecture, product strategy or prose.
3. **Progressive disclosure.** The system skill carries the model and reading path. Contracts, activity references and domain skills load only when relevant.
4. **Capability-based composition.** Use available subject and craft expertise by description, not a hardcoded dependency graph.
5. **Stable vocabulary.** Artifact, type, plane, home, authority, maturity, contract, relation, evidence, activity, stopping point, transition, method, workflow, role and phase mean the same thing in every skill.
6. **Separate what / how / where / whether.** What = artifact contract. How = domain method and craft. Where = homes and repository map. Whether = quality bar and assurance.
7. **No universal template.** A PRD, ADR, runbook and ECR have different functional requirements. The shared model is fields and relations, not identical sections.
8. **Evaluate composition, not just individual skills.** A change should be judged by whether the PRD, ECR, RFC/ADR, issue, PR, code, tests, architecture view and runbook agree on scope, status, revision and evidence.

## Reading paths

### For a change

1. Choose the activity in [activity system](skills/activity-system/SKILL.md).
2. Use the [artifact catalog](skills/artifact-system/references/catalog.md) to select the ECR and any linked types.
3. Resolve the ECR home with [artifact homes](skills/artifact-system/references/homes.md) and [coordination storage](skills/artifact-system/references/storage/coordination.md).
4. Read the [ECR contract](skills/artifact-system/references/contracts/ecr.md).
5. Apply the [quality bar](skills/artifact-system/references/quality-bar.md) and [assurance](skills/artifact-system/references/assurance.md).

### For a repository document

1. Read the repository artifact home map.
2. Choose the type: architecture set, ADR, runbook, README, guide, release note or API reference.
3. Read its [contract](skills/artifact-system/references/contracts/README.md).
4. Use the domain method for the subject and [technical writing](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/documentation/skills/technical-writing/SKILL.md) for craft.
5. Apply the quality bar and update the map if the type, home or owner changed.

### For a work product

1. Link it to the ECR, issue, requirement or ADR it implements or verifies.
2. Use the language/framework/test guidance for implementation quality.
3. Record the checked revision and evidence.
4. Reconcile affected architecture views, contracts, runbooks and API reference.
5. Do not turn the work product into a second ECR.

## Boundaries

This is guidance, not an executable gate. Package checks establish structure, links and packaging; they do not establish agent adherence, application behavior or deployment. The activity and artifact systems do not grant permission to create issues, publish documents, merge, deploy or access providers beyond the requested scope.

A compact artifact can pass; a long artifact can fail. The test is whether the reader can decide and act, not whether every heading exists.

## Migration

The former workflow, task, help, completion and per-plugin composition files are retired. Use `activity-system` for routing, `test` for verification, and the repository artifact home map for placement. `system-documentation` absorbed current-state architecture documentation. See the [migration guide](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/migration.md).

## References

| Need | Source |
| --- | --- |
| Artifact model and planes | [artifact model](skills/artifact-system/references/model.md) |
| Type selection and contracts | [artifact catalog](skills/artifact-system/references/catalog.md) |
| Home resolution and repository map | [artifact homes](skills/artifact-system/references/homes.md) |
| Readiness, consistency and convergence | [artifact assurance](skills/artifact-system/references/assurance.md) |
| Activity selection and stopping points | [activity system](skills/activity-system/SKILL.md) |
| Composition and fallback | [activity composition](skills/activity-system/references/composition.md) |
| Coordination storage | [coordination storage](skills/artifact-system/references/storage/coordination.md) |
| Repository foundations | [project conventions](skills/project-conventions/SKILL.md) |
| User-facing guide | [engineering artifacts and workspaces](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/artifact-workflow.md) |
| Migration from old names | [migration guide](https://github.com/joao-aires/agent-skills-public/blob/main/documentation/migration.md) |
