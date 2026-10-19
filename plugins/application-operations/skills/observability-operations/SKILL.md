---
name: observability-operations
description: Implement, audit and maintain application/infrastructure logs, metrics,
  traces, client telemetry and collection pipelines during setup, feature work or
  recurring instrumentation improvements.
metadata:
  scope: generic
  invocation: both
  version: '2.1'
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

## Keep instrumentation independent of the backend

Use the accepted instrumentation contract and compatible framework/database/HTTP libraries. OpenTelemetry/OTLP are options when standard interchange and a replaceable backend meet the requirements; a generic signal method does not require a new SDK or exporter. Keep business spans/metrics in application code, SDK/export initialization at the application boundary, and backend endpoints/credentials/routing in configuration or Collector exporters. Validate the selected SDK and effective configuration at the application boundary. Preserve an existing stack unless migration is authorized; do not run competing SDKs/providers that create duplicate spans.

Give telemetry consistent service, environment and application revision identity using adopted resource conventions. Add bounded domain outcome attributes and propagate supported context across API, queue/worker and tool boundaries. Track trace/run IDs in diagnostic records, not unbounded metric labels. Use version-matched GenAI conventions for model/tool spans and record relevant model/prompt version, latency, outcome and usage. Review evolving semantic conventions and third-party instrumentation compatibility rather than assuming every framework emits the same fields.

Keep application instrumentation separate from backend routing, credentials and storage. Use a bounded collection/processing boundary when needed, and verify units, aggregation, resource identity and supported signal types during translation. Standard transport does not make dashboards, queries, alerts, profiling or proprietary features portable. Use available tooling-conventions for selected backend/Collector configuration and matching stack expertise for SDK initialization.

For browser/mobile/desktop telemetry use suitable supported SDKs and a controlled ingestion boundary with appropriate rate limits, network/CORS configuration and source redaction. Never ship privileged backend credentials or sensitive payloads to a client. Collector redaction is secondary to preventing capture. Telemetry failure must not break the user journey: bound buffers/retries, expose drops and verify degraded-export behavior.

## Connect local telemetry to evaluation

Use the project's selected local service mechanism with explicit connectivity, readiness and resource/retention bounds. Add only the backend the requested diagnostic capability needs. Expose supported read/query APIs or CLI for agents as well as dashboards for people; an MCP is optional and its availability must be verified. Keep query access scoped and correlate scenario/run, revision and environment with the relevant trace and logs. Capture sanitized diagnostic artifacts for failed checks; do not claim ingestion from a container being healthy.

Exercise a representative successful journey and a controlled error through actual services. Check expected span relationships across request/worker/tool boundaries, durations/units/outcomes, log correlation and sensitive-data exclusion. Assert generated telemetry at an inspectable export/test boundary and verify receipt/query in the selected backend when available. This separates an application instrumentation defect from a routing/backend failure; document unverified destinations instead of claiming compatibility with every backend. For a backend switch test ingestion and affected translations/queries explicitly.

AI execution telemetry explains latency, failures, tool use and usage; it does not prove answer quality. Keep evaluation cases, expected outcomes and deterministic scoring/version identity portable in the application. Add an external dataset/experiment service only for a useful accepted workflow, through an adapter without a service dependency in domain logic. Avoid duplicate instrumentation/exports and identify which pipeline owns each signal. Use matching technical guidance for backend/version-specific setup; missing tooling leaves that destination unverified, not a reason to select a vendor.

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
