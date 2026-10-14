---
name: test-application-performance
description: Design, implement, run or review k6 load and performance checks for application
  journeys locally, against an application started on a CI runner, or against a deployed
  non-production environment. Use for latency, concurrency, throughput, saturation
  and performance regressions; preserve target authority and existing tooling.
metadata:
  scope: stack-specific
  invocation: both
  stack: Grafana k6
  role: support
user-invocable: false
---

# Test application performance

Use local k6 execution by default; no Grafana Cloud account, MCP or distributed operator is required. Keep scripts and useful workload fixtures within the target application's tests, following its layout. Add actual CI workflows there when delivery work is in scope, rather than introducing a plugin-owned pipeline framework. Preserve a suitable existing performance suite unless replacement is requested.

## Define the claim and workload

Read critical journeys, architecture, accepted targets and operating constraints. Use `reliability-design`, `plan-application-capacity` and `observability-operations` when available for outcome contracts, demand and trustworthy signals. Choose representative authenticated reads/writes, data volumes, cache conditions and traffic mix; avoid measuring only an unauthenticated health endpoint. For async work, distinguish admission from completion and track accepted jobs that miss their deadline. HTTP duration alone does not establish user-journey latency or browser rendering performance; retain Playwright for browser correctness and use browser-performance evidence when that is the claim.

Record intended arrival rate or concurrency, duration, warmup, thresholds, target and resources. Derive acceptance from user needs or an accepted comparable baseline. Label provisional values and seek unresolved product decisions; do not invent production commitments. Keep a short low-load smoke profile for script correctness, a bounded regression/load profile and longer stress/spike/soak profiles only when justified. A short smoke pass is not a capacity result.

## Implement meaningful k6 scenarios

Choose virtual-user executors for a fixed concurrent population or arrival-rate executors for independent incoming demand. Iterations can contain multiple requests: distinguish iteration rate from request rate. Size the load generator and VU allocation; inspect achieved throughput and `dropped_iterations`. A test that did not generate its intended load cannot establish that the application sustained it. In a closed model, slower responses can reduce offered traffic; account for that when interpreting overload.

Check semantic outcomes as well as expected status codes. Set explicit thresholds for relevant checks, error rate and journey/operation latency; `check()` failures alone do not make the CLI fail. Use bounded metric tags, separate important operations and explicit units. Keep scripts compatible with the pinned k6 runtime and lock or vendor remote modules. Inject credentials through protected environment/configuration and sanitize reports; never commit tokens or log full authenticated payloads.

## Support three execution targets

| Mode | Required behavior | Evidence limit |
| --- | --- | --- |
| Local development | Start the application and required dependencies, migrate and seed owned test data, confirm readiness, run the chosen profile, retain results and clean up owned resources. | This machine/configuration only. |
| Application on CI runner | Start the affected application stack on the runner, including the selected database and workers needed by the journey. Apply migrations, seed isolated data, wait for readiness and run k6 locally in that job. | Runner regression evidence; application and generator can compete for CPU/memory. |
| Deployed non-production | Run local k6 from CI or a suitable worker against an explicitly identified deployed non-production target; record served revision and environment configuration. | That deployment, traffic and resource configuration; not automatic production capacity proof. |

Reuse scenario behavior across targets with explicit target/profile configuration. Require a nonempty target and verify its identity; no fallback to production. Match the script's addresses to its network location: container localhost is not the host or another service. Fixture providers are appropriate for repeatable runner checks; label them, and exercise real integrations separately within agreed quotas and authority.

## Integrate with readable CI/CD

Use `build-delivery-pipelines` for workflow conventions and security. Prefer `performance-<application>.yml` displayed as `Performance / <Application>` with jobs `load-runner` and `load-nonprod`; adapt a clear existing convention. Use steps such as `Start application`, `Apply migrations`, `Seed test data`, `Wait for readiness`, `Run k6`, `Upload performance results` and `Stop application`.

Run small runner checks on relevant PR changes where stable and affordable. Put deployed-target checks after deployment or behind explicit/manual or project-approved scheduled triggers; installing this skill does not create a schedule. Bind the target/profile to the environment, serialize shared-environment tests and prevent untrusted PR code from receiving environment credentials. Pin k6 and any setup actions/images to reviewed versions/SHAs/digests.

Preserve k6's failing exit status through wrappers/pipes; do not mask failures with retries, `continue-on-error` or artifact upload success. Required checks must report explicitly when skipped or unavailable. Upload sanitized summaries and relevant logs on failure as well as success. Always attempt teardown via workflow cleanup/finally, including failures; k6 teardown alone cannot guarantee cleanup after process termination. Remove only owned test data/resources.

## Run, interpret and recover

Agree the deployed target's scope, duration, load ceiling, side effects, shared users, external costs and stop conditions within existing task authority. Use dedicated identities/test data and route email/payment/AI side effects to controlled fixtures or permitted sandboxes. Production testing and fault injection require their own explicit scope. Heavy load on a shared non-production environment is still a consequential operation.

Compare equivalent revisions, resources, datasets, cache state, profiles and generator conditions. Collect offered/achieved load, sample counts, latency distribution, failures, drops and relevant application/database/queue saturation. Attribute uncertainty instead of blaming the service when the generator or shared environment is constrained. Diagnose regressions; never relax thresholds merely to obtain a green check. For overload profiles verify service/queue recovery after load stops, without expanding into an unrequested chaos exercise.

Report script/profile revision, target/deployed revision, workload, thresholds, measured outcomes, fixture/live boundaries and cleanup/recovery evidence. Separate authored scripts, locally executed tests, runner checks and deployed-target checks; state blocked execution. Consult [k6 details and CI decisions](references/k6-and-ci.md) for specific unanswered questions.

Use `test-application-resilience` for controlled dependency/component faults and recovery evidence. Combining a load profile with a fault is a separate scoped experiment; a throughput result alone does not establish outage resilience.
