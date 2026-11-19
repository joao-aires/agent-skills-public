# Pricing and Packaging

## Purpose

Pricing is a strategy choice, not a calculation applied after the product is built. It determines who can buy, which value is captured, what the sales motion must be and which customers the business attracts.

Use this reference when setting or changing price, packaging, the pricing metric or discount policy. Use [revenue quality and unit economics](revenue-quality-and-unit-economics.md) for margin and retention definitions, and [financial scenario modeling](financial-scenario-modeling.md) for the revenue effect of a pricing choice.

## Price against value, not cost

Cost sets the floor; the alternative is the reference point, not the ceiling. Value-based pricing starts from the customer's next-best option and the value of the improvement, so the ceiling is the next-best cost plus the value that improvement has for this customer (or their stated willingness to pay), less switching cost.

```text
willingness to pay: next-best cost
  + value of the improvement (less switching)
          ↑
     price range
          ↑
our cost to serve + required contribution
```

Estimate:

- the full cost of the alternative — license, implementation, operations, internal labor, failure cost;
- the economic value of the difference, in the customer's unit;
- how much of that difference the customer must keep to justify switching;
- which budget the purchase comes from and who controls it;
- what the customer has paid for comparable outcomes.

Do not infer willingness to pay from a competitor's list price. Their price reflects their cost structure, positioning and discount behavior, not this customer's value.

### Value split

A useful discipline is to state the split explicitly:

```text
value created per year:      €X
price to customer per year:  €Y
customer's retained value:   €X − Y − switching cost
```

If the customer's retained value is thin or negative, the deal depends on persuasion rather than economics and will not renew.

## Willingness-to-pay evidence

Rank methods by what they can actually establish.

| Method | Establishes | Limits |
|---|---|---|
| Observed purchases of alternatives | Budget exists and a price point is accepted | Different product, different value |
| Win/loss and negotiation records | Resistance points and discount behavior | Mix of segments and sales skill |
| Direct price conversations with buyers | Ranges, budget constraints, trade-offs | Stated intent, relationship effects |
| Priced pilot or pre-order | Willingness to commit real money | Small n, early-adopter bias |
| Choice-based or conjoint study | Relative preference across features and prices | Hypothetical, sample-dependent, costly |
| Price test in a live funnel | Conversion response at a price point | Confounded by traffic mix and season |
| Van Westendorp-style ranges | Plausible price band for a category | Not a demand forecast; needs interpretation |

Rules:

- Ask about the alternative and the budget before asking about your price.
- Test a range, not a single number. Anchoring on one price produces a yes/no about that price.
- Separate "too expensive" from "not my budget" and "not worth the change".
- Never present a survey or an interview as evidence of demand; only a commitment is.
- Segment the evidence. An enterprise buyer and a self-serve user answer different questions.

Use [experiments and PMF](experiments-and-pmf.md) to define the bar before running a price test.

## The pricing metric

The metric should scale with the value the customer receives and be predictable enough to budget.

Common metrics:

- seats or active users;
- usage — transactions, documents, tokens, events, queries;
- capacity — storage, environments, connected accounts;
- outcome — resolved case, processed invoice, qualified lead;
- platform fee plus usage;
- transaction take rate.

Evaluate a metric on:

- **alignment** — does the bill grow when the customer's value grows?
- **predictability** — can the customer forecast the bill?
- **controllability** — can the customer influence cost by changing behavior?
- **measurability** — can both sides agree on the count?
- **gaming** — can the customer reduce the metric without reducing value?
- **sales complexity** — can it be explained in one sentence?
- **margin protection** — does it track variable cost, especially for AI or infrastructure?

A metric that is technically precise but impossible to forecast creates procurement friction and churn. A metric that is easy to budget but disconnected from value leaves money on the table or punishes success.

## Packaging and tiers

Packaging translates value into a choice the buyer can make.

Define:

- **entry offer** — the smallest thing that delivers a complete outcome;
- **core offer** — the standard buying unit for the beachhead;
- **expansion** — what increases with usage, teams, workflows or outcomes;
- **enterprise** — governance, assurance, integration and commercial terms;
- **free or open-source boundary** — what must be free for adoption and trust, and what must be paid for to fund delivery.

