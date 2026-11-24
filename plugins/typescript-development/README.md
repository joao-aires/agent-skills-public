# TypeScript development plugin: runtimes, libraries, services and clients

The `typescript-development` plugin carries implementation guidance for TypeScript outside React: module and package contracts, runtime boundaries, validation and verification. It is stack-specific and applies to an accepted runtime and toolchain.

## Purpose

Use this package when the work depends on TypeScript mechanics: how modules and public types are shaped, how runtime and build boundaries differ, how input is validated, or how the project proves a change with its actual toolchain.

## Responsibilities

| Skill | Type | Responsibility |
| --- | --- | --- |
| [typescript-conventions](skills/typescript-conventions/SKILL.md) | method | Module and package contracts, runtime and build boundaries, validation, dependencies and checks |

## Boundaries

- React and Next.js implementation belongs to the React package.
- Backend service behavior and data contracts belong to backend design.
- The package does not choose a runtime or framework; the accepted stack does.

## Maintenance

Bump `plugin.json` when packaged content changes. Keep the skill descriptions as the selection surface: a new capability needs a description that says when to use it and when not to, not a route from another skill. Acquired skills stay pinned in `agent-depot.json`; update them through [upstream maintenance](../../docs/maintainers/upstreams.md) and never edit the upstream body.
