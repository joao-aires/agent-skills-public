# Artifact quality bar

Apply this bar to every engineering artifact: ECR, issue, pull request, research report, RFC, ADR, product brief or roadmap. It defines the minimum for a reader who was not in the conversation. It is not a section template; the artifact's [contract](contracts/README.md) defines its sections and status vocabulary.

A compact artifact can pass. A long artifact can fail. The test is whether the reader can decide and act, not whether every heading exists. Length is not the measure; answers are.

## The six properties

### 1. Self-contained context

The artifact must survive the conversation. A reader with the artifact and its linked authorities, but without the chat, must be able to start.

- State the starting condition, the desired outcome and the scope boundary.
- Define an unfamiliar term at its first useful occurrence; use the same name afterwards.
- Do not rely on "as discussed", "the above", "the existing issue" or "the current design" without a link and a short explanation.
- For an agent reader, include exact paths, commands, revisions and target environments. Do not assume implicit tool state or session memory.
- If the artifact is a view of a larger authority, summarise enough context to act and link the authority for detail.

### 2. Explicit maturity and evidence

Every artifact states its own maturity and what evidence backs each claim. Do not borrow another artifact's lifecycle.

| Maturity | Claim the artifact may make | Evidence it needs |
| --- | --- | --- |
| Proposed | A recommendation or plan exists | Rationale, alternatives, open decision and owner |
| Accepted | A decision is made | Decision owner, constraints, affected work |
| Implemented | The change exists in source | Revision or diff link, affected paths |
| Verified | The behavior was observed | Command or scenario, environment, result and revision |
| Released | The target has it | Target, rollout state and observation |
| Superseded | A later artifact replaced it | Link to the replacement and reason |

A later-phase claim needs its own evidence. A product brief does not claim implementation; an RFC does not claim release; a local probe does not claim production behavior. Write evidence in the past tense. "Will verify", "should pass" and "create/read/update will confirm" are plans, not verification.

### 3. Reader sufficiency

A section is complete when it answers its reader's decision or action question. A section that only restates its heading, links elsewhere for its substance, or says "pending" after the activity has been performed is an index, not a section.

Name the actor, action, condition, observable result and the relevant denial or failure path. If a reader must open another artifact to understand the core claim, the section is incomplete. Put the summary here and the detail behind a link.

Use this cold-reader test before handoff:

1. What is this, and why does it exist?
2. What changed or will change, for whom, and what must not change?
3. What evidence supports the current status, and what remains open?
4. What is the next action, who owns it, and where is the authority?

If any answer is only "see X", add the self-contained summary. The link is for depth, not for the core answer.

### 4. Resolvable navigation

Every commit, revision, pull request, issue, page, file, diagram and external source cited in a published artifact must be one of:

1. A resolvable link in the artifact's publication context: an absolute URL for a hosted artifact, or a verified relative path within the same accessible repository or workspace; or
2. An explicit local-only reference: `repo/path@<full-sha>`, the branch and worktree, and the words "not published; no URL".

Never write a bare short SHA, a branch name, "the PR" or "the ECR" without a link. A bare hash is ambiguous: the reader cannot tell whether it is public, private, or a local fixture that was never pushed.

| Object | Link form |
| --- | --- |
| Commit | `https://github.com/<owner>/<repo>/commit/<sha>` |
| Pull request | `https://github.com/<owner>/<repo>/pull/<n>` |
| File at revision | `https://github.com/<owner>/<repo>/blob/<sha>/<path>#Lx-Ly` |
| File in the same accessible workspace | A verified relative Markdown path |
| Issue or work item | Provider URL plus the human key, such as `ECRREV-1` |
| Page or document | Provider page URL |
| Local-only revision | `repo@<full-sha>`, branch, worktree; mark "not published" |

Resolve links when writing, not later. Verify each one in the intended publication context. A link that requires workspace membership must say so. Link bidirectionally where the reader will move between views: the ECR links the issue, the issue links the ECR, and the PR links both.

### 5. Render fidelity

Author in Markdown or the provider's native rich text. Avoid hand-written HTML unless the provider requires it.

After publishing, read the rendered view, not only the API response. Check headings and their order, list nesting, tables, code blocks, link destinations, diagram rendering, truncation and encoding. Compare the rendered text with the intended outline. A successful tool call is not proof of persistence; re-read the saved artifact.

Provider behavior matters. Plane, for example, adds editor attributes to headings and paragraphs and replaces a Page body on update. Inspect semantic content rather than raw HTML equality, and re-read after every whole-body write. If the provider stores a diagram as source code, link a verified rendering and include a short text equivalent. If the rendered view degrades, fix it or state the limitation; do not claim the artifact is readable.

### 6. Single authority and cross-view consistency

Keep one authoritative document per concern. Views are projections, not copies.

- The ECR owns the evolving engineering account.
- An issue owns intended work and coordination.
- A pull request owns the submitted diff and review evidence.
- A product brief owns product intent.
- An ADR owns a durable decision.
- A research report owns a bounded inquiry and recommendation.

Every view agrees on scope, status, revision and next action. When one changes, update the others only if their meaning changed and the edit is authorized. No issue, PR or page becomes a second ECR. Do not create a competing authority because the configured one is temporarily unavailable; report the blocker and preserve the original identity.

## Hard failures

- A bare short or long SHA without a link or an explicit local-only label.
- A required section that contains only a link, "pending", or a restatement of its heading.
- A verification claim in future tense.
- A published artifact that was never read back in its rendered form.
- Status, scope or revision disagreement between the ECR, issue and PR.
- A diagram that does not parse or render and has no text equivalent.
- A link to private content in a public artifact without an access check.
- A one-line issue in a ready or todo state.

## Relationship to other guidance

- Artifact fields, planes and relations: [artifact model](model.md).
- Artifact type selection and default homes: [artifact catalog](catalog.md).
- Home resolution and the repository map: [artifact homes](homes.md).
- Artifact sections, status vocabulary and examples: the artifact's [contract](contracts/README.md).
- Cross-artifact readiness and convergence: [artifact assurance](assurance.md).
- Prose, explanation and document order: use available reader-oriented writing expertise.
- Current architecture and ADR coverage: use available architecture documentation expertise.
- Publication mechanics and provider limits: [engineering workspace](../../engineering-workspace/SKILL.md) and its [provider reference](../../engineering-workspace/references/providers.md).
