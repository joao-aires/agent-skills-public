# Product feedback analysis contract: evidence for a product decision

A product feedback analysis owns the **interpretation of user feedback and product evidence for one decision**. It records what was observed, what it supports and what remains uncertain. It is not a PRD, an ECR, a research report about technology choices or an implementation plan.

Apply the [artifact quality bar](../quality-bar.md). The analysis is complete when a reader can find the decision question, the evidence and its limits, the supported findings, competing explanations and the recommended next decision without reopening every raw record.

Read the [product feedback analysis guide](../../../guide-product-feedback-analysis/SKILL.md) for writing conventions, examples and review checks.

## Reader questions

A product or engineering decision owner must be able to answer:

1. What decision does this analysis inform, and how will the result be used?
2. Which product, segment, time period and sources does it cover?
3. What evidence exists, how was it collected, and what limits apply?
4. What did users say, and what did they actually do?
5. Which outcomes, friction and unmet needs are supported, for whom?
6. Which competing explanations remain, and what evidence distinguishes them?
7. What should happen next, and what is still unknown?
8. Who owns the artifact, and at which revision is it current?

## Contract

```markdown
# Decision question and intended use

## Scope
Product or area, affected segment, time period and sources covered; what is
excluded.

## Evidence sources, limits and confidence
Each source, its collection method, period, coverage and known gap. State
confidence per finding, not once for the whole document.

## What users said vs what they did
Reported statements and requests separated from observed behavior, usage or
outcomes, with source references. Note where they disagree.

## Observed outcomes, friction and unmet needs
Supported findings: what happens, to whom, why it matters, and the evidence
that establishes it. Keep hypotheses distinct from findings.

## Competing explanations
Plausible alternative causes, contradictory cases and the evidence that would
separate them.

## Implications and recommended next decisions
The response the evidence supports, the expected improvement, the observable
follow-up measure and the decision owner.

## Open questions and evidence gaps
Questions the current evidence cannot answer, the missing data, and the
authorized next step needed to obtain it.

## Status, owner and revision
Draft, current or superseded; owner; date and revision or source snapshot;
superseded-by link when replaced.
```

Guidance:

- **Decision question and intended use.** Name the decision: improve an interaction, investigate a problem, continue or stop an experiment, change scope or prioritize. State how the answer will be used and by whom. An analysis without a decision is a note.
- **Scope.** Give the product or area, segment, period and source set. Separate new and experienced users, plans, regions or cohorts when the evidence differs. State what was not examined.
- **Evidence sources, limits and confidence.** List each source with its collection method, period, denominator or participant count and known gaps. Distinguish representative data from convenience samples, support complaints and individual reports. State confidence per finding and what weakens it.
- **What users said vs what they did.** Keep quotes, requests and interpretations separate from observed behavior, outcome attainment, drop-off or repeat use. A request for export is not evidence that export will improve the outcome. A usage count is not evidence that the behavior was useful.
- **Observed outcomes, friction and unmet needs.** Write findings as what happens, to whom, why it matters and which records establish it. Group by the difficulty or unmet outcome rather than only by a requested feature. Count distinct people or accounts separately from repeated mentions. Retain important outliers.
- **Competing explanations.** Include the plausible alternatives: discoverability, reliability, a changed workflow, a different audience or a measurement gap. Note contradictory cases and the evidence that would distinguish the explanations. Do not force one cause.
- **Implications and recommended next decisions.** Recommend a response to the underlying difficulty, not automatically the requested feature. State the expected improvement, the observable outcome and when it will be assessed. Distinguish a supported recommendation from an experiment or investigation still needed. Name the decision owner when known.
- **Open questions and evidence gaps.** Record what the current evidence cannot settle and what authorized work would settle it. Do not propose contacting users, adding tracking or running an experiment unless that activity was requested.
- **Status, owner and revision.** State the current status, owner and the source snapshot or revision. A later analysis supersedes through an explicit link; do not silently overwrite the evidence basis of an accepted decision.

