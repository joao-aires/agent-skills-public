---
name: tooling-conventions
description: Configure selected GitHub Actions, Docker/Compose, local quality tools,
  telemetry backends and web test drivers. Use for their implementation and compatibility
  details after the project selects those tools; preserve existing alternatives.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  role: support
  stack: GitHub Actions, Docker, Compose, prek, Gitleaks, Playwright, OpenTelemetry Collector
---

# Implement the selected development tools

Read the accepted toolchain, project commands and versions before changing configuration. This skill supplies implementation choices for matching tools; it does not select an application stack, install services merely to follow a reference or authorize publication. Preserve an existing suitable setup. Use available project, delivery, journey or operations methods for the intended outcome; retain meaningful checks and recovery evidence when those optional skills are absent.

## Choose the relevant reference

| Selected work | Reference |
| --- | --- |
| Code/configuration/secret checks and local hook setup | [Quality tools](references/quality-checks.md) |
| Dockerfiles, image inputs and runtime startup | [Container builds](references/container-builds.md) |
| Compose profiles, isolated local services and diagnostics | [Local environment](references/local-environment.md) |
| GitHub Actions adapters, trust, inputs and concurrency | [Workflow implementation](references/workflow-implementation.md); use installed github-actions-hardening for deeper matching review |
| Chosen registry and release artifact checks | [Artifact defaults](references/artifact-defaults.md) |
| Selected Collector/backend routing and AI evaluation service | [Telemetry backends](references/telemetry-backends.md) |
| Browser/Electron drivers and component workbenches | [Journey drivers](references/journey-drivers.md); use installed playwright-cli when applicable |
| Scoped fault fixtures or a selected network proxy | [Failure tools](references/failure-tools.md) |

Read only the relevant reference. Language-specific checks and packaging follow the accepted stack's conventions; native drivers follow native-client-development when available. Use performance-testing for an accepted k6 implementation, rather than imposing k6 on an existing suite.

## Verify the actual integration

Pin compatible tool versions and dependencies, keep local/CI command semantics aligned, and validate configuration with its real parser/linter and an appropriate execution boundary. A YAML parse, image build, healthy collector or static component catalogue establishes only that stage. Inspect startup, representative behavior, emitted/received signals, failure status and cleanup where those are the claim. Preserve credentials, data ownership, partial staging and protected CI trust boundaries. Record authored, locally checked, remotely run and unavailable capabilities separately.
