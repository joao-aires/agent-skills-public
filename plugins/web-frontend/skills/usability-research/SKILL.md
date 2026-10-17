---
name: usability-research
description: Plan task-based usability studies and analyze supplied observations for a specific interface or flow. Use for research questions, participant tasks, neutral discussion guides or evidence synthesis; distinguish proposed studies, heuristic review and actual participant findings.
user-invocable: true
metadata:
  scope: generic
  invocation: both
  role: support
---

# Investigate usability with observable tasks

Use directly for a requested study/analysis or to address a material unresolved user question during authorized product/design work. A routine UI edit does not require a study. [Interaction design](../interaction-design/SKILL.md) owns the proposed flow; [interface quality](../interface-quality/SKILL.md) supplies heuristic inspection, which is a different evidence source.

## Frame the question and study boundary

Establish what decision the research should inform, which users/tasks matter and which flow or supplied frames are in scope. Inspect the intended experience and known constraints. Ask only missing facts that change the study; otherwise label reasonable planning assumptions. If no selection is available, use a supplied frame link, flow or local prototype rather than pretending a Figma selection exists.

Choose a method suited to the uncertainty and available access: task-based observation for completion/recovery, or an explicitly scoped concept/wording question when that is the real objective. Explain meaningful limitations. Propose participant characteristics, recruitment approach, session length and sample rationale as a plan; never present a proposed sample as recruited participants or turn a small convenience sample into a population claim.

Justify a proposed sample through the decision, participant variation and study limits. Do not attach a fixed percentage of discoverable problems to a participant count without an applicable source, model assumptions and uncertainty. When those are unavailable, state the qualitative learning aim without a coverage percentage.

## Prepare tasks and observations

Create realistic scenarios around participant goals, without naming the control to press or hinting at the expected answer. For each task define an observable end state, what to watch for and neutral follow-up probes. Include meaningful failure/recovery or return-use scenarios when relevant. Scale the guide to the decision and flow; do not prescribe a fixed task count.

For recovery questions, observe naturally occurring errors during a normal goal task, or have the moderator prepare a failed/interrupted prototype state before the participant resumes their original goal. Keep that setup out of participant wording: do not tell them which input to omit, which error to trigger or which field to fix. Labelling a coached attempt as an intentional exercise does not make it a neutral recovery task. A separately requested instructional/comprehension exercise needs its own purpose and cannot substitute for the study's recovery question.

A moderator guide should introduce the purpose, explain that the experience is being tested, invite think-aloud where suitable and avoid leading or teaching during the task. Separate task completion, assistance, errors/hesitation and post-task interpretation. Ratings need a stated question and scale, not an invented success threshold. Check that tasks are achievable in the prototype and map back to the research questions.

Use synthetic data where possible. Recording, recruitment, participant contact, private-data collection and external publication require their own authorized scope and appropriate consent handling. Do not contact anyone or write annotations into a shared design merely because a research plan was requested. Deliver in the existing project note or conversation; Figma guide frames are optional when the user has authorized canvas writes and tools support them.

## Analyze the evidence actually supplied

Keep observed behavior, participant statements, researcher interpretation and proposed design changes distinct. Link findings to the relevant task/session and artifact, redact identities where appropriate and group repeated causes. Preserve contradictory or unsuccessful cases. Report how many observations support a finding only when that count is available; no invented quotes, sessions, metrics or research conclusions.

Explain participant/prototype limitations and prioritize effects on the intended task. Propose a repair and a useful follow-up test for important uncertainty. Reuse the actual accepted product constraints; evidence can reopen a decision but does not itself authorize changing it.

Return a proposed study/guide or an evidence-backed synthesis, with assumptions and gaps. Agent exploration, simulated personas, static critique and automated accessibility checks cannot substitute for real participant observations. If no sessions occurred, say the study is prepared and unexecuted. Carry actual findings into requirements/design and verify implemented repairs through the existing test loop.
