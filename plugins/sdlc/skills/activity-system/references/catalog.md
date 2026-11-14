# Activity catalog: choose the work and its stopping point

An activity is a requested engagement. Use this catalog to choose the activity whose **default result and stopping point** match the request. The linked skill is the activity method; supporting methods deepen the work but do not change the stopping point.

## Core activities

| Activity | Use when | Default result | Stopping point | Artifacts | Supporting methods |
| --- | --- | --- | --- | --- | --- |
| [setup](../../setup/SKILL.md) | New project foundations or existing-project adoption | Working context, commands, foundations and artifact home map | Before feature implementation | README, project instructions, artifact home map, ECR workspace pointer | [project-conventions](../../project-conventions/SKILL.md), [artifact-system](../../artifact-system/SKILL.md), delivery expertise |
| [plan](../../plan/SKILL.md) | Outcome, first slice, feasibility or sequencing is open | Scoped decision to proceed, investigate or defer | Planning decision and in-scope handoff | ECR overview/problem, PRD or roadmap link, issue when coordination warrants | Product discovery, feasibility, [system-documentation](../../system-documentation/SKILL.md) |
| [refine](../../refine/SKILL.md) | Rough idea, brief or optional ticket needs definition | Actionable requirements and observable acceptance, or decision blockers | Requirements ready for design or implementation | ECR requirements, acceptance, open decisions | [requirements-engineering](../../requirements-engineering/SKILL.md), product/security/operations expertise |
| [design](../../design/SKILL.md) | UX, contracts or architecture need decisions | Text/visual behavior design before code | Design accepted, limited or blocked | ECR solution design, target views, RFC/ADR when independent | [system-design](../../system-design/SKILL.md), interface/backend/security expertise |
| [develop](../../develop/SKILL.md) | Rough idea to implementation in one engagement | Useful verified slice, with questions and assumptions | Requested development outcome | ECR across performed phases, work products, verification, issue/PR views | Refine, design, implementation preparation, verification, review |
| [implement](../../implement/SKILL.md) | Defined work is ready; explicit implementation requested | Implemented and verified change through the contribution flow | Completed local change and checks | Work products, tests, ECR implementation/verification, PR when authorized | [git-contributions](../../git-contributions/SKILL.md), [test](../../test/SKILL.md), technical/design expertise |
| [implement-spec](../../implement-spec/SKILL.md) | Agreed spec should become dependency-ordered work | Implemented slices on an integration branch | Agreed spec implemented and checked | Work products, tests, ECR/plan, PR when authorized | Parallel worktrees, [git-contributions](../../git-contributions/SKILL.md), [test](../../test/SKILL.md) |
| [test](../../test/SKILL.md) | Evidence for a change or journey is needed; verification and completion evidence | Checks, observations, results and gaps | Claimed behavior verified or precise blocker | ECR verification, test evidence, coverage gaps | [journey-testing](../../journey-testing/SKILL.md), [resilience-testing](../../resilience-testing/SKILL.md), property-based testing, stack test guidance |
| [review](../../review/SKILL.md) | PR, branch or diff needs assessment | Findings against intended behavior, design and standards | Review findings; no default source edits, post or merge | Review evidence, PR comments only when authorized | [code-review](../../code-review/SKILL.md), [differential-review](../../differential-review/SKILL.md), [artifact assurance](../../artifact-system/references/assurance.md) |
| [release](../../release/SKILL.md) | Readiness or a named authorized delivery action | Prepared assessment or verified execution | Named release/deployment boundary | Release note, ECR verification, runbook/SLO updates, deployment evidence | Delivery expertise, [test](../../test/SKILL.md), operations expertise |
| [fix](../../fix/SKILL.md) | A defect needs repair | Diagnosed, verified repair and handoff | Repaired behavior and evidence; no unrelated cleanup | Work products, regression tests, ECR/issue/PR evidence | [diagnosing-bugs](../../diagnosing-bugs/SKILL.md), [tdd](../../tdd/SKILL.md), design expertise |
| [improve](../../improve/SKILL.md) | Opportunity discovery or a specific improvement | Prioritized findings or focused implementation for an explicit objective | Findings or requested improvement | Findings, ECR/work item, work products and checks when implemented | [improve-codebase-architecture](../../improve-codebase-architecture/SKILL.md), [codebase-design](../../codebase-design/SKILL.md), domain modeling |
| [harden](../../harden/SKILL.md) | Scoped security/privacy improvement | Evidenced fixes and residual risks | Scoped hardening and evidence | ECR/security record, work products, verification | Security/privacy design, threat review |
| [dependencies](../../dependencies/SKILL.md) | Updates, findings or dependency PR maintenance | Per-item evidence and changes; merge only under explicit policy | Dependency decision or authorized remediation | Dependency record, work products, checks, PR | Delivery, security and stack expertise |

## Operate and learn

