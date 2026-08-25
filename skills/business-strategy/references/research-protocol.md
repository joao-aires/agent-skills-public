# Claim-Led Research Protocol

## Principle

Research should reduce uncertainty around a decision, not maximize the number of sources collected.

Start with the thesis and ask:

> Which uncertain claims, if wrong, would most change the strategy?

Prioritize approximately by:

```text
research priority = decision impact × uncertainty × cost of being wrong
```

## 1. Create decision-changing claims

For standard/deep work, write 5–15 high-impact claims with stable IDs.

Example:

```text
C01 — Mid-market security teams have an urgent budgeted need for cross-vendor agent governance.
C02 — Existing cloud platforms will not eliminate the need for an independent control plane within 24 months.
C03 — A developer-led OSS wedge can convert naturally into enterprise governance spend.
```

Avoid claims that are merely topics:

- bad: "AI agent market growth"
- good: "The number of production agent deployments is growing fast enough that governance becomes a budgeted problem within 24 months."

## 2. Classify the claim

Useful types:

- demand / customer behavior
- market size
- competitor capability
- competitor trajectory
- technology / feasibility
- regulation
- pricing / willingness to pay
- distribution
- unit economics
- future-market structure

The claim type should determine the preferred source route.

## 3. Route evidence to the claim

Prefer evidence generated closest to the underlying fact.

Examples:

- pricing → official pricing pages, contracts, procurement sources
- public-company economics → filings and investor materials
- regulation → regulator / legislation
- product capability → official docs plus practitioner evidence
- customer pain → interviews, reviews, forums, support discussions, workflow observation
- market counts → government/industry datasets or transparent bottom-up estimates
- private revenue/valuation → credible reporting, clearly labeled as reported estimates

Top-down consultancy market reports are directional, not ground truth.

## 4. Maintain an evidence ledger

For deep work, record each meaningful evidence item with:

- claim ID
- source
- date / period
- geography
- evidence type
- supporting or contradicting
- key fact
- source quality
- confidence impact
- notes on definitions or limitations

Use `../assets/evidence-ledger-template.md`.

## 5. Separate epistemic types

Every important statement should be identifiable as one of:

- **Fact** — directly supported
- **Derived calculation** — computed from explicit inputs
- **Inference** — reasoned conclusion from facts
- **Assumption** — required but unverified belief
- **Strategic judgment** — choice made under uncertainty

Do not make an inference look like a sourced fact.

## 6. Search for disconfirmation

For each critical thesis claim, ask:

- What would a skeptic search for?
- Who benefits if this claim is believed?
- What evidence would show the opposite?
- Is there a failed precedent?
- Is the observed demand actually caused by a temporary transition?

A strategy that only accumulates confirming evidence is fragile.

## 7. Independence and contradiction handling

Two articles repeating one press release are one evidence origin, not two independent confirmations.

When sources conflict, do not average automatically. Check:

- definition
- time period
- geography
- sample / methodology
- accounting basis
- incentives
- whether one source is downstream of the other

Record unresolved contradictions when they matter.

## 8. Confidence

Use simple confidence levels:

- **High** — strong direct evidence from multiple independent origins
- **Medium** — reasonable evidence but meaningful uncertainty remains
- **Low** — indirect, sparse, stale, or contradictory evidence

Confidence should be claim-specific, not one rating for the whole report.

## 9. Gap closure

After an initial research pass:

1. identify the highest-impact unresolved claims;
2. run targeted follow-up research;
3. stop when additional evidence is unlikely to change the decision or the search budget is exhausted;
4. state remaining gaps explicitly.

Do not polish an answer into certainty when a critical claim remains unresolved.

## 10. Synthesis

Research synthesis is not a summary of sources.

For each high-impact finding ask:

- So what does this imply for the strategy?
- Which option becomes stronger or weaker?
- Which assumption changes confidence?
- Does the thesis need to mutate?
- What should be researched or tested next?

The result should be an updated decision, not a bibliography.