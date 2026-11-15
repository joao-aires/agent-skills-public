# Transitions: how activities hand off

The lifecycle is a graph of outcomes, not a compulsory pipeline. A request can start at any activity and stop at its result. When several activities are carried forward, each hands off accepted decisions, artifacts and evidence to the next; the next activity checks what it received before depending on it.

A phase can also reopen an earlier decision when new evidence invalidates its premise. Update the owning artifact and recheck dependents; do not keep implementing on a contradicted design.

## Outcome graph

| From | To | Entry evidence | Output / artifact |
| --- | --- | --- | --- |
| Setup / foundations | Planning | Working context, commands, artifact home map and accepted constraints are discoverable | README, project instructions, artifact home map, ECR workspace pointer |
| Planning | Requirements or investigation | Outcome, scope, feasibility and next decision are clear or linked | ECR problem/scope, PRD or roadmap link, investigation issue |
| Requirements | Design | Actors, permissions, behavior, quality constraints and observable acceptance are sufficient | ECR requirements and acceptance, or a decision blocker |
| Requirements | Design (parallel) | A material design question can be explored while requirements settle; the open requirement is named | Parallel threads, provisional design options, open decision |
| Design | Design validation | The chosen direction still carries material uncertainty about behavior, feasibility or quality | Validation evidence, revised option or explicit limit |
| Design validation | Design | Evidence supports, limits or contradicts the direction | Updated proposal, accepted or reopened decision |
| Design | Implementation preparation | Proposed target, affected software types, seam, alternatives and consequential decisions are understood or blocked | ECR solution design or design proposal, target views, RFC/ADR when independent |
| Implementation preparation | Implementation | Dependency-ordered increments, verification, migration and rollback are covered | ECR implementation strategy, implementation-preparation reference |
| Implementation | Verification and change review | Actual change revision, protected behavior, deviations and planned checks are known | Work products, tests, ECR implementation/verification |
| Implementation | Design (reopen) | Implementation reveals a missing state, an invalid contract or a contradicted premise | Reopened design thread, updated seam, dependent work paused |
| Verification and change review | Design (reopen) | Observed behavior contradicts the accepted design or an assumption | Updated design proposal, ECR, recheck of dependents |
| Verification and change review | Release | Actual checked behavior, findings, coverage gaps and current-head evidence are available | ECR verification/change review, PR, release readiness |
| Release | Operate | Actual artifact, target, gates, rollout/recovery and observed state are separated | Release note, deployment record, runbook/SLO updates |
| Operate | Incident or improvement | A signal, user impact or review finding warrants action | Incident record, operations review, change proposal |
| Incident | Recovery and postmortem | Impact is stabilized and evidence is preserved | Recovery evidence, incident record, postmortem draft |
| Postmortem | Planning or design | Learning actions change a requirement, design, control or runbook | Postmortem, action register, ECR/decision update |
| Operate / postmortem | Design (reopen) | A signal, incident or review changes an assumption or reveals a gap | Incident/postmortem, ECR update, new decision |

Cross-cutting activities (`fix`, `improve`, `harden`, `dependencies`) can start at any point and do not require a full lifecycle. Security, privacy and governance are **methods** that attach to the activity that owns the decision and evidence; they do not form a separate phase.

## Parallel threads

Work may have more than one active thread. A thread is one activity with its own stopping point, evidence and, when it changes the evidence, a software type.

```markdown
Threads:
- Requirements and acceptance — backend — accepted
- Backend saved-searches contract — backend — current focus
- Saved-searches panel — frontend — waiting on the contract
- Seam: error and pagination — shared — open
```

Rules:

- one focus, many threads;
- switching focus is explicit;
- each thread keeps its own stopping point and artifact;
- a type is recorded only when it changes the evidence;
- a decision in one thread that changes another reopens the affected thread explicitly.

Read [software types](../../artifact-system/references/software-types.md) for the type evidence and [engagement state](engagement-state.md) for the state block.

## Re-entry and reopens

Returning to an earlier activity is a **reopen**, not a reset:

1. Name the decision or premise that changed and the evidence that changed it.
2. Reopen the owning thread and update its artifact; do not rewrite history silently.
3. Identify dependent decisions, artifacts and implementation slices.
4. Update or mark them superseded, and recheck the seam.
5. State what implementation must pause or be revised.
6. Record the new decision owner and the next evidence needed.

Keep accepted decisions that the new evidence does not touch. A reopen does not require a full lifecycle restart.

## Side topics

When an interruption appears, classify it:

| Kind | Response |
| --- | --- |
| In-scope aside | Answer briefly and return to the current focus |
| Blocking decision | Pause only dependent work; record the owner |
| New activity | State the activity, its stopping point and whether it replaces or follows the current work |
| Out of scope | Record it as parked or deferred; do not expand scope silently |

Do not let an aside silently change the phase. If it changes a design premise, say so and reopen design explicitly.

## Stopping points

- **Plan** stops at the decision to proceed, investigate or defer.
- **Refine** stops when requirements and acceptance are ready for design, or at the precise open decision.
- **Design** stops when the target is accepted, limited or blocked; it does not implement.
- **Design validation** stops at validated, limited or blocked; it does not become implementation verification.
- **Implementation preparation** stops at the breakdown when that is the request.
- **Implement**, **fix** and **harden** include the authorized code, checks and commits within their flow; they do not silently merge, deploy or publish.
- **Test** stops at the verification result and evidence gaps.
- **Change review** stops at findings; source edits, posting and merge require their own authority.
- **Release** stops at readiness or the named authorized delivery action.
- **Develop** can carry multiple activities in one engagement when implementation is authorized; it still reports the actual outcome and unfinished parts.

## Handoff evidence

At each handoff, the next activity should be able to identify:

- the accepted outcome and scope;
- the current artifact and its authority;
- the revision or target actually checked;
- the evidence and its limits;
- the decisions still open and their owners;
- the next activity and stopping point.

Use the [artifact system](../../artifact-system/SKILL.md) for the artifact contract and [artifact assurance](../../artifact-system/references/assurance.md) for consistency and convergence. Use [implementation preparation](implementation-preparation.md) when implementation needs a dependency-ordered breakdown.

## Proportionality

A small fix can move directly from reproduction to repair and verification. A new product needs enough outcome, feasibility, requirements and design evidence before irreversible commitments. Do not invoke every activity for every change; invoke the ones whose outcome the work actually needs.

When a request changes from one stopping point to another, say so and apply the new activity. For example, a design discussion that becomes "build it" is an implementation request; a bug report that becomes "why is this happening?" is an investigation. Do not silently cross the boundary.
