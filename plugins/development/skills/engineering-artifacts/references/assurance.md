# Artifact assurance: readiness, consistency, convergence

Apply this method whenever an engineering activity uses or updates an ECR. The activity and domain specialist own the actual engineering; assurance checks whether the **claims and handoffs** are justified by artifact and implementation evidence. These checks are **not** a compulsory seven-command sequence, a new user-facing task, an autonomous approver, or permission to publish/merge/deploy.

## Three levels of checks

1. **Structural and reference integrity** (deterministic where possible): the ECR's seven named sections, status/disposition for pending work, source and artifact references, current vs target labels, actual evidence identifiers. For a local Markdown ECR and available Python, run `python <engineering-artifacts>/scripts/check_ecr.py <ecr.md>` (or `--json` for machine-readable diagnostics). This bundled checker validates headings, order, nonempty sections and dispositions only; it **does not** establish correctness, links, approval, implementation or tests. For provider-backed documents, use available provider data; do not export private ECRs into an unauthorized workspace to run a script.
2. **Semantic cross-artifact consistency** (evidence-based engineering analysis): compare accepted problem/requirements and acceptance against proposed UX, C4/sequence/contracts, decisions, implementation slices and planned verification. Name the actual contradictory statements and affected artifacts; a polished diagram or "all sections filled" is not sufficient. Specialist architecture/security/UX expertise owns deeper domain reasoning.
3. **Implementation convergence** (source/test/runtime evidence): compare accepted behavior, design invariants and failure cases against the checked code diff, tests and actual observations. Check that relevant current-state application diagrams/ADRs match implemented source. A check passed at an old commit does not establish a later head. Explicitly distinguish *implemented*, *verified*, *merged*, *released* and *observed in target*.

## Use at dependencies, not artificial meetings

| Boundary | Required reasoning and evidence |
| --- | --- |
| Requirements → design | Actor, permission, outcome and quality constraints have observable acceptance. Material product/authority conflicts are decided by their owner or blocked; implementation suggestions aren't mistaken for requirements. |
| Design → planning | Proposed flow/C4/sequence covers accepted requirements, including important denied/failure paths; affected current baseline identified; material design choices accepted or clearly blocked. |
| Planning → implementation | Each material acceptance and critical failure path has an implementable increment and credible verification; migrations/compatibility/recovery addressed if applicable. No work proceeds that depends on an unresolved consequential decision. |
| Implementation → verification/review | Actual changed revision, protected behavior, proposed-vs-implemented deviations, corresponding canonical-doc reconciliation and real tests/known gaps are available. |
| Review → merge readiness | PR *actual diff*, ECR accepted intent, claims about tests/diagrams/release and latest-head evidence agree; findings are explicit. Approval/merge remains with repository policy and authorized human/host. |
| Release → operations | Real artifact, environment, verification, rollout/recovery and observed target state are separated. A merge or passing CI cannot be labeled production verified. |

The agent may proceed through multiple boundaries within `develop` without invoking phase tasks or asking for signoff on every step. If a contradiction can be fixed within **already accepted** constraints, correct the owning artifact and recheck dependents. If it changes product scope, authorization, consequential architecture or other protected decisions, preserve the evidence and ask the owner; unrelated independent work may continue. A narrow bug fix still checks acceptance and actual regression evidence, but does not invent target diagrams or a task graph.

## Explicit readiness dispositions

- **Ready**: all *applicable, consequential* dependencies have sufficient decision and evidence for the next requested activity.
- **Ready with limitations**: named gaps are nonblocking for the stated next *bounded* action; say what cannot yet be claimed and who resolves each gap.
- **Blocked**: a consequential decision, contradiction, missing source or missing authorization prevents the dependent action. Do not implement that dependency based on a guess.

Evaluate readiness **relative to the next activity**. For instance, requirements may be ready for design but not implementation. "Ready" is an agent assessment backed by cited artifacts, **not** product-owner approval or a branch protection bypass. When the ECR cannot be read/persisted, report the exact boundary and unpersisted result, not an invented passed check.

## Report meaningful findings and repair them at their source

For each consequential finding, record in the relevant ECR section or return inline if persistence is unavailable:

- **Claim and evidence**: precise requirement, diagram step, plan increment, source path/line or test result (at a revision/target), showing the conflict or gap.
- **Impact**: what incorrect behavior, safety/authorization risk or failed outcome could result.
- **Disposition**: fixed and rechecked; ready with stated limitation; or blocked with responsible decision owner and next required evidence.
- **Dependent impact**: other ECR sections, proposed views, issue/PR summaries or application docs that must be updated. Do not create an additional assurance document by default.

Example: an accepted requirement revokes export permission on every execution, but the target sequence authorizes only schedule creation. Mark design → plan **blocked** for that path, update the proposed sequence and acceptance coverage, then recheck. If implementation tests never execute the revocation path, report it as **unverified**, not converged; don't soften the accepted requirement to match the code.

## Separate PR alignment from an ECR copy

Before describing a contribution as review-ready, compare **the cumulative PR base-to-current-head diff** with its PR description, ECR intent, accepted/proposed design deviations, canonical-doc changes, actual latest-head check results and operational risk. Fix incorrect summary claims when editing is authorized; otherwise report a precise PR-description finding. A private ECR may require an access-safe self-contained PR explanation; never paste private record content into a public review. Do not infer that CI passed simply because CI exists.

## Limits of enforcement

The checker below provides deterministic **shape checks** on accessible Markdown, not workflow execution gates or semantic correctness. Agent assurance checks are instructions plus evaluation scenarios; they are not guaranteed runtime hooks or independently executed tests. A future optional orchestrator or CI can run selected checks as hard gates only in an explicitly configured environment with reliable revision/persistence semantics. Don't claim this skill alone prevents an agent from skipping a step.
