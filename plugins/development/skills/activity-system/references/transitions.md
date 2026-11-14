# Transitions: how activities hand off

The lifecycle is a set of outcomes, not a compulsory pipeline. A request can start at any activity and stop at its result. When several activities are carried forward, each hands off accepted decisions, artifacts and evidence to the next; the next activity checks what it received before depending on it.

## Outcome sequence

| From | To | Entry evidence | Output / artifact |
| --- | --- | --- | --- |
| Planning | Requirements or investigation | Outcome, scope, feasibility and next decision are clear or linked | ECR problem/scope, PRD or roadmap link, investigation issue |
| Requirements | Design | Actors, permissions, behavior, quality constraints and observable acceptance are sufficient | ECR requirements and acceptance, or a decision blocker |
| Design | Implementation preparation | Proposed target, baseline revision, alternatives and consequential decisions are understood or blocked | ECR solution design, target views, RFC/ADR when independent |
| Implementation preparation | Implementation | Dependency-ordered increments, verification, migration and rollback are covered | ECR implementation strategy, implementation-preparation reference |
| Implementation | Verification and review | Actual change revision, protected behavior, deviations and planned checks are known | Work products, tests, ECR implementation/verification |
| Verification and review | Release | Actual checked behavior, findings, coverage gaps and current-head evidence are available | ECR verification/review, PR, release readiness |
| Release | Operations and learning | Actual artifact, target, gates, rollout/recovery and observed state are separated | Release note, deployment record, runbook/SLO updates |
| Operations and learning | Planning or design | Incident, signal or feedback changes an assumption or reveals a gap | Incident/postmortem, ECR update, new decision |

A phase can reopen an earlier decision when new evidence invalidates its premise. Update the owning artifact and recheck dependents; do not keep implementing on a contradicted design.

## Stopping points

- **Plan** stops at the decision to proceed, investigate or defer.
- **Refine** stops when requirements and acceptance are ready for design, or at the precise open decision.
- **Design** stops when the target is accepted, limited or blocked; it does not implement.
- **Implementation preparation** stops at the breakdown when that is the request.
- **Implement**, **fix** and **harden** include the authorized code, checks and commits within their flow; they do not silently merge, deploy or publish.
- **Test** stops at the verification result and evidence gaps.
- **Review** stops at findings; source edits, posting and merge require their own authority.
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

When a request changes from one stopping point to another, say so and apply the new activity. For example, a design discussion that becomes “build it” is an implementation request; a bug report that becomes “why is this happening?” is an investigation. Do not silently cross the boundary.
