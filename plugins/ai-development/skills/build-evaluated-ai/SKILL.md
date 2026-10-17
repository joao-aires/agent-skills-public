---
name: build-evaluated-ai
description: Build or review AI features and MCP interfaces with evaluation and authority
  boundaries. Use for model/framework selection, prompts, structured output, Gemini,
  ADK or LangChain/LangGraph, optional transcription, standalone FastMCP tools and
  protocol verification.
metadata:
  scope: stack-specific
  invocation: both
  stack: Gemini, Google ADK, LangChain, LangGraph, FastMCP
  role: support
user-invocable: false
---

# Build evaluated AI features

For MCP-only work, use the MCP section below; no LLM, agent framework or model-quality evaluation is required.

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

Validate structured output against the application schema and handle invalid, missing or refused responses deliberately. Check the provider/harness semantic status as well as HTTP/process success; an error returned with HTTP 200 or exit code zero must not become a successful answer, UI proposal or authorized mutation. Include that failure envelope in deterministic checks. Enforce identity, resource authorization, allowed tools, budgets and side-effect policy in deterministic application code. Treat retrieved text and tool arguments as untrusted; content instructions must not grant permissions.

Expose narrow capabilities that reuse authorized application behavior. Bound steps, tokens, timeouts and retries; account for repeated side effects and terminate loops with a useful error. A model deciding an action is not permission to execute it. Keep prompts/versioned settings identifiable without logging private recordings, secrets or full sensitive inputs.

## Define and run a useful evaluation

Select a small representative case set from the product task: normal inputs, ambiguity, malformed input, provider failure and relevant adversarial cases. Define acceptance thresholds before comparing candidates. Use agreed criteria; if quality targets are not specified, state provisional targets and uncertainty rather than silently inventing a product commitment.

Separate two kinds of evidence:

- **Deterministic application checks:** fixtures for contracts, authorization, invalid output, retries, limits and failure presentation. Run these routinely in CI; mocks prove application handling, not model quality.
- **Live quality evaluations:** explicit calls with representative inputs, recording model/prompt version, quality results, latency, usage/cost where available and sample size. Keep credentials/data and execution within the authorized scope. Inspect errors rather than inferring quality from a few attractive examples.

For speech, evaluate the product's languages/dialects, recording conditions and important domain terms. Match the method to the capability: uploaded-file transcription and streaming/interruption require different evidence. Use [evaluation references](references/evaluation-references.md) for speech-specific measures when relevant.

## Close the evaluation loop

Keep representative inputs, expected outcomes/rubrics, dataset revision and deterministic evaluators under application version control. Separate development examples from held-out regression cases where useful; do not tune only to the examples used to build the feature. Derive cases from accepted product behavior, include meaningful failure/adversarial conditions and preserve privacy when promoting observed failures into fixtures. No external dataset service or record format is required.

After meaningful AI changes run deterministic handling checks, then authorized live quality comparisons when relevant. Record code/model/prompt/tool configuration and dataset/evaluator versions, sample size, per-case failures, latency and usage alongside quality. Repeat stochastic cases sufficiently for the decision and report variability; one favorable generation or aggregate score cannot hide failed authority/task constraints. Calibrate model judges against accepted human examples, include human review for unresolved subjective judgments and keep deterministic invariants outside the judge. Do not silently change expected outputs, thresholds or rubrics to pass. Mocks establish application behavior only.

Use OpenTelemetry-compatible model/tool instrumentation and configurable OTLP routing where supported, without adding vendor calls to business logic. Coordinate SDK ownership to avoid duplicate spans. Execution telemetry must distinguish logical task completion from one successful model call; protect prompt/input/output data at source. Use observability-operations when installed for deeper pipeline guidance, but retain these portable defaults independently.

Use Langfuse only when its datasets/experiments/prompt workflow is useful; publish through an integration boundary and retain runnable application-side cases/scorers. SigNoz can provide a unified execution view without replacing quality evaluation. Match edition/version support and service footprint to the project. Evaluation should remain runnable without a dashboard; missing provider access leaves live quality unverified. Consult [evaluation references](references/evaluation-references.md) for deeper setup.

## Report completion and limits

Version evaluation examples and prompts when they affect behavior. Report what is implemented, deterministic checks run, live evidence gathered and unresolved gaps. Compare against the stated criteria; do not declare quality verified when live evaluation is blocked. Use the workflow bundle for documentation/E2E/delivery when available and update operational notes for quotas, limits and failure handling.

## Build MCP interfaces

Use installed `mcp-builder` for protocol implementation. Prefer Python and standalone `fastmcp` (`uv add fastmcp`, `from fastmcp import FastMCP`) with a tested compatible version pinned for production. Its API differs from the MCP SDK's `mcp.server.fastmcp`; adapt Context, lifecycle, auth and transport examples against version-matched standalone documentation. Preserve an existing server until migration is in scope.

Expose narrow typed tools over authorized application services. Verify discovery, contracts, missing/invalid credentials, resource ownership, side-effect policy, failure handling and transport/lifespan cleanup. MCP tooling can support AI applications without making the server itself an AI system.

## Connect agent interactions and generated UI

Consider AG-UI for typed agent/user interaction events, streaming messages/state/tool results and cancellation, and A2UI for declarative generated UI rendered through a client-controlled component catalog. These are complementary implementation choices, not interchangeable agent frameworks or substitutes for application authorization. Use them when the product benefits from interactive agent state or generated surfaces; preserve an accepted simpler interface.

Read [interaction protocols](references/interaction-protocols.md) when selecting or implementing them. Verify installed SDK, framework adapter, transport and renderer compatibility against a pinned protocol version; do not mix A2UI message families across versions. Validate allowed components/actions, bindings and resource/tenant scope in deterministic code. Generated UI is untrusted data and cannot execute arbitrary scripts or authorize a mutation. Test malformed/unknown components, unauthorized actions, stream interruption, reconnect/cancellation, stale events and real rendered user interactions. Separate fixture-driven protocol/renderer evidence from live model output quality.

For collaborative/spatial or existing-session products, use the corresponding branches in interaction-protocols: verify state ownership, concurrency and supported session/permission contracts independently of generated UI quality. A fixture establishes only its simulated boundary.
