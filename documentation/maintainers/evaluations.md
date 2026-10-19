# Evaluating the collection

[Current status](#architecture-implementation-boundary) · [Run a scenario](#run-and-grade-a-scenario) · [Generation trials](#generation-trials) · [Historical evidence](#historical-evidence) · [Maintainer guide](../maintainer-reference.md)

The [evaluation cases](../../evals/development-workflows.json) contain 38 behavior prompts, 12 generation trials and a nine-flow coverage map, with separate actor inputs and evaluator criteria. They assess engineering behavior, evidence accuracy and unnecessary complexity. Planning exercises and package checks do not prove a working application. These trials do not run automatically in CI.

## Architecture implementation boundary

Product-management, generic visual/backend methods, the AI method/adapter separation and conditional navigation are implemented as a follow-up to the merged writing refactor. This work stops before the planned architecture evaluation stage at my request. No new behavioral cases or application generation trials were executed, and existing scenario definitions remain unchanged. Repository checks establish metadata, links, packaging and resource consistency only; routing, cross-stack transfer and product outcomes remain for the next evaluation stage.

The current architecture contains 64 local and 39 pinned upstream skills, including the later agents-md and frontend-design additions. Earlier results below describe their own inventories and revisions; they do not verify this architecture. Documentation reorganization does not rerun those trials.

The package split preserves the local skill inventory and native invocation controls, plus the original 37 reviewed source commit/tree pins and complete resource groups. The later AI-skill rename and scope expansion are documented in migration; one evaluation prompt now uses its current name, without changing scenario criteria. Two later acquisitions add agents-md and frontend-design with their own reviewed pins/licenses; the AI split adds generic testing/operations plus explicitly named Python DeepEval testing and OpenTelemetry observability implementations. Their runtime behavior has not been evaluated. There are 17 packages, including nine generic capabilities and eight explicitly selected technical packages. Metadata, link, unit, complete-build and independent-build checks establish structural/resource integrity. The default build contains only the development workflow. The authoring helper's narrower quick validator rejects the supported `user-invocable` field; the repository validator retains and checks native controls.

Capability-based local entry points describe needed expertise, with fallback to project evidence, general expertise and primary sources. Shared framing and upstream adaptations stay inside the selected package. The [architecture explanation](../architecture.md) distinguishes missing guidance from missing decisions/tools. Client installation/discovery and routing/absence behavior have not been rerun; existing actor passes remain tied to their historical snapshots.

## Intended flows and execution levels

The specification's flow_matrix links every scenario to an intended user outcome: product-to-design, setup versus complete application, existing UI assessment/repair, design-tool handoff, research/learning, private platform applications, AI/session integration, delivery/operations and maintenance/evidence. Existing migration, job, incident, performance, resilience and library cases remain in scope; new UI methods do not replace them.

| Level | What runs | What it establishes |
| --- | --- | --- |
| Definition/package checks | Metadata, resource parity, evaluation structure/references, unit checks | Definitions and bundles are internally consistent; no actor behavior established. |
| Bounded behavioral probes | Supplied artifacts or small local fixtures for one case | Scoped decision, authority, method and evidence handling at recorded revisions. |
| Multi-phase generation/repair | Actual repository, real accepted answers, implemented checks and relevant running targets | Requested phase outcomes and verified application boundaries; retain partial/blocked results. |
| External/native capabilities | Separately authorized live MCP, provider, named session, packaged app or device checks | Only the specific capability observed in that environment. |

New fields evaluator_setup, evidence, negative_controls and capability_gates tell the evaluator how to prepare raw artifacts, inspect outcomes and avoid false passes. They are not additional instructions to paste into the actor's prompt. Do not tell a blind fresh actor which defect to find or provide grader answers; use actual raw fixtures. Repair trials intentionally receive defect reports and must be labelled separately. No executable actor harness, participant study or new application fixture is supplied by these definitions; prepare/version the required raw fixtures before a run and record any unavailable prerequisite.

Run python scripts/validate_evaluations.py to check IDs, required prompts/criteria and coverage references. The existing CI unit-test command exercises this validator through test_evaluations.py; it does not run the described behavioral suite. It rejects duplicate/dangling/unmapped scenarios and missing phase/assertion definitions; it does not measure compliance or fixture quality.

## Run and grade a scenario

1. Pin the source/build, target repository/fixture and client configuration. Verify actual skill/tool inventory and authorized local resources. Record model identity only when exposed. Use distinct ports, database/project names and native identity, preserve unrelated services and never search global profiles/history for credentials or sessions.
2. Prepare the case's raw artifacts and expected baseline outside the actor workspace. For a regression, establish that the original behavior fails the meaningful assertion. Supply only prompt, raw context, real capabilities, action scope and actual accepted decisions; keep criteria, negative controls, prior diagnoses and answer keys with the evaluator.
3. Resolve genuine user decisions through an actual reply. For unattended exercises, a needs-decisions result can satisfy the decision-policy criterion while dependent implementation remains blocked. A proposal, evaluator preference or old plan is not user acceptance. Record factual handoffs and any intervention.
4. Inspect actual diffs/commits, commands/results, rendered interactions and persisted outcomes. Grade each criterion as pass, fail, partial, blocked or not-run, with artifact references and mocked boundaries. A known defect remains a failure even if another platform is unavailable. Missing read traces make routing unknown, not necessarily incorrect; explicit reads alone do not establish correct use.
5. Keep correctness, authentication/ownership, component behavior, visual review, usability observations, foundations, protocol conformance and native/live execution separate. Never average away a critical failure. Record actual target identity; browser viewports, filtered Jest cases and cargo check cannot establish native device/app operation.
6. Bound execution time and cleanup to owned resources. Provider 503/errors and runner SUCCESS-with-unfinished-output require artifact inspection; preserve partial/uncommitted work and report the execution boundary. A coordinator intervention or repair continuation is a separate result, not a blind generation pass.

### Checks motivated by observed failures

| Previous observation | Scenario evidence required now |
| --- | --- |
| Generic desktop UI and skipped UX work | Product-content rationale, representative actual screen, relevant states, rendered review/repair and preserved accepted visual character. No universal palette or subjective numeric grade. |
| Handwritten modal escaped focus despite passing tests | Actual compatible primitive, keyboard/Tab/Shift+Tab/Escape/trigger checks, meaningful failing-then-passing regression and affected caller verification. |
| Fresh app had no frontend tests or complete delivery foundations | Committed affected component checks plus actual journey; clean onboarding, configuration/code checks, service builds/startup and CI/artifact/recovery definitions. Setup-only phases are not required to implement features. |
| Unsigned/default fixture identity exposed private notes | Real authentication, missing/invalid credential cases, fixtures off by default, explicit local/test opt-in, production rejection and direct cross-user read/update/delete denial with unchanged data. |
| Own-format tests passed invalid A2UI and private AG-UI events | Selected published contract/SDK validation and independent renderer/action evidence; custom event semantics use the appropriate standard extension mechanism. |
| Provider ERROR with HTTP 200/exit zero produced a proposal | Semantic-error fixture yields controlled failure and no successful answer/proposal; transport status cannot override it. |
| Canvas stored JSON but no visible cards or reload restoration | Actual client render, reload state, accept/reject/undo and stale/concurrent human-edit checks. |
| CLI session continuation overclaimed ACP attachment | Bounded public-interface evidence for the named session; distinguish continuation, protocol support, actual access and fixtures. |
| Proposed library terms/business pivots treated as accepted | General consequential-decision and continuation cases; facts versus choices, real answers and dependent-work boundaries. Canvas dependency is a candidate until verified and accepted. |
| SUCCESS/503 completion prose overstated readiness | Per-boundary artifacts, actual contribution state, unexecuted checks and intervention/provider status. |

### Run order and controls

Start with definition/package checks, then direct and automatic routing/authority probes, then focused regression repairs and clean-foundation checks. Use the small documentation and small-UI cases as controls against unnecessary setup, full audits, research or external tooling. Compare craft/copy review with acceptable intentional design variants as well as known defects; count useful findings and false positives with inspected scope, not report length.

Run ui-review-to-authorized-repair to exercise assessment, actual acceptance and implementation continuity; research-plan-to-evidence-synthesis uses explicitly synthetic session records and establishes analysis behavior only. Research preparation, agent exploration and automated accessibility checks do not establish participant outcomes.

Next run fresh-desktop-from-product-idea from an empty repository without old code, prior diagnoses or specialist names, and desktop-known-defect-repair against the preserved defective baseline. Original setup-first new-application/native trials remain useful phase-entry controls; they are not blind full-lifecycle discovery trials. Evaluate iOS and Android separately, retaining overlapping fixture tests as fixture evidence only.

Keep Figma declaration/discovery/OAuth/read/write, protocol/renderer, named-session and voice/provider checks independently gated. Missing Figma tools allow useful supplied/local review but do not satisfy a live read/write claim. Never connect an account, upload private product artifacts or publish Storybook merely to pass a test without that action being authorized.

Most definitions remain unexecuted; the focused observations below identify the cases actually run. The architecture follow-up contains 64 local plus 39 pinned upstream skills; the focused runs below used the earlier 55-local inventory. Historical 87- and 90-skill results retain their original revisions and scope.

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

## Local runner example: agy

I chose `agy` for my local tests. The [installation guide](../installation.md#load-them-in-your-client) owns installation instructions; this example adds no dependency to the trial specification or plugins.

```bash
agy plugin validate "$AGENT_PLUGINS_DIR/development-workflow"
agy plugin list --json
agy -p '<phase prompt>' --output-format stream-json --print-timeout 20m
```

Run from the target repository, capture stdout/stderr outside it, and use the installed client's conversation option for continuation. The 20-minute limit is a local choice. Check tool events and soft denials even on exit zero. Use scoped permissions and the client's sign-in flow; never put sign-in codes in prompts/traces. The recorded discovery run used workflow 0.17.0; fresh sign-in and Docker availability blocked application/Compose execution independently.

## Historical evidence

These observations preserve executed results, failures and earlier proposals. Use the recorded source/client boundary for each claim. Expand the history to investigate a regression or the reason behind an evaluation case.

<details>
<summary>Recorded trials, corrections and follow-up proposals</summary>

## Focused UI/UX observations

At merged source `58ad31c`, I ran five fresh agy 1.3.5 probes with 92 installed skills: interface-quality-direct-read-only, ux-writing-review-and-scope, usability-research-plan-only, figma-capability-boundaries and small-ui-change-proportionality. Grading found one pass (the isolated typo correction) and four partial results. The actor received tasks, contracts and capabilities; diagnoses and criteria stayed with the evaluator.

The review found real browser defects but proposed an unverified contrast replacement (2.35:1 while claiming at least 3:1). Copy blurred queued and started states and omitted irreversible-deletion explanation. Research planning coached an invalid attempt and claimed a discovery percentage without evidence. The Figma fallback respected remote boundaries but chose a session scratch path outside the allowed script destination. No explicit design entry-point read was visible; this is a routing evidence gap, not proof of unavailable design guidance.

The contrast applicability guidance follows [W3C’s explanation of non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), including when a visible boundary is necessary to identify a control.

The focused guidance changes address these decision points, and the corresponding criteria now check default wording, complete confirmations, neutral recovery tasks, numeric recommendations and chosen output paths. The live Figma case separately checks client-specific authentication, persisted create/read/update and cleanup. Repository checks validate the definitions; they do not execute these cases.

I also completed an authenticated Figma round trip through the Codex Figma integration: created a disposable file, recorded its empty page, created a named frame with two text nodes, read design context, updated its text, inspected the updated render, removed only the recorded test nodes and confirmed their absence in a separate read. The blank disposable file remains. This verifies that connection's native writes and context reads, not agy authentication, design-system fidelity, real product design or implementation. No sharing, publication or paid upgrade occurred. Account identifiers and private file links are excluded from this repository.

The first adjusted snapshot produced three passes and two partials across the same five independent probes. After tightening research and inspection guidance and adding the calculator, fresh research and local Figma-fallback probes passed; scripts used the permitted evidence path. The interface probe used the calculator for existing colors but still invented a replacement ratio: `#8c9689` on `#f8f6ef` is 2.84:1, not the claimed 3.05:1. It also overclaimed an AAA focus result. Numeric recommendation verification remains incomplete, despite passing helper tests. The unchanged copy and small-edit controls passed on the earlier adjusted snapshot; this is not an all-case pass on one revision.

For direct agy Figma access, I added the official HTTP endpoint with the supported native CLI command after the local probes. The capability actor then inspected client logs outside its permitted workspace, so I stopped it. Authentication, live file access and the explicit design route remain unverified in agy. No credentials were copied between clients. This is an actor scope failure, not evidence that Figma OAuth is unsupported or that another account setup step will solve it. At that stage the PR remained draft while recommendation accuracy and bounded discovery needed further work. Raw client logs and account data are excluded from repository evidence.

A final fresh interface probe after adding a pre-return claim check passed the targeted review criteria. It measured every proposed color against the actual backgrounds: the intermediate border `#889088` is 3.04:1 on paper and 3.29:1 on white. It excluded optional labelled-button outlines from failures, verified that the clipped URL remains fully selectable and kept focus contrast separate from AAA focus appearance. Source hashes stayed unchanged. Selection retrieval is demonstrated; OS clipboard behavior and physical screen-reader output remain outside independently verified evidence. This closes the local recommendation blocker in one run, not a repeatability claim. The new bounded-discovery guidance has not been rerun against agy; live authorization/file access and design activation remain open client gates.

At the user's request, I continued the Figma-dependent trials with fresh Codex session subagents using the connected Figma integration and guidance from `6dae643`. The authenticated read/write/cleanup case passed: a subagent inspected the empty disposable page, created a frame and child, read design context, updated the child, inspected the changed render and removed both nodes. My separate read confirmed their absence. This tests the session connector; agy authentication and bounded discovery remain unverified. Preservation of populated or concurrently edited content was not exercised.

A second subagent explicitly loaded Design and relevant frontend, interaction, copy and interface-quality guidance. Given a raw Fieldnote brief, it created eight editable desktop/narrow saved, editing, failed-save, queued-export and deletion views, semantic variables, text styles and reusable buttons, then delivered a React/Tauri handoff. The reading-oriented visual proposal preserved the accepted compact density and six-point rhythm. The agent found and repaired layout/button sizing issues. Five post-repair screenshots were inspected; Figma's reported Starter MCP limit blocked three others. Final structure reported no horizontal overflow, but desktop failed-save, narrow saved and desktop deletion remain visually unverified after repair. The handoff separates queue acceptance from completion, specifies draft retention and named irreversible deletion, and leaves runtime behavior and unresolved contracts for implementation.

A third subagent reviewed the raw brief and eight rendered artifacts without reading the designer's rationale or handoff. Its sole connector read returned screenshot URL metadata; visual conclusions used saved native PNGs. It found no confirmed defect in the five final captures. A cramped desktop delete label and inconsistent failed-state header in earlier captures remain provisional until final renders can be checked. Component structure and actual Figma token bindings were not independently reviewed. The review issued no Figma mutations; my cleanup removed only recorded test roots, styles and collection, and a separate read confirmed the original empty page with no local text styles or variable collections. Native writes and cleanup remained available despite the earlier screenshot-limit errors.

The design and review trials are partial adaptations at the design stage, not passes for the full design-to-implementation-handoff case. No application repository, existing Storybook, implementation, native runtime or persistence journey was supplied or tested. I kept private file links, account identifiers and raw tool records outside the public repository. No account changes, publication or paid upgrade occurred.

## Scope of the focused corrections

I removed the bundled contrast helper and its dedicated tests in favor of tool-independent measurement and recommendation verification. Figma remains an optional design surface with local HTML/CSS or SVG alternatives. Client-specific observations above are historical evidence, not prerequisites for UI work. Concrete regression scenarios remain in the evaluation definitions.

The final simplification received repository checks only. At my request, no fresh behavioral evaluations were run before merging; the recorded passes remain tied to their original revisions and the design-stage gaps remain unverified.

## Guidance refactor validation

The collection-wide guidance refactor is based on the focused findings above and an instruction-structure review across the local inventory, with upstream scope/adaptation screening. Earlier behavioral passes apply to their recorded revisions. Consolidating or relocating a rule does not inherit those passes automatically.

Keep the existing 38 cases, 12 trials and nine-flow definitions intact, including scope, contrast applicability/recommendation checks, neutral research, truthful copy, license decisions, native/Storybook boundaries and real protocol interoperability. Package checks establish structure and resource preservation only. Behavioral reruns were explicitly deferred at my request; earlier passes do not establish the final refactored behavior.

Initial snapshot validation passed plugin metadata/containment, 287 maintained links, eight additional relative links in changed/new references, all 28 repository unit tests, the complete seven-plugin build with 92-skill resource parity, and five explorer smoke checks. All 55 local names, invocation controls and metadata remain intact; upstream pins/adaptations and existing evaluation definitions are unchanged. The original visual guides and resources were retained, with links rebased. The final writing pass clarifies that their visual profiles are adaptable defaults. Independent Standards and Spec reviews found no actionable issue; those reviews do not establish runtime or model behavior.

Use unfamiliar products as well as the saved-search/Fieldnote regressions when testing generalization: a localized appointment cancellation flow with an asynchronous refund, a dense laboratory sample editor with ambiguous acknowledgement, a kiosk with a constrained native runtime, or an operations recovery plan where a restore succeeds but dependent work remains paused. Give actors raw constraints without previous diagnoses. Judge decision quality, scope, evidence and preserved outcomes rather than particular words, file names or a smaller token count. These are proposed transfer trials, not executed results or new prerequisites for application work.

## Recorded evidence and limits

| Check | Recorded result | Boundary |
| --- | --- | --- |
| Collection packaging | Seven bundles: 50 local + 37 upstream skills. Metadata, 18 repository tests, all-plugin builds and complete inventory/resource checks pass. | Package checks establish packaging, not application behavior. |
| Copilot CLI 1.0.95 | Earlier session-local discovery of 85 skills and the default 56-skill set. | Revised 87-skill collection has not been rerun in Copilot. Menu filtering/compliance remains unproven. |
| agy 1.3.5 | Revised seven bundles installed locally with 87 skills; initial default-bundle resource parity checked. | Installation does not establish use or compliance; model selection was not exposed by these trial records. |
| Original generation trials | Small README change and focused SQLModel change completed; SQLModel full suite passed 270 tests. Saved-search application demonstrated PostgreSQL persistence and cross-user denial. | Saved-search setup omitted delivery foundations and frontend regression coverage; independent keyboard checks found dialog focus defects. |
| Revised foundations | Explicit setup created an objective worktree, component READMEs, Dockerfiles, CI and release/deployment procedures. Independent API tests (10), frontend tests (2), build and lint pass. | Root README and final commit are missing; runner ended with an unfinished progress narrative despite SUCCESS. Remote CI, image publication, deployment and recovery were not executed. |
| Tauri desktop | Packaged macOS app launched; independent create, PostgreSQL persistence, app restart, identity separation and failed-save/retry worked. API tests (19), frontend tests (20), web build/lint and API Docker image build pass. | Edited a branch in the base checkout instead of a worktree; fixture identities default enabled and native auth uses web session storage. Other desktop targets, signing and production readiness unverified. |
| Expo iOS/Android | Python tests (14), JavaScript iOS-filtered tests (16), Android-filtered tests (17), typecheck and lint pass. | Filtered Jest suites are not native-device runs; shared cases overlap. Full Xcode and Android SDK/emulators are absent. Both native runtime outcomes remain blocked. |
| AG-UI/A2UI | Python tests (17) and frontend tests (14) pass. Independent published A2UI 0.9.1 schema check rejects the private payload. | Production web build fails: missing index.html; lint fails: ESLint absent. Own-format tests and installed SDK names do not establish A2UI interoperability or an end-to-end app. |
| Canvas strategy/design | Initial strategy and design exercised; fresh strategy rerun improved decision status to proposed. | Unsupported competitor/economic claims remained; first pass misstated tldraw licensing and ACP attachment guarantees. Revisions address guidance; successful correction is not yet established. |
| Canvas diagnosed implementation | Local commit bd01ab7; independent 14 backend tests passed with one live test skipped; production frontend build and lint (with warnings) passed. Dedicated agy conversation continuity demonstrated; semantic provider-error guard repaired. | Browser showed unlabeled sample shapes, no visible proposed annotation/session card and an empty canvas after saved-state reload. Private events still fail AG-UI schema; live ACP/voice and complete foundations remain unverified/incomplete. No frontend regression suite. This was a diagnosed repair with coordinator intervention, not a blind rerun. |
| VS Code and deployment | Loading instructions follow official documentation. | Revised client behavior, remote CI/publication, deployment, restore and live voice/model quality remain unverified. |

These are revision-specific local observations, not a controlled estimate of skill effectiveness. Initial revised trials used revision 27bc2cc; strategy rerun used the f9e1612 business bundle; canvas implementation uses a8695b8. Later guidance changes require their own reruns. Some agy runs returned backend 503 errors alongside completion prose; preserve both execution status and actual artifact evidence. No broad claims of native parity, live AI quality or production readiness follow from the passing checks.

## Foundation, native-client and AI trials

The expanded generation set adds project-foundations, tauri-desktop-application, expo-ios-android-application, agui-a2ui-application and ai-canvas-product-to-implementation. The mobile trial shares TypeScript/Expo and a Python backend but grades iOS and Android separately. The revised canvas trial carries the accepted engineer audience and existing-session goal through strategy, system design and implementation; the previously suggested canvas SDK remains a candidate until its terms/capabilities are verified and accepted. Consequential unresolved choices block dependent work.

New application foundations are evaluated as actual artifacts and runnable commands: human READMEs, configuration checks, behavior tests, containerizable app Dockerfiles/Compose, GitHub Actions and release/deployment/recovery process. Registry defaults configure GHCR and PyPI for distributable Python packages without authorizing publication. Native runtime/signing, live model/voice and real harness attachment are recorded separately from source, browser and fixture checks.

The initial local application trial demonstrated API tests and persistence/ownership, but omitted CI/containers/root onboarding, wrote directly on main, seeded test identities without an environment guard and used dialogs without focus containment/restoration. These observations motivate the revised guidance and grader criteria; keep the diagnosis out of independent actor inputs. The initial READMEs and backend tests existed, but scaffold text and API-only evidence did not establish complete setup or UI verification. Updated trial results must be recorded from execution rather than inferred from the revised instructions.

The first engineer-canvas strategy trial also presented unaccepted pivots as decisions, overstated competitor/pricing certainty and incorrectly treated the tldraw SDK as MIT-licensed. Strategy evidence and template guidance now require current sources, explicit unknowns and proposed versus user-accepted decision status. Preserve that failed output before a fresh-context rerun; changed instructions alone do not establish a successful correction.

Independent validation of the first AG-UI/A2UI setup found that its private surface tree failed the published A2UI 0.9.1 envelope schema while its own format tests passed. Protocol guidance now requires published-schema and independent renderer/conformance evidence. Native runtime and live provider checks remain separate capabilities.

## Visual-quality follow-up

The desktop trace recorded native-client guidance reads but no observed frontend-conventions or interaction-design reads. Its manifest had no shadcn/Tailwind dependencies. Functional/native checks therefore did not establish compliance with the product/visual/UX process. The local frontend fallback also prescribed generic neutral/blue styling. Revised routing retains frontend/interaction guidance for Tauri; visual direction now derives from the brief and requires representative rendered review/repair. A new behavioral case and UI-trial criteria distinguish visual quality, usability/accessibility and functional regression evidence. These changes are not yet validated by a fresh generation; screenshot evidence from the earlier app is not a passing visual baseline.

## Lifecycle and licensing follow-up

Most creation probes entered with prescribed features/stacks through setup and develop; they were not blind tests of business-to-product discovery. Canvas strategy/design ran but did not resolve SDK licensing or actual existing-session feasibility before implementation. Revised develop guidance owns explicit new-application outcomes, setup clarifies its narrower scope, system-design requires consequential dependency decisions and a behavioral case checks commercial SDK constraints. Repair and fresh desktop trials are distinct: repair receives the known defects; fresh generation receives the product brief and constraints without old implementation or grader diagnoses. New guidance alone does not establish compliance.

Consequential-finding decisions are now owned by shared workflow guidance across all phases; system-design and operations supply evidence rather than defining separate approval policies. A cross-lifecycle case checks security/privacy and reliability choices plus an independent routine fix as a control against unnecessary questioning. These policy changes occur after the desktop trials were dispatched; their recorded source revision remains 99ea936.

The subsequent 99ea936 desktop variants remain partial. Fresh generation read the new flow/frontend guidance and used a real worktree, but lacked frontend tests and complete foundations; five backend tests, build and cargo check did not establish native/UI completion. Coordinator browser operation confirmed reload persistence and exposed unauthenticated default-identity reads. Repair increased frontend coverage to 25 tests alongside 19 backend tests and repaired a PostgreSQL/API migration failure, but coordinator keyboard testing still escaped the delete dialog; no native launch/design review was established and the runner ended with a 503 error before a final commit. Both runner status and independent artifacts are retained.

A later synthetic read-only plan probe loaded the 5468cb2 shared WORKFLOW policy and returned unresolved data/cost/recovery questions while treating a known reversible parser defect as routine work. Its recommendations were not technically validated and no real stakeholder answer/integration occurred. This is narrow decision-classification evidence, not universal detection/compliance or successful new-application generation.

## Design handoff follow-up

Figma is a preferred optional tool for substantial UI exploration and handoff; existing designs and local prototypes remain usable. Visual-direction guidance now connects product scenarios, representative designs, semantic tokens, target components and rendered reconciliation. Storybook covers actual component states and can link to design references; application/native journeys remain separate. The design-to-implementation-handoff case checks this boundary with read-only Figma access and no publication permission. This new behavioral case has not been executed; package checks do not establish compliance.

## Next validation sequence

This sequence records the earlier follow-up proposal. Execution remains deferred under the current architecture boundary above. The Figma status in this section describes that earlier change; later connection evidence is recorded in the focused UI/UX observations.

Keep the failed application outputs and actor traces as baselines. Resolve one behavior class at a time through focused PRs and fresh contexts; compare actual outcomes, not skill-read counts or runner completion prose.

1. Run the existing lifecycle and design-handoff cases in bounded first-slice projects. Check that accepted product scenarios, constraints, design decisions and verification expectations exist before dependent implementation. Reuse existing answers; missing outcomes should prompt the missing work rather than more mandatory documents.
2. Use desktop repair to reproduce and correct dialog focus, failed-save draft retention and fixture/authentication boundaries. Commit regressions that fail on the original defect and pass after repair. Run affected component checks plus real private-data and persistence journeys.
3. Validate generated foundations from a clean checkout: onboarding commands, configuration linting, containerized services, CI checks, artifact construction and release/recovery instructions. Do not publish artifacts merely to verify workflow syntax.
4. Compare the existing reviewer with the selected licensed craft/microcopy candidates on the same representative surfaces and known defects. Measure useful findings, false positives, token preservation, contextual visual fit and read-only scope. Research-guide quality is judged on neutral tasks and coverage; actual user research remains separate.
5. Rerun fresh desktop generation after the targeted fixes, without old code or grader diagnoses. Grade design, component tests, backend/authentication, real journey, foundations and native execution separately. Resolve harness 503 failures independently and preserve incomplete output.
6. Continue protocol/schema/independent-renderer and real-session capability probes before canvas implementation; run iOS/Android native checks only with the required SDKs/device environment. Keep unavailable boundaries explicit.

The Figma MCP declaration and Storybook guidance have package-level checks only. A later agy 1.3.5 validation recognizes the portable MCP declaration (one server); the earlier skipped-declaration observation is superseded. Declaration recognition still does not establish authenticated server discovery. No Figma OAuth/tool round-trip, new Community-skill behavioral trial or fresh application generation is claimed for this change.

## Documentation integration after lifecycle changes

PR #8 was rebased after #11–#15. Its documentation methods retain current lifecycle, contribution, UI/UX and evaluation guidance, use discipline names and preserve the split maintainer references. Its earlier application worked case reported author/source checks, typed examples and 14 parsed/rendered Mermaid diagrams; this rebase does not rerun that application case or establish independent reader comprehension.

Two new unexecuted cases assess evidence-backed writing and current/target architecture views. They require preserving authoritative contracts, distinguishing transport success from committed outcomes, and keeping configuration/proposals separate from deployed verification. Package, definition and link checks establish integration integrity only.

</details>
