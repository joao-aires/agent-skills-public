# AI LangChain development plugin: LangChain and LangGraph implementation

The `ai-langchain-development` plugin carries implementation guidance for LangChain agents and LangGraph workflows: dependencies, graph construction, state and persistence. It is stack-specific and applies only after the project has chosen these libraries.

## Purpose

Use this package when the work is to build with LangChain or LangGraph rather than to decide what the AI feature should do. It covers package and dependency choices, `create_agent` tools and middleware, `StateGraph` nodes and edges, commands and streaming, and checkpoint or conversation persistence.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [langchain-dependencies](skills/langchain-dependencies/SKILL.md) | method (acquired) | Package versions, installation and dependency management for LangChain projects |
| [langchain-fundamentals](skills/langchain-fundamentals/SKILL.md) | method (acquired) | Agents with `create_agent`, tool definitions, middleware, human-in-the-loop and error handling |
| [langgraph-fundamentals](skills/langgraph-fundamentals/SKILL.md) | method (acquired) | StateGraph, state schemas, nodes, edges, Command, Send, invoke and streaming |
| [langgraph-persistence](skills/langgraph-persistence/SKILL.md) | method (acquired) | Checkpointing, conversation memory, history and subgraph persistence |

## Boundaries

- Evaluation design and evidence belong to the AI evaluation activity and the Python evaluation package.
- Provider and model selection, product behavior and acceptance remain with their owning activities.
- Deployment, credentials and runtime operations belong to delivery and platform packages.

### Acquired sources

| Skill | Source | Pin |
| --- | --- | --- |
| langchain-dependencies, langchain-fundamentals, langgraph-fundamentals, langgraph-persistence | langchain-ai-langchain-skills | `16a992f` |

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](https://github.com/joao-aires/agent-skills-public/blob/main/docs/maintainers/upstreams.md) and never edit the upstream body.
