# Roadmap contract: sequence outcomes across changes

A **roadmap** coordinates several changes toward outcomes. It is intent-first and owns sequencing, prerequisites, ownership and the boundary between proposed and committed work. It is not a backlog of tasks, a release note or an ECR.

A **product roadmap** expresses product direction for a product, segment or journey; the product-direction decision belongs to Plan and its owners. A strategic roadmap is a pre-SDLC strategy record owned by the strategy pack, not this artifact. This contract records and sequences the direction it is given; it does not accept the strategy or priority itself.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the product/project workspace; a repository `docs/product/roadmap.md` is an acceptable alternate when the team keeps product direction with the code.

Read the [roadmap guide](../../../guide-roadmap/SKILL.md) for writing conventions, examples and review checks.

## Reader questions

A reader who was not in the conversation must be able to answer:

1. What outcomes are we pursuing, and for whom?
2. In what order, and why that order?
3. What must be true before each step can start?
4. What is committed versus proposed or exploratory?
5. Who owns each outcome or decision?
6. Which ECRs, PRDs or issues carry the work?

## Contract

```markdown
# <Product> roadmap

## Horizon
Now, Next and Later, with what each horizon means for this product.

## Outcomes
The outcomes the sequence serves, with the evidence or assumptions behind them.

## Sequence
Ordered outcomes or work packages, with dependencies and prerequisites.

## Commitment
Committed, proposed, exploratory and explicitly deferred items.

## Confidence
Per outcome: the evidence behind it, what would change the sequence and its review trigger.

## Capacity
The assumed capacity and the constraint that makes the sequence feasible.

## Ownership
Outcome owners, decision owners and coordination points.

## Status and review
Document maturity, review cadence and the events that reopen the sequence.

## Links
PRDs, ECRs, issues and decisions that carry the work.
```

Guidance:

- **Outcomes.** Describe the change in user, business or system terms. Do not list features without the outcome they serve.
- **Sequence.** Explain why the order matters: dependencies, risk, learning, capacity or commitments. A list without dependencies is a backlog.
- **Commitment.** Use explicit labels: committed, proposed, exploratory, deferred. Now/Next/Later is a horizon view, not a substitute for commitment. A roadmap item is not authorized implementation.
- **Ownership.** Name the owner or role when known. Do not invent commitments or dates.
- **Links.** Link the PRD, ECR or issue that carries each item. The roadmap summarizes and sequences; it does not duplicate the change record.

## Handoff

The delivery and product reader needs the outcomes, sequencing, prerequisites, committed versus proposed work and owners. Link the ECRs, PRDs and issues rather than copying them. See [handoff](../handoff.md).

## Home and maintenance

Keep one current roadmap in the established product/project home. Update it when priorities, dependencies, owners or commitments change. Do not rewrite history to make a missed commitment disappear; record the change and its reason.

## Review

Can a reader understand what is committed, what is proposed, why the order makes sense and where the work is recorded? If the roadmap is only a list of feature names, it is not a roadmap.
