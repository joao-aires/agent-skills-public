# Artifact model: one system for engineering work

An **engineering artifact** is a durable, addressable unit of engineering intent, knowledge, implementation or evidence that a reader can inspect and that has an authority, a lifecycle and a home.

That definition includes documents, code, tests, migrations, contracts, diagrams, issues, pull requests and release records. The ECR is one artifact type — the coordination spine for a change — not the center of the system.

## Why the model exists

The earlier skills were split on different axes: artifact type and lifecycle, subject matter, writing craft and storage placement. Those are orthogonal dimensions, so the skills overlapped. A single artifact model gives every type the same fields, then lets the contract and domain method specialize the content.

The model separates:

- **Functional requirements** — purpose, authority, lifecycle, status, required content, evidence, relations and update rules. These belong in the artifact contract and the domain method.
- **Non-functional requirements** — reader fit, explanation, structure, examples, style, navigation, links and render fidelity. These belong in the shared quality bar plus the writing craft, with the contract supplying audience and style parameters.

## Artifact fields

| Field | Question | Example |
| --- | --- | --- |
| Identity | What stable name or key identifies it? | `ECR-42`, `docs/architecture/containers.md`, `src/queue.mjs` |
| Type | What kind of artifact is it? | ECR, PRD, ADR, issue, PR, architecture set, runbook, code module, test suite |
| Plane | What is its primary role? | Intent, coordination, system knowledge, implementation, delivery, entry |
| Authority | Is it the source of truth for its concern? | Canonical current architecture vs a proposed target view |
| Home | Where does it live? | Engineering workspace, app repo, tracker, git provider, operations repo |
| Maturity | What claim may it make? | Proposed, accepted, implemented, verified, released, superseded, active, retired |
| Reader | Who needs it and for what? | Product, implementer, reviewer, operator, new contributor |
| Contract | What must it contain? | The artifact's contract in this skill |
| Relations | How does it connect? | Derives from, informs, decides, implements, verifies, documents, projects |
| Evidence | What backs its claims? | Source revision, test result, CI run, runtime observation |
| Freshness | When must it be updated or retired? | Boundary change, accepted decision, release, incident |
| Access | Who can read it? | Public, private workspace, audience-specific |

## Planes are roles, not storage

A plane describes the artifact's primary role. It does not describe where the artifact lives.

| Plane | Role | Example artifacts | Typical readers |
| --- | --- | --- | --- |
| Intent | Why and what to pursue | PRD, roadmap, product decision record | Product, leadership |
| Coordination | Track a change, its decisions and evidence | ECR, research report, RFC, issue, PR | Change participants, reviewers |
| System knowledge | Explain the implemented system | Architecture set, contracts, API reference, ADRs, runbooks, SLOs | Contributors, operators |
| Implementation | Build and verify the system | Code, tests, migrations, configuration | Engineers, reviewers |
| Delivery and operations | Release and operate | Release notes, changelog, deployment records, incidents, postmortems | Operators, maintainers |
| Entry and knowledge | Help someone start or learn | README, guides, tutorials, glossary, contributor guide | New users, contributors |

Storage is a separate attribute. An architecture view usually lives in the application repository under `docs/architecture/`; a runbook may live in an operations repository; an ECR lives in the engineering workspace. The same artifact type can move homes without changing its plane or contract. Read [artifact homes](homes.md) for the resolution method and the repository map.

Planes are a navigation view, not an exclusive taxonomy. An artifact has a **primary plane** and may have secondary relations:

- The ECR is coordination-first but links intent, implementation, system knowledge and delivery.
- An ADR is system-knowledge-first but records a change decision.
- A PR is coordination-first but is also delivery evidence.
- A test suite is implementation-first but is also verification evidence.
- A README is entry-first but also describes the system.

Do not force an artifact into one plane when its relations cross planes. The graph handles that; the primary plane is the default reading direction.

## All artifacts are change artifacts

Every artifact participates in change, but not every artifact is a **coordination** artifact.

- **Coordination artifacts** exist to track and communicate a change: ECR, research report, RFC, issue, PR.
- **Work-product artifacts** are produced or updated by the change and have their own authority and lifecycle: code, tests, docs, architecture views, ADRs, runbooks, release records.

The ECR links and reconciles the work products. It does not absorb them, and they do not become sub-documents of the ECR. The application repository remains the authority for implemented system knowledge.

## Relations

Use a small, stable vocabulary so the graph remains readable:

| Relation | Meaning |
| --- | --- |
| `derives_from` | This artifact takes its intent or constraints from another |
| `informs` | This artifact provides evidence or context to another |
| `decides` | This artifact records an accepted choice that constrains another |
| `proposes` | This artifact offers a design that another may accept or reject |
| `implements` | This artifact realizes an accepted change |
| `verifies` | This artifact observes or proves accepted behavior |
| `documents` | This artifact explains the implemented system or its operation |
| `projects` | This artifact presents a view of another authority for an audience |
| `supersedes` | This artifact replaces an earlier artifact or decision |
| `releases` | This artifact records delivery to a target |
| `operates` | This artifact governs running-system behavior |

A view must link to its authority. A projection must not become a second authority. A superseded artifact remains traceable and links its replacement.

## Functional and non-functional requirements

| Requirement | Examples | Owner |
| --- | --- | --- |
| Functional | Purpose, authority, required sections, status, evidence, relations, update and retire rules | Artifact contract + domain method |
| Shared non-functional floor | Self-contained context, readable structure, resolvable links, render fidelity, accessibility, one authority | [Quality bar](quality-bar.md) |
| Writing craft | Reader modeling, explanation, examples, precision, tone, navigation | Writing craft expertise |
| Artifact-specific non-functional | ADR conciseness and immutability; runbook scannability under pressure; PRD persuasive but evidence-based; architecture-view precision | Contract parameters + domain method |

The contract states the outcome; the craft skill teaches how to achieve it. This is why writing is not a section inside every contract and not a separate artifact system.

## Reading path

1. Identify the artifact type and its primary plane using the [catalog](catalog.md).
2. Resolve its home using [artifact homes](homes.md).
3. Read its [contract](contracts/README.md).
4. Apply the [quality bar](quality-bar.md).
5. Apply [assurance](assurance.md) at a handoff or convergence boundary.
6. Use the domain method for the subject and writing-craft expertise for the prose.
