# Work-product contract: code, tests, migrations and configuration

A **work product** is the implementation artifact that realizes an accepted change: source code, tests, migrations, configuration or a generated contract. It is implementation-first but is also verification and delivery evidence.

This contract owns the work product's **identity, authority, home, relations and evidence**. Language, framework, database, test and platform guidance owns its substance and quality. The artifact system does not prescribe code style.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the application repository.

## Reader questions

A reader who was not in the conversation must be able to answer:

1. What behavior or contract does this work product implement?
2. Where does it live, and what is the authoritative revision?
3. Which change, requirement or decision does it realize?
4. What evidence shows it works, and what remains unverified?
5. What compatibility, migration or operating effect does it have?
6. Who owns it, and what must change when its boundary changes?

## Contract

| Field | Required |
| --- | --- |
| Identity | Repository-relative paths, package/module names and the current revision |
| Authority | Whether this is the canonical implementation or a generated/projected artifact |
| Home | Application repository, package repository or monorepo path |
| Relations | The ECR, issue, requirement, ADR or interface it implements or verifies |
| Maturity | Proposed, implemented, verified, released or superseded, per claim |
| Evidence | Commands, tests, CI run or runtime observation at the checked revision |
| Compatibility | Consumer contracts, migrations, configuration and rollout effects |
| Freshness | What triggers an update: behavior, contract, dependency, security or platform change |
| Owner | Team or role responsible for the work product |

Do not claim a work product is verified because it compiles, because a test exists or because CI is configured. Link the observed check and the revision.

## Relations

A work product usually has several relations:

- `implements` an ECR increment, accepted requirement or issue.
- `verifies` an acceptance case when it is a test.
- `documents` a contract when it is a generated schema or API definition.
- `decides` nothing by itself; a consequential choice belongs in an ADR.
- `releases` through a delivery record; the work product itself does not establish deployment.

Link the change record and the evidence, not every file in the repository. A work product is not a second ECR.

## Home and maintenance

The application repository is the default home. A monorepo may keep a package path; a shared library may live in a package repository. Preserve the established layout and build tooling.

Update the work product and its affected documentation together when behavior, contracts, persistence, configuration or dependencies change. Reconcile the architecture set, ADRs, runbooks and API reference when their boundaries change.

## Review

Use the repository's language/framework/test guidance for code quality and the [artifact quality bar](../quality-bar.md) for the handoff:

- Can a reviewer identify the intended behavior and the exact checked revision?
- Do the tests observe the promised result, including denial and failure paths where relevant?
- Are the affected contracts, migrations and configuration changes linked?
- Is the evidence at the current revision, not an older head?
- Are generated artifacts linked to their source rather than maintained as competing copies?
