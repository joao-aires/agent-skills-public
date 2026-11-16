# Strategy option set

Use this reference in `explore` and `decide` work, and whenever `develop` or `review` reopens a material choice. Its purpose is to prevent a polished recommendation for the first plausible idea. The option set is a decision instrument, not a catalogue of features.

## Minimum set

Before converging, develop **at least three materially different strategies or business models**. A different feature list, price point, segment label or visual identity is not a different strategy if the customer, wedge, product layer, channel and monetization remain the same.

- At least one option should challenge the initial concept's core assumption, not merely execute it better.
- Include the status quo or do-nothing path as a baseline. It may be one of the three only when it is a genuine strategy with its own economics and risks, not a placeholder.
- Each option must be one a competent operator could choose. A deliberately weak option is a strawman, not an alternative.
- Compare options at the same scope, time horizon and definition of customer, segment and market. Changing the horizon mid-comparison can make a slow, durable option look inferior to a fast, fragile one.
- If two options differ only in execution quality, treat them as one strategy with a capability comparison.

## Option matrix

Use the same fields for every option. Leave a field blank only when it is genuinely immaterial, and say why.

| Field | Option A | Option B | Option C |
| --- | --- | --- | --- |
| Option and thesis | | | |
| Customer/segment and economic buyer | | | |
| Wedge / entry job | | | |
| Product layer / scope | | | |
| Channel / GTM | | | |
| Monetization / pricing metric | | | |
| Capital intensity | | | |
| Time-to-value | | | |
| Profitability path (margin, payback, path to positive unit economics) | | | |
| Key risks | | | |
| Defensibility / control point | | | |
| Leading indicators | | | |
| Opportunity cost | | | |
| Evidence and confidence | | | |
| What must be true / kill criteria | | | |

Field guidance:

- **Customer/segment and economic buyer.** Name who pays and who uses or benefits. A different buyer can change the product, channel and sales motion more than a different feature set does.
- **Wedge / entry job.** State the first job, use case or beachhead and why it creates a path to the larger position. A wedge that does not expand is a niche, not a strategy.
- **Product layer / scope.** Locate the offer in the value chain: application, workflow layer, infrastructure, data, marketplace, service or component. Different layers imply different control points and competitors.
- **Channel / GTM.** Identify how the buyer is reached: self-serve, sales-led, partner, marketplace, ecosystem, community or embedded distribution. Channel economics and cycle time belong here, not in a separate marketing plan.
- **Monetization / pricing metric.** State who pays, for what outcome and on what metric. Test whether the model changes adoption, buyer, product or channel.
- **Capital intensity.** Compare upfront investment, working capital, infrastructure, inventory, compliance and people. A capital-light option with weak defensibility is not automatically better.
- **Time-to-value.** Distinguish time to first customer value, time to meaningful revenue and time to a repeatable motion. Fast learning can be more valuable than fast revenue.
- **Profitability path.** Use gross margin, variable-cost exposure, payback and a stated path to positive unit economics. Do not compare revenue without the cost to serve it.
- **Key risks.** Include execution, adoption, competition, platform dependency, regulatory, financing and capability risks. State which risk would end the option.
- **Defensibility / control point.** Name what accumulates, what is scarce and what prevents the position from being copied or bundled away. "First mover" and "AI" are not mechanisms.
- **Leading indicators.** Choose observable signals that would move before revenue proves the thesis: activation, time to first value, repeat use, sales-cycle length, pull-through, retention cohort, gross margin, channel payback. Give a baseline, threshold and review window.
- **Opportunity cost.** State what the option forecloses: capital, time, focus, a channel, an option to expand later, a customer relationship or strategic flexibility. Include cannibalization where relevant.
- **Evidence and confidence.** Separate fact, derived calculation, inference, assumption and strategic judgment. Do not let a filled cell imply evidence that does not exist.
- **What must be true / kill criteria.** Record the assumptions the option depends on and the evidence that would stop it. An option without a kill criterion is a preference.

## Material-difference test

Ask of each pair:

