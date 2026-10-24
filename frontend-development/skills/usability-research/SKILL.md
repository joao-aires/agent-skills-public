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

Choose research to resolve a user question or inform a decision. Use for requested study preparation or supplied observations; routine UI work can use [interface quality](../interface-quality/SKILL.md) without a study. [Interaction design](../interaction-design/SKILL.md) owns the proposed flow.

## Frame the decision and method

Begin with the decision the team cannot yet make. Identify whose experience matters, what those people are trying to accomplish, and which uncertainty observation could resolve. Inspect the supplied flow, frame or prototype to see whether it supports that task, including the states the study intends to observe.

Form research questions about behavior or understanding that could change the design. Choose the method after framing the question: watching task performance can reveal where people become stuck, while asking for opinions alone cannot establish that they can use the interface. Reuse available context; ask only for facts that change the study and label planning assumptions.

| Question | Suitable method |
| --- | --- |
| Can participants complete or recover a task? | Observe realistic task performance. |
| How do participants understand a concept or wording? | Use a scoped concept/wording inquiry. |

Justify participant variation, recruitment, session length and sample through the decision and access limits. Quantitative coverage or population claims need an applicable source/model, assumptions and uncertainty; otherwise state the qualitative learning aim. A proposed sample remains a plan until recruitment occurs.

## Observe without coaching

Give participants realistic goals and observable end states while leaving them to discover the interaction.

- Separate moderator setup, participant instructions and neutral follow-up probes.
- Recovery tasks can start from naturally occurring failures or a moderator-prepared failed state; instructions should preserve the original goal without teaching an invalid attempt or its correction.
- Instructional/comprehension exercises answer a different question and need their own interpretation.

Prepare a moderator guide that keeps the participant's goal separate from the interface's solution. Describe the situation and desired end state without naming the control to use. Decide what counts as independent completion, when assistance will be offered, and how assisted completion will be recorded, so the moderator does not quietly turn a failed task into a success.

Invite participants to explain what they expect and what they are looking for. Use neutral follow-up probes after observing the behavior; record errors, hesitation, assistance and the participant's own explanation separately from your interpretation. Check task feasibility in the prototype and trace tasks to research questions. Ratings require a stated question/scale and an interpretation justified by the method.

Use synthetic data where possible. Recruitment, contact, recording, private-data collection, publication and canvas writes require their own authorized scope and consent arrangements. A local guide or conversation can be sufficient output.

## Synthesize the evidence supplied

Separate observed behavior, participant statements, interpretation and proposed changes.

- Link findings to actual tasks/sessions/artifacts, protect identities, group repeated causes and preserve contradictory cases.
- Counts and quotes require supplied evidence.

Explain sample/prototype limitations and prioritize effects on the intended task. Recommend a bounded repair or next test and carry accepted findings into requirements/design. Return the study as prepared and unexecuted when no sessions occurred. Static critique, automated checks, agent exploration and simulated personas are different evidence sources; distinguish them from participant research and verify implemented repairs through the existing test loop.
