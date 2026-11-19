# Handoff: what the next phase actually needs

A **handoff** is the set of accepted outcomes, decisions, evidence and open questions the next phase needs to start safely. It is not a document type and not an approval gate. One phase may satisfy a handoff with several artifacts: an ECR section, a design proposal, a design specification, a C4 view, a contract, a test result or a runbook.

The contract for each artifact says what that artifact must contain. This reference says what the **consumer** needs at the boundary. If an artifact is missing content the next phase depends on, the handoff is incomplete even when every document exists.

## The rule

> Hand off content, not documents. Link the authoritative source; do not copy it into a new handoff file.

A handoff can be assembled from linked artifacts. The reader should be able to see:

- the accepted outcome and scope;
- the current artifact and its authority;
- the revision, target or environment actually checked;
- the evidence and its limits;
- the decisions still open and their owners;
- what may start, what must wait and what is blocked.

## Phase handoff matrix

| From | To | Handoff content | May be assembled from |
| --- | --- | --- | --- |
| Planning | Requirements | Outcome, first useful slice, feasibility, constraints, next decision | PRD/roadmap, ECR overview, research report, product feedback analysis |
| Requirements | Design | Actors and permissions, behavior, observable acceptance, constraints, open decisions | ECR requirements/acceptance, PRD, issue, research report, product feedback analysis |
| Design | Implementation preparation | Decision, affected components and types, alternatives, linked design artifacts, seam, validation, start/blocked | Design proposal, design specification, data model, C4/sequence/state views, RFC/ADR |
| Implementation preparation | Implementation | Ordered increments, dependencies, verification per slice, migration and rollback | ECR implementation strategy, implementation-preparation reference, issue |
| Implementation | Verification and review | Actual revision, changed behavior, protected behavior, planned checks, deviations | Code/tests, ECR implementation/verification, PR |
| Verification and review | Release | Checked behavior, evidence, findings, gaps, risk, readiness | ECR verification, PR, test evidence |
| Release | Operations | Target, rollout, recovery, signals, runbook/SLO updates, observed state | Release note, deployment record, runbook, signal contract |
| Operations | Incident / learning | Impact, response, recovery evidence, open questions | Incident record, operations review, runbook |
| Incident | Postmortem | Timeline, impact, response, recovery, preserved evidence | Incident record, logs/signals, runbook |
| Postmortem | Planning / design | Causal analysis, actions, changed assumptions, owners | Postmortem, action register, ECR/decision |
| Any reopen | Earlier phase | What changed, invalidated premise, dependent work, pause/authority | Design proposal/ECR/decision, verification evidence |

## What each handoff must make visible

### Requirements to design

The designer must know who acts, what they may do, what observable result is promised, which quality constraints matter and which decisions are still open. A list of features is not enough.

### Design to implementation

The implementer must know the accepted decision, the affected components and types, the alternatives that were rejected, the linked design artifacts that define the behavior, the seam between components, what evidence validated the direction and what may start or must wait.

A design specification is the usual carrier for the interface handoff: flows, screens, states, content, components, tokens, responsive behavior, accessibility, motion and assets. C4, sequence and state views carry the system handoff. A design proposal carries the decision and the rejected alternatives.

### Implementation to verification

The verifier must know the actual revision, the behavior that changed, the behavior that must not change, the checks already planned or run and any deviations from the accepted design. A summary of intentions is not evidence.

### Verification to release

The release owner must know what was actually checked, at which revision and target, what failed or was skipped, what risk remains and whether readiness is ready, limited or blocked.

### Release to operations

The operator must know the target, rollout state, recovery path, signals, runbook changes and what was observed after release. A merge or build is not a deployment.

### Operations to learning

The reviewer must know impact, response, recovery evidence and what remains unknown. Do not collapse customer impact into response duration.

## Recording the handoff

- Put the summary in the owning artifact (ECR, design proposal, release note, incident record) and link the source.
- State the revision or target for every claim that depends on one.
- Separate confirmed evidence, plan and unknown.
- Name what may start and what is blocked.
- Keep one authority per concern; do not create a second copy because a handoff is convenient.
- When a handoff changes, reopen the dependent decision rather than silently updating a summary.

## Proportionality

A small fix may hand off in one paragraph with a revision and a test result. A boundary-changing design needs a decision, linked artifacts, a seam and validation evidence. The test is whether the next reader can act, not whether a handoff template was filled.
