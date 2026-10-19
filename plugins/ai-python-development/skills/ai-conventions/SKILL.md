---
name: ai-conventions
description: Implement accepted Python model/provider adapters and standalone FastMCP interfaces. Use for Gemini integration, version-matched Python MCP APIs and interaction integration; preserve established providers and frameworks.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  stack: Python, Gemini, standalone FastMCP
  role: support
---

# Apply the selected AI stack

Use AI contract and evaluation expertise when available for task contracts, authority and evaluation; otherwise retain explicit success/failure, authorization and quality evidence in the application. This guidance owns technical defaults and integration choices, not product scope or quality commitments. Preserve an accepted provider/framework unless changing it is requested or a consequential decision is reopened.

## Implement the accepted provider boundary

Use the application's Python adapter and locked, compatible SDK version. Framework choice belongs to the accepted architecture: use installed ADK or LangChain/LangGraph specialists only for that chosen framework, without introducing either family for a direct SDK call. Keep provider configuration and credentials at the integration boundary.

Prefer Gemini for low-cost LLM and transcription experiments. Verify current capabilities, quota, pricing and data-handling terms for the selected model/account before live use; free-tier eligibility is not a promise that all calls are free. Keep settings and credentials in configuration and domain behavior testable without the provider. Uploaded-audio transcription and streaming voice need different implementations and evidence.

## Implement Python MCP with version-matched APIs

Use installed mcp-builder for protocol implementation when available. Prefer Python and standalone fastmcp (`uv add fastmcp`, `from fastmcp import FastMCP`) with a tested compatible production version. Its API differs from the MCP SDK's mcp.server.fastmcp; check Context, lifecycle, authentication and transport against the selected standalone version. Preserve an existing server until migration is in scope.

Reuse authorized application services. Verify discovery, contracts, denied access, resource ownership, side effects and transport/lifespan cleanup; use AI contract and evaluation expertise when available for the method. An MCP-only server requires protocol and application evidence rather than model-quality evaluation.

## Integrate without owning the application

Coordinate Python SDK/instrumentation ownership to avoid duplicate spans and protect sensitive inputs at source. Use the accepted export backend and compatible library versions; use available observability expertise for signal contracts and guidance for the selected development tools for selected Collector/backend setup. Keep evaluation cases and scorers runnable without those services. Use [DeepEval testing](../ai-deepeval-testing/SKILL.md) when DeepEval is the accepted evaluator and [Python AI observability](../python-ai-observability/SKILL.md) when implementing OpenTelemetry instrumentation; neither selects a hosted service. An installed SDK does not establish interoperability or answer quality.

For an accepted AG-UI/A2UI integration, read [version-matched interaction integration](references/interaction-integration.md) and use the chosen framework's compatible adapter. Keep technical configuration, actual stream/render checks and unavailable capabilities explicit.
