---
name: postmortem-facilitation
description: Reconstruct incident history, conduct a focused blameless evidence-led
  interview and generate or review a postmortem with causal analysis, uncertainty,
  impact and measurable learning actions.
metadata:
  scope: generic
  invocation: both
  version: '1.1'
  role: task
---

# Postmortem facilitation

Read [composition guidance](../../COMPOSITION.md) for optional expertise, fallback and scope.

Help responders think through what happened rather than fill a template with plausible explanations. Ask the next question that most changes understanding or the prevention plan.

## Modes

- **Interactive interview (only when requested):** review provided history first, maintain an evidence ledger, ask one substantive question at a time and follow its answer. Summarize newly established facts and explain why the next gap matters.
- **Draft/review:** assemble what sources establish, challenge unsupported claims and return targeted unresolved questions. Do not require an interview when the evidence already answers them.
- **Recurring review:** identify incidents needing review, assemble drafts/question queues, detect contradictory or weak causal accounts and prepare grounded action candidates. Do not invent participant answers, endorse ownership on their behalf or publish a draft as approved.

Consult [references/facilitation-guide.md](references/facilitation-guide.md) for deeper implementation details when needed.

## Facilitation workflow

1. Ingest ticket, chat/timeline, changes, metrics/traces/logs, actions and stakeholder communications. Normalize timestamps with source/timezone and separate customer impact from response and ticket duration.
2. Create a fact/claim/unknown ledger and a first causal/response timeline. Read system evidence before asking questions answerable from code or history.
3. Ask adaptively about the highest-value gap: actual user harm, failure mechanism, decision context, detection gap, mitigation delay, recovery evidence or recurrence protection.
4. Challenge contradictions neutrally: cite competing evidence, ask what reconciles it, retain both until resolved. Use “what information/control made this outcome possible?” rather than “who failed?”
5. Analyze trigger, contributing conditions, propagation, barriers, detection, response and recovery. Do not force all incidents into one root cause or a fixed five-whys chain.
6. Derive specific learning and candidate actions with a causal rationale and observable completion criterion. Distinguish confirmed correction from hypotheses to investigate.
7. Draft the review in the local format with impact, timeline, analysis, what worked, gaps, unknowns and actions. Mark owner/reviewer confirmation pending where needed.
8. Review for factual accuracy, psychological safety, useful depth and testable prevention. Hand approved work to `postmortem-followup` or return the register directly.

For proxy/security or detection-gap incidents, consult the [worked review case](references/proxy-security-review.md) when useful. Reconcile inconsistent clocks and distinguish confirmed impact from plausible shared-consumer exposure. A claim that an issue is “not detectable” needs a measurement-boundary analysis, not unquestioned acceptance.

## Stop condition and output

Finish the interview when the material decisions are sufficiently evidenced or the user elects to stop. Preserve unknowns rather than prolong a low-value interrogation. Deliver the postmortem draft, evidence ledger, unanswered questions, action candidates and reviewed/published status. Resolution may be proven while the underlying cause remains unknown.
