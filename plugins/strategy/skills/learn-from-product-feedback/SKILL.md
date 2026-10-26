---
name: learn-from-product-feedback
description: Analyze user feedback and product usage to evaluate outcomes, identify
  problems and inform the next product decision. Use when reviewing a shipped feature,
  investigating adoption/usability or prioritizing evidence; do not start surveys,
  contact users or install analytics without a request.
metadata:
  scope: generic
  invocation: both
  role: task
---

# Learn from product feedback

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

## Ask a decision question

Start with the intended user outcome and the decision this evidence should inform: improve an interaction, investigate a problem, continue an experiment, change scope or stop. Read the product's assumptions and existing feedback. A shipped feature is an output; whether people can achieve the intended outcome is the question. Keep the activity small enough to change a real decision.

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

1. Extract distinct observations, statements and relevant behavior from each source. Retain the source, user segment and task context; keep a participant's words separate from your interpretation.
2. Give related observations descriptive labels, then group them into candidate patterns. Group by the difficulty or unmet outcome rather than only by the requested feature. Count distinct people or accounts separately from repeated mentions.
3. Check each candidate against its supporting records and contradictory cases. Split patterns that have different causes or user contexts, and retain important outliers rather than forcing every observation into a group.
4. Express a supported pattern as a finding: what is happening, to whom, why it matters and which evidence establishes it. Mark an explanation that still needs testing as a hypothesis.

Compare sources that can answer the same question. Usage records may help establish how often a behavior occurs; interviews may help explain the circumstances. If they disagree, check their populations, definitions and collection periods before treating either as decisive.

### Interpret available measures

Choose a small number of meaningful measures when data exists: reaching the intended outcome, drop-off between relevant steps, repeat use or retention.

- State denominator, time window, segment and event definitions.
- Check missing events and selection bias before interpreting a funnel.
- Counts of page views or feature clicks alone do not prove usefulness.

For a saved-search feature, ask whether users can save and later reuse a search. Compare available save/reopen behavior with reports of confusing names, missing searches or poor discoverability. If only a few users exist, examining their journeys and asking focused usability questions can be more useful than proposing an underpowered A/B test.

## Turn evidence into a small next step

Follow each important finding back through the user journey. Identify where the person could no longer achieve the intended result and which explanation the evidence supports. Similar complaints can have different causes; compare the reports with actual behavior before recommending a feature.

Prioritize using severity, relevance to intended users, evidence strength and the cost of learning or fixing. Preserve segment differences: a frequent user's success does not establish that a new user can get started. Use numerical scoring only when its inputs make the choice clearer.

Recommend a response to the underlying difficulty. A feature request may reveal a problem better solved by clearer interaction, different defaults, better reliability or a narrower product promise.

For a recommended response, identify:

- The finding it addresses and the expected improvement.
- The observable outcome and how it will be assessed later.
- Any remaining assumption that needs investigation before committing to the change.

Bring accepted work into requirements and planning; the conversation or Markdown can be sufficient. Use [product management](../product-management/SKILL.md) for reprioritization and the next useful slice, and refinement for detailed engineering requirements. Keep the roadmap and relevant decisions aligned without making every comment a backlog commitment.

After the change, check whether the intended outcome improved. Contacting or reporting back to users remains subject to the requested scope.

## Keep collection respectful and optional

Minimize collected personal data and raw contents, define purpose/retention/access and use the project's privacy guidance before changing telemetry. Do not add session replay, third-party analytics or identity tracking by default. Existing exports and a short evidence note can be sufficient.

The upstream [Amplitude feedback skill](https://github.com/amplitude/builder-skills/tree/51838c2d85560466d1bbc174ea0e645bb9c44ea9/analytics-skills/skills/analyze-feedback) is an optional reference for projects already using its feedback/analytics MCP tools. It is vendor-specific and is not bundled here: no explicit redistribution license was found at that reviewed commit. Do not imply it is installed or configure Amplitude automatically. Matt's installed research/clarification skills can support a requested investigation, but are not substitutes for actual user evidence.

Finish with the decision question, evidence and limits, recommended action and follow-up measure. Do not claim causality or broad adoption from a small sample.