Good packaging:

- differentiates by **job and outcome**, not by arbitrary feature slices;
- keeps the entry tier genuinely useful;
- makes the upgrade reason obvious to the customer, not only to sales;
- prices the value-bearing dimension;
- avoids gating capabilities that create trust or safety;
- limits the number of tiers to what a buyer can compare.

Bad packaging patterns:

- feature soup with no coherent job per tier;
- a free tier that removes the reason to pay;
- enterprise-only basics such as security or export;
- usage pricing the customer cannot forecast;
- per-seat pricing for a product whose value does not grow with seats;
- discounts that vary by salesperson rather than by segment or term.

For AI and infrastructure products, check whether the package exposes variable cost honestly. A flat price with unbounded inference or compute can produce revenue growth and margin collapse. See [revenue quality and unit economics](revenue-quality-and-unit-economics.md).

## Unit economics

Pricing is only defensible if the economics survive it.

### Contribution

```text
revenue per customer
− variable delivery cost (infrastructure, inference, support, payment fees, third-party APIs)
− service cost that scales with the customer
= contribution
```

### CAC, payback and lifetime value

[Revenue quality and unit economics](revenue-quality-and-unit-economics.md) owns the CAC, payback and lifetime-value definitions; use them rather than a second formula. State what is included in CAC: one that excludes sales salaries or partner commissions is not comparable across motions.

Treat this as a rough planning estimate, not a precise asset. It is sensitive to churn assumptions, expansion, discounting and cost drift. For recurring revenue, a cohort-based view is stronger than a blended average.

### Retention and expansion

Use logo retention, net revenue retention and cohort behavior; do not use a single churn number for all segments. Pricing changes affect retention, and retention affects whether a low price is actually cheap.

### Segment margins

Compute unit economics by segment, not only in aggregate. Enterprise and self-serve commonly differ in:

- acquisition cost and cycle length;
- implementation and support burden;
- gross margin and infrastructure intensity;
- expansion path and ceiling;
- concentration and renewal risk;
- discount depth and payment terms.

A blended CAC or margin can hide a segment that is subsidized by another. State which segment the strategy depends on and whether its economics work on their own.

## Price changes

When changing price or packaging:

- define the objective — revenue, mix, margin, adoption or positioning;
- model the response by segment, including churn and downgrade;
- decide grandfathering, notice period and migration path;
- prepare the sales narrative and objection handling;
- set a review window with leading indicators;
- keep contracts and communications consistent with what was promised.

Do not use a price increase to fix a value problem; it usually accelerates churn in the segment with the weakest value.

Discounting is a pricing decision. Define who can discount, on what basis, and what is exchanged — term, volume, reference, case study, prepayment. Uncontrolled discounting teaches the market that the list price is fictional.

## Decision record

For a material pricing or packaging change, record:

```text
Decision:
Segment and offer affected:
Current price, metric and packaging:
Proposed change:
Value and alternative evidence:
Willingness-to-pay evidence and limits:
Unit economics at the proposed price:
Migration and grandfathering:
Expected effect on mix, churn and margin:
Leading indicators and thresholds:
Revisit trigger:
Status (proposed / accepted / rejected):
```

Keep it with `decision-log.md` if persistent state exists.

## Failure modes

- Cost-plus pricing that captures none of the value created.
- Copying competitor prices and calling it market pricing.
- A pricing metric that grows with usage but not with value.
- Packaging designed to win the demo rather than to serve a job.
- Quoting ARR without the cost to serve it.
- Using LTV as proof of a good business while payback is unmeasured.
- Reporting blended unit economics that hide a loss-making segment.
- Testing price on a sample that cannot buy.
- Treating a discount as a sales tactic rather than a strategic signal.
- Raising price to compensate for weak retention.

## Output

End with:

- the pricing logic and the evidence for it;
- the chosen metric and why it tracks value;
- the packaging and the upgrade path;
- unit economics by segment, with assumptions and sensitivity;
- the migration and communication plan for a change;
- the indicators that would reopen the decision.

The useful result is a price the target customer can justify internally and the company can defend economically.
