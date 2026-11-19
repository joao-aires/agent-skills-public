---
name: retro
description: Review a session for durable improvements to instructions, checks, navigation
  and tool economy. Use when asked what should change so future runs need less correction.
  Stops at candidates; applying them is separately authorized.
user-invocable: true
disable-model-invocation: true
metadata:
  kind: workflow
  origin: local
  pack: sdlc
  domain: development
  phase: cross-phase
  scope: generic
  invocation: user
  role: support
---

# Retro: turn a session into durable improvements

The subject is the **working environment**, not the product and not the people. A retro finds the few changes that would make the next session need less correction and better evidence, then stops before applying them.

Read [writing-for-agents](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/documentation/skills/writing-for-agents/SKILL.md) for how an instruction earns its place, and route durable repository changes through [project conventions](../project-conventions/SKILL.md). That skill owns the repository's instruction surface, structure and checks.

## Fix the evidence

Use the session the user names, otherwise the current one. Read the actual transcript, tool calls, diffs, commands and outputs. Separate what happened from what the user remembers and from what the agent claimed it did. Note the revision, environment and any part of the session that was not observable.

A candidate needs an observed cost: a wrong turn, a repeated search, a missed check, a correction the user had to make, an expensive call that returned little, or a failure that a guardrail would have caught. Do not propose improvements from general preference or from a single stylistic dislike.

## Find the costly moments

Walk the session in order and mark where work stalled or repeated:

- the agent guessed at a convention instead of finding it, or found it only after searching several files;
- the same information was read, restated or rediscovered across turns;
- a mechanical error shipped and was caught by the user rather than a check;
- an instruction was present but ignored, or absent and had to be supplied;
- a command, tool or service produced more noise than the decision needed;
- a fact was unavailable and the agent substituted an assumption;
- the owner had to restate scope, authority or a constraint.

Group those into four durable categories:

| Category | Look for | Durable fix |
| --- | --- | --- |
| Instructions | repeated correction, missing convention, oversized, duplicated or no-op steering | a rule at the narrowest owner; prefer deleting or merging before adding |
| Checks | a mistake a deterministic check could catch; an existing check that is unwired, slow or silently broken | wire or repair the existing check, then add the smallest missing one |
| Navigation | slow discovery, hidden dependency, stale pointer, information far from its use | a pointer, index entry or move near the entry point |
| Tool economy | repeated reads, expensive calls, noisy output, missing access | fewer round trips, a focused command or output, read-only access to the needed signal |

Prefer the smallest fix that changes the observed behavior. A new document, a new agent or a broader process is usually more expensive than the problem.

## Classify before recommending

A **mechanical violation** is a fixed, checkable pattern: a banned API, an import shape, a required file location, a missing command, a schema or formatting rule. Its durable fix is an executable check — a lint rule, typecheck, test, schema validation, hook or CI job — in the toolchain the repository already uses.

A **judgement call** is not reducible to a deterministic check: cross-file consistency, matching the surrounding style, choosing a boundary, interpreting an ambiguous request, deciding when an exception is justified. Its durable fix is a short rule at the instruction surface the relevant actor actually reads.

Use the distinction honestly:

- do not write a rule for something a check can enforce; the check is more reliable and cheaper to keep true;
- do not force a check for a judgement call; a brittle check teaches the agent to satisfy the check rather than the intent;
- when a mechanical violation has no feasible check, say why, and place the narrowest rule at the point of use;
- when a rule is ignored repeatedly, the problem may be its location, wording or competing instructions, not its absence.

## Route to the existing owner

Do not assume a particular repository shape or agent topology. A repository may have no `CODING_STANDARDS.md`, no `package.json` scripts, no lint command, no pre-commit hook, and no separate implementation and review agents. Read what exists: contributor instructions, task runner, CI, hooks, docs index, test layout and the roles that actually participated.

Name the file or mechanism that exists. If the right home does not exist, the candidate is to establish it through [project conventions](../project-conventions/SKILL.md), with an owner, a cost and a verification path — not to invent a parallel standards file.

For durable instruction changes, involve both owners:

- [project conventions](../project-conventions/SKILL.md) owns where the instruction, check or repository structure belongs;
- [writing-for-agents](https://github.com/joao-aires/agent-skills-public/blob/main/plugins/documentation/skills/writing-for-agents/SKILL.md) owns whether the wording, pointer and information hierarchy will actually change behavior.

A check belongs to the toolchain or CI owner. A navigation entry belongs to the repository's docs index or the component that hides the dependency. A tool-economy change belongs to the command, tool or access owner. Do not create a new standards document or a new agent split merely to hold a candidate.

## Present the candidates

Order by severity: failures that escaped first, then repeated cost, then hygiene. For each candidate give:

- the observed evidence, with the turn, command or tool call that shows it;
- the category and the classification (check or rule);
- the proposed owner and the file or mechanism that would hold it;
- the smallest change, and whether it adds, rewrites, moves or removes something;
- the expected effect on the next session and how you would notice it worked;
- the cost, risk and confidence.

Separate "add" candidates from "remove or merge" candidates. A retro that only adds is usually growing the problem. Name a candidate you considered and rejected, with the reason, when the user is likely to ask.

## Stop at candidates

Do not edit instructions, checks, configuration, documentation or code during the retro. Applying a candidate is new work with its own scope, owner and verification; perform it only when the user separately authorizes it.

Do not recommend a change that requires authority the session does not have. Name the owner, the decision and the evidence that would justify it. Stop when the costly moments are accounted for, the candidates have an owner and a cost, and further analysis would only improve phrasing.

## Anti-patterns

- **Session diary** — narrating the session instead of naming durable causes.
- **Rule for a mechanical pattern** — writing prose where a check would be deterministic.
- **Check for a judgement call** — encoding taste as a brittle gate.
- **One-off promotion** — turning a workaround for this incident into a repository rule.
- **New document reflex** — creating a file instead of fixing the pointer, owner or existing instruction.
- **Assumed topology** — prescribing an implementation/reviewer split or a `CODING_STANDARDS.md` that the repository does not use.
- **Uncosted advice** — recommending a change without saying who maintains it or what it costs.
- **Applying during review** — editing the environment the retro is supposed to assess.
