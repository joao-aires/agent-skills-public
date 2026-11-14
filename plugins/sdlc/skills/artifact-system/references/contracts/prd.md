# Product brief / PRD contract: product intent, not an engineering record

A product brief or PRD owns **product intent**: the user problem, the audience, the desired outcome, priority, scope and success signal. It does not own implementation design, engineering verification or release evidence. Those belong in the ECR, RFC and PR.

Apply the [artifact quality bar](../quality-bar.md). The brief is complete when a product or engineering reader can understand who the work is for, what outcome matters, what is excluded, and what would change the priority.

## Contract

```markdown
# Product outcome

## Problem and audience
Who is affected, what is costly or missing today, and the evidence.

## Desired outcome
What becomes possible for the user or business, in observable terms.

## Scope and non-goals
What this direction includes and what it deliberately excludes.

## Success signal
The product evidence that would show the outcome is working.

## Constraints and dependencies
Product, commercial, legal, platform or delivery constraints that shape the choice.

## Open decisions
What still needs a product decision, the owner, and the next evidence.

## Links
Research, strategy, roadmap, related briefs and any ECR that carries the work.
```

Guidance:

- **Problem and audience.** Name the user or segment and the observed problem. Link research, support evidence, analytics or a decision record. Do not substitute a solution for the problem.
- **Desired outcome.** Describe what the user can do or what the business can observe. Avoid invented metrics; if a success signal is unknown, mark it open.
- **Scope and non-goals.** State the useful slice and what is deferred. This is the boundary that keeps implementation from expanding.
- **Success signal.** Use existing evidence or an explicit proposed signal. Distinguish a hypothesis from an accepted target.
- **Constraints and dependencies.** Include product, commercial, legal, platform and delivery constraints that could change the decision. Do not silently accept an undisclosed obligation.
- **Open decisions.** Name the choice, its owner and what evidence would settle it.
- **Links.** Link research, strategy, roadmap, related briefs and the ECR that carries the change. Use the [link rules](../quality-bar.md#4-resolvable-navigation).

## Maturity

A product brief moves from **draft** to **proposed** to **accepted** or **superseded**. It does not claim implementation or verification. If the product direction changes, preserve the prior decision and link the replacement rather than rewriting history.

## Relationship to other artifacts

- **Product strategy and discovery** expertise owns the product method: market, user, priority and value reasoning.
- The **brief or PRD** owns the product-intent document and its reader completeness.
- The **roadmap** owns sequencing across changes.
- The **ECR** owns the engineering change, requirements, design, verification and release evidence. Link the brief; do not copy it into the ECR.
- A **product decision record (PDR)** owns a durable product decision. Use the [decision record contract](adr.md) with product-specific context.

## Reader test

A reader who was not in the conversation must be able to answer:

1. Who is this for, and what problem does it solve?
2. What outcome matters, and what would show it is working?
3. What is in scope, and what is deliberately excluded?
4. What constraint or dependency could change the decision?
5. What is still undecided, who owns it, and where is the evidence?

## Example outline

> **Saved-search sharing for a two-person research team**
>
> **Problem and audience.** The team maintains saved searches locally and cannot hand a curated set to a colleague. Today they copy queries by hand; the observed cost is repeated setup and inconsistent results.
>
> **Desired outcome.** A team member can share a saved search with a colleague who can open and run it without retyping the query.
>
> **Scope and non-goals.** In scope: one-to-one sharing of an existing saved search, with the owner's permission. Out: public galleries, team-wide defaults, cross-workspace sharing.
>
> **Success signal.** A shared search opens with the same query and filters, and the recipient can run it without contacting the owner. Proposed until measured.
>
> **Constraints and dependencies.** The existing saved-search model and permission boundary must be preserved. No new external service.
>
> **Open decisions.** Whether a shared search is a copy or a live reference; owner: product. Whether revocation is required in the first slice; owner: security.
>
> **Links.** [Research](https://example.invalid/research), [roadmap](https://example.invalid/roadmap), [ECR](https://example.invalid/ecr).
