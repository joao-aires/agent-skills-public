# Architecture set contract: the documents that explain the system

An **architecture set** is the coherent group of documents that explain the implemented system's structure, runtime behavior, interfaces, deployment and consequential decisions. It is system-knowledge-first, but it may also record a proposed target view during a change.

This contract defines **which documents the set contains, what each must answer, how the set relates and how it is maintained**. Use available architecture documentation expertise for view selection, C4/arc42 reasoning and source-backed explanation.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the application repository under `docs/architecture/`; a multi-repo system may use a dedicated architecture repository.

## Reader questions

A reader who was not in the conversation must be able to answer:

1. What is the system boundary, and what is outside it?
2. What are the major containers/components, and what does each own?
3. How does a critical operation move through authority, validation, state and an external effect?
4. Where is data owned, stored, cached or projected?
5. How is the system deployed, and what differs between environments?
6. Which interfaces and contracts do consumers depend on?
7. Which quality attributes and failure paths matter?
8. Which decisions constrain the design, and where are they recorded?
9. What is implemented now, what is proposed, and what is unknown?

## Document set

| Document | Must answer | Typical path |
| --- | --- | --- |
| Context view | System boundary, actors, external systems and responsibilities | `docs/architecture/context.md` |
| Container view | Applications, data stores, responsibilities, protocols and trust boundaries | `docs/architecture/containers.md` |
| Component views | Selected components whose internal responsibility or coupling needs explanation | `docs/architecture/components/<name>.md` |
| Runtime/sequence views | Critical journeys, external interfaces, startup/release, failure and recovery | `docs/architecture/runtime/<journey>.md` |
| Data and ownership | Canonical stores, ownership, lifecycle, consistency and migration boundaries | `docs/architecture/data.md` |
| Interface view | Important consumer contracts, authority, errors, idempotency and compatibility | `docs/architecture/interfaces.md` or linked API reference |
| Deployment view | Environments, nodes/processes, storage, networks, release jobs and trust boundaries | `docs/architecture/deployment.md` |
| Quality and failure | Relevant quality scenarios, failure/retry/recovery and observability consequences | `docs/architecture/qualities.md` |
| Decisions | Consequential choices and links to ADRs | `docs/decisions/` linked from the set |
| Glossary | Domain and system terms used consistently across the set | `docs/glossary.md` linked from the set |

Not every system needs every document. Add a document when its independent reader question or lifecycle justifies it. A small application may need only a context view, a container view and a runtime sequence for its critical journey.

## Required content

For each document in the set:

- **Scope and status.** What part of the system it covers, at which revision, and whether it is current, proposed, or partially verified.
- **Elements and responsibilities.** Named elements, what each owns, and the relationships that matter.
- **Text equivalent.** A short prose explanation of the important relationships, so the view is usable when the diagram does not render.
- **Evidence links.** Source paths, contracts, tests, runtime observations or decisions that support the claims. Link exact revisions where the claim depends on them.
- **Uncertainty.** Unknown rationale, unverified deployment state, unowned boundaries and open decisions.
- **Navigation.** A link from the docs index and from related views. A reader should not have to guess where the set starts.

A diagram does not establish architectural truth by itself. A clean C4 view can still be wrong; compare it with source, contracts and observed behavior.

## Current versus target

Keep the distinction explicit:

- **Current** means implemented and evidenced at a linked revision.
- **Proposed** means a target view in an ECR or RFC, not yet implemented.
- **Mixed** means part of the view is current and part is proposed; label the parts.

Do not update the canonical current view to match a proposal. Reconcile it after implementation and link the decision that authorized the change.

## Home and maintenance

| Change | Update |
| --- | --- |
| System boundary, external dependency or trust boundary | Context and container views |
| Component responsibility or coupling | Container or component view |
| Critical journey, authority, state or external effect | Runtime/sequence and data views |
| Public interface or contract | Interface view and API reference |
| Persistence, ownership or migration | Data view and migration/recovery notes |
| Deployment topology or release process | Deployment view |
| Quality target, failure or recovery behavior | Quality/failure view and runbook/SLO links |
| Accepted consequential decision | Decision record and affected views |

Update the set when the implemented system changes. A proposed change updates the ECR/RFC target view first; the canonical set changes only when implementation evidence justifies it.

## Example outline

```markdown
# Architecture — <system>

## Scope and status
What this set covers; current at <revision>; proposed changes linked from <ECR/RFC>.

## Context
Actors, external systems, boundary and responsibilities. [Context diagram]

## Containers
Applications, data stores, protocols, trust boundaries. [Container diagram]

## Critical runtime views
- <journey>: authority → validation → state → external effect → user-visible result.
- Failure/retry/recovery: <what the reader must understand>.

## Data and ownership
Canonical stores, ownership, lifecycle, consistency, migration.

## Interfaces
Important consumer contracts, errors, idempotency and compatibility.

## Deployment
Environments, nodes/processes, storage, networks, release and recovery.

## Qualities and failure
Relevant scenarios, observability, recovery and open gaps.

## Decisions
Links to accepted ADRs.

## Evidence and open questions
Source paths, tests, runtime observations and unresolved facts.
```

## Review

Use the [cold-reader test](../quality-bar.md#3-reader-sufficiency). Can a contributor trace a critical operation, identify authority and state boundaries, explain a failure/retry and locate the evidence? If not, the set is an inventory of diagrams, not an architecture explanation.

Check diagram syntax and rendering separately from architectural truth. A rendered diagram can still misstate the system; a stored diagram can fail to render for the intended reader. Report those as separate limitations.
