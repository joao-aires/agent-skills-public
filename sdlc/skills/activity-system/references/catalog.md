# Activity catalog: choose the work and its stopping point

An activity is a requested engagement. Use this catalog to choose the activity whose **default result and stopping point** match the request. The linked skill is the activity method; supporting methods deepen the work but do not change the stopping point.

## Core activities

| Activity | Use when | Default result | Stopping point | Artifacts | Supporting methods |
| --- | --- | --- | --- | --- | --- |
| [setup](../../setup/SKILL.md) | New project foundations or existing-project adoption | Working context, commands, foundations and artifact home map | Before feature implementation | README, project instructions, artifact home map, ECR workspace pointer | [project-conventions](../../project-conventions/SKILL.md), [artifact-system](../../artifact-system/SKILL.md), delivery expertise |
| [plan](../../plan/SKILL.md) | Outcome, first slice, feasibility or sequencing is open | Scoped decision to proceed, investigate or defer | Planning decision and in-scope handoff | ECR overview/problem, PRD or roadmap link, issue when coordination warrants | Product discovery, feasibility, [guide-system-documentation](../../guide-system-documentation/SKILL.md) |
| [refine](../../refine/SKILL.md) | Rough idea, brief or optional ticket needs definition | Actionable requirements and observable acceptance, or decision blockers | Requirements ready for design or implementation | ECR requirements, acceptance, open decisions | [requirements-engineering](../../requirements-engineering/SKILL.md), [write-spec](../../write-spec/SKILL.md), product/security/operations expertise |
| [design](../../design/SKILL.md) | Consequential UX, contract, AI or architecture choices need options and a decision | Options, linked artifacts and an accepted, limited or blocked design decision before code | Design accepted, limited or blocked; no implementation | Design proposal (ECR §4, RFC or linked record), target views, ADR when independent | [design-system](../../design-system/SKILL.md), [option set](../../design/references/option-set.md), [design validation](../../design/references/design-validation.md), interface/backend/AI/security expertise |
| [develop](../../develop/SKILL.md) | Rough idea to implementation in one engagement | Useful verified slice, with questions and assumptions | Requested development outcome | ECR across performed phases, work products, verification, issue/PR views | Refine, design, implementation preparation, verification, review composition |
| [implement](../../implement/SKILL.md) | Defined work is ready; explicit implementation requested | Implemented and verified change through the contribution flow | Completed local change and checks | Work products, tests, ECR implementation/verification, PR when authorized | [git-contributions](../../git-contributions/SKILL.md), [test](../../test/SKILL.md), technical/design expertise |
| [test](../../test/SKILL.md) | Evidence for a change or journey is needed; verification and completion evidence | Checks, observations, results and gaps | Claimed behavior verified or precise blocker | ECR verification, test evidence, coverage gaps | installed testing-journey expertise, [testing-resilience](../../testing-resilience/SKILL.md), [property-based testing](../../test/references/property-based.md), stack test guidance |
| [release](../../release/SKILL.md) | Readiness or a named authorized delivery action | Prepared assessment or verified execution | Named release/deployment boundary | Release note, ECR verification, runbook/SLO updates, deployment evidence | `ci-cd-pipelines`, [test](../../test/SKILL.md), operations expertise |
| [run-production-readiness-review](../../run-production-readiness-review/SKILL.md) | A service, launch or material change needs a scoped readiness verdict | Evidence-backed readiness verdict or gaps | Ready, ready with limits, or not yet ready | Assurance assessment, ECR/readiness evidence | [release](../../release/SKILL.md) for authorization, [test](../../test/SKILL.md), operations and design-system expertise |
| [fix](../../fix/SKILL.md) | A defect needs repair | Diagnosed, verified repair and handoff | Repaired behavior and evidence; no unrelated cleanup | Work products, regression tests, ECR/issue/PR evidence | [diagnosing-bugs](../../diagnosing-bugs/SKILL.md), [tdd](../../tdd/SKILL.md), design expertise |
| [improve](../../improve/SKILL.md) | Opportunity discovery or a specific improvement | Prioritized findings or focused implementation for an explicit objective | Findings or requested improvement | Findings, ECR/work item, work products and checks when implemented | [architecture scan](../../improve/references/architecture-scan.md), [codebase-design](../../codebase-design/SKILL.md), [domain-modeling](../../domain-modeling/SKILL.md) |
| [harden](../../harden/SKILL.md) | Scoped security/privacy improvement | Evidenced fixes and residual risks | Scoped hardening and evidence | ECR/security record, work products, verification | [design-security](../../design-security/SKILL.md), threat review |
| [run-product-feedback-analysis](../../run-product-feedback-analysis/SKILL.md) | Shipped product behavior or user evidence needs interpretation | Evidence-backed feedback analysis and decision implications | Findings, limits and open questions | [product-feedback-analysis](../../artifact-system/references/contracts/product-feedback-analysis.md) | [plan](../../plan/SKILL.md), product-management, [research](../../research/SKILL.md) |
| [run-dependency-maintenance](../../run-dependency-maintenance/SKILL.md) | Dependency or runtime updates and update PRs need review | Per-item compatibility evidence and disposition | Update accepted or precise blocker | Dependency record, work products, checks, PR | Delivery, stack expertise; security findings route to their owners |

## Review a change

Review is a composition, not a separate activity. Use the owner for each concern:

| Concern | Owner |
| --- | --- |
| Code-diff standards and spec | [code-review](../../code-review/SKILL.md) |
| Verification evidence and gaps | [test](../../test/SKILL.md) |
| Cross-artifact consistency and convergence | [artifact assurance](../../artifact-system/references/assurance.md) |
| Artifact-specific review questions | The matching `guide-*` |
| Shared artifact properties | [quality bar](../../artifact-system/references/quality-bar.md) |
| In-review stopping point | `develop` or `implement` |

