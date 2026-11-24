# AI Python development plugin: providers, MCP servers, evaluation suites and observability

The `ai-python-development` plugin carries the Python side of AI implementation: model and provider adapters, standalone MCP servers, DeepEval suites and OpenTelemetry instrumentation. It is stack-specific and composes with the generic AI design and evaluation activities.

## Purpose

Use this package when an accepted AI design needs Python implementation detail: a version-matched provider adapter, a FastMCP interface, an evaluation suite that runs, or traces and spans that explain an AI task. It does not decide what to evaluate or whether a result is good enough.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [ai-conventions](skills/ai-conventions/SKILL.md) | method | Python model/provider adapters and standalone FastMCP interfaces, version-matched SDK use and packaging |
| [ai-deepeval-testing](skills/ai-deepeval-testing/SKILL.md) | method | DeepEval suites for model, retrieval, agent trajectory, conversation and end-to-end quality |
| [mcp-builder](skills/mcp-builder/SKILL.md) | method (acquired) | Model Context Protocol server design and implementation |
| [python-ai-observability](skills/python-ai-observability/SKILL.md) | method | OpenTelemetry setup and verification for AI tasks, tools and retrieval |

## Boundaries

- Evaluation cases, graders and sufficiency belong to [ai-evaluation](../ai-development/skills/ai-evaluation/SKILL.md); this package implements the chosen approach.
- Product behavior, provider strategy and model choice are accepted elsewhere.
- Serving, scaling and release belong to delivery and platform packages.

### Acquired sources

| Skill | Source | Pin |
| --- | --- | --- |
| mcp-builder | anthropics-skills | `8a1541c` |

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](../../docs/maintainers/upstreams.md) and never edit the upstream body.
