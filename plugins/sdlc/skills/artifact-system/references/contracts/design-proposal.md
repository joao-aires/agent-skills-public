# Design proposal contract: options, linked artifacts and the decision

A **design proposal** records a consequential design choice before implementation: the question, the constraints, at least three materially different options, the linked design artifacts that let a reviewer judge them, the tradeoffs, the seam decisions and the recommendation.

It is coordination-first. It may be materialized as the ECR solution-design section, an RFC, or a linked design record. It is not an implementation plan and does not claim implemented behavior.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). Read [software types](../software-types.md) for the affected component types.

Read the [design proposal guide](../../../design-proposal-guide/SKILL.md) for writing conventions, examples and review checks.

## Reader questions

A reviewer, implementer or future maintainer must be able to answer:

1. What decision is being made, and what constraints bound it?
2. Which components and software types are affected, and which are not?
3. Which materially different options were considered, and from which perspectives?
4. What linked artifact lets me judge each option's behavior?
5. What does each option optimize, sacrifice and do under failure or denial?
6. When several components meet, what has been decided at the seam?
7. Which option is recommended, who decides, and when should the decision be revisited?
8. What evidence exists, and what remains unknown?

## When to use it

Use a design proposal when the choice is consequential:

- a new product, substantial redesign or greenfield component;
- navigation, information architecture or a core interaction model;
- an architecture boundary, ownership, state or consistency choice;
- a security, privacy or trust boundary;
- a migration, compatibility or rollout strategy;
- a provider, platform or build-versus-buy choice;
- a decision that is expensive to reverse;
- a change that touches more than one software type.

Do not require it for a routine local fix, a token or copy change, an obvious defect repair or a change with one evident solution. There, one recommended change with a short rationale is proportionate.

## Materialization

Use the lightest form that meets the sufficiency floor:

| Form | When |
| --- | --- |
| ECR solution-design section | A normal change; the proposal fits in the change record |
| RFC | The proposal needs its own audience or decision process |
| Linked design record | The linked artifacts, review or audience justify a separate document |

If a linked design record or RFC is used, the ECR summarizes the decision and links the authority. Do not duplicate the full proposal in both.

## Contract

```markdown
# <Decision title>

## Question and constraints
The decision, the accepted outcome, the constraints, the current state or
"greenfield; no implementation exists", and the authority source.

## Affected software types
Per component: type, status (designed / not affected / undecided), and the
reason. Include the seam when more than one type is involved.

## Options
At least three materially different options when the choice is consequential.
For each: name, perspective or lens, what it optimizes, what it sacrifices.

## Linked design artifacts
One or more linked artifacts per option, at comparable fidelity, sufficient to
judge the option for its software type. Link the design specification, C4 view,
sequence view, state machine, compatibility matrix or evaluation plan.

## Tradeoffs and failure behavior
How each option behaves under error, denial, concurrency, migration,
recovery, cost or other relevant failure. State the evidence and its limits.

## Seam decisions
When several types meet: error and denial mapping, loading/empty distinctions,
pagination, auth/tenant boundaries, retry/idempotency, versioning and
compatibility. Decide once and reference it from each type section.

## Recommendation and decision
Recommended option, why, who accepts it, status, accepted/rejected
alternatives, revisit trigger and owner.

## Evidence and open questions
What was inspected or probed, at which revision or target, and what remains
unknown or undecided.
```

## Linked artifacts by software type

A linked artifact is sufficient when a reviewer can judge the option's behavior for the active type. It is an artifact with its own contract or guide, not the design decision. Read the matching guide for structure, notation, fidelity and review.

| Type | Typical linked artifacts | Guide |
| --- | --- | --- |
| [Frontend](../software-types/frontend.md) | Wireframe, mockup, Figma frame, rendered slice, interactive prototype, component-state view | [Design specification](../../../design-spec-guide/SKILL.md) |
| [Backend](../software-types/backend.md) | API/event contract, sequence, C4 context/container/component, data/ownership view, state machine | [C4](../../../c4-view-guide/SKILL.md), [sequence](../../../sequence-view-guide/SKILL.md), [state machine](../../../state-machine-guide/SKILL.md) |
| [AI](../software-types/ai.md) | Context/retrieval/tool flow, data contract, evaluation plan and case matrix, harness view | Use the available AI testing method for the evaluation plan |
| [Library/CLI](../software-types/library-cli.md) | API or command surface, compatibility matrix, dependency surface, usage and failure examples | [Compatibility matrix](../../../compatibility-matrix-guide/SKILL.md) |

Use the [architecture-set contract](architecture-set.md) when a C4, sequence or data view becomes durable system knowledge. Use the [diagram lifecycle](../diagram-lifecycle.md) to keep current and proposed views distinct.

## Decision block

End the proposal with a compact decision block that can be carried into an ADR or RFC:

```markdown
Decision:
Options considered:
Chosen because:
Rejected because:
Accepted/delegated by:
Status: proposed | accepted | rejected | superseded
Revisit if:
```

## Handoff

The implementation consumer must know the decision, affected software types, options, linked design artifacts, seam, start/blocked state and open questions. See [handoff](../handoff.md).

## Maturity

Use **proposed**, **accepted**, **rejected** and **superseded**. A proposal may be proposed while the surrounding implementation does not exist. A proposed option is not an accepted design, and an accepted design is not implemented behavior.

## Review

Read the proposal as an implementer who was not in the conversation:

- Is the decision and its constraints clear?
- Are at least three options materially different, not cosmetic variants?
- Does each option have a linked artifact a reviewer can judge?
- Are the failure, denial, migration or recovery consequences stated?
- Is the seam decided once when several types meet?
- Is the recommendation explicit, with an owner and a revisit trigger?
- Are unaffected types stated, not silently omitted?

If the proposal only lists preferences, or presents three variations of one direction, it is not a design proposal.

## Anti-patterns

- Three color, spacing or copy variants presented as options.
- Options that differ only in implementation detail, not in responsibility or behavior.
- A recommendation without alternatives or tradeoffs.
- A linked artifact that does not let the reviewer judge the question.
- Two type-specific proposals that duplicate the same seam.
- A proposal that claims "accepted" without a decision owner.
- A proposal that silently omits an affected type.
