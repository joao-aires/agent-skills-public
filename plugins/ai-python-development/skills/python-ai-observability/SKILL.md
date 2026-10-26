---
name: python-ai-observability
description: Set up and verify Python AI observability with OpenTelemetry and compatible model/framework instrumentation. Use for AI task/tool/retrieval traces, usage and latency signals, export/privacy configuration and operational diagnosis; keep the chosen backend and quality evaluation separate.
user-invocable: false
metadata:
  scope: stack-specific
  invocation: both
  stack: Python, OpenTelemetry, OTLP
  role: support
---

# Instrument Python AI execution

Use the accepted task/service outcomes and operating constraints. Seek available reliability/observability and AI-evaluation expertise for signal meaning and quality boundaries; keep those outcomes explicit when specialist guidance is absent. This skill owns Python AI instrumentation and export integration. Collector/backend deployment, service SLO design and quality scoring remain separate responsibilities.

## Establish instrumentation ownership

Inspect existing Python SDKs, framework/provider integrations, tracer/meter providers, exporter configuration and process lifecycle. Reuse the application telemetry owner rather than initializing another global provider or instrumenting the same model call twice. Select compatible locked API/SDK, exporter and instrumentor versions; provider/framework wrappers need support for the actual installed versions and execution path.

Place application spans around work whose completion matters to the user or operator, then connect provider, retrieval and tool calls beneath that work where supported. A span should have a recognizable beginning and end and record whether its own operation succeeded. Ending a parent request while background work continues requires an explicit lifecycle and supported context propagation, rather than keeping an unrelated span open indefinitely.

Choose manual OpenTelemetry spans for application task boundaries and supported automatic instrumentation for concrete provider/framework calls when useful. Follow [Python instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/) and the selected instrumentor's primary documentation. A direct SDK call, a framework graph and a remote harness have different visibility; inspect supported hooks rather than claiming hidden remote steps are traced.

For application-owned manual setup, use the compatible SDK's `Resource` and `TracerProvider`, a `BatchSpanProcessor` and the selected `OTLPSpanExporter`; application spans use `trace.get_tracer()` and its context-managed span API. Libraries obtain the configured tracer rather than installing a provider. Match startup/flush/shutdown to the actual worker/server lifecycle.

## Describe useful AI signals

Link the request/task, retrieval, model, tool and relevant delegated-work spans through actual trace context.

- Separate user task success from provider completion, tool result status and evaluation score.
- Capture operation/configuration revision, duration, failure category and usage where available; mark estimates and missing fields explicitly.
- Measure time to first useful output versus full completion when that distinction matters.

Use the compatible [GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) supported by the chosen instrumentation. Check their version/stability and opt-in behavior instead of copying assumed attribute names. Keep application-specific outcome fields clearly owned and documented; do not emit vendor-specific fields into unrelated backend spans. Use bounded metric dimensions; per-user/session/request identifiers belong only in permitted trace context, not unbounded metric labels.

Preserve context through async tasks and background jobs using supported propagation. Define when each operation begins and ends, including work that outlives its initiating request.

Correlate retries, cancellation and resumed work without inventing parent spans or exposing internal reasoning. For remote peers, retain only the relationships their supported correlation can establish; missing context remains a visibility gap.

## Protect content and configure export

Prefer operational metadata without raw prompts, completions, retrieved documents, tool arguments/results or recordings.

- Enable content capture only for an accepted purpose with appropriate access, redaction, sampling, retention and deletion.
- Filter sensitive payloads before recording/export; exporter-side redaction cannot undo earlier local capture.
- Keep credentials and private instructions out of attributes and exception events.

Use the application's selected backend and supported OTLP transport.

- Configure the compatible exporter, destination, credentials/TLS and resource identity through the existing configuration.
- Follow [Python exporters](https://opentelemetry.io/docs/languages/python/exporters/); verify actual environment-variable support, endpoint shape and protocol rather than assuming gRPC and HTTP settings are interchangeable.
- Use batching, bounded queues/sampling and process-appropriate flush/shutdown.
- Instrumentation failures must not turn into duplicate tool effects or uncontrolled request failure.

A selected AI observability platform may add its own exporter, fields, experiment views or online scoring. Verify region, license/edition and data-handling constraints before integration; do not introduce an account, dashboard or second telemetry backend merely because one SDK recommends it. Use relevant deployment expertise for Collector/backend setup when available.

## Verify received evidence and operating behavior

1. Test a representative deterministic path with an in-memory or isolated exporter: nesting/context, success/failure, retries/cancellation, bounded dimensions, sensitive-data exclusion and shutdown.
2. Within authorized scope, confirm receipt and useful correlation at the selected destination for a known task.

SDK initialization or successful export alone cannot prove queryable end-to-end traces.

Exercise queue pressure, unreachable exporters, sampling and process shutdown to the extent relevant to the service. Distinguish dropped/sampled records from complete coverage and check overhead against the operating budget. Keep retention/export failures visible through the project's diagnostics without leaking payloads.

Use traces to diagnose execution and select privacy-reviewed evaluation cases; use separate evaluators to judge task usefulness. Link known configuration/evaluator revisions rather than silently equating a healthy trace or a sampled online score with complete quality verification. Report the actual target, received signals, fixture/live boundaries and unresolved collection gaps, then update the relevant runbook/configuration notes.
