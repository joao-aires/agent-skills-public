# Go development plugin: accepted services, libraries and CLIs

The `go-development` plugin carries implementation guidance for Go: modules and package boundaries, lifecycle and error contracts, concurrency, dependency choice and verification. It is stack-specific and applies to an accepted design.

## Purpose

Use this package when the work depends on Go mechanics: how to shape packages and APIs, how errors and lifecycle are expressed, how concurrency and cancellation are bounded, or which standard tooling proves the change.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [go-conventions](skills/go-conventions/SKILL.md) | method | Module and package structure, API and error contracts, lifecycle, concurrency, dependencies and checks |

## Boundaries

- Service behavior, authority and data contracts belong to backend design.
- Infrastructure, pipelines and release stay with delivery and platform packages.
- The package does not select Go for a project; the accepted stack does.

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](https://github.com/joao-aires/agent-skills-public/blob/main/docs/maintainers/upstreams.md) and never edit the upstream body.
