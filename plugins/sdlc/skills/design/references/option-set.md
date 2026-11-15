# Option set: three directions before a decision

Use an option set when a design choice is consequential. The purpose is not to produce many ideas; it is to make a real choice visible by showing alternatives that differ on a dimension that matters.

## When to use it

Use it when at least one is true:

- a new product, substantial redesign or greenfield component;
- navigation, information architecture or a core interaction model;
- an architecture boundary, ownership, state or consistency choice;
- a security, privacy or trust boundary;
- a migration, compatibility or rollout strategy;
- a provider, platform or build-versus-buy choice;
- a decision that is expensive to reverse;
- a change that touches more than one software type;
- the user is explicitly comparing directions.

Do not use it for a routine local fix, a token or copy change, an obvious defect repair or a choice with one evident solution. There, one recommendation with a short rationale is proportionate.

## Minimum

For a consequential choice, present **at least three materially different options**.

"Materially different" means the options differ in responsibility, behavior, ownership, failure handling, cost or another consequential dimension. Three colors, three spacings or three copies of one layout are not an option set.

Each option states:

| Field | Question |
| --- | --- |
| Name | What is this direction? |
| Lens | Which perspective does it optimize? |
| Optimizes | Which outcome or constraint does it serve best? |
| Sacrifices | What does it give up or put at risk? |
| Failure behavior | What happens under error, denial, scale, migration or recovery? |
| Linked artifact | What can the reviewer inspect? |
| Decision | Recommended, rejected, delegated or still open |

## Lenses by software type

Choose lenses that actually separate the options. Read [software types](../../artifact-system/references/software-types.md) for the component types.

| Type | Useful lenses |
| --- | --- |
| Frontend | Task efficiency, trust and accessibility, expressive/brand-led, data density, progressive disclosure, platform-idiomatic |
| Backend | State ownership and consistency, availability/failure/recovery, security/privacy boundary, operability, cost/capacity, migration/compatibility |
| AI | Output quality, evaluation coverage, latency/cost, failure/drift, human control, provider portability |
| Library/CLI | API ergonomics, compatibility, dependency surface, packaging, migration and deprecation |

Constraints add lenses but not new types:

- browser extension: runtime lifecycle, permissions, store review;
- REST API: resource shape, versioning, compatibility;
- multi-tenant SaaS: isolation, entitlements, billing;
- offline-first: sync, conflict, local storage;
- real-time: transport, ordering, reconnection.

## Linked artifacts

Each option needs a linked artifact at comparable fidelity, sufficient to judge the question for its type:

- frontend: wireframe, mockup, Figma frame, rendered slice or prototype;
- backend: contract sketch, sequence, C4 view or state machine;
- AI: context/tool flow, data contract or evaluation plan;
- library/CLI: API/command surface, compatibility matrix or usage example.

Do not compare a detailed mockup against a one-line description. If one option has a linked artifact, the others need one at a comparable level.

## Seam options

When the change touches more than one type, the seam is part of the option set. Each option should state:

- the contract or data shape between the components;
- error and denial mapping;
- loading, empty and no-results distinctions;
- pagination, ordering and freshness;
- auth, tenant and permission boundaries;
- retry, duplicate submit and idempotency;
- versioning and compatibility.

Decide the seam once. Do not let each type section invent its own.

## Decision block

Record the result in the design proposal or ECR solution-design section:

```markdown
Decision:
Options considered:
Chosen because:
Rejected because:
Accepted/delegated by:
Status: proposed | accepted | rejected | superseded
Revisit if:
```

Use the [design proposal contract](../../artifact-system/references/contracts/design-proposal.md) for the full record. Use the [option-set rules](#minimum) above, not a separate document per option.

## Anti-patterns

- three cosmetic variants of one direction;
- options that differ only in implementation detail;
- the same lens applied to every option;
- a recommendation with no alternatives or tradeoffs;
- a linked artifact that does not let the reviewer judge the question;
- options that ignore failure, denial or migration behavior;
- a decision without an owner or revisit trigger;
- duplicating the seam in two type sections instead of deciding it once.

## Small changes

For a reversible, low-impact change, skip the formal option set. State the change, the reason it is sufficient, and any alternative that was considered and rejected. The [design proposal contract](../../artifact-system/references/contracts/design-proposal.md) still applies when the choice is consequential.
