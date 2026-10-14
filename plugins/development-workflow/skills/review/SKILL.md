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

Pin target/base/head from the PR or current repository context; ask only if ambiguity changes the diff. Use the agreed request/spec/ticket when present, without requiring a tracker or inventing requirements. Review scope, correctness, contracts, UX coverage, data/authority, reliability and delivery consequences with relevant specialists. Use code-review or security techniques only as supported by the client's invocation controls; review inline if delegation is unavailable.

Inspect existing checks and run appropriate authorized local tests when useful, including actual affected user journeys. Do not claim all tests passed from CI status alone. Return severity, concrete location/scenario, impact and an actionable fix; distinguish missing evidence from proven defects. Leave source unchanged by default, apart from owned test/runtime artifacts. Post review comments, apply fixes, approve or merge only when requested or covered by trusted job policy. A changed head invalidates earlier review/test conclusions.
