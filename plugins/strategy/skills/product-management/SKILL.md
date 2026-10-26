---
name: product-management
description: Shape product direction from user problems, evidence and constraints. Use for discovery, prioritization, useful first slices, success measures and product sequencing before development or when new evidence changes priorities; reuse accepted decisions for defined changes.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Decide which product outcome to pursue

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

Help decide which user problem to address, what to deliver first and how to find out whether it helped. Apply directly to a product question or as support in an authorized development engagement.

Scale discovery to the unresolved question. A personal tool may need a short purpose and scope decision; an uncertain commercial proposition needs stronger evidence of demand and adoption. Reuse accepted context for a defined bug or feature.

## Establish the problem and evidence

Read existing product decisions, supplied research, feedback and actual behavior.

- Identify the intended users, their job and current workaround, the difficulty or unmet outcome, and the intended personal, internal or commercial use.
- Separate observed facts, interpretations and untested demand or solution assumptions.
- Reuse answers already established.

Identify what the proposed feature would change in the current workflow. Compare it with a simpler product, a process change or an existing tool when those could solve the same problem. Investigate technical facts before asking the user to settle priorities, intended usage or commitments.

Use [business strategy](../business-strategy/SKILL.md) when the question concerns competitive position, value capture or business viability. Work within accepted strategy; new product evidence can explain why a strategic decision needs revisiting.

## Choose a useful slice and what to defer

Compare plausible responses to the same problem, including doing less or changing the surrounding workflow. Examine candidates on common dimensions:

| Dimension | What to establish |
| --- | --- |
| Intended users | Who benefits, and whether that group is the one the product serves. |
| Frequency and impact | When the problem occurs and what it prevents people from completing. |
| Evidence | What has been observed, which sources support it and what remains assumed. |
| Delivery and upkeep | What it takes to learn about, implement and maintain the response. |
| Adoption | Which people, teams or external systems must change for the response to work. |

Use the comparison to recommend a response and explain why it is preferable under the accepted constraints. State which uncertain belief could reverse the choice and what is deferred. A feature request is evidence to investigate, not an automatic backlog commitment.

Use a scoring framework when its inputs can be defended and it makes the tradeoff easier to understand. Missing data should remain visible; assigning an unsupported number does not resolve the uncertainty.

Choose a coherent experience that lets the intended user achieve a meaningful result.

- Describe the main journey, scope/non-goals and the important assumptions.
- Keep must-have behavior separate from ideas and later options.
- Ask for a consequential product choice when alternatives change the accepted outcome; choose reversible details within scope without another approval ceremony.

Sequence the work around useful outcomes and unresolved assumptions:

- Distinguish committed work, the next candidate and later possibilities.
- Base dates on actual capacity or external commitments.
- Use a bounded prototype or investigation when an evidence gap could change the product choice.

Keep research findings, customer claims, forecasts and delivery promises tied to their actual sources or accepted assumptions.

## Define success and a way to learn

Choose an observable user outcome and, where useful, a measure with its population, time window, data source and interpretation.

- Identify failure or harm signals as well as the desired improvement.
- Separate proposed targets from accepted commitments and existing measurements.
- Small populations may support qualitative observation better than a statistically unsupported experiment.

Choose evidence for the decision that remains open:

| Uncertainty | Investigation to consider |
| --- | --- |
| Can people find and complete the task? | Observe realistic task performance and recovery. |
| Is the result worth adopting? | Investigate the current workaround, its consequences and willingness to change. |
| Is a proposed improvement occurring? | Compare an appropriate outcome measure with its baseline, accounting for who was observed and when. |

Before gathering more evidence, define which results would lead to continuing, revising or stopping. Prioritize assumptions whose failure would change the decision, then choose the least costly credible investigation.

Use available usability research expertise for participant methods and [product feedback](../learn-from-product-feedback/SKILL.md) for evidence synthesis. Keep a prepared study distinct from one that ran. Contact, recording, telemetry changes and live experiments require the corresponding authorized scope.

## Carry direction into development and back

Return the product decision with:

- Recommended or accepted problem and intended users.
- Useful slice and deferred scope.
- Evidence, assumptions and unresolved choices.
- Success signal and next decision.

Use the existing brief, PRD or conversation; no mandatory template, tracker or parallel decision register is needed.

### When engineering work follows

Carry the accepted product decision into observable requirements, then system/experience design and implementation sequencing as the engagement requires. Reuse the supporting methods for those activities without automatically invoking explicit-only tasks. A product-only request ends with the product decision and evidence plan.

### After delivery

Feed actual outcomes through product feedback and revisit the affected priority or assumption. Keep accepted product decisions authoritative until changed by new evidence or the user; neither a completed feature nor a polished prototype establishes product success.
