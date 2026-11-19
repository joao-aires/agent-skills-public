# Security diff review

Use this reference when a review covers a diff, commit or pull request that can affect access, data, state, value, credentials, external trust or the configuration that governs them. It supplies the security-specific questions for a change; use [code review](../../code-review/SKILL.md) for general standards and [verification](../../test/SKILL.md) for evidence expectations. A documentation-only, formatting-only or otherwise inert change is ordinary review, not a security diff.

## Establish the baseline

Identify the base and head revisions, the change's stated intent and the behavior that must be preserved. Read the accepted invariants, authority model and relevant design decisions for the affected area. Inspect both versions rather than reviewing added lines in isolation.

Treat a refactor as security-relevant until the diff shows it preserved the checks, ordering and trust boundaries. Size is not a risk signal: a small change to authorization or validation can matter more than a large mechanical edit.

## Inspect the security-sensitive change

| Concern | What to check |
| --- | --- |
| Authentication and authorization | Removed, relaxed or moved checks; changed roles, tenants or ownership; new entry points; default-allow branches; checks that moved to a caller or client. |
| Input and encoding | Removed validation, new parsers or deserializers, path and query construction, template output, redirects, file handling and archive extraction. |
| Cryptography and secrets | Changed algorithms, modes, key sources, nonces, comparison or randomness; secrets in logs, errors, generated files or client bundles; new credential authority. |
| External calls and trust | New hosts, callbacks, webhooks, providers or delegated identities; unchecked responses; changed timeout, retry or redirect behavior across a trust boundary. |
| State and value | Changed ordering, idempotency, accounting, inventory, quotas or privilege transitions; races and partial effects; destructive cleanup that becomes reachable earlier. |
| Failure behavior | Fail-open defaults, expanded error detail, missing denial evidence, and logging that records sensitive values or hides an important failure. |
| Configuration and dependencies | More permissive defaults, disabled protections, new privileged runtime settings, and dependencies that add install or execution surface. |

## Read removed security code and its history

For each removed or weakened control, find out why it existed before deciding it is redundant. Use the repository history and blame for the removed lines, the security-relevant commit messages and any linked incident or advisory. A control restored after an earlier removal can be a regression; a control removed because the underlying mechanism changed may be safe only if the replacement covers the same path.

Check the replacement, not just the removal: a validation moved to a shared middleware, a permission moved to a route policy or a check moved to the data layer can be correct. A comment claiming the move is not evidence that every caller crosses the new path.

## Trace blast radius

Identify who can reach the changed behavior and what else depends on it. Include HTTP routes, background jobs, scheduled tasks, exports, administrative tools, event consumers and direct API or database access. Trace callers far enough to find shared helpers, cached state and downstream consumers.

Prioritize by reach and consequence, not line count. A changed helper used by one disabled path is different from a changed helper used by every authenticated request. State the callers and entry points inspected, and name the ones left uninspected.

## Find coverage and regression gaps

Security-relevant changes need evidence for the denied path, not only the successful one. Check whether tests cover the removed control's original purpose, the new authority boundary, invalid or hostile input, ownership and tenant denial, and the failure behavior.

- A removed or weakened test is a coverage gap even when another happy-path test still passes.
- A new sensitive branch with no test raises uncertainty; it is not automatically a vulnerability, but it limits what the diff establishes.
- A test that asserts only the client response does not establish that the server or stored state is protected.
- Record checks that could not run and the resulting limits on the finding.

## Model adversarial paths

For a plausible weakness, state the attacker's starting position, the entry point and privileges required, the preconditions, the concrete sequence that reaches the affected code, and the impact. Show why the change enables the path and what evidence supports it. Distinguish a demonstrated path from a theoretical one, and state the confidence.

Use the accepted invariants and trust boundaries as the cross-check: a path that violates one is stronger evidence than a pattern match. Do not present a generic vulnerability category as a finding without the actual route through this change.

## Report and stop

Report each finding with its severity, the affected file and line or hunk, the relevant revision or commit, the scenario, the impact, the confidence and the coverage limits. Separate observed defects from questions that need a product or security decision.

The review ends at findings. Apply fixes through [harden](../SKILL.md) or an authorized remediation, and verify the legitimate and denied behavior through [verification](../../test/SKILL.md). A report is review evidence, not a new artifact type, and the review does not authorize merging, deploying or accepting risk.
