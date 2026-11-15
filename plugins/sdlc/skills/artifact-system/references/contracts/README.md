# Artifact contracts

Each contract defines the reader-facing content, status and evidence for one artifact type. Read the contract for the artifact you are creating or materially updating, then apply the [artifact quality bar](../quality-bar.md). Resolve the artifact's home with [artifact homes](../homes.md).

The plane is the artifact's primary role, not its storage. A contract can be used in more than one home.

There is one contract per artifact **type**, not one per software type. A software type changes the representation and evidence an artifact needs; it does not create a parallel contract. Create a new artifact type only when the reader, authority, lifecycle or home differs. Read [software types](../software-types.md) for the four supported types and their constraints.

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
