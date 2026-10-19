# Failure experiments

Use the entry point for routine decisions. Choose mechanisms from the actual application/platform rather than transplanting a tool's example into production.

| Case | Observe |
| --- | --- |
| Slow/refusing upstream | Bounded request deadline, retry budget, useful failure response and unaffected journeys. |
| Remote write with lost response | Actual provider state/idempotency reconciliation before repetition; unresolved effects stay visible. |
| Worker loss after durable progress | Restart-safe progress, correct claim/acknowledgment behavior and no repeated business effect. |
| Connection/pool exhaustion | Bounded waiting, deliberate rejection/backpressure, retained diagnostics and restored service after release. |
| Dependency restart/unavailability | Data invariants, client reconnection, meaningful readiness/liveness behavior and independent user recovery. |
| Invalid configuration/flag evaluation | Validated defaults, chosen failure policy and observable effective revision; no broad permissive fallback. |

Record control/baseline, hypothesis, target, fault method and scope, observation, stop condition and restoration. Use the existing project record format. Do not import numerical thresholds or a production-first experiment policy from a reference.

- [Principles of chaos engineering](https://principlesofchaos.org/) explains hypothesis-driven experiments and limiting impact. Apply the task's authorized environment/action boundaries.

A fixture may reproduce an application's error branch without reproducing a real provider's ambiguous commit behavior. If that ambiguity matters, use a controlled service capable of committing and withholding its acknowledgment. Confirm the fault mechanism and persistent outcome independently; don't label a mock result as verified external recovery.
