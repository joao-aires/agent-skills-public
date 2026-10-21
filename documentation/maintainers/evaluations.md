# Evaluating the collection

[Current status](#current-status) · [Run a scenario](#run-and-grade-a-scenario) · [Generation trials](#generation-trials) · [Evidence limits](#recorded-evidence-and-limits) · [Maintainer guide](../maintainer-reference.md)

The [evaluation specification](../../evals/development-workflows.json) contains 52 behavior cases, 12 generation trials and an eleven-flow coverage map. It separates actor inputs from evaluator criteria. Definition checks run in CI; behavioral trials require their own fixtures, capabilities and execution.

## Current status

The [ownership catalogue](sources.md#plugin-ownership) records the current package and skill inventory. Repository checks validate metadata, maintained links, acquisition pins, resource closure, complete inventories and independent builds. They do not establish correct discovery, routing, cross-stack transfer, live integration or application behavior.

A [bounded planning/assessment record](../../evals/results/capability-expansion/results.json) covers nine synthetic cases at its recorded source revision, including a workflow-only fallback case. Independent actors received source guidance; the author graded their outputs against criteria withheld from them. All nine met those scoped criteria. This establishes neither installed-client discovery nor application/runtime behavior; the record retains inputs, outputs and per-criterion observations.

The current collection has not received a complete behavioral rerun. Earlier trials used different inventories and configurations; their results cannot be transferred to the current guidance. See [recorded evidence and limits](#recorded-evidence-and-limits) for the boundaries of those observations and [architecture](../architecture.md) for the supported composition model.

## Intended flows and execution levels

The specification's flow_matrix connects cases to user outcomes: product-to-design, project setup versus complete applications, UI assessment/repair, design-tool handoff, research, native/private-data applications, AI/session integration, delivery/operations and maintenance. Migration, jobs, incidents, performance, resilience and libraries are also represented. Cross-cutting cases assess identity/access lifecycle, SaaS dashboards and commercial recovery, GDPR/SOC 2 evidence, PostgreSQL, TypeScript and Go contracts, plus absent-specialist fallback. Browser-extension cases cover design-only work, an existing UI system, standalone guidance, real MV3 contexts/lifecycle and store preparation without promotion.

| Level | Evidence produced | Boundary |
| --- | --- | --- |
| Definition/package checks | Valid structure, references, inventories and resources | No agent behavior established |
| Bounded behavioral probes | A decision or action against supplied artifacts and scoped fixtures | Only the recorded case, revision and environment |
| Application generation or repair | Actual code, checks, rendered interactions and persisted outcomes | Retain incomplete, blocked and fixture-only boundaries |
| External/native checks | Authorized tools, providers, named sessions, packaged apps or devices | Only the capabilities actually exercised |

Use evaluator_setup, evidence, negative_controls and capability_gates to prepare and grade a case. Do not paste grader answers, prior diagnoses or negative-control criteria into a blind actor's prompt. Prepare/version the required raw fixtures and record unavailable prerequisites. No executable actor harness or participant study is supplied by the definitions.

Run `python scripts/validate_evaluations.py` to validate IDs, prompts, criteria and flow references. The repository unit suite exercises this validator; neither command executes behavioral trials or assesses fixture quality.

## Run and grade a scenario

1. Pin the source/build, target repository/fixture and client configuration. Verify actual skill/tool inventory and authorized local resources. Record model identity only when exposed. Use distinct ports, database/project names and native identity, preserve unrelated services and never search global profiles/history for credentials or sessions.
2. Prepare the case's raw artifacts and expected baseline outside the actor workspace. For a regression, establish that the original behavior fails the meaningful assertion. Supply only prompt, raw context, real capabilities, action scope and actual accepted decisions; keep criteria, negative controls, prior diagnoses and answer keys with the evaluator.
3. Resolve genuine user decisions through an actual reply. For unattended exercises, a needs-decisions result can satisfy the decision-policy criterion while dependent implementation remains blocked. A proposal, evaluator preference or old plan is not user acceptance. Record factual handoffs and any intervention.
4. Inspect actual diffs/commits, commands/results, rendered interactions and persisted outcomes. Grade each criterion as pass, fail, partial, blocked or not-run, with artifact references and mocked boundaries. A known defect remains a failure even if another platform is unavailable. Missing read traces make routing unknown, not necessarily incorrect; explicit reads alone do not establish correct use.
5. Keep correctness, authentication/ownership, component behavior, visual review, usability observations, foundations, protocol conformance and native/live execution separate. Never average away a critical failure. Record actual target identity; browser views, unit fixtures and compilation cannot establish native device/app operation.
6. Bound execution time and cleanup to owned resources. Provider/execution failures and successful exits with unfinished output require artifact inspection; preserve partial/uncommitted work and report the execution boundary. A coordinator intervention or repair continuation is a separate result, not a blind generation pass.

## Inspect outcomes rather than completion prose

| Concern | Useful evidence |
| --- | --- |
| Product and visual decisions | Accepted scope, contextual rationale, representative states, rendered inspection and preserved design intent |
| Interaction and accessibility | Actual keyboard/focus behavior, compatible primitives and meaningful regressions through affected callers |
| Project foundations | Clean-checkout onboarding, configuration/code checks, behavior tests, builds and applicable CI/artifact/recovery definitions |
| Private data and side effects | Real authentication, resource ownership, denied actions, safe fixtures and verified resulting state |
| Protocol/runtime interoperability | Published contracts and actual compatible peers; private schemas and installed SDK names alone are insufficient |
| Provider and stream failures | Semantic status, controlled errors, interruption/recovery and absence of unauthorized or duplicate effects |
| Generated/shared interfaces | Visible actions, persisted state, reload/reconnect, stale/concurrent edits and human control |
| Consequential decisions | Verified facts, real accepted choices and clear boundaries for dependent work |

Choose cases for the affected uncertainty. Use small-change controls to detect unnecessary setup, audits or external tooling. Grade useful findings and false positives on inspected scope; preserve acceptable intentional design variants. Research plans, synthetic observations and automated checks do not establish participant outcomes.

Keep repair and fresh generation distinct: repair receives a defect report and preserved baseline; fresh generation receives the product brief and constraints without old code or grader diagnoses. Evaluate native platforms separately. Browser views, filtered unit tests and compilation cannot establish native runtime operation.

Gate live Figma, provider, protocol/renderer, named-session and voice checks independently. Useful local or supplied-artifact work does not satisfy a live integration claim. Account connections, private uploads and publication require their own established action scope.

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

Past trials established some bounded application and tool behavior and also exposed material failures. Their detailed historical summaries remain in Git history; the summary below does not claim a passing result for the current collection.

| Area | Observed boundary |
| --- | --- |
| Client discovery | Discovery was observed with particular older client versions and inventories; current installation and instruction adherence need separate checks |
| Application generation | Some persistence and access-control journeys worked, while foundations, UI behavior, contribution isolation and authentication still had gaps |
| Native clients | A macOS application was exercised; iOS/Android unit fixtures did not establish device/runtime behavior |
| Agent/UI protocols | Application-owned format checks passed payloads rejected by a published protocol schema; interoperability remained unverified |
| Figma | Scoped design reads/writes and cleanup were observed; design-stage work did not establish a complete implementation handoff, token/component fidelity or application journeys |
| Existing agent sessions and voice | Replay, CLI continuation and fixture events did not establish the required live attachment, protocol support or real-time behavior |

Keep each result tied to its actual guidance/application revision, client/model configuration, fixtures, interventions and artifacts. A provider error, incomplete output or coordinator repair cannot be converted into an independent passing run. No broad production-readiness, native-parity or live-quality claim follows from package checks or isolated successes.