| Activity | Use when | Default result | Stopping point | Artifacts | Supporting methods |
| --- | --- | --- | --- | --- | --- |
| [incident-response](../../incident-response/SKILL.md) | Live service impact, degradation or suspected incident | Stabilized service with evidence and handover | Recovered or precise blocker | Incident record, ECR/repair link, follow-ups | [observability](../../observability/SKILL.md), [security-maintenance](../../security-maintenance/SKILL.md), [fix](../../fix/SKILL.md) |
| [observability](../../observability/SKILL.md) | Instrumentation, telemetry or collection changes | Verified signal contracts and pipeline | Signals implemented and observed | Signal/observability contract, ECR verification | [system-design](../../system-design/SKILL.md), backend/runtime expertise |
| [runbook-authoring](../../runbook-authoring/SKILL.md) | Create, exercise or audit a runbook | Actionable, exercised procedure | Runbook published and linked to its alert | [Runbook contract](../../artifact-system/references/contracts/runbook.md) | Operations and platform expertise |
| [data-recovery](../../data-recovery/SKILL.md) | Backup, restore or disaster-recovery change | Verified recovery path and evidence | Restore verified or precise gap | Runbook, recovery evidence, ECR verification | Database/platform expertise, [incident-response](../../incident-response/SKILL.md) |
| [security-maintenance](../../security-maintenance/SKILL.md) | Credential lifecycle or vulnerability remediation | Verified rotation/revocation or patched targets | Every affected consumer/target verified or dispositioned | Operational system of record, ECR summary | [security-and-privacy-design](../../security-and-privacy-design/SKILL.md), [incident-response](../../incident-response/SKILL.md) |
| [capacity-and-cost](../../capacity-and-cost/SKILL.md) | Capacity, scaling, saturation or spend decision | Bounded capacity/cost decision and verification | Decision accepted or change verified | ECR/decision record, operations review | Platform, database and provider expertise |
| [operations-review](../../operations-review/SKILL.md) | Recurring operational review | Prioritized findings and bounded actions | Review closed with owners | Operations review, ECR/issue links | Capacity/cost, recovery, security maintenance, runbook authoring |
| [postmortem](../../postmortem/SKILL.md) | Incident learning and action follow-up | Reviewed postmortem with verified actions | Actions verified or explicitly dispositioned | [Postmortem contract](../../artifact-system/references/contracts/postmortem.md), action tracker | [incident-response](../../incident-response/SKILL.md), [improve](../../improve/SKILL.md) |

## Assure

Security and governance are **methods**, not phases. They attach to the activity that owns the decision and evidence.

| Method | Use when | Output |
| --- | --- | --- |
| [security-and-privacy-design](../../security-and-privacy-design/SKILL.md) | Identity, data, trust boundaries, external input or security/privacy design | Security/privacy decisions in ADR/ECR, verification evidence and residual risk |
| [security-auth-development](../../security-auth-development/SKILL.md) | Authentication, authorization, sessions, federation, machine identity or tenant access | Auth/identity decision and verification evidence |
| [compliance-readiness](../../compliance-readiness/SKILL.md) | GDPR, SOC 2 or another scoped compliance assessment | [Assurance assessment](../../artifact-system/references/contracts/assurance-assessment.md) |
| [harden](../../harden/SKILL.md) | Scoped security/privacy weakness or remediation | Evidenced fixes and residual risks |

## Explicit upstream workflows

These are named workflows, not default activities. They require an explicit request or a deliberate selection by the user. Their names, bodies and native controls are preserved from upstream.

| Workflow | Use when | Output |
| --- | --- | --- |
| [grill-me](../../grill-me/SKILL.md) | The user wants a plan or design stress-tested by interview | Sharpened plan or design |
| [grill-with-docs](../../grill-with-docs/SKILL.md) | The same interview should also produce durable decision/glossary notes | Sharpened plan plus docs |
| [grilling](../../grilling/SKILL.md) | A reusable interview technique is needed | Questions that expose assumptions |
| [to-spec](../../to-spec/SKILL.md) | A conversation should become a spec | Spec, optionally published when authorized |
| [to-questionnaire](../../to-questionnaire/SKILL.md) | A decision needs input from someone else | Questionnaire |
| [retro](../../retro/SKILL.md) | A coding session needs retrospective learning | Retrospective findings |
| [handoff](../../handoff/SKILL.md) | Another agent must pick up the current conversation | Handoff document |
| [improve-codebase-architecture](../../improve-codebase-architecture/SKILL.md) | An explicit architecture improvement scan is requested | Findings and agreed deepening work |

## Reading the catalog

- The **activity skill** owns the method and its detailed stopping point.
- The **supporting methods** deepen a concern; they do not silently start another activity.
- The **artifacts** column uses the [artifact catalog](../../artifact-system/references/catalog.md) types. Resolve their homes with [artifact homes](../../artifact-system/references/homes.md).
- If the request spans several activities, `develop` can carry them in one engagement when implementation is authorized. Otherwise, stop at the requested activity and hand off.
- If the request is for help, explain the matching activity and its result; do not start it.
