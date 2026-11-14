# Roadmap contract: sequence outcomes across changes

A **roadmap** coordinates several changes toward outcomes. It is intent-first and owns sequencing, prerequisites, ownership and the boundary between proposed and committed work. It is not a backlog of tasks, a release note or an ECR.

Apply the [artifact quality bar](../quality-bar.md) and resolve the home with [artifact homes](../homes.md). The default home is the product/project workspace; a repository `docs/product/roadmap.md` is an acceptable alternate when the team keeps product direction with the code.

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
# <Product or programme> roadmap

## Outcomes
The outcomes the sequence serves, with the evidence or assumptions behind them.

## Sequence
Ordered outcomes or work packages, with dependencies and prerequisites.

## Commitment
Committed, proposed, exploratory and explicitly deferred items.

## Ownership
Outcome owners, decision owners and coordination points.

## Links
PRDs, ECRs, issues and decisions that carry the work.
```

Guidance:

- **Outcomes.** Describe the change in user, business or system terms. Do not list features without the outcome they serve.
- **Sequence.** Explain why the order matters: dependencies, risk, learning, capacity or commitments. A list without dependencies is a backlog.
- **Commitment.** Use explicit labels: committed, proposed, exploratory, deferred. A roadmap item is not authorized implementation.
- **Ownership.** Name the owner or role when known. Do not invent commitments or dates.
- **Links.** Link the PRD, ECR or issue that carries each item. The roadmap summarizes and sequences; it does not duplicate the change record.

## Home and maintenance

Keep one current roadmap in the established product/project home. Update it when priorities, dependencies, owners or commitments change. Do not rewrite history to make a missed commitment disappear; record the change and its reason.

## Review

Can a reader understand what is committed, what is proposed, why the order makes sense and where the work is recorded? If the roadmap is only a list of feature names, it is not a roadmap.
