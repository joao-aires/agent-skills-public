# Engineering Change Record: required content contract

An ECR is the **durable, reader-oriented specification of one coherent engineering change**, not a commit log, a ticket dump, or the current application architecture. An engineering workspace owns its location; the application's repository owns actual implementation and canonical current-state documentation. A project ECR may cover several work packages, each with its own links and review status.

Apply the [artifact quality bar](../quality-bar.md) and the shared [presentation guidance](../../SKILL.md#present-outcomes). The ECR's format is Markdown-like prose with stable headings; **no YAML/JSON manifest or prescribed file tree is required**.

## Reader questions

A change participant or reviewer must be able to answer:

1. What is changing, for whom, and why?
2. What is in scope and out of scope?
3. What must be true for the change to be accepted?
4. What was proposed, and which alternatives were rejected?
5. What has actually been built or checked, at which revision?
6. What has been released, and what remains pending?
7. Which decisions were made, and what remains open?

## Modes

Use a **full record** when the change introduces or changes behavior across components, a boundary, a migration, security or compatibility, a consequential design choice, or coordination with another person or change.

Use a **compact record** only when all are true: local and reversible; one component; one evident approach; no boundary, migration, security or compatibility change; no new consequential decision; and no cross-change coordination.

```markdown
# <Change>

## Overview
What changes, for whom, why and the current status.

## Change and acceptance
The implemented behavior, preserved behavior and observable acceptance.

## Verification
What ran, at which revision, with what result and what remains unverified.

## Decisions and open items
Any decision made, its owner and what remains open.
```

A compact record is still an ECR. If the change reveals a decision or a boundary, promote it to the full record and reopen the affected sections.

## When not to create an ECR

- A typo, comment, formatting or dependency bump with no decision or behavior change: use the commit or PR note.
- An unrelated defect found mid-change: create a separate issue or ECR; do not bundle it.
- An agent repairing its own implementation or testing mistake inside the current change: record it in the current ECR implementation/verification sections as a deviation or repair, not a new ECR.
- A behavior change that needs durable evidence: use a compact ECR, or the issue/PR plus the actual test evidence.

## Contract

A full ECR has these seven headings in this order. Use truthful `Pending`, `Not applicable — reason`, or `Blocked — decision/evidence needed` for content not yet established. This makes the format predictable without presenting future work as finished.

### 1. Overview and lifecycle

- Short title and a discoverable change link or workspace-relative reference.
- Current outcome, scope, key evidence and the next action, including its owner when known.
- ECR status versus claim status: proposed, accepted, implemented, verified, released and superseded are **separate statements**; report which claim has which evidence.
- Links to the parent PRD/project, relevant roadmap, implementation issues and PRs where they exist. Do not create them just to fill a field.

### 2. Problem and scope

- Current observed problem, actor or customer impact, intended outcome, inclusions and exclusions, important existing behavior, feasibility evidence and assumptions.
- Distinguish supplied evidence from hypotheses and approved product direction. Link to the PRD for product-wide value or priority; do not copy the entire PRD.
- Capture delivery prerequisites when they affect the decision to proceed.

### 3. Requirements and acceptance

- Actors and permitted actions, functional behavior, relevant quality/security/operating constraints, denied/partial/failure paths and compatibility.
- Named, observable acceptance cases. For each, state the action, the condition, the result a reader can observe, and its status. Include the denial or failure path where it affects the promised behavior.
- Open decisions that prevent readiness, with their owner. Label material requirements accepted, proposed or unknown.
- A user journey or wireflow when interaction work benefits from it; no invented design mechanism or arbitrary SLO.

Name the affected areas and the target. An area is where the change lands — a journey, service API, stored data set, integration, background job, CLI surface or model behavior — derived from the target's software type, not a fixed frontend/backend split. List only the applicable dimensions, and where a reader would otherwise wonder, mark an excluded one `Not applicable — reason` instead of adding an empty row. Design requirements cover user-facing or contract surfaces and stay separate from the software implementation requirements they constrain.

Full form:

```markdown
Affected areas: <area>, <area>. Target/PRD: <link or Not applicable — reason>.

| ID | Area | Requirement | Priority | Status |
| --- | --- | --- | --- | --- |
| FR-<area>-001 | <area> | <actor, trigger, observable result, denial path> | Must / Should / Could | Accepted / Proposed / Open |

| ID | Dimension | Area | Target or tolerance | Conditions | Priority | Evidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NFR-<dimension>-001 | <dimension> | <area> | <target or unresolved decision> | <population, workload, failure> | Must / Should | <benchmark, monitor, probe or Pending> | Accepted / Proposed / Open |

| ID | Surface | Type | Requirement | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
| DR-<surface>-001 | <surface> | Functional / Non-functional | <interaction, state, content or contract obligation> | <linked design spec, view, prototype or Pending> | Accepted / Proposed / Open |

| ID | Requirement IDs | Check | Environment / revision | Result | Evidence |
| --- | --- | --- | --- | --- | --- |
| AC-001 | FR-<area>-001, NFR-<dimension>-001 | <action and observation> | <environment, target, revision> | Passed / Failed / Not run / Blocked | <path, URL or command> |

| ID | Statement | Owner | Needed by | Status |
| --- | --- | --- | --- | --- |
| DEC-001 / ASM-001 | <decision or assumption> | <owner> | <date or phase> | Open / Resolved / Accepted risk |
```

Compact form for a small local change:

```markdown
Requirements: R1 <observable behavior>; R2 <failure or denial path>.
Constraints: <only the applicable dimension with its target or tolerance and observation>.
Design: <the user-facing or contract obligation, only when one exists>.
Acceptance: R1 <check at environment/revision → result, evidence>; R2 <...>.
Open: DEC-001 <decision>, owner <owner>.
```

Keep each ID stable once design, tests or release reference it; do not renumber to match implementation order. Acceptance maps to requirement IDs, not the reverse. Use a short `R<n>` list in the compact form only where nothing outside the record depends on the identifier.

### 4. Solution design

- Existing-system baseline at a source revision, linked to the exact file or commit. Then the **proposed** system, UX or service behavior.
- Affected software types per component and which are explicitly **not affected**. When more than one type is involved, record the seam decision once: error/denial mapping, loading/empty distinctions, pagination, authority, retry/idempotency and compatibility. See [software types](../software-types.md).
- For a consequential choice, use the [design proposal](design-proposal.md): at least three materially different options, the linked design artifacts the decision needs, trade-offs and failure behavior, a recommendation and a decision owner. Keep the proposal in this section for a normal change, or link an RFC or design record when the audience or views justify it.
- Selected approach, meaningful alternatives, trade-offs, data and authority boundaries, failure and migration consequences.
- Link or attach target C4 context/container/component views and critical sequence or journey diagrams when applicable. Keep **current versus target** and status explicit. See the [diagram lifecycle](../diagram-lifecycle.md).
- Use the [artifact catalog](../catalog.md) to decide whether a proposal needs its own RFC or an accepted choice needs a canonical ADR. Summarize the relevant rationale and link the fuller record when one exists.
- Record the acceptance or decision owner. A draft proposal cannot silently satisfy an implementation dependency.

### 5. Implementation strategy

- Ordered deliverable increments, affected contracts and components, prerequisites, compatibility and migrations, verification per slice, delivery and rollback, and remaining implementation blockers.
- Link execution issues only if coordination warrants them; no obligatory ticket graph or folder-by-folder plan.
- State what is ready to start, what depends on a decision, and what can proceed independently.

### 6. Verification and release

- What was actually exercised, at which revision or target, in which environment, with the exact command or scenario, the observed result, and the evidence path.
- Failed, skipped, unavailable and blocked checks. Variance from the proposed design. Material review findings. Remaining risk.
- Documentation reconciliation and release or readiness versus actual deployed state.
- Link CI, review and run evidence and the PR. Never turn a green build into proof of user-visible behavior.
- A CI run, test report or PR check may be the evidence authority. Link it; do not create a separate Markdown copy unless the project already uses one.

Write evidence in the past tense. "Will verify", "should pass" and "create/read/update will confirm" are plans. Put a planned check in the implementation strategy or mark it "not yet verified" here until it runs.

### 7. Decision history and references

- Accepted, rejected and superseded choices, owner and rationale; outstanding questions and disposition.
- Links to the canonical PRD, RFC, ADR, diagrams, baseline, issues, PRs and runtime evidence.
- History is a readable set of **consequential changes**, not an automatically appended full activity log.

## Sufficiency floor

A section is complete when a reader who was not in the conversation can answer its questions from this document and the linked authorities.

| Section | The reader must be able to answer |
| --- | --- |
| Overview | What is changing, what state is it in, what is the next action, and who owns it? |
| Problem and scope | What is broken or missing today, for whom, and what is deliberately excluded? |
| Requirements | Which affected areas and requirement IDs apply, what observable outcomes will be accepted including denial and failure, and which are still open? |
| Solution design | What exists today at which revision, what is proposed, what alternatives were rejected and why, and what can fail? |
| Implementation strategy | In what order will this be delivered, what depends on what, and how will each increment be checked? |
| Verification | What command or scenario ran, where, at which revision, what was observed, and what remains unverified? |
| Decisions | What was decided, by whom, why, and what is still open? |

A section that only restates its heading, links elsewhere for its substance, or says "pending" after the activity has been performed is not complete. A compact record can pass; a long record can fail. The test is the answers, not the word count.

## Keep the current state first

Each section leads with the current state. Dated checkpoints, older attempts and superseded evidence belong in a `History` subsection at the end of that section or in section 7. Do not leave an old `Pending` paragraph above a newer `Current result` paragraph; the reader cannot tell which is true.

When a claim is superseded, keep the prior decision traceable but mark it as superseded and link its replacement. Do not rewrite a requirement to match incomplete code.

## Phase completion and consumer checks

| Completed activity | ECR content required before describing it as ready |
| --- | --- |
| Project planning | Desired outcome, scope, feasibility, relevant prerequisites and the next action or decision are clear or linked |
| Refine | Outcome, affected areas, identified requirement IDs across applicable dimensions, observable acceptance and open decision owners are sufficient for design |
| Design | Proposed target, affected software types and the seam are understood; material alternatives and linked design artifacts are resolved or blocked; the baseline revision is linked |
| Implementation preparation | Dependency-ordered increments reference accepted requirements and design; verification, migration and rollback are covered |
| Implement | Actual change revision, deviations, relevant canonical-doc edits and checks are reported |
| Test/review | Observations and findings are tied to the checked revision; untested claims are not promoted |
| Release | Actual artifact and target, gates, recovery, and promotion or verification status are stated precisely |
| Maintenance | Findings, incidents, signals and remediation are linked to affected requirements and decisions as needed |

Entry points may stop earlier; no task automatically authorizes later phases. The ECR is updated incrementally and the reader must be able to tell what is pending. At each completed or attempted handoff, update the readiness disposition and consequential findings in the relevant section without creating a mandatory eighth section. Follow [artifact assurance](../assurance.md) for contradictions, source/test convergence, PR alignment and truthfulness limits.

Read the [ECR guide](../../../guide-ecr/SKILL.md) for writing conventions, examples and review checks.

## Handoff

The phase-readiness table is the ECR's handoff view. A handoff may be assembled from this record and linked artifacts: a design specification or C4 view for design, a PR or test evidence for verification, a runbook for operations. Link the authority; do not copy it into the ECR. See [handoff](../handoff.md) for the phase matrix and the rule that a handoff is content, not a document.

## Multi-work-package ECRs

A project-level ECR may cover several work packages. Keep the shared problem, cross-cutting design decisions, batch verification and decision history in the ECR. Give each work package a row with its own issue, observable acceptance, status and evidence:

| Work package | Issue | Observable acceptance | Status | Evidence |
| --- | --- | --- | --- | --- |
| README entry point | [SKILLS-1](https://example.invalid/SKILLS-1) | A library, CLI and app example each produce a runnable quickstart; one contrasting example is verified | Implemented | `repo@<full-sha>` ([commit](https://example.invalid/commit)) |
| Documentation order | [SKILLS-2](https://example.invalid/SKILLS-2) | Common document types have a reader-oriented sequence and one worked example | Verified | `repo@<full-sha>` ([commit](https://example.invalid/commit)) |

The ECR must not replace each work package's requirements with a link to a one-line issue. The issue owns the work and coordination; the ECR owns the cross-cutting account and the batch-level evidence.

## Compact but complete example (small bug)

The same seven headings can carry a small change without padding. This example is complete enough for a reader to review the change and the evidence.

> **1. Overview and lifecycle.** Rapid language changes can persist an older selection. Implemented and verified locally at `app@<full-sha>` ([commit](https://example.invalid/app/commit)); release pending. Next action: review the local commit. Owner: feature author.
>
> **2. Problem and scope.** At baseline `app@<full-sha>` ([commit](https://example.invalid/base)), the preference writer completes out of order, so a slower earlier write can overwrite a newer selection. In scope: the last valid selection persists across reload. Out of scope: cross-device sync and server-side preferences. Evidence: the failing regression is linked below.
>
> **3. Requirements and acceptance.** R1: select B, wait for the save, reload; B is selected. R2: select B then C quickly, reload; C is selected. R3: a rejected save leaves the previous selection intact. R1–R3 accepted; failed-save user feedback remains open with the product owner.
>
> **4. Solution design.** Baseline: the existing state owner writes asynchronously at `app@<full-sha>` ([file](https://example.invalid/app/blob)). Proposed: a monotonic revision guard that applies only the newest completed write. Alternative: debounce, rejected because it still permits out-of-order completion. No architecture, data-ownership or journey change; no C4, sequence or ADR is required.
>
> **5. Implementation strategy.** Add failing regressions for R2 and R3; implement the revision guard in the existing state owner; run the full suite; reconcile docs (none affected); commit. No migration, compatibility or rollout step.
>
> **6. Verification and release.** Revision: `app@<full-sha>` ([commit](https://example.invalid/app/commit)). Environment: macOS 15, Node 22.16.0. `npm test -- language-preference` → 12 passed, 0 failed. Before the fix: 2 failed (R2, R3). Not exercised: real browser quota failure and production telemetry. Release not performed; PR pending. No production claim.
>
> **7. Decision history and references.** 2026-11-13: selected the revision guard over debounce; owner feature author. Rationale: it preserves the last completed write under out-of-order completion. Open: failed-save feedback; product owner. Baseline: [language-preference.ts](https://example.invalid/app/blob).

## Too thin: not acceptable

This record has all seven headings and is still unusable. It is an index of intentions, not an engineering account.

> **1. Overview.** Fixed the language selector bug.
>
> **2. Problem and scope.** See issue #12.
>
> **3. Requirements and acceptance.** As described in the issue.
>
> **4. Solution design.** Implement the fix.
>
> **5. Implementation strategy.** Add tests.
>
> **6. Verification and release.** Tests pass. Pending.
>
> **7. Decision history and references.** `c4718a6`

Why it fails:

- No baseline, actor impact, scope or excluded behavior.
- No named acceptance case, denial path or open decision.
- No design baseline, alternative, trade-off or failure consequence.
- "Tests pass" has no command, environment, revision or result.
- "Pending" sits where a performed activity belongs, with no distinction from the current state.
- A bare SHA is not a link and does not say whether it is public, private or local-only.

Keep the artifact inspectable and meaningful, not padded. For a major new system the same headings grow, and separate supporting diagrams, PRDs and RFCs are justified.
