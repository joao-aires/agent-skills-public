# Requirements dimensions

Use this reference when a change needs more than the obvious functional path: to find the areas it lands in, choose the dimensions that materially constrain them, and state design requirements for surfaces a person or another system observes. It does not define the artifact; the [ECR contract](../../artifact-system/references/contracts/ecr.md#3-requirements-and-acceptance) owns the template.

## Start with affected areas

An **area** is where the change becomes observable: a journey step, a contract, stored data, a scheduled process, an operator task. Derive areas from the target's actual responsibility and software type, not from a fixed frontend/backend split. A change can have several areas of one kind and none of another.

| Target | Areas it commonly has | Question that finds them |
| --- | --- | --- |
| Web or mobile application | journey, screen state, client persistence, sync, platform permission, accessibility | What does the person see and do, and what survives reload, offline or a permission prompt? |
| HTTP API or service | endpoint contract, authorization policy, stored records, downstream call, queue/worker, rate limit | Who may call it, what must be true after success, and what does a caller see on denial or timeout? |
| Background job or data pipeline | trigger, input contract, idempotency, backlog, data quality, retry/dead-letter, operator signal | How is a run identified, what happens on duplicate or partial input, and who notices a stalled run? |
| CLI, library or SDK | command/API surface, configuration, exit codes and errors, package compatibility, docs example | What can a clean consumer install and invoke, and what breaks an existing caller? |
| AI feature | context and input, output contract, evaluation set, tool authority, refusal/failure, cost and latency | What quality is promised, on which evaluation set, and what may the model do without a person? |
| Platform or infrastructure | resource boundary, deployment unit, identity/permission, observability, backup/recovery | What is the blast radius, who can change it, and how is recovery proved? |

Name the areas in the ECR, then state which dimensions apply to each. Do not import areas from a different product shape to look thorough.

## Dimension prompts

For each dimension ask: does the accepted outcome depend on this? If yes, state the condition and how it will be observed. If no, omit it, or record `Not applicable — reason` when a reader would expect it.

| Dimension | Ask | Target or tolerance shape | Evidence |
| --- | --- | --- | --- |
| Functional | Which actor, trigger, precondition, result, stored effect and denial path? | Behavior a person or consumer can observe | Scenario, contract test, journey run |
| Reliability | What happens on partial failure, retry, duplicate, timeout, restart or dependency outage? | Recovery expectation, duplication tolerance, data-loss bound | Fault injection, integration test, replay |
| Performance | Which operation, at what load and dataset, measured where? | Latency percentile, throughput, batch window, with population and observation point | Benchmark, load test, production monitor |
| Security/privacy | Who may act on whose data; what is minimized, logged, retained or exposed? | Authorization rule, retention period, exposure limit | Denied/allowed checks, data inspection, review |
| Maintainability/operability | Can an operator detect, diagnose and recover this without the author? | Signal, runbook step, supported configuration | Exercised runbook, logs/metrics/trace, startup check |
| Cost | Which resource grows with usage, and what bound is acceptable? | Unit cost, quota, budget ceiling at stated volume | Usage estimate, billing data, load run |
| Compatibility | Which existing consumer, version or data shape must keep working? | Supported versions, migration window, deprecation rule | Consumer test, compatibility matrix, migration rehearsal |
| Accessibility | Which users and input modes must complete the task? | Named standard or project criterion, keyboard/screen-reader path | Manual and automated checks, rendered review |
| Compliance | Which policy, contract or regulation constrains the data or behavior? | Obligation with source, scope and owner | Policy reference, audit evidence, decision record |

The dimension list is a prompt, not a required set. A capability can legitimately have none of a dimension: a pure formatting change has no new performance requirement. What it cannot have is a dimension named with no decision, no target and no reason for omission.

## Design requirement prompts

Design requirements describe obligations of a surface, not the mechanism that implements them. Use them for user-facing surfaces and for contracts another person or system consumes.

- **Task**: what must the person understand, decide and do at this point? Which action is primary?
- **States**: what do empty, loading, partial, stale, denied, failed and complete look like, and what can the person do in each?
- **Content**: which labels, units, dates, errors and confirmations must say what? Which must never be shown?
- **Contract**: what shape, field meaning, error taxonomy and compatibility promise does a consumer rely on?
- **Access**: keyboard, focus, screen reader, contrast, text scaling and input method where the platform applies.
- **Platform**: responsive behavior, offline, notification, permission and native lifecycle behavior.
- **Trust**: what explains an automated or consequential action, and how is it undone or corrected?

A design requirement links to the design specification, prototype, view or contract artifact that resolves it. The ECR does not carry the specification itself. "The row states which records were excluded and why" is design; "the query filters by tenant_id" is implementation. Keep the implementation statement in solution design.

## Worked example: scheduled report

Affected areas: report builder (web), schedule API, delivery worker, email surface.

| ID | Area | Requirement | Priority | Status |
| --- | --- | --- | --- | --- |
| FR-reports-001 | schedule API | An authorized workspace member can schedule a report for a named recipient list and cadence; a member without report access is denied without disclosing schedule contents | Must | Accepted |
| FR-reports-002 | delivery worker | A schedule fires once per cadence window; a worker restart does not send a second copy for the same window | Must | Proposed |

| ID | Dimension | Area | Target or tolerance | Conditions | Priority | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NFR-reliability-001 | reliability | delivery worker | Transient mail-provider failure is retried with at-least-once delivery and a dedupe key | Provider 5xx for up to 3 attempts | Must | Integration test with provider sandbox | Accepted |
| NFR-security-001 | security/privacy | email surface | Recipients see only records permitted at send time; removed access cancels the pending send | Permission change before send | Must | Allowed/denied scenario | Accepted |
| NFR-performance-001 | performance | delivery worker | Batch completes within the agreed window for 10k schedules; target unresolved | Weekday morning peak | Must | DEC-001, benchmark pending | Open |

| ID | Surface | Type | Requirement | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
| DR-email-001 | report email | Functional | The email states the report name, data window, cadence, recipient scope and how to stop future sends | design spec §4.2 | Accepted |

| ID | Requirement IDs | Check | Environment / revision | Result | Evidence |
| --- | --- | --- | --- | --- | --- |
| AC-001 | FR-reports-001 | Non-member requests a schedule; response is denied and shows no schedule fields | staging, `api@<sha>` | Passed | `pytest tests/schedules` |
| AC-002 | NFR-security-001 | Remove recipient access after queueing; send does not include protected records | staging, `worker@<sha>` | Failed | run `r-142`, blocked on DEC-003 |

| ID | Statement | Owner | Needed by | Status |
| --- | --- | --- | --- | --- |
| DEC-001 | Acceptable weekday batch completion window | operations owner | design handoff | Open |
| ASM-001 | Mail provider retries are safe to dedupe by schedule window | delivery owner | implementation | Accepted risk |

The example is deliberately incomplete: `NFR-performance-001` has no number, `AC-002` failed, and `DEC-001` is still open. Those states are more useful than invented targets or a green row.

## Anti-patterns

- **Area taxonomy copied from a stack.** Listing "frontend" and "backend" when the change is a data pipeline hides the worker, schedule and operator areas that actually fail.
- **Dimension checklist.** Nine dimensions each marked "considered" with no target, decision or omission reason. A checklist is not analysis.
- **Design specification in the requirement table.** Pasting screen layouts or API schemas turns the ECR into a duplicate authority; state the obligation and link the artifact.
- **Invented numbers.** A latency or availability target with no owner, population or observation point becomes a commitment nobody agreed to.
- **Requirement as implementation.** "Use a queue and a cron trigger" names a solution; the requirement is the delivery promise it must satisfy.
- **Acceptance detached from IDs.** Checks that prove something ran, without saying which commitment they establish.
- **Unstable IDs.** Renumbering requirements to match implementation order breaks test, review and release references.
- **Empty tables.** Headers with no rows, or every row `TBD`, claim coverage that does not exist; use the compact form instead.
- **Design requirements without an owner.** A surface obligation with no linked design artifact and no decision is an unresolved requirement, not an accepted one.
