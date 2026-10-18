---
name: ai-conventions
description: Apply Gemini, Google ADK, LangChain/LangGraph and standalone FastMCP conventions to an accepted AI or MCP design. Use when selecting or integrating those providers, frameworks, observability tools or Python MCP APIs; preserve established implementations.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  stack: Gemini, Google ADK, LangChain, LangGraph, FastMCP
  role: support
---

# Apply the selected AI stack

Use [evaluated AI engineering](../build-evaluated-ai/SKILL.md) for task contracts, authority and evaluation. This guidance owns technical defaults and integration choices, not product scope or quality commitments. Preserve an accepted provider/framework unless changing it is requested or a consequential decision is reopened.

## Select implementation depth

For one generation, extraction or transcription call, start with a direct model SDK behind an application adapter. Use Google ADK or LangChain when orchestration/integrations justify it; consider LangGraph for explicit stateful branching or resumable workflows. Do not introduce both framework families by default. Load installed ADK or LangChain/LangGraph specialists only for the selected stack and unfamiliar implementation details.

Prefer Gemini for low-cost LLM and transcription experiments. Verify current capabilities, quota, pricing and data-handling terms for the selected model/account before live use; free-tier eligibility is not a promise that all calls are free. Keep settings and credentials in configuration and domain behavior testable without the provider. Uploaded-audio transcription and streaming voice need different implementations and evidence.

## Implement Python MCP with version-matched APIs

Use installed mcp-builder for protocol implementation when available. Prefer Python and standalone fastmcp (`uv add fastmcp`, `from fastmcp import FastMCP`) with a tested compatible production version. Its API differs from the MCP SDK's mcp.server.fastmcp; check Context, lifecycle, authentication and transport against the selected standalone version. Preserve an existing server until migration is in scope.

Reuse authorized application services. Verify discovery, contracts, denied access, resource ownership, side effects and transport/lifespan cleanup through build-evaluated-ai. An MCP-only server requires protocol and application evidence rather than model-quality evaluation.

## Integrate observability without owning the application

Use OpenTelemetry-compatible instrumentation and configurable OTLP routing where supported; coordinate SDK ownership to avoid duplicate spans and protect sensitive inputs at source. Langfuse is optional when its dataset/experiment/prompt workflow is useful; retain runnable application-side cases and scorers. SigNoz can provide execution visibility without replacing quality evaluation. Match edition/version support and service footprint to the project; no dashboard is required for evaluation.

Use [evaluation references](../build-evaluated-ai/references/evaluation-references.md) for deeper setup and the chosen protocol's version-matched guidance for AG-UI/A2UI. Keep technical configuration, actual checks and unavailable capabilities explicit; an installed SDK does not establish end-to-end interoperability.
