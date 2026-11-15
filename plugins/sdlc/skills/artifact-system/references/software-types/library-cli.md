# Library/CLI

## What this is

Software consumed by other developers or operators rather than end users through a screen: a published package, SDK, command-line tool or automation entry point. Its useful behavior is judged through its public surface, compatibility and packaging.

## Design record must show

- the public API, command surface or module entry points;
- the consumer and the task the surface supports;
- compatibility: versions, platforms, runtimes and breaking-change policy;
- the dependency surface and what the consumer must accept;
- packaging and distribution: registry, binary, container or install path;
- errors, exit codes, diagnostics and help behavior;
- usage examples for the main path and one failure path;
- an artifact that lets a reviewer judge the surface.

## Typical artifacts

Read [compatibility matrix](../../../compatibility-matrix-guide/SKILL.md) for versions, platforms and consumer evidence. Typical artifacts also include an API or module sketch, command tree and flags, dependency graph or surface summary, usage examples including one failure or misuse case, and package/install layout.

## Seam decisions

When a library/CLI meets a service, runtime or consumer, decide once:

- versioning and deprecation policy;
- error and exit-code contract;
- configuration and environment precedence;
- authentication or credential expectations;
- platform and runtime support;
- packaging and install behavior.

## Variants and constraints

| Variant | Constraint owner |
| --- | --- |
| Go module, service or CLI | `go-development` — lifecycle, dependency, error and verification contracts |
| TypeScript package or CLI | `typescript-development` — module/package contracts and validation |
| Python automation or CLI | `backend-python-development` — Python automation engineering |
| Packaged binary or container | `development-tooling` — build, registry and supply-chain checks |

These are constraints on the library/CLI baseline, not separate software types.

## Verification that counts

- install or invocation in a clean consumer environment;
- the public surface exercised through its documented entry point;
- compatibility checked against the claimed versions and platforms;
- error and exit-code behavior observed;
- packaging artifact inspected, not only built.

## Optional specialists

`go-development`, `typescript-development`, `backend-python-development`, `development-tooling` and the relevant packaging guidance. If absent, retain the public-surface, compatibility and packaging reasoning.

## Not required

Wireframes, visual direction, C4 views for a single package, or a service contract when no service boundary exists.

## Example

A cache-warming CLI:

```markdown
- Affected type: library-cli
- Surface: `cache-warm --url <url> --concurrency <n>`
- Compatibility: Go 1.24+, macOS/Linux, no Windows claim
- Dependencies: standard library plus one HTTP client
- Errors: non-zero exit and a diagnostic line per failed target
- Artifact: command tree plus usage example and failure output
- Backend: not affected — the service already exposes the endpoint
```
