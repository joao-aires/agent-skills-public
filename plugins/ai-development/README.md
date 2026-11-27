# AI development plugin: application method, evaluation and operations

The `ai-development` plugin carries provider-independent guidance for building and assessing AI-enabled applications. It covers the application method, the evaluation method, the evaluation program and AI operations; it does not select a framework, provider or evaluation SDK, and it does not own the delivery decision.

## Purpose

Use this package when a task needs inference, generation, retrieval or agent behavior and the question is how to bound it, how to know whether it works, or how to operate it. It composes with the project's design and verification activities and with a selected implementation package for runners and SDKs.

## Conceptual model

Four disciplines answer different questions. The split is deliberate: one builds, one decides what evidence means, one runs the evidence as a program, one observes the result in production.

| Question | Owner | Not the owner of |
| --- | --- | --- |
| What should the application do, with which task boundary, context, tools and protocol? | [ai-development](skills/ai-development/SKILL.md) | Evaluation program or production operation |
| What should be evaluated, at which boundary, and what can the evidence establish? | [ai-testing](skills/ai-testing/SKILL.md) | Dataset lifecycle, gates or reporting |
| How does an evaluation program run across a change, release or product claim? | [ai-evaluation](skills/ai-evaluation/SKILL.md) | Test design or operating signals |
| How does the capability behave in production, within provider and cost limits, and how does it recover? | [ai-operations](skills/ai-operations/SKILL.md) | Application design or acceptance thresholds |

Both `ai-testing` and `ai-evaluation` are methods: `ai-testing` owns what to evaluate and what each evidence level proves; `ai-evaluation` owns the program mechanics. The testing phase composes them when a claim is about AI behavior. Neither replaces application verification or the release decision.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [ai-development](skills/ai-development/SKILL.md) | method | Task and system boundary, model-versus-code split, result design, context, retrieval, tools, harnesses, protocols, interaction and application verification needs | A design or implemented behavior with evidence needs | Choosing a vendor SDK or authorizing live actions |
| [ai-testing](skills/ai-testing/SKILL.md) | method | Acceptance levels, representative cases, slices, measures, graders and what each evidence level proves | An evaluation approach with actual results and limits | Program scheduling, release gating or production sampling policy |
| [ai-evaluation](skills/ai-evaluation/SKILL.md) | method | Evaluation decision and claim, dataset and slice governance, baselines, experiments, CI gates, production sampling, red-team coverage and reporting | A go, conditional or no-go recommendation with evidence | Merge, deployment or publication authority |
| [ai-operations](skills/ai-operations/SKILL.md) | method | Task observability, quality monitoring, latency and cost, provider limits, drift, rollout, recovery and configuration identity | Operating evidence, blind spots and next actions | Application design, acceptance criteria or release approval |

## How it materialized

| Model element | Implementation |
| --- | --- |
| Application method and protocol guidance | [ai-development](skills/ai-development/SKILL.md) and its references |
| Evaluation method and evidence levels | [ai-testing](skills/ai-testing/SKILL.md), [evaluation methods](skills/ai-testing/references/evaluation-references.md) |
| Program mechanics: datasets, slices, variance, gates | [evaluation program](skills/ai-testing/references/evaluation-program.md) |
| Program activity and reporting | [ai-evaluation](skills/ai-evaluation/SKILL.md) |
| Operating signals, limits and recovery | [ai-operations](skills/ai-operations/SKILL.md) and its references |

## Reading paths

## How it composes

| Need | Use |
| --- | --- |
| Build or change an AI application | [AI development](skills/ai-development/SKILL.md) |
| Decide what to evaluate and what the evidence means | [AI testing](skills/ai-testing/SKILL.md) |
| Plan, gate and report an evaluation program | [AI evaluation](skills/ai-evaluation/SKILL.md) |
| Implement a selected Python/DeepEval suite | `ai-deepeval-testing` when installed and chosen |
| Verify application behavior, contracts and persisted journeys | `test` when installed |
| Implement traces, metrics and logs | `design-system` observability guidance when available; stack telemetry tooling |
| Make the delivery decision | `release` when installed |

Common sequences:

1. **New AI capability** → [ai-development](skills/ai-development/SKILL.md) → [ai-testing](skills/ai-testing/SKILL.md) for acceptance and evidence levels → project design record.
2. **Release or product claim** → [ai-testing](skills/ai-testing/SKILL.md) for the method → [ai-evaluation](skills/ai-evaluation/SKILL.md) for the program, gates and recommendation → the established delivery authority.
3. **Quality regression in production** → [ai-operations](skills/ai-operations/SKILL.md) to locate the signal → [ai-testing](skills/ai-testing/SKILL.md) to turn observed failures into regression cases.
4. **Provider, cost or rollout change** → [ai-operations](skills/ai-operations/SKILL.md) for limits, configuration identity and recovery → [ai-development](skills/ai-development/SKILL.md) only if the task or architecture changes.

## Boundaries

- **Evidence versus decision.** Evaluation evidence supports a decision; it does not authorize merge, deployment, publication or live mutation.
- **Scope of a score.** A component score, simulated user or recorded output establishes a narrower claim than a live end-to-end journey.
- **Provider and SDK.** Provider, framework and evaluation-SDK choices stay with the project. The plugin requires no hosted evaluation service, synthetic data or particular library.
- **Application verification.** Protocol compatibility, authorization, accessibility and persisted journeys remain with application verification capabilities.
- **Records.** Results update the existing change or verification record. The artifact system and project conventions own artifact types, homes and evidence shape.
- **Acquired implementation.** A selected Python, ADK or LangChain package owns its runner, APIs and instrumentation; this package does not.

## Authority and optional tools

The package declares no MCP servers and no external services. Live provider calls, dataset publication, production sampling and red-team activity require scope from the request, approved data and the relevant account access. Installing the package selects no model, provider or evaluation platform.

## Maintenance

Owning sources are `skills/*/SKILL.md` and their `references/`. Update this README when the four-way responsibility split, an evidence boundary or the composition with implementation packages changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests.
