# Editorial review of authored skills

This review covers all 83 collection-authored skill entrypoints against the purpose-specific [authoring guidance](../../../plugins/documentation/skills/documentation-writing/references/structured-instructions.md). It revisits the wording after the initial authoring/workflow changes recorded in this directory. Managed upstream snapshots are outside the editing scope.

## What was examined

For each skill, the reviewer considered whether a reader can identify the task, follow a working method, understand a consequential choice, find conditional detail and distinguish evidence from a plan. The review compared proposed edits with their previous wording to retain applicability conditions, exceptions, authority limits, accepted-stack choices and invocation controls.

Connected prose remains where it explains a cause, mechanism or tradeoff. Lists expose parallel checks or questions; sequences express actual method dependencies; tables compare alternatives or evidence on common dimensions. No paragraph-length, table-count or common-section target was applied. Existing examples remain when they clarify a real distinction; no application scenario was inserted merely to make a skill longer.

The follow-up revises **40 entrypoints** and retains **43** after review. “Retained” describes the decision in this editorial follow-up, not whether an earlier commit in the PR touched the file. The record explains those decisions individually below. An editorial judgment is not participant comprehension research or evidence of collection-wide agent adherence.

## Per-skill decisions

| Skill | Follow-up disposition | Reason |
| --- | --- | --- |
| [ai-development](../../../plugins/ai-development/skills/ai-development/SKILL.md) | Revised | Expose orchestration alternatives and provider criteria; separate output shape, domain validity, authority and usefulness. |
| [ai-operations](../../../plugins/ai-development/skills/ai-operations/SKILL.md) | Revised | Separate configuration/correlation identity from sampling and visibility limits. |
| [ai-testing](../../../plugins/ai-development/skills/ai-testing/SKILL.md) | Revised | Compare scoring approaches by applicability; separate comparison populations from confounding variables. |
| [ai-conventions](../../../plugins/ai-python-development/skills/ai-conventions/SKILL.md) | Revised | Expose adapter result states separately from framework selection. |
| [ai-deepeval-testing](../../../plugins/ai-python-development/skills/ai-deepeval-testing/SKILL.md) | Revised | Make available/retrieved context and expected/actual tool distinctions individually inspectable. |
| [python-ai-observability](../../../plugins/ai-python-development/skills/python-ai-observability/SKILL.md) | Revised | Separate asynchronous span lifetime from correlation across remote boundaries. |
| [backend-design](../../../plugins/backend-development/skills/backend-design/SKILL.md) | Retained | Retain causal explanations of caller promises, concurrency, uncertain remote effects and contract compatibility. |
| [backend-conventions](../../../plugins/backend-python-development/skills/backend-conventions/SKILL.md) | Revised | Separate AI selection from enforcement checks and consumer-contract evidence from tool choice. |
| [python-automation-engineering](../../../plugins/backend-python-development/skills/python-automation-engineering/SKILL.md) | Revised | Separate collection completeness from mutation resumption while retaining their different success meanings. |
| [browser-extension-delivery](../../../plugins/browser-extension-development/skills/browser-extension-delivery/SKILL.md) | Retained | Retain artifact inspection, disclosure comparison and ordered external-promotion stages with separate authority. |
| [browser-extension-development](../../../plugins/browser-extension-development/skills/browser-extension-development/SKILL.md) | Revised | Expose worker registration, durable acknowledgement, recovery and scheduled-work behavior under their actual conditions. |
| [browser-extension-security](../../../plugins/browser-extension-development/skills/browser-extension-security/SKILL.md) | Revised | Group privileged-handler checks together without weakening sender, target or endpoint authority. |
| [browser-extension-testing](../../../plugins/browser-extension-development/skills/browser-extension-testing/SKILL.md) | Retained | Retain evidence-level comparison and consequential transition checks; driver limitations remain explicit. |
| [browser-extension-ui](../../../plugins/browser-extension-development/skills/browser-extension-ui/SKILL.md) | Revised | Separate component compatibility, appearance/density and context-sensitive lifecycle checks; retain task-to-surface method. |
| [database-design](../../../plugins/database-development/skills/database-design/SKILL.md) | Retained | Retain the explanations connecting domain invariants, concurrent operations and compatible data evolution. |
| [database-performance](../../../plugins/database-development/skills/database-performance/SKILL.md) | Retained | Retain workload diagnosis and before/after reasoning, including waiting versus SQL execution and write costs. |
| [postgresql-development](../../../plugins/database-postgresql-development/skills/postgresql-development/SKILL.md) | Retained | Retain role/policy comparison, complete-transaction retry reasoning and migration conditions. |
| [postgresql-operations](../../../plugins/database-postgresql-development/skills/postgresql-operations/SKILL.md) | Retained | Retain recovery-unit reasoning, evidence levels and conditional upgrade procedure. |
| [postgresql-performance](../../../plugins/database-postgresql-development/skills/postgresql-performance/SKILL.md) | Retained | Retain plan-reading explanation, diagnostic execution limits and workload-dependent tuning costs. |
| [delivery-pipelines](../../../plugins/delivery/skills/delivery-pipelines/SKILL.md) | Revised | Expose verification, release and deployment inputs/results without changing promotion or recovery authority. |
| [deliver-reliable-changes](../../../plugins/development/skills/deliver-reliable-changes/SKILL.md) | Revised | Separate actor/revision provenance from the limits of review evidence in the completion handoff. |
| [dependencies](../../../plugins/development/skills/dependencies/SKILL.md) | Retained | Retain update investigation steps and distinct disposition rules; head changes still require revalidation. |
| [design](../../../plugins/development/skills/design/SKILL.md) | Revised | Expose reuse, changed responsibilities and integration points in the implementation handoff. |
| [develop](../../../plugins/development/skills/develop/SKILL.md) | Revised | Separate the existing-feature trace from how its evidence informs the slice; preserve new-application scope. |
| [git-contributions](../../../plugins/development/skills/git-contributions/SKILL.md) | Revised | Separate description maintenance from published-revision verification and worktree retention. |
| [harden](../../../plugins/development/skills/harden/SKILL.md) | Revised | Keep positive/denial verification together and separate specialist routing from the verification method. |
| [improve](../../../plugins/development/skills/improve/SKILL.md) | Revised | Expose proposal evidence, bounded change, measurement, protected behavior and cost comparison. |
| [journey-testing](../../../plugins/development/skills/journey-testing/SKILL.md) | Retained | Retain platform/evidence distinctions, observable journey method and component-versus-runtime limits. |
| [plan](../../../plugins/development/skills/plan/SKILL.md) | Revised | Expose component, reuse and integration-check planning alongside the explanation of useful increments. |
| [project-conventions](../../../plugins/development/skills/project-conventions/SKILL.md) | Retained | Retain foundation comparison and focused quality-check method; conditional instruction maintenance remains linked. |
| [refine](../../../plugins/development/skills/refine/SKILL.md) | Revised | Expose consequential-failure questions before explaining functional and quality consequences. |
| [release](../../../plugins/development/skills/release/SKILL.md) | Retained | Retain release-boundary discovery and delivery-owner handoff without introducing another release procedure. |
| [resilience-testing](../../../plugins/development/skills/resilience-testing/SKILL.md) | Retained | Retain hypothesis, scope, fault-removal and recovery sequence; live impact limits remain beside execution. |
| [review](../../../plugins/development/skills/review/SKILL.md) | Revised | Separate defect evidence from edit/publication scope and revision-validity checks. |
| [setup](../../../plugins/development/skills/setup/SKILL.md) | Retained | Retain new/existing foundation comparison and clean local command path with explicit unexercised targets. |
| [system-design](../../../plugins/development/skills/system-design/SKILL.md) | Revised | Expose quality questions and changing-state reasoning under distinct topics; preserve architecture alternatives. |
| [system-mapping](../../../plugins/development/skills/system-mapping/SKILL.md) | Revised | Expose the compact feature trace contents while retaining code-evidence and proposed/current distinctions. |
| [test](../../../plugins/development/skills/test/SKILL.md) | Retained | Retain behavior-first coverage selection and claim-to-boundary comparison; distinguish fixtures from real integration. |
| [workflow-help](../../../plugins/development/skills/workflow-help/SKILL.md) | Retained | Retain the activity-selection procedure, client-aware examples and read-only help boundary. |
| [bash-engineering](../../../plugins/development-tooling/skills/bash-engineering/SKILL.md) | Retained | Retain explanations of argument preservation, explicit failure handling and cleanup ownership. |
| [performance-testing](../../../plugins/development-tooling/skills/performance-testing/SKILL.md) | Revised | Compare smoke, regression/load and stress/spike/soak profiles by their actual evidentiary purpose. |
| [tooling-conventions](../../../plugins/development-tooling/skills/tooling-conventions/SKILL.md) | Retained | Retain conditional reference selector and actual-integration checks without choosing an application stack. |
| [architecture-documentation](../../../plugins/documentation/skills/architecture-documentation/SKILL.md) | Retained | Retain structural/runtime/interface distinctions, source tracing and question-based verification. |
| [documentation-conventions](../../../plugins/documentation/skills/documentation-conventions/SKILL.md) | Retained | Retain work-tracking versus operating-knowledge ownership and affected-record synchronization. |
| [documentation-writing](../../../plugins/documentation/skills/documentation-writing/SKILL.md) | Retained | Retain reader-purpose comparison, explanation method and local structure choices; no further template is needed. |
| [interaction-design](../../../plugins/frontend-development/skills/interaction-design/SKILL.md) | Revised | Expose placement/container choices and coverage dispositions while retaining state ownership reasoning. |
| [interface-quality](../../../plugins/frontend-development/skills/interface-quality/SKILL.md) | Revised | Separate cross-view transition/composition inspection from accessibility and quantitative evidence. |
| [usability-research](../../../plugins/frontend-development/skills/usability-research/SKILL.md) | Revised | Expose moderator completion/assistance decisions and keep their effect on interpretation explicit. |
| [ux-writing](../../../plugins/frontend-development/skills/ux-writing/SKILL.md) | Revised | Expose confirmation object, effect and consequences without dropping localization or task meaning. |
| [visual-design](../../../plugins/frontend-development/skills/visual-design/SKILL.md) | Revised | Compare component-system responsibilities and separate semantic roles from appearance mapping. |
| [native-client-development](../../../plugins/frontend-native-development/skills/native-client-development/SKILL.md) | Revised | Separate reproducible client foundations from release/signing prerequisites and authority. |
| [frontend-conventions](../../../plugins/frontend-reactjs-development/skills/frontend-conventions/SKILL.md) | Revised | Separate foundations, variation ownership and conditional version migration guidance. |
| [go-conventions](../../../plugins/go-development/skills/go-conventions/SKILL.md) | Retained | Retain practical cancellation/channel ownership explanations and targeted verification references. |
| [compliance-design](../../../plugins/governance/skills/compliance-design/SKILL.md) | Retained | Retain applicability-to-control reasoning, responsibility boundaries and distinct evidence levels. |
| [gdpr-readiness](../../../plugins/governance/skills/gdpr-readiness/SKILL.md) | Revised | Expose lifecycle implementation questions while keeping accepted legal interpretation distinct from mechanisms. |
| [soc2-readiness](../../../plugins/governance/skills/soc2-readiness/SKILL.md) | Revised | Expose automated-job and performed-review evidence questions within the actual examination scope. |
| [credential-lifecycle](../../../plugins/operations/skills/credential-lifecycle/SKILL.md) | Retained | Retain planned rotation versus exposure response and consumer-verification sequence. |
| [incident-response](../../../plugins/operations/skills/incident-response/SKILL.md) | Retained | Retain bounded response loop, competing hypotheses and evidence discipline. |
| [observability-operations](../../../plugins/operations/skills/observability-operations/SKILL.md) | Revised | Separate local service setup, diagnostic access, evaluation evidence and pipeline ownership. |
| [operational-housekeeping](../../../plugins/operations/skills/operational-housekeeping/SKILL.md) | Retained | Retain domain selector and candidate-versus-authorized-cleanup reasoning; no universal cadence is introduced. |
| [optimize-application-cost](../../../plugins/operations/skills/optimize-application-cost/SKILL.md) | Retained | Retain bill attribution, useful-work denominator and constraint-based savings verification. |
| [plan-application-capacity](../../../plugins/operations/skills/plan-application-capacity/SKILL.md) | Retained | Retain demand-to-concurrency explanation, admission bounds and conditional platform references. |
| [postmortem-facilitation](../../../plugins/operations/skills/postmortem-facilitation/SKILL.md) | Retained | Retain reconstruction method and distinction between triggers, contributing conditions and hindsight. |
| [postmortem-followup](../../../plugins/operations/skills/postmortem-followup/SKILL.md) | Retained | Retain verification of deployed control effect and recurrence investigation before closure. |
| [protect-and-restore-data](../../../plugins/operations/skills/protect-and-restore-data/SKILL.md) | Retained | Retain recovery-objective reasoning, isolated restore procedure and partial-failure handling. |
| [reliability-design](../../../plugins/operations/skills/reliability-design/SKILL.md) | Retained | Retain journey-to-indicator derivation, denominator explanation and conditional arithmetic reference. |
| [runbook-engineering](../../../plugins/operations/skills/runbook-engineering/SKILL.md) | Retained | Retain ordered author/validate procedure with expected observations and recovery limits. |
| [vulnerability-management](../../../plugins/operations/skills/vulnerability-management/SKILL.md) | Retained | Retain triage, compensating controls, delivered-fix verification and no-fix handling. |
| [infra-jvm-optimization](../../../plugins/operations-platforms/skills/infra-jvm-optimization/SKILL.md) | Retained | Retain hypothesis-driven measurement, JVM/hosting interaction and conditional promotion checks. |
| [kubernetes-resource-engineering](../../../plugins/operations-platforms/skills/kubernetes-resource-engineering/SKILL.md) | Retained | Retain resource-contract versus rendering/delivery structure and admission/scaling evidence. |
| [saas-dashboard-design](../../../plugins/saas-development/skills/saas-dashboard-design/SKILL.md) | Revised | Separate audience and context from accepted design scope and conditional reference use. |
| [saas-design](../../../plugins/saas-development/skills/saas-design/SKILL.md) | Revised | Separate tenancy definitions, explanatory relationship examples and proportionate scope/reference guidance. |
| [saas-readiness](../../../plugins/saas-development/skills/saas-readiness/SKILL.md) | Retained | Retain promise-to-evidence method, gap classification and cohort-specific verdicts. |
| [security-and-privacy-design](../../../plugins/security/skills/security-and-privacy-design/SKILL.md) | Revised | Give credential/recipient reasoning its own topic and separate specialist selection from evidence limits. |
| [security-auth-development](../../../plugins/security/skills/security-auth-development/SKILL.md) | Retained | Retain composable identity/policy alternatives, lifecycle reasoning and resource-level enforcement. |
| [business-opportunity-analysis](../../../plugins/strategy/skills/business-opportunity-analysis/SKILL.md) | Retained | Retain explicit legacy routing and standalone fallback; compatibility behavior remains intact. |
| [business-strategy](../../../plugins/strategy/skills/business-strategy/SKILL.md) | Retained | Retain the established mode selector, substantive strategy methods and triggered specialist references. |
| [learn-from-product-feedback](../../../plugins/strategy/skills/learn-from-product-feedback/SKILL.md) | Revised | Explain observation-to-finding synthesis, contradictions, distinct people and decision-linked recommendations. |
| [product-management](../../../plugins/strategy/skills/product-management/SKILL.md) | Revised | Expose priority/adoption dimensions, evidence choices, sequencing and product-to-engineering handoffs. |
| [typescript-conventions](../../../plugins/typescript-development/skills/typescript-conventions/SKILL.md) | Retained | Retain runtime-validation explanation, host/compiler distinctions and distributed-artifact verification. |
| [architecture-diagramming](../../../plugins/visualization/skills/architecture-diagramming/SKILL.md) | Revised | Compare structural, sequence and lifecycle meanings before layout; retain artifact verification. |
| [presentation-building](../../../plugins/visualization/skills/presentation-building/SKILL.md) | Retained | Retain message-to-visual reasoning and actual-slide inspection without a fixed slide structure. |
| [system-flow-explorer](../../../plugins/visualization/skills/system-flow-explorer/SKILL.md) | Retained | Retain executable validation/render steps and stable-identity modeling rules with conditional depth. |

## Validation boundary

Metadata, links, snapshot integrity and complete-bundle checks cover structure and preservation. Independent product and AI probes exercise selected revised methods using synthetic, isolated inputs; their [exact sources, criteria and limits](editorial-probes/assessment.md) are recorded separately. They do not establish that every skill is equally comprehensible or that application workflows succeed in an installed client.
