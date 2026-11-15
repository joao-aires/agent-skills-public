---
name: guide-evaluation-plan
description: Guide to producing and reviewing an AI evaluation plan. Use for cases, graders, baselines, regression, refusal and failure behavior, human review, cost and latency evidence.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: ai
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Evaluation plan guide

Read [activity system](../activity-system/SKILL.md) for scope, the [design proposal contract](../artifact-system/references/contracts/design-proposal.md) for authority and [software types](../artifact-system/references/software-types.md) for the AI evidence.

An evaluation plan is a **view artifact and evidence plan**. It states how the AI behavior will be judged before it is trusted; it is not a demo script, a single prompt result or a claim that the model works.

## Reader question

Can a reviewer tell which cases matter, how each is graded, what baseline is being compared, and what failure or regression would block acceptance?

## When to use

- an AI feature or agent has a quality or acceptance bar;
- a model, prompt, provider or retrieval change could regress behavior;
- refusal, citation, tool use or human review matters;
- cost or latency is part of the design;
- a design decision depends on behavior that cannot be judged from a single sample.

Do not use an evaluation plan as a substitute for service tests or security review.

## Minimum content

- task and quality dimensions;
- case set: normal, boundary, adversarial, denial/refusal and regression cases;
- grader or human-review method for each dimension;
- baseline and acceptance threshold;
- environment, model/provider and revision;
- cost and latency limits where relevant;
- failure handling and escalation;
- what is not covered.

## Structure and quality

- Derive cases from the user task and known failure modes, not from the model's output.
- Keep a stable baseline and report the comparison, not only the new score.
- Separate correctness, safety, helpfulness, citation and tool-use dimensions.
- State who grades subjective cases and how disagreement is resolved.
- Record the exact model, prompt, retrieval index and revision.
- Keep evaluation data free of secrets and unnecessary personal data.
- Distinguish a local probe from production behavior.

## Common failures

- one happy-path prompt presented as evaluation;
- grader criteria that change between runs;
- no baseline or no regression set;
- measuring only latency or only quality;
- ignoring refusal, hallucination, stale context and provider failure;
- claiming production quality from a local run.

## Authority, home and review

- **Authority:** the design proposal/ECR quality bar; `ai-testing` owns the evaluation method.
- **Home:** evaluation workspace or repository `evals/` when durable; link the dataset and revision.
- **Review:** use [design review](../design/references/design-review.md) and the AI testing guidance.

## Specialist route

Use `ai-testing` for evaluation strategy, `ai-operations` for drift and production signals, and the selected AI implementation pack for provider or framework mechanics. A missing evaluator does not lower the quality bar.

## Handoff

Record the case set, grader, baseline, result and limits in the design proposal. Do not claim the AI feature is accepted or production-ready from a plan or a single run.
