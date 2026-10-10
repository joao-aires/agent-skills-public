---
name: build-evaluated-ai
description: Build or review LLM, agent and speech-to-text features with clear evaluation and tool boundaries. Use for framework/model selection, prompts, structured output, Gemini experiments, ADK or LangChain/LangGraph workflows, transcription and AI regression checks.
---

# Build evaluated AI features

## Choose the smallest useful AI boundary

Define the product task, input/output contract and observable success before choosing an agent framework. Preserve agreed scope and existing architecture.

| Need | Starting point |
| --- | --- |
| One generation, extraction or transcription call | Direct model SDK behind an application adapter |
| Useful agent orchestration or integrations | Google ADK or LangChain, according to the project |
| Explicit stateful branching or resumable workflows | Consider LangGraph when those requirements justify it |

Avoid introducing both framework families by default. Use installed ADK agent-builder/architecture or LangChain/LangGraph fundamentals, dependencies and persistence skills for the chosen framework. Keep domain logic and data access testable without the model.

Prefer Gemini for low-cost LLM and transcription experiments. Verify current capabilities, free-tier eligibility, quota, pricing and relevant data-handling terms for the chosen model/account before live use; do not assume every request is free. Keep model/provider settings and credentials in configuration, outside prompts. Distinguish uploaded-audio transcription from a streaming voice application.

## Keep correctness outside the model

Validate structured output against the application schema and handle invalid, missing or refused responses deliberately. Enforce identity, resource authorization, allowed tools, budgets and side-effect policy in deterministic application code. Treat retrieved text and tool arguments as untrusted; content instructions must not grant permissions.

Expose narrow capabilities that reuse authorized application behavior. Bound steps, tokens, timeouts and retries; account for repeated side effects and terminate loops with a useful error. A model deciding an action is not permission to execute it. Keep prompts/versioned settings identifiable without logging private recordings, secrets or full sensitive inputs.

## Define and run a useful evaluation

Select a small representative case set from the product task: normal inputs, ambiguity, malformed input, provider failure and relevant adversarial cases. Define acceptance thresholds before comparing candidates. Use agreed criteria; if quality targets are not specified, state provisional targets and uncertainty rather than silently inventing a product commitment.

Separate two kinds of evidence:

- **Deterministic application checks:** fixtures for contracts, authorization, invalid output, retries, limits and failure presentation. Run these routinely in CI; mocks prove application handling, not model quality.
- **Live quality evaluations:** explicit calls with representative inputs, recording model/prompt version, quality results, latency, usage/cost where available and sample size. Keep credentials/data and execution within the authorized scope. Inspect errors rather than inferring quality from a few attractive examples.

For Portuguese uploaded-audio transcription, include the product's dialects, recording conditions, noise and silence. Assess transcription errors and preservation of important domain terms; report word error rate when suitable, alongside task usefulness. A fixture transcript cannot establish live transcription quality, and uploaded-file success cannot establish real-time behavior.

## Report completion and limits

Version evaluation examples and prompts when they affect behavior. Report what is implemented, deterministic checks run, live evidence gathered and unresolved gaps. Compare against the stated criteria; do not declare quality verified when live evaluation is blocked. Use the workflow bundle for documentation/E2E/delivery when available and update operational notes for quotas, limits and failure handling.
