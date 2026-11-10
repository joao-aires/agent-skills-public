## 1. Overview and lifecycle

Change: export-revocation. Owner: fixture engineer. Activity: implement/verify. Requirements accepted, design reconciled, implementation and tests verified at app revision 6b8852e86ce913516c7731582811b588d8b00ccf; no release/deployment performed. App baseline: 3355a84185754a5979032c8a5089970a0ef6fd68.

## 2. Problem and scope

An export can execute after a user's access to its document has been revoked, because scheduling is the only authorization boundary. Preserve allowed exports and denied scheduling; reject execution after revocation. No remote provider or deployment in scope.

## 3. Requirements and acceptance

R1 (accepted): an authorized member may schedule an export of an accessible document.
R2 (accepted): before executing a scheduled export, the system must revalidate the member's current access and never return content if access was revoked.
A1: allowed member schedules and executes. A2: denied member cannot schedule. A3: revocation between schedule and execution results in denial without content.

## 4. Solution design

Accepted target sequence (after correcting the contradiction):
1. Check permission when scheduling.
2. Store scheduled job.
3. Immediately before execution, check current member permission on the document.
4. On revoked access, reject with DENIED and return no content.
5. Otherwise export the permitted document.

Design-to-plan readiness: ready for the scoped change after reconciling R2/A3. Existing app canonical docs remained unchanged during design. No new C4 boundary introduced.

## 5. Implementation strategy

Implemented: add revocation regression A3, confirm red against baseline; implement execution-time permission check; rerun tests; reconcile canonical implemented-state docs based on checked code. No boundary change or migration.

## 6. Verification and release

Verified at app revision 6b8852e86ce913516c7731582811b588d8b00ccf: baseline tests at 3355a84185754a5979032c8a5089970a0ef6fd68 passed 2/2 without revocation coverage. New regression failed as expected on baseline (3 tests: 2 pass, 1 fail), then passed after fix (3 tests: 3 pass, 0 fail) using Node 22.16.0. Current architecture documentation was reconciled with implementation. Release/deployment pending and not performed.

## 7. Decision history and references

Accepted: revalidate current access immediately before export execution. Initial proposed design contradicted R2 by checking scheduling only; design-to-plan blocked until corrected. Evidence/limitations: ../assessment.md. No tracker, remote provider, PR, deployment or production observability in this fixture.
