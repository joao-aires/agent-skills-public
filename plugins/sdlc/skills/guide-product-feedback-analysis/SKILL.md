---
name: guide-product-feedback-analysis
description: Guide to writing a product feedback analysis. Covers the decision question, scope, evidence limits, said versus did, findings, competing explanations, implications and open gaps.
user-invocable: true
metadata:
  kind: guide
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
---

# Product feedback analysis guide

A product feedback analysis turns existing user feedback and product evidence into a decision. It records what was observed, what it supports and what remains uncertain. It is not a feature list, a sentiment report or a claim that a small sample represents everyone.

## Reader questions

1. What decision does this analysis inform, and how will the result be used?
2. Which product, segment, time period and sources does it cover?
3. What evidence exists, how was it collected, and which limits apply?
4. What did users say, and what did they actually do?
5. Which outcomes, friction and unmet needs are supported, for whom?
6. Which competing explanations remain, and what evidence distinguishes them?
7. What should happen next, and what is still unknown?
8. Who owns the analysis, and at which revision is it current?

## Minimum content

- decision question and intended use;
- scope: product or area, segment, period and sources;
- evidence sources, collection limits and confidence per finding;
- what users said versus what they did;
- observed outcomes, friction and unmet needs;
- competing explanations and contradictory cases;
- implications and recommended next decisions, with expected improvement and follow-up;
- open questions and evidence gaps;
- status, owner and revision.

## Structure and quality

- Put the decision question and the strongest supported finding near the top.
- Name the segment and period for every consequential claim. A frequent user's success does not establish that a new user can start.
- Keep participant words, observed behavior and your interpretation in separate sentences or columns.
- State the denominator, time window and event definition for usage measures; explain missing events before interpreting a funnel.
- Count distinct people or accounts separately from repeated mentions.
- Group findings by the difficulty or unmet outcome, not only by the requested feature.
- State confidence per finding and what would weaken or reverse it.
- Keep hypotheses labelled as hypotheses, and retain outliers that do not fit the pattern.
- Compare what people said with what they did; disagreement is evidence, not noise to resolve away.
- Recommend a response to the underlying difficulty. The requested feature may not be the best response.
- Describe the observable follow-up measure; do not claim an outcome improved before it was measured.
- Link the raw extracts or source snapshot rather than pasting personal data or long transcripts.
- Keep one analysis per decision and period. Use a new revision or superseding artifact when evidence changes.

## Common failures

- a dashboard summary with no decision question;
- a quote from the loudest customer presented as the population;
- a request for a feature treated as proof that the feature will help;
- usage counts or page views presented as usefulness;
- aggregating segments that behave differently;
- a funnel without denominator, event definition or missing-data check;
- one cause asserted where several explanations remain plausible;
- findings mixed with recommendations and assumptions;
- confident language for a convenience sample;
- confidential records, personal data or credentials copied into the artifact;
- a plan that copies the findings instead of linking the analysis;
- starting surveys, user contact, tracking or experiments without an authorized request.

## Review

Read the analysis as the decision owner:

- Is the decision and its intended use explicit?
- Is the scope narrow enough to interpret, and are the limits visible?
- Can you tell what was said from what was done?
- Are the findings traceable to sources and separated from hypotheses?
- Do the numbers have a denominator, period and definition?
- Are competing explanations and contradictory cases fairly represented?
- Is the recommended next step proportionate to the evidence?
- Are the open questions and the authorized way to settle them clear?
- Is the status, owner and revision current?

## Handoff

The product direction and planning reader needs the decision question, supported findings, limits, competing explanations, recommended next decision and open questions. The analysis stays the evidence authority; planning and requirements link it rather than restating it. When the recommendation is accepted, the affected change record owns scope and delivery, and later evidence reopens that decision.
