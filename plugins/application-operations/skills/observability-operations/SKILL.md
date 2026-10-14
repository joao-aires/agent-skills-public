---
name: observability-operations
description: Implement, audit and maintain application/infrastructure logs, metrics,
  traces, client telemetry and collection pipelines during setup, feature work or
  recurring instrumentation improvements.
metadata:
  scope: generic
  invocation: both
  version: '2.0'
  role: task
---

# Observability implementation and operations

Make the application's behavior observable with trustworthy, affordable and protected telemetry. Journey definitions, SLO targets and alert policy belong to `reliability-design`; this skill implements their signal contracts.

## Modes and discovery

- **Interactive/setup:** inspect the runtime and existing libraries/collectors, explain integration options and implement the chosen signal contract.
- **Feature/maintenance:** instrument new or changed request/job/event paths, preserve schema compatibility and update collection/configuration/tests.
- **Recurring review:** audit changed code/config plus actual sample data, detect missing fields/context/redaction and pipeline regressions, prepare bounded fixes and track stable findings. Do not manufacture an SLO or mute alerts as an instrumentation fix.

Identify actual service/environment/version tags, instrumentation libraries, runtime/collector configuration, export protocol, logs/metrics generation stages, sampling, access and retention. Declaration in a manifest does not prove collection works. Mark live checks outstanding when access is absent.

Consult [references/signal-contract.md](references/signal-contract.md) for deeper implementation details when needed.

## Implement signals

1. Emit structured JSON logs with UTC-compatible timestamp, severity, service, environment, version and message; maintain the project's schema or explicit mappings.
2. Propagate trace context across request and async boundaries using supported libraries; add custom correlation only where it provides missing coverage. Clear scope after completion to avoid context leakage.
3. Emit one canonical summary per work/attempt including failures and bounded duration/outcome fields. Observe start/admission and deadline/completion separately where silent failures matter.
4. Implement counters and duration histograms/distributions with explicit units and bounded labels. Request/user/work IDs, arbitrary URLs and exception text are not metric dimensions.
5. Configure platform/runtime/queue/datastore collection and separate role/deployment identities where needed. Normalize operation routes and preserve useful failure signals.
6. Keep secrets, authentication session values, personal/financial payloads and sensitive query strings out at source. Apply collector masking as a secondary barrier; logging must not fail the application.
7. Version-control collection/filter/retention/sampling configuration and validate effective target overrides. Filter low-value successful health traffic without hiding failures.
8. Test parsing/types, context propagation, success/failure/timeout summaries, metric labels/units, redaction and exporter outage behavior. Verify representative data reaches the intended backend.

## Operate the pipeline

Inspect drop/filter/sampling rules, export queue/backpressure, collector health and ingestion latency. Trace storage sampling may differ from statistics generation. Derived metrics must use fields available at their actual processing stage.

Temporary diagnostic logging/profiling needs a bounded scope/time, protected writable storage and restoration. Apply data-classification retention/access requirements locally. Provide signal/query documentation for downstream reliability and incident work.

## Completion evidence

Return implementation/configuration changes, schema/contract tests, representative signal evidence, pipeline coverage/cost implications and outstanding live checks. Keep locally tested and backend verified states separate; stable recurring findings can conclude no change is needed.