Keep raw records available when durable, but do not paste personal data, credentials or unnecessary transcripts into the artifact. Link the extracts or summarize them with an access note.

## Relationship to other artifacts

A [research report](research-report.md) covers any bounded inquiry, including user research. When existing user evidence drives a product decision, this analysis owns that evidence and the research report links it rather than restating it. Requirements and design link the findings they rely on; they do not create a second evidence record.

## Handoff

The product direction and planning reader needs the decision question, supported findings, limits, competing explanations, recommended next decision and open questions. Plan uses the artifact as evidence, links the revision it used and summarizes only what the planning decision or ECR needs; it does not re-derive the analysis or create a second evidence narrative. Requirements work links the findings that constrain behavior and acceptance. See [handoff](../handoff.md).

When later evidence changes a conclusion within the same decision and period, revise the artifact and keep its history and current status. When the decision or period changes, or a conclusion is replaced, create a superseding artifact and reopen the affected decision. Do not keep a second narrative in a planning document.

## Maturity

A product feedback analysis normally moves from **draft** to **current** to **superseded**. It may support a proposed or accepted product decision, but it does not itself accept a priority, promise implementation or prove that an outcome improved. Findings are only as strong as the recorded evidence and its limits.

## Reader test

A reader who was not in the analysis must be able to answer:

1. Which decision this analysis informs, and how the result will be used?
2. Which product, segment, period and sources it covers?
3. What was observed, what was said and where they diverge?
4. Which findings are supported, at what confidence, and which remain hypotheses?
5. Which competing explanations remain plausible?
6. What should happen next, who owns the decision and what is still unknown?
7. At which revision the analysis is current, and what superseded it if anything?

If the reader must reopen raw records to find the main finding or its limit, the analysis is not complete.

## Example

> **Decision question and intended use.** Should the next small slice improve handover discovery for new shift leads, or add CSV export for experienced leads? The team has capacity for one small change this week.
>
> **Scope.** Internal handover tool; twelve shift leads; last four weeks; support messages, three supplied observations and the existing usage export. No data exists for four leads. Tracking was disabled for two accounts.
>
> **Evidence sources, limits and confidence.** Support messages and observations are a convenience sample, not a representative survey. The event export covers eight accounts and defines a reopen as every repeat, not one per handover. Completion and matching timestamps are missing. Confidence is moderate that new leads struggle to find earlier handovers; low that export would change the intended outcome.
>
> **What users said vs what they did.** Two experienced leads requested export and described pasting into chat. One new lead could create a handover when observed but could not find it on the next shift without help, and requested search. Another new lead requested notifications but had no observed session. In the export, 48 creates came from eight accounts and 31 reopens from five; reopens do not show whether the right handover was found.
>
> **Observed outcomes, friction and unmet needs.** Friction is concentrated in retrieving unfinished work on the next shift, especially for new leads. The evidence supports a discovery problem, not an export problem. Experienced leads already use saved browser links with no reported difficulty.
>
> **Competing explanations.** Poor discoverability, missing notification of the latest edit, or unfamiliar naming could each explain the new-lead reports. The single observed failure points to retrieval; notification has no behavioral evidence; naming has no direct evidence. A focused usability observation would separate them.
>
> **Implications and recommended next decisions.** Improve retrieval of recent handovers for new leads before adding export. Expected improvement: a new lead finds unfinished work without assistance. Follow-up: observe the same task after the change and check whether assisted retrieval drops. The product owner decides whether to fund the slice; export remains a candidate for a later analysis of experienced-lead outcomes.
>
> **Open questions and evidence gaps.** No evidence exists for four leads, and the reopen count cannot establish successful retrieval. Notification value remains untested. Obtaining more evidence would require an authorized observation or instrumented completion event.
>
> **Status, owner and revision.** Current; prepared by the product owner; evidence snapshot `handover-export@<full-sha>`, four weeks ending 2026-11-14. Supersedes no earlier analysis.

## References

Primary sources, the source export or extract, and any existing product brief, roadmap or decision the analysis informs. Use the [link rules](../quality-bar.md#4-resolvable-navigation).
