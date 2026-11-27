---
name: develop
description: Take a rough business idea, feature, refactor or improvement through
  clarification, design, implementation, testing and review in one requested engagement.
  Use when the user asks to build a feature, including after a discussion of its requirements or design. Reuse agreed decisions and fill only gaps needed to implement safely.
user-invocable: true
metadata:
  kind: activity
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
---

# Develop

Take a rough idea, feature, refactor or improvement through clarification, design, implementation, testing and review, and stop at the requested outcome with its verified, reviewed change. Reuse accepted decisions and fill only the gaps needed to implement safely.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. For the ECR this activity keeps current, read [guide-ecr](../guide-ecr/SKILL.md). Read [guide-prd](../guide-prd/SKILL.md) and [guide-issue](../guide-issue/SKILL.md) when those artifacts are produced.

When the affected stack, architecture or domain has installed expertise or guidance, read it and carry its conclusions. If none exists, use project evidence and primary sources; this activity keeps the outcome, acceptance and stopping point.

## When starting a new application

Read [new-application flow](references/new-application-flow.md). Reuse sufficient accepted evidence and establish missing outcomes before work that depends on them:

1. Purpose and business context.
2. Product outcome and useful slice.
3. Requirements and observable acceptance.
4. Feasibility and system design.
5. UX and visual direction.
6. Implementation plan and foundations.
7. Implementation, testing and repair.
8. Delivery and learning.

A named stack or starter kit does not supply missing decisions. Defined existing work reuses accepted context. It does not restart the full lifecycle.

When the work interleaves requirements, design and implementation, keep [engagement state](../activity-system/references/engagement-state.md): one focus, several threads and explicit reopens. Announce a change of stopping point rather than silently crossing it.

When client-specific implementation commands, a typechecker or a Git commit are unavailable, use the [local implementation flow](references/implementation-flow.md). It preserves the implementation outcome without inventing a command surface or an unrequested repository.

When optional guidance assumes commands, Git or tools that are unavailable, follow [composition](../activity-system/references/composition.md) and record the adaptation. Do not treat an upstream default as authority over the accepted project.

Use [test](../test/SKILL.md) and the review composition (`code-review`, artifact assurance, guides/quality bar) as part of the engagement when implementation is authorized. Their authority still stops at local verification and assessment.

## Establish a useful slice

Treat the rough idea as an outcome to shape, not an instruction to build every imagined feature. Inspect the repository and supplied references first.

For existing behavior, use [system documentation guide](../guide-system-documentation/SKILL.md#trace-a-feature-before-changing-it) to follow the relevant path and a comparable implementation. Establish how users enter the feature, where decisions and state changes happen, and which tests observe the result.

Use that evidence to answer technical questions and expose material unknowns before designing the extension. Keep the trace narrow enough for the slice. A new application needs its constraints and intended journey, not an invented existing architecture.

- For a new product select a useful coherent first slice; for existing work preserve architecture, identity, UI and operations constraints.
- When outcome, scope, feasibility or priority is open, apply the [planning method](../plan/SKILL.md) before dependent requirements or design. Use business strategy expertise if business direction or viability is unresolved.
- Reuse accepted context for defined work.

## Resolve decisions before dependent work

Clarify material user/business outcomes, data/authority boundaries and high-impact UX/API/architecture choices before dependent work.

- Ask a small coherent set of decision-changing questions; retain answers already provided.
- State reversible assumptions for ordinary details and proceed within scope.
- In unattended mode return the concrete blocking decisions and useful independent findings instead of fabricating them.

## Design and prepare the slice

Turn the selected slice into a small set of outcomes that can be demonstrated. Then identify the design choices that could change those outcomes or force substantial rework. Resolve those before coding their dependents, while leaving ordinary implementation details to the implementation work.

At implementation, apply [implementation preparation](../activity-system/references/implementation-preparation.md) when the next increment needs a breakdown. Keep the reasoning connected across phases. At each consequential dependency, apply [artifact assurance](../artifact-system/references/assurance.md) to identify accepted decisions, missing coverage and contradictions **before** dependent work. Carry explicit ready / ready-with-limitations / blocked dispositions into the ECR without interrupting for unnecessary approval. The product outcome should explain the requirements. The requirements should explain the design. The design should explain the implementation order and verification. Producing separate documents with inconsistent decisions does not establish this continuity. Keep one ECR current across performed outcomes, link the product/design authorities, and leave unperformed sections pending. The end-to-end flow needs neither separate phase invocations nor an issue tracker.

- For meaningful frontend work use available integrated interface-design expertise for product-derived structure, interaction, visual direction and affected-surface coverage. Incorporate relevant domain/archetype and platform constraints before coding; carry their accepted conclusions through the existing implementation handoff. A narrow UI fix reuses the accepted direction without reopening it.
- For backend work establish authority, invariants, state/failure and compatibility contracts using service-contract design expertise when available.
- Apply only matching accepted-stack conventions; missing optional methods do not remove these decision outcomes.
- Use text, wireframes or mockups to settle the actual uncertainty. The ECR's standard sections are compulsory, but separate documents per phase, screen approvals and complete scaffolds are not.

## Implement and verify

Implement in increments that can be exercised, using relevant supporting skills directly and preserving native invocation controls. After each meaningful change, run the checks that observe its behavior, inspect the result, and repair defects before extending the same approach elsewhere. If implementation disproves an assumption, revisit the affected design or requirement and carry that change through the remaining work.

[test](../test/SKILL.md) runs this scenario/test/inspect/repair loop and owns the evidence needed to claim completion. Git contributions owns isolation and publication. Reconcile accepted ECR decisions and proposed C4/sequence diagrams with code, test evidence and canonical current-state docs. A merged revision does not establish production deployment. For UI work, inspect the running experience. For stored behavior, check what can be read back through the real application path.

When the request spans several threads, this session is the coordinator: it keeps the thread map, the decisions and the acceptance, and calls a delegate for each phase of each thread. A delegate is one thread in one phase — it receives the [delegation](../activity-system/references/delegation.md) envelope and the artifacts at a revision, and returns artifacts rather than a summary. Two threads at different phases are normal. Know which is where, and keep one writer per file set.

## Review and close

Use [test](../test/SKILL.md) for final review of the integrated change and resolution of material findings. Check convergence against accepted requirements and design at the current implementation revision. Verify PR-summary claims against the cumulative diff and actual latest-head checks. Record any unresolved acceptance gap before reporting completion. Carry the accepted outcome and actual verification evidence into that review. Identify an independent review as such only when it occurred. Revisit the affected design or check if a finding changes its premise.

Finish with the implemented user outcome, the checks actually performed, and any unfinished or blocked part. Delivery and learning are part of considering the result, but publishing, deploying or contacting users still follows the established contribution/delivery scope.

## Composition

Read [artifact-system](../artifact-system/SKILL.md) and [coordination storage](../artifact-system/references/storage/coordination.md) for the artifact model, contracts and configured filesystem or document-provider home. Record each performed outcome in the ECR, even within an end-to-end `develop` request. A tracker is optional, and publication requires authority. Before creating or moving a durable artifact, read the repository artifact home map and [artifact homes](../artifact-system/references/homes.md). Use [design-system](../design-system/SKILL.md) after product refinement or when the feature changes consequential architecture, before dependent implementation. Read [git-contributions](../git-contributions/SKILL.md) for the objective's feature worktree, [test](../test/SKILL.md) for testing and completion.
