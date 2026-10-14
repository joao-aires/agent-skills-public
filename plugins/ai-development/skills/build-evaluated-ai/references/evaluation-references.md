# AI evaluation and telemetry references

- [Langfuse datasets](https://langfuse.com/docs/evaluation/experiments/datasets): representative cases and experiments; keep application-side cases/scorers runnable independently.
- [Langfuse self-hosting](https://langfuse.com/self-hosting): local Compose and supported deployment boundaries.
- [OpenTelemetry GenAI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/): verify stability and installed integration compatibility.
- [SigNoz AI observability](https://signoz.io/docs/ai-observability/): execution cost/usage/latency/tool visibility, distinct from product quality acceptance.

Deterministic authorization, side-effect and schema checks remain required even when a model judge rates an answer highly. Report provider calls, judge variability and unexecuted cases accurately.
