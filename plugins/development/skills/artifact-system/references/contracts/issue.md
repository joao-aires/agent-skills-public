# Issue contract: independently actionable work

An issue owns the **intended work and coordination**. An ECR owns the evolving engineering account. A pull request owns the submitted diff and review evidence. Repeat the context, constraints, acceptance and evidence the reader needs to act independently; link the authority for depth.

Apply the [artifact quality bar](../quality-bar.md). An issue is complete when a reader can pick it up **without opening the ECR** and still know what to do, what not to do, how success is observed, and where the evidence lives.

## Actionable issue contract

Use this body when the work is ready or nearly ready to pick up. Adapt the headings to the tracker without dropping the content.

```markdown
## Context
Current behavior, who is affected, and the evidence link.

## Intended outcome
What will be true after this is done.

## Scope and non-goals
What is in, what is explicitly out, and which existing behavior must not change.

## Acceptance
- [ ] Observable check 1, including the denial or failure path where relevant
- [ ] Observable check 2
- [ ] Observable check 3

## Constraints and dependencies
Contracts, data, compatibility, owners, blockers.

## Verification
Command or scenario, environment, expected result.

## References
ECR (link), design (link), baseline (link), related issues or PRs.

## Status
Ready, in progress or blocked; owner; next action.
```

Guidance for each part:

- **Title.** Name the intended outcome, not the topic. "Prevent cancelled webhook jobs reaching the receiver" is actionable; "Webhook bug" is not.
- **Context.** Two to four sentences. State the current behavior, the impact, and a link to the failing case, reproduction, report or ECR section. Do not make the reader reconstruct the conversation.
- **Intended outcome.** One or two sentences in the user's or operator's terms. Distinguish the outcome from the implementation.
- **Scope and non-goals.** Name affected surfaces, contracts and data. State what must remain unchanged. This prevents a bounded fix from becoming a redesign.
- **Acceptance.** Use observable checks, not activity labels. Include the denial, failure, retry or compatibility case when it affects the promised behavior. Three to seven checks is usually enough. Link the detailed acceptance table in the ECR if it is larger.
- **Constraints and dependencies.** Name contracts, migrations, compatibility, owners, prerequisites and blockers. Say which work can proceed independently.
- **Verification.** Give the command or scenario, environment and expected result. If the check cannot run yet, say why and what evidence will be needed.
- **References.** Link the ECR, design, baseline revision, related issues and PRs. Use the [link rules](../quality-bar.md#4-resolvable-navigation); a bare SHA or "the ECR" is not a reference.
- **Status.** Ready, in progress, blocked or done. Name the owner and the next action. Do not mark done without linked evidence.

## The issue-only pickup test

Before publishing, read the issue as if you had never seen the ECR or the conversation. Can you answer:

1. What is the problem and who is affected?
2. What exactly is in scope, and what is out?
3. What must be true for this to be done, including the failure or denial case?
4. What is the first action, and what depends on another decision?
5. How will the result be verified, and where is the evidence?
6. Where is the authoritative record and the baseline revision?

If any answer requires opening another artifact without a self-contained summary, the issue is a note, not a work item.

## Roadmap and idea items are different

A one-line issue in a "ready" or "todo" state is the worst of both worlds: it looks actionable but is not. If the work is still an idea, keep it in the roadmap or mark it as an idea and give it a short body:

```markdown
## Problem
What is missing or costly today.

## Desired outcome
What would be better, without pretending the solution is decided.

## Open questions
What must be decided before this becomes actionable.

## Next step
The investigation or decision that turns this into work.
```

If the tracker is the agreed roadmap home, that is enough. Do not give an idea a fake acceptance checklist or a "done" state. If it becomes actionable, replace the idea body with the issue contract above.

## Publish

1. Locate the existing issue through the [engineering workspace](../../../engineering-workspace/SKILL.md). Reuse it when its scope matches.
2. Use the configured tracker to create or update an issue only within authorized scope. If publishing is outside scope, return the draft.
3. If the issue and ECR live in different tools, repeat the acceptance criteria and link the authoritative record. Do not copy the whole ECR.
4. Respect visibility. Do not paste private workspace content into a public issue; link it only if the audience can access it.

## Review

Read the saved issue on its own. Check that the reader can identify what to do, what is outside scope and how to verify success. Apply the [quality bar](../quality-bar.md) and the [artifact assurance](../assurance.md) reader inspection. If the provider normalizes the body, inspect the rendered result, not only the tool response. Fix defects within scope and recheck.

## Close

Preserve the intent and applicable acceptance. Add the actual result, evidence and remaining work. Link the PR, commit or verification record using the [link rules](../quality-bar.md#4-resolvable-navigation). Do not rewrite the original acceptance to match a partial result; mark the uncovered part as remaining or blocked.

## Example

> **Prevent cancelled webhook jobs reaching the receiver**
>
> **Context.** A public-API reproduction delivers a job after `cancel()` returned true. The receiver is called once for a cancelled job. Baseline `queue@<full-sha>` ([commit](https://example.invalid/queue/commit)); failing test linked in the ECR.
>
> **Intended outcome.** A successfully cancelled queued job never reaches the deliver callback, while a different waiting job still progresses.
>
> **Scope and non-goals.** In scope: the in-memory queue dispatch path and its regression tests. Out: durable delivery, HTTP changes and production rollout. Preserve FIFO among eligible jobs and retry of receiver errors.
>
> **Acceptance.**
> - [ ] `enqueue → cancel → runNext` never calls the receiver for the cancelled job.
> - [ ] A different waiting job reaches the receiver with its original ID and payload.
> - [ ] Repeated dispatch on a cancelled-only or drained queue returns `null`.
> - [ ] A receiver error remains retryable and propagates the original error.
>
> **Constraints and dependencies.** No new dependency or storage. Use the existing native Node test runner. The fixture is local-only; no remote publication is implied.
>
> **Verification.** `node --test queue.test.mjs` at the repaired revision; expected 7 passed, 0 failed. Record the failing baseline separately.
>
> **References.** [ECR](https://example.invalid/ecr), baseline `queue@<full-sha>` ([commit](https://example.invalid/queue/commit)), failing regression at `queue@<full-sha>` ([commit](https://example.invalid/queue/red)).
>
> **Status.** Ready. Owner: bug actor. Next action: reproduce, then repair dispatch eligibility.
