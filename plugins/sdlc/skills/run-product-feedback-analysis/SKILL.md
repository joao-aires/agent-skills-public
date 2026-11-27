---
name: run-product-feedback-analysis
description: Analyze existing user feedback and product usage evidence to evaluate outcomes,
  identify friction and unmet needs, and inform the next product decision. Use when
  reviewing a shipped feature, investigating adoption or usability, or prioritizing
  from available evidence; do not start surveys, contact users or install analytics
  without a request.
metadata:
  kind: activity
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
user-invocable: true
---

# Run product feedback analysis

Turn user evidence into a product-feedback analysis that supports a named decision, and stop at the recorded findings and their limits.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. For the artifact this activity produces, read the [product-feedback-analysis contract](../artifact-system/references/contracts/product-feedback-analysis.md) and [guide-product-feedback-analysis](../guide-product-feedback-analysis/SKILL.md). Resolve its home with [artifact homes](../artifact-system/references/homes.md) before writing.

When the affected stack, architecture or domain has installed expertise or guidance, read it and carry its conclusions. If none exists, use project evidence and primary sources; this activity keeps the outcome, acceptance and stopping point.

## Ask a decision question

Start with the intended user outcome and the decision this evidence should inform: improve an interaction, investigate a problem, continue an experiment, change scope or stop. Read the product's assumptions and existing feedback. A shipped feature is an output. Whether people can achieve the intended outcome is the question. Keep the activity small enough to change a real decision.

Use available evidence before adding tools: support reports, user-provided interviews, usability observations, reviews and existing usage data.

- Identify source, period, segment and collection limitations.
- Analyze only data the project is authorized to access.
- Sending questionnaires, contacting users, adding tracking or running experiments requires a request that includes that activity.

## Combine what users say and do

| Evidence | Helps explain | Interpretation limit |
| --- | --- | --- |
| Qualitative feedback | Context and friction | The loudest customer or an AI-generated sentiment score does not establish a representative population. |
| Quantitative usage | Prevalence and outcomes | Check missing events, definitions and selection bias before interpreting the population. |

### Develop findings from observations

Keep the source material available while building the interpretation:

1. Extract distinct observations, statements and relevant behavior from each source. Retain the source, user segment and task context. Keep a participant's words separate from your interpretation.
2. Give related observations descriptive labels, then group them into candidate patterns. Group by the difficulty or unmet outcome rather than only by the requested feature. Count distinct people or accounts separately from repeated mentions.
3. Check each candidate against its supporting records and contradictory cases. Split patterns that have different causes or user contexts, and retain important outliers rather than forcing every observation into a group.
4. Express a supported pattern as a finding: what is happening, to whom, why it matters and which evidence establishes it. Mark an explanation that still needs testing as a hypothesis.

Compare sources that can answer the same question. Usage records may help establish how often a behavior occurs. Interviews may help explain the circumstances. If they disagree, check their populations, definitions and collection periods before treating either as decisive.

### Interpret available measures

Choose a small number of meaningful measures when data exists: reaching the intended outcome, drop-off between relevant steps, repeat use or retention.

- State denominator, time window, segment and event definitions.
- Check missing events and selection bias before interpreting a funnel.
- Counts of page views or feature clicks alone do not prove usefulness.

For a saved-search feature, ask whether users can save and later reuse a search. Compare available save/reopen behavior with reports of confusing names, missing searches or poor discoverability. If only a few users exist, examining their journeys and asking focused usability questions can be more useful than proposing an underpowered A/B test.

## Write the evidence as one artifact

Record the analysis in a `product-feedback-analysis` artifact instead of returning disconnected findings. Read its [contract](../artifact-system/references/contracts/product-feedback-analysis.md) for the required sections and the [guide](../guide-product-feedback-analysis/SKILL.md) for craft and review. This activity adds the synthesis but does not own a second structure.

Keep raw records and source extracts available beside the artifact when they are durable. One analysis covers one decision and period. Start a new revision or artifact when either changes. Do not add implementation, design or release sections to make it look complete.

## Turn evidence into a small next step

Follow each important finding back through the user journey. Identify where the person could no longer achieve the intended result and which explanation the evidence supports. Similar complaints can have different causes. Compare the reports with actual behavior before recommending a feature.

Rank findings for the decision owner using severity, relevance to intended users, evidence strength and the cost of learning or fixing. Accepting a priority belongs to the product owner. Preserve segment differences: a frequent user's success does not establish that a new user can get started. Use numerical scoring only when its inputs make the choice clearer.

Recommend a response to the underlying difficulty. A feature request may reveal a problem better solved by clearer interaction, different defaults, better reliability or a narrower product promise.

For a recommended response, identify:

- The finding it addresses and the expected improvement.
- The observable outcome and how it will be assessed later.
- Any remaining assumption that needs investigation before committing to the change.

Hand the artifact to [plan](../plan/SKILL.md) and the available product-direction method as evidence for the next product decision. Plan uses the recorded findings, limits and open questions rather than re-deriving them. Use [refine](../refine/SKILL.md) when the accepted direction needs detailed requirements. Keep the roadmap and relevant decisions aligned without making every comment a backlog commitment.

After the change, check whether the intended outcome improved. Reopen the analysis with a new revision when later evidence changes its conclusions. Contacting or reporting back to users remains subject to the requested scope.

## Keep collection respectful and optional

Minimize collected personal data and raw contents, define purpose/retention/access and use the project's privacy guidance before changing telemetry. Do not add session replay, third-party analytics or identity tracking by default. Existing exports and a short evidence note can be sufficient.

The upstream [Amplitude feedback skill](https://github.com/amplitude/builder-skills/tree/51838c2d85560466d1bbc174ea0e645bb9c44ea9/analytics-skills/skills/analyze-feedback) is an optional reference for projects already using its feedback/analytics MCP tools. It is vendor-specific and is not bundled here: no explicit redistribution license was found at that reviewed commit. Do not imply it is installed or configure Amplitude automatically. Installed research or clarification skills can support a requested investigation, but they are not substitutes for actual user evidence.

Finish with the decision question, the artifact's home and revision, evidence and limits, recommended action and follow-up measure. Do not claim causality or broad adoption from a small sample.