1. Does the customer, segment or economic buyer change?
2. Does the wedge or first job change?
3. Does the product layer or scope change?
4. Does the channel or GTM motion change?
5. Does the monetization model or pricing metric change?
6. Do capital intensity, time-to-value or profitability structure change enough to require different capabilities?

If the answer is no to all six, the options are variants. Merge them and generate a real alternative. If only one dimension changes, explain why that single change is strategically material rather than a repositioning of the same business.

## Comparison discipline

- Use ranges and stated assumptions for capital, pricing and profitability. False precision hides disagreement.
- Keep the same currency, period and market definition across options. Normalize one-time and recurring costs.
- Do not use a weighted score as the decision. Scoring can expose trade-offs; the recommendation still needs causal reasoning.
- Actively look for evidence that weakens the preferred option. An option set that only confirms the initial concept is not an option set.
- Distinguish a reversible experiment from a path-dependent commitment. Cheap learning can justify a weaker near-term option; an irreversible choice needs more evidence.
- Include the do-nothing baseline in the opportunity-cost discussion, not only in the matrix.

## Anti-patterns

- Three versions of the same product with different feature counts.
- A "premium" and a "self-serve" option that share the same buyer, channel and cost structure.
- A strawman "do nothing" or a deliberately bad third option.
- Comparing a mature incumbent's economics with a new option's early-stage economics on the same scale without adjustment.
- TAM-only comparison that ignores reachable demand, channel access and cost to serve.
- Treating a competitor's price as willingness to pay.
- Choosing first and backfilling criteria, weights or evidence.
- Ignoring cannibalization, channel conflict or opportunity cost.
- Presenting a recommendation without naming what was rejected and why.
- Confusing an option's narrative with its unit economics.
- Applying the full matrix to a bounded operational question that is not a strategy or business-model choice; handle that as a light question outside `explore`/`decide` rather than weakening the gate inside them.

## Decision record

Keep the record with the existing `strategy-state.md` and `decision-log.md` roles; do not create a parallel register. For a material choice, capture:

```text
Decision:
Owner:
Date and horizon:
Options considered (A/B/C):
Criteria and any weights:
Recommendation:
Causal rationale:
Opportunity cost (capital, time, focus, channel, option value):
Rejected alternatives and why (specific, not "worse"):
Critical assumptions and confidence:
Leading indicators, baseline and threshold:
Revisit triggers:
Status (proposed / accepted / rejected / superseded):
Evidence links:
```

The recommendation must state the chosen option, the opportunity cost and the rejected alternatives. "Option B is better" is insufficient; say what B gains, what A or C would have provided, and why that trade is acceptable under the current constraints and evidence.

## Revisit triggers

Reopen the option set when:

- a leading indicator misses its threshold for the agreed review window;
- a critical assumption is falsified or a key risk materializes;
- customer, buyer, channel or pricing economics shift materially;
- a competitor, platform, supplier or regulator changes the basis of competition;
- capital availability or the cost of capital changes the feasible set;
- time-to-value or payback exceeds the accepted bound;
- a required capability proves unavailable within the window;
- the option value of a rejected alternative rises;
- actual customer mix, ACV, retention or channel performance drifts from the plan;
- the decision owner or strategic objective changes.

Record the trigger, the affected assumptions, the options reopened and the revised recommendation. A trigger that fires without changing a choice is still evidence; say why the thesis was reaffirmed.

## Sources

- Michael E. Porter, [What Is Strategy?](https://hbr.org/1996/11/what-is-strategy), *Harvard Business Review*, November–December 1996 — strategy as distinct activities, trade-offs and choosing what not to do.
- A. G. Lafley and Roger L. Martin, *Playing to Win: How Strategy Really Works*, Harvard Business Review Press, 2013 — the strategy choice cascade and integrated where-to-play/how-to-win choices.
- Richard P. Rumelt, *Good Strategy Bad Strategy: The Difference and Why It Matters*, Crown Business, 2011 — diagnosis, guiding policy and coherent action; distinguishing strategy from ambition.
