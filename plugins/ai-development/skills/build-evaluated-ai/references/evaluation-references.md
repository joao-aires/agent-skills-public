# AI evaluation and telemetry references

- [Langfuse datasets](https://langfuse.com/docs/evaluation/experiments/datasets): representative cases and experiments; keep application-side cases/scorers runnable independently.
- [Langfuse self-hosting](https://langfuse.com/self-hosting): local Compose and supported deployment boundaries.
- [OpenTelemetry GenAI conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/): verify stability and installed integration compatibility.
- [SigNoz AI observability](https://signoz.io/docs/ai-observability/): execution cost/usage/latency/tool visibility, distinct from product quality acceptance.

Deterministic authorization, side-effect and schema checks remain required even when a model judge rates an answer highly. Report provider calls, judge variability and unexecuted cases accurately.

## Speech evaluation

Select representative languages/dialects, recording devices/conditions, noise, silence and domain vocabulary from the actual product. For Portuguese, include the intended Portuguese variants rather than assuming one dialect represents all speakers. Assess recognition errors and preservation of consequential terms; use word error rate when suitable alongside task usefulness. A fixture transcript cannot establish live quality. Uploaded-audio success cannot establish streaming latency, turn-taking or interruption.
