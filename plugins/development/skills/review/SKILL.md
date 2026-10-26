---
name: review
description: Review a PR, branch or current diff against its intended behavior and
  engineering standards, checking appropriate test evidence. Use for explicit reviews
  or configured PR-review jobs; default to assessment rather than source changes,
  publication or merge.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Review

Read [task guidance](../../TASKS.md). Read [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) for completion evidence and scope. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

## Establish and assess the review target

Pin target/base/head from the PR or current repository context; ask only if ambiguity changes the diff.

- Use the agreed request/spec/ticket when present, without requiring a tracker or inventing requirements.
- Follow the changed behavior from its caller to its result. Read enough surrounding code to understand existing callers, stored state and error handling, then check whether the new behavior agrees with them.
- Examine consequential assumptions: which actor is trusted, which changes happen together, what a retry means, and which consumers may still use the previous behavior. Use relevant specialists to deepen concerns that the diff actually changes.
- For affected UI use interface assessment expertise and interface-language expertise when installed; distinguish rendered/runtime evidence from static inspection.
- Use usability research expertise only for relevant supplied observations or a requested research plan, not to fabricate validation.
- Use code-review or security techniques only as supported by the client's invocation controls; review inline if delegation is unavailable.

## Verify and report findings

Inspect existing checks and run appropriate authorized local tests when useful, including actual affected journeys. CI status alone does not establish that all tests passed.

For each finding, provide:

- Severity and concrete location/scenario.
- User or system impact.
- An actionable fix.

Support a defect with the path through the changed code, the condition that makes it fail and the accepted behavior it violates. If the conclusion depends on an unverified assumption, state that assumption and the evidence needed to resolve it. Missing evidence and a proven defect are different findings.

### Preserve review scope and revision

- Leave source unchanged by default, apart from owned test/runtime artifacts.
- Post comments, apply fixes, approve or merge only under the request or trusted job policy.
- Reassess affected conclusions after a head change; earlier review and test evidence does not establish the new revision's behavior.
