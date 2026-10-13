# k6 details and CI decisions

Use the entry point for routine decisions. These official references explain executor semantics and version-sensitive behavior.

| Question | Reference |
| --- | --- |
| What makes the CLI pass or fail? | [Thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) and [checks](https://grafana.com/docs/k6/latest/using-k6/checks/). Define the performance/correctness acceptance explicitly; failed checks need a threshold to affect pass/fail. |
| How should load be scheduled? | [Open versus closed models](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/) and [executors](https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/). Model actual demand; virtual users and requests per second are different quantities. |
| Why was requested load not achieved? | [Dropped iterations](https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/dropped-iterations/). Inspect VU allocation and generator resource limits alongside application slowdown. |
| How do targets and fixtures vary? | [Environment variables](https://grafana.com/docs/k6/latest/using-k6/environment-variables/) and [test lifecycle](https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/). Project environment variables must be consumed by the script; a custom profile label alone changes nothing. |
| How can GitHub Actions install the runtime? | [Official setup action](https://github.com/grafana/setup-k6-action). Pin its reviewed commit and the chosen k6 version; install is separate from creating the application environment. |

A runner check should explicitly establish: isolated services -> migration -> fixtures -> readiness -> k6 -> results -> cleanup. Keep failure propagation and cleanup independent so result-upload success cannot overwrite the test outcome. A deployed-target check reuses the scenario but validates target identity, revision, credentials, fixture ownership and load policy rather than trying to start or reset that environment.

The runner profile catches regressions under bounded reproducible conditions. Longer deployed-environment profiles examine the actual routing, replicas, database, cache and worker topology. Keep thresholds/profile differences explicit. Neither requires Grafana Cloud or a Kubernetes k6 operator; adopt distributed generation only after the single generator is demonstrably the bottleneck.

Keep large runtime traces and credentials outside source control. Retain enough sanitized summaries to explain a regression and compare equivalent runs; storage/retention follows the project's existing policy.