Stop at findings. Posting comments, editing source, merging and deploying require their own authority. Do not create a separate review skill for this composition.

## Design modes

Design is one activity with several modes. They are not separate activities or phases.

| Mode | Use when | Output |
| --- | --- | --- |
| Frame | The decision, constraints, components or types are unclear | Bounded question, affected types, current state or greenfield |
| Explore options | A consequential choice has more than one plausible direction | Three or more materially different options with lenses |
| Represent | The options cannot be judged from text alone | Type-appropriate wireframes, mockups, contracts, sequences, state machines or evaluation plans |
| Decide | A direction is supportable or must be blocked | Design proposal, recommendation, owner, status and revisit trigger |
| Validate | Material uncertainty remains about behavior, feasibility or quality | Validated, limited or blocked evidence |
| Review / hand off | Implementation or another reviewer will depend on the design | Findings, accepted design, seam, open decisions and authority |

Use the modes proportionately. A small local change may need only a short decision and review. Read [engagement state](engagement-state.md) when design threads run in parallel with requirements or implementation.

## Artifact guides

Artifact guides are support methods, not activities. Each artifact type has a contract and, where the craft is distinct, a guide. The one-to-one pairing and the full list are in the [guide registry](../../artifact-system/references/guide-registry.md).

A guide can be used inside an activity or requested directly. It owns how to write the artifact well; the contract owns the artifact's lifecycle, authority, maturity, evidence and handoff.

## Operate and learn

| Activity | Use when | Default result | Stopping point | Artifacts | Supporting methods |
| --- | --- | --- | --- | --- | --- |
| [run-incident-response](../../run-incident-response/SKILL.md) | Live service impact, degradation or suspected incident | Stabilized service with evidence and handover | Recovered or precise blocker | Incident record, ECR/repair link, follow-ups | [design-system](../../design-system/SKILL.md), [run-security-maintenance](../../run-security-maintenance/SKILL.md), [guide-runbook](../../guide-runbook/SKILL.md), [fix](../../fix/SKILL.md) |
| [run-security-maintenance](../../run-security-maintenance/SKILL.md) | Credential lifecycle or vulnerability remediation | Verified rotation/revocation or patched targets | Every affected consumer/target verified or dispositioned | Operational system of record, ECR summary | [design-security](../../design-security/SKILL.md), [run-incident-response](../../run-incident-response/SKILL.md) |
| [run-operations-review](../../run-operations-review/SKILL.md) | Recurring operational review | Prioritized findings and bounded actions | Review closed with owners | Operations review, ECR/issue links | [analyze-capacity-cost](../../analyze-capacity-cost/SKILL.md), recovery evidence, security maintenance, [guide-runbook](../../guide-runbook/SKILL.md) |
| [run-postmortem](../../run-postmortem/SKILL.md) | Incident learning and action follow-up | Reviewed postmortem with verified actions | Actions verified or explicitly dispositioned | [Postmortem contract](../../artifact-system/references/contracts/postmortem.md), action tracker | [run-incident-response](../../run-incident-response/SKILL.md), [improve](../../improve/SKILL.md) |

## Assure

Security and governance are **methods**, not phases. They attach to the activity that owns the decision and evidence.

| Method | Use when | Output |
| --- | --- | --- |
| [design-security](../../design-security/SKILL.md) | Trust boundaries, data flow, privacy, authority placement, authentication, authorization, sessions, federation or machine identity | Security/privacy decisions in ADR/ECR, verification evidence and residual risk |
| [run-compliance-assessment](../../run-compliance-assessment/SKILL.md) | GDPR, CCPA/CPRA, SOC 2 or another scoped compliance assessment | [Assurance assessment](../../artifact-system/references/contracts/assurance-assessment.md) |
| [harden](../../harden/SKILL.md) | Scoped security/privacy weakness or remediation | Evidenced fixes and residual risks |

## Explicit workflows

These are named workflows, not default activities. They require an explicit request or a deliberate selection by the user. Upstream names, bodies and native controls are preserved where applicable.

| Workflow | Origin | Use when | Output |
| --- | --- | --- | --- |
| [grill-me](../../grill-me/SKILL.md) | Upstream | The user wants a plan or design stress-tested by interview | Sharpened plan or design |
| [grill-with-docs](../../grill-with-docs/SKILL.md) | Upstream | The same interview should also produce durable decision/glossary notes | Sharpened plan plus docs |
| [grilling](../../grilling/SKILL.md) | Upstream | A reusable interview technique is needed | Questions that expose assumptions |
| [to-questionnaire](../../to-questionnaire/SKILL.md) | Upstream | A decision needs input from someone else | Questionnaire |
| [write-spec](../../write-spec/SKILL.md) | Local | An existing conversation or decision should become a spec | ECR spec section |
| [retro](../../retro/SKILL.md) | Local | A coding session needs retrospective learning | Retrospective findings |

## Reading the catalog

- The **activity skill** owns the method and its detailed stopping point.
- The **supporting methods** deepen a concern; they do not silently start another activity.
- The **artifacts** column uses the [artifact catalog](../../artifact-system/references/catalog.md) types. Resolve their homes with [artifact homes](../../artifact-system/references/homes.md).
- If the request spans several activities, `develop` can carry them in one engagement when implementation is authorized. Otherwise, stop at the requested activity and hand off.
- Several activities may run as parallel threads, especially requirements and design or frontend and backend design. Use [engagement state](engagement-state.md); report the current focus and do not pretend an inactive thread is finished.
- If the request is for help, explain the matching activity and its result; do not start it.
