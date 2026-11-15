# Artifact contracts

Each contract defines the reader-facing content, status and evidence for one artifact type. Read the contract for the artifact you are creating or materially updating, then apply the [artifact quality bar](../quality-bar.md). Resolve the artifact's home with [artifact homes](../homes.md).

The plane is the artifact's primary role, not its storage. A contract can be used in more than one home.

There is one contract per artifact **type**, not one per software type. A software type changes the representation and evidence an artifact needs; it does not create a parallel contract. Create a new artifact type only when the reader, authority, lifecycle or home differs. Read [software types](../software-types.md) for the four supported types and their constraints.

## Contract, guidance and handoff

A contract is **normative**. It states the artifact's purpose, reader questions, required content, authority, maturity, evidence, relations and the handoff the next phase needs. It is not a drafting guide.

| Layer | Question | Owner |
| --- | --- | --- |
| **Contract** | What must this artifact contain and what may it claim? | This directory |
| **Guidance** | How do I produce and review it well? Examples, structure, anti-patterns, critique | A `guide-*` method, technical writing or the domain method |
| **Handoff** | What does the next phase need, and where does it come from? | The contract's handoff section plus [handoff](../handoff.md) |

A contract may contain a short handoff section; detailed drafting advice, long examples and review checklists belong in guidance. Do not add a new contract because an artifact needs better guidance.

Within a contract file, treat the reader questions, the `## Contract` block, maturity/evidence and `## Handoff` as normative. Treat `## Review`, `## Example`, `## Anti-patterns`, `## Relationship to other artifacts` and “when to use” material as guidance that may move to a dedicated guide as the set matures.

### Current guidance owners

| Contract | Existing guidance | Dedicated guide? |
| --- | --- | --- |
| Product brief / PRD | Product method + technical writing | Candidate |
| RFC | System design + technical writing | Candidate |
| Decision record | System design + technical writing | Candidate |
| Architecture set | System documentation | Candidate for view and set craft |
| ECR | Artifact system examples + assurance | No |
| Design proposal | Design activity + option set + design review | No |
| Runbook | Runbook authoring | No |
| Incident record | Incident response | No |
| Postmortem | Postmortem method | No |
| Assurance assessment | Compliance readiness | No |
| Issue / PR | Git contribution method + technical writing | No |
| Research report | Research method + technical writing | No |
| Release note | Release method | No |
| README / guide | Technical writing | No |
| Work product | Language, framework and test guidance | No |

“Candidate” means the artifact has distinct craft that may justify a dedicated guide later. It does not require a new skill now; technical writing and the domain method already cover the contract.

Read [handoff](../handoff.md) for the phase-to-phase matrix and the rule that a handoff is content, not a document. It may be assembled from several linked artifacts.

## Coordination

| Artifact | Contract | Primary reader |
| --- | --- | --- |
| ECR | [ecr.md](ecr.md) | Change participants, reviewers |
| Research report | [research-report.md](research-report.md) | Decision owner, engineering |
| RFC | [rfc.md](rfc.md) | Design reviewers, decision owner |
| Design proposal | [design-proposal.md](design-proposal.md) | Design reviewers, decision owner, implementer |
| Issue | [issue.md](issue.md) | Implementer, coordinator |
| Pull request | [pr.md](pr.md) | Reviewer |

## Intent

| Artifact | Contract | Primary reader |
| --- | --- | --- |
| Product brief / PRD | [prd.md](prd.md) | Product, engineering, leadership |
| Roadmap | [roadmap.md](roadmap.md) | Product, delivery, leadership |

## System knowledge

| Artifact | Contract | Primary reader |
| --- | --- | --- |
| Architecture set | [architecture-set.md](architecture-set.md) | Contributors, architects, operators |
| Decision record (ADR/PDR) | [adr.md](adr.md) | Future maintainers, decision owners |
| Runbook | [runbook.md](runbook.md) | Operators, on-call responders |
| Incident record | [incident-record.md](incident-record.md) | Responders, reviewers, postmortem facilitators |
| Postmortem | [postmortem.md](postmortem.md) | Future maintainers, action owners |
| Assurance assessment | [assurance-assessment.md](assurance-assessment.md) | Service owners, security/governance reviewers |
| API reference | Use available API/contract expertise and the generated contract; link it from the repository docs index. | Implementers, consumers |
| SLO / signal contract | Use available reliability/observability expertise and the architecture set; link the evidence. | Operators, service owners |

## Implementation

| Artifact | Contract | Primary reader |
| --- | --- | --- |
| Code, tests, migrations, configuration | [work-product.md](work-product.md) | Engineers, reviewers, operators |

Language, framework, database and test guidance owns the substance of a work product. This contract owns its identity, authority, home, relations and evidence.

## Delivery and operations

| Artifact | Contract | Primary reader |
| --- | --- | --- |
| Release note / changelog | [release-note.md](release-note.md) | Reviewers, operators, users |
| Deployment record, credential inventory, vulnerability finding | Use the relevant delivery/operations method and the operational system of record; link the evidence. No competing Markdown copy is required. | Operators, maintainers |

## Entry and knowledge

| Artifact | Contract | Primary reader |
| --- | --- | --- |
| Repository README | [repository-readme.md](repository-readme.md) | New users, contributors |
| Guide / tutorial | [guide.md](guide.md) | Users, contributors |
| Glossary | Use the repository's docs index or glossary page; keep terms consistent with the contracts and architecture set. | All readers |

## Naming note

The product brief contract is named `prd.md`; the catalog calls the artifact "product brief or PRD." The decision record contract covers both ADRs and product decision records (PDRs). The repository README contract is `repository-readme.md` to avoid a case-insensitive filename collision with this index.

The design-proposal contract may be materialized as the ECR solution-design section, an RFC, or a linked design record. The contract governs the content wherever the proposal lives; it does not require a separate file for every change.
