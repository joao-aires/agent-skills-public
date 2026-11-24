# AI ADK development plugin: Google ADK architecture, implementation and maintenance

The `ai-adk-development` plugin carries the complete Google ADK skill suite: the runtime model, agent construction, debugging, code review, style, unit documentation, samples, snippet verification, git conventions and local setup. It is stack-specific guidance for a project that has already chosen ADK.

## Purpose

Use this package when a decision depends on how ADK actually executes: what a node and graph do, how `Context` and events flow, where checkpoints and resumption live, how to structure an agent with tools and sub-agents, or how to diagnose a run that misbehaves. It does not choose the model provider, design the product behavior or decide whether an evaluation is sufficient.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [adk-architecture](skills/adk-architecture/SKILL.md) | method (acquired) | Runtime model: node and graph execution, context and event flow, checkpoint and resumption, state boundaries |
| [adk-agent-builder](skills/adk-agent-builder/SKILL.md) | method (acquired) | Python agents with tools, graph workflows of function and agent nodes, composition and handoff patterns |
| [adk-debug](skills/adk-debug/SKILL.md) | method (acquired) | Diagnose sessions, events, tool calls and model requests with `adk run` and the `adk web` debug endpoints |
| [adk-review](skills/adk-review/SKILL.md) | method (acquired) | Review an uncommitted ADK changeset for correctness, API stability, tests, samples and docs |
| [adk-style](skills/adk-style/SKILL.md) | method (acquired) | Python and repository conventions: visibility, imports, typing, Pydantic, formatting, logging, async and test layout |
| [adk-unit-design](skills/adk-unit-design/SKILL.md) | method (acquired) | As-built architecture document for one code unit, describing what is implemented and what must not change |
| [adk-unit-guide](skills/adk-unit-guide/SKILL.md) | method (acquired) | Hands-on developer guide for one code unit: runnable example, options, advanced uses and limits |
| [adk-sample-creator](skills/adk-sample-creator/SKILL.md) | method (acquired) | New samples under `contributing/samples/`, following the existing sample and README conventions |
| [adk-verify-snippets](skills/adk-verify-snippets/SKILL.md) | method (acquired) | Extract, compile and run every Python block in a Markdown file and report per-snippet results |
| [adk-git](skills/adk-git/SKILL.md) | method (acquired) | Commit messages and pull-request descriptions for the ADK repository's conventions and template |
| [adk-setup](skills/adk-setup/SKILL.md) | method (acquired) | Local ADK Python environment: uv virtualenv, extras, pre-commit hooks and a first unit-test run |

## Boundaries

- Model and provider selection, prompt strategy and evaluation policy belong to the AI design and evaluation activities.
- Application requirements, architecture and contracts are accepted before this package applies.
- Delivery, credentials and scale-out belong to the delivery and platform packages.
- The suite is the complete upstream ADK group at one pin. Its skills cross-reference each other, and every referenced skill is packaged here rather than left as a dangling pointer.

### Acquired sources

| Skill | Source | Pin |
| --- | --- | --- |
| the complete ADK skill suite (11 skills) | google-adk-python | `6be386d` |

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](../../docs/maintainers/upstreams.md) and never edit the upstream body.
