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

Group repeated reports by underlying problem, preserve representative evidence, deduplicate repeated contacts and distinguish people/accounts from mentions.

Choose a small number of meaningful measures when data exists: reaching the intended outcome, drop-off between relevant steps, repeat use or retention.

- State denominator, time window, segment and event definitions.
- Check missing events and selection bias before interpreting a funnel.
- Counts of page views or feature clicks alone do not prove usefulness.

For a saved-search feature, ask whether users can save and later reuse a search. Compare available save/reopen behavior with reports of confusing names, missing searches or poor discoverability. If only a few users exist, examining their journeys and asking focused usability questions can be more useful than proposing an underpowered A/B test.

## Turn evidence into a small next step

For each important pattern, keep the underlying observation visible, explain your interpretation, and identify what remains a hypothesis. Look for the point in the journey where the user could no longer achieve the intended result. The same symptom can have different causes, so compare the reports with available behavior before recommending a feature.

Prioritize problems by severity, relevance to the intended users, strength of evidence and the cost of learning or fixing them. Explain conflicting evidence rather than averaging it away: different segments may have different needs, and a satisfied frequent user may never encounter the obstacle that prevents a new user from starting. Use numeric scoring only when its inputs add clarity.

Recommend a response to the underlying difficulty. A feature request may reveal a problem better solved by clearer interaction, different defaults, better reliability or a narrower product promise.

Recommend a bounded response with an observable outcome and a way to assess it later. Bring accepted work into requirements/planning, using the conversation or Markdown when sufficient; no ticket requirement. Use [product management](../product-management/SKILL.md) for product reprioritization and the next useful slice; refinement owns detailed engineering requirements. Keep the roadmap, assumptions and decision log aligned without turning every comment into backlog work. Close the loop by checking the outcome after the change; contact/report back to users only when requested.

## Keep collection respectful and optional

Minimize collected personal data and raw contents, define purpose/retention/access and use the project's privacy guidance before changing telemetry. Do not add session replay, third-party analytics or identity tracking by default. Existing exports and a short evidence note can be sufficient.

The upstream [Amplitude feedback skill](https://github.com/amplitude/builder-skills/tree/51838c2d85560466d1bbc174ea0e645bb9c44ea9/analytics-skills/skills/analyze-feedback) is an optional reference for projects already using its feedback/analytics MCP tools. It is vendor-specific and is not bundled here: no explicit redistribution license was found at that reviewed commit. Do not imply it is installed or configure Amplitude automatically. Matt's installed research/clarification skills can support a requested investigation, but are not substitutes for actual user evidence.

Finish with the decision question, evidence and limits, recommended action and follow-up measure. Do not claim causality or broad adoption from a small sample.
