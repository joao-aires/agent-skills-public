# AI development plugin: application method, evaluation and operations

The `ai-development` plugin carries provider-independent guidance for building and assessing AI-enabled applications. It covers the application method, evaluation method, evaluation program and AI operations; it does not select a framework, provider or evaluation SDK.

## What it owns

| Skill | Owns |
| --- | --- |
| [AI development](skills/ai-development/SKILL.md) | Task and system boundary, context, tools, harnesses, protocols and interaction design. |
| [AI testing](skills/ai-testing/SKILL.md) | What to evaluate, acceptance at each boundary, case and grader design, and what the evidence can establish. |
| [AI evaluation](skills/ai-evaluation/SKILL.md) | The evaluation program: decision and claim, dataset and slice governance, baselines, gates, production sampling, red-team coverage and reporting. |
| [AI operations](skills/ai-operations/SKILL.md) | Operating signals, quality monitoring, provider limits, latency/cost, drift, rollout and recovery. |

The evaluation pair is deliberately split. `ai-testing` is the method for choosing and interpreting evaluation evidence. `ai-evaluation` is the activity for running that method as a program across a change, release or product claim. Neither replaces application verification or the delivery decision.

## How it composes

| Need | Use |
| --- | --- |
| Build or change an AI application | [AI development](skills/ai-development/SKILL.md) |
| Decide what to evaluate and what the evidence means | [AI testing](skills/ai-testing/SKILL.md) |
| Plan, gate and report an evaluation program | [AI evaluation](skills/ai-evaluation/SKILL.md) |
| Implement a selected Python/DeepEval suite | `ai-deepeval-testing` when installed and chosen |
| Verify application behavior, contracts and persisted journeys | `test` when installed |
| Implement traces, metrics and logs | `observability` when installed |
| Make the delivery decision | `release` when installed |

## Boundaries

- Evaluation evidence supports a decision; it does not authorize merge, deployment or external publication.
- A component score, simulated user or recorded output establishes a narrower claim than a live end-to-end journey.
- Provider and SDK choices stay with the project. The plugin does not require a hosted evaluation service, synthetic data or a particular framework.
- Durable artifacts and homes belong to the project's artifact system. Evaluation results update the existing change or verification record rather than creating a new artifact type.

Use the skill descriptions and the project's accepted requirements to select guidance; this README is orientation, not a required sequence.
