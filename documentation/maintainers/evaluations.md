# Evaluating the collection

[Maintainer guide](../maintainer-reference.md) · [Trial procedure](#generation-trials) · [Evidence](#recorded-evidence-and-limits) · [Local agy example](#local-runner-example-agy)

The [evaluation cases](../../evals/development-workflows.json) contain 16 behavior prompts and three generation trials, with separate evaluator criteria. They assess engineering behavior, evidence accuracy and unnecessary complexity. Planning exercises and package checks do not prove a working application. These trials do not run automatically in CI.

## Generation trials

The specification is harness-independent: interactive or automated execution, supported plugin/skill loading, explicit selection or plain-language requests, and conversation continuation or factual handoffs. Preserve resources and native controls; record unsupported capabilities. No particular CLI, slash syntax or trace format is required.

| Trial | Phases | Evidence |
| --- | --- | --- |
| New saved-search application | setup → agreed answers → develop | Working startup/migrations, private persisted journeys, rendered UI, checks, feature worktree and local commit |
| Existing SQLModel library | improve → approve a finding → implement | Real reproduction/baseline, focused fix, preserved tools/contracts, regression checks and local commit |
| Small documentation change | implement | Focused contribution without unnecessary setup, UI design or application testing |

1. Prepare a disposable repository with no production credentials or writable publication remote. Confirm guidance inventory, tools, authentication, allowed actions and run limits.
2. Establish baseline behavior and expected acceptance before implementation. Give the acting agent only the raw phase prompt, repository and product context; keep evaluator criteria and prior diagnoses separate.
3. Answer consequential setup questions and carry accepted answers forward. Approve one real OSS finding before implementation; select another task if no useful finding exists instead of inventing a defect.
4. Continue the phases with their accepted context. Use fresh checkout/context for independent reruns. Preserve explicit-only invocation controls.
5. Inspect actual diffs, commits, commands and runtime evidence. Classify completed, partial or blocked; distinguish guidance failures from missing capabilities. Process exit and self-rating alone cannot establish success.

| Record | Include |
| --- | --- |
| Inputs | Repository/guidance revisions, harness/model versions/configuration, inventory, capabilities, scope and limits |
| Execution | Commands/results, diff/commit, runtime artifacts, interventions and redacted session/tool events where available |
| Limits | Unexecuted checks, mocked boundaries and unknown routing evidence; reported time/token usage only when available |

If skill reads cannot be observed, routing remains unknown. Keep secrets out of prompts and artifacts. Repair a demonstrated failure and independently rerun the affected case. Grade behavior rather than phrase matching or an arbitrary passing percentage. A single run cannot guarantee quality.

## Compare and simplify

Compare complete bundles with pristine upstream guidance and its native dependency groups. Hold application baseline, outcome, context, harness, model, tools and permissions constant. Use equivalent plain-language requests where local activity names do not exist upstream, recording the difference. Unavailable prerequisites remain limitations; do not invent tracker setup or weaken controls. Cross-harness/model comparisons cannot isolate the effect of the skills.

Inspect observed behavior, missed pointers, repeated reading, unnecessary work and available cost/latency evidence. Consolidate one repeated rule at a time and rerun the affected full and small-change cases. Keep short authority boundaries beside live actions. Preserve upstream bodies/resources and record adapter changes. [Rule ownership](../maintainer-reference.md#keep-guidance-focused) identifies where shared guidance belongs.

## Recorded evidence and limits

| Check | Recorded result | Boundary |
| --- | --- | --- |
| Collection packaging | Seven bundles: 48 local + 37 upstream skills. Metadata, regression tests, all-plugin builds, inventory/notices/resource parity and explorer smoke checks passed. | Current checks run in [CI](https://github.com/joao-aires/agent-skills-public/actions); not application execution. |
| Copilot CLI 1.0.95 | Session-local discovery of all 85 skills and the default three-plugin set of 56. | Menu filtering/compliance unproven. Direct installation warned of deprecation and dropped an unrelated entry on reinstall; README uses session-local loading. |
| agy 1.3.5 | Default bundles installed; 56 discovered skills and complete installed-file parity. | Generation probe required fresh sign-in; no generated application result. |
| Planning and local Git | Fresh scoped planning exercises; disposable feature/test/Conventional Commit/local-remote push exercise passed. | No live GitHub PR publication established by that exercise. |
| Diagrams and explorer | SDLC SVG rendered/inspected; original architecture resources preserved; explorer model/render smoke checks passed. | Browser execution blocked by missing Chromium; no native-device verification. |
| VS Code | Loading instructions follow official documentation. | Not exercised here. |
| Application trials | SQLModel checkout prepared. | Full generation trials remain unexecuted; local Docker unavailable for Compose. |

No telemetry ingestion, native-client run, live AI quality/load/fault test, deployment or restore is established by these checks. Package/discovery success does not prove model compliance or production readiness. Revision-specific history remains in Git; keep this table about useful evidence and open limits.

## Local runner example: agy

I chose `agy` for my local tests. The [README](../../README.md#2-load-them-in-your-client) owns installation instructions; this example adds no dependency to the trial specification or plugins.

```bash
agy plugin validate "$AGENT_PLUGINS_DIR/development-workflow"
agy plugin list --json
agy -p '<phase prompt>' --output-format stream-json --print-timeout 20m
```

Run from the target repository, capture stdout/stderr outside it, and use the installed client's conversation option for continuation. The 20-minute limit is a local choice. Check tool events and soft denials even on exit zero. Use scoped permissions and the client's sign-in flow; never put sign-in codes in prompts/traces. The recorded discovery run used workflow 0.17.0; fresh sign-in and Docker availability blocked application/Compose execution independently.
