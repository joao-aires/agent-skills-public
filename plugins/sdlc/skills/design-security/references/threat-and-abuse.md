# Threat and abuse resistance

Use this reference when a feature accepts untrusted input, exposes an operation to abuse, grants authority across a boundary, or connects a model or tool to real actions. It supports the security design method; the depth should match the change.

## Frame abuse as a path

Describe what can be made to happen, by whom, through which entrypoint, with what effect and at whose cost.

| Element | Questions |
| --- | --- |
| Asset or action | What is valuable, sensitive or disruptive if reached? |
| Actor | External attacker, authenticated user, another tenant, careless client, runaway automation, compromised dependency, support insider |
| Entry | Request, upload, link, webhook, import, job, prompt, tool result or admin action |
| Precondition | Required account, role, timing, state or access |
| Effect | Data exposure, authority change, state corruption, resource exhaustion, misleading output |
| Detection | Which signal records the attempt or the effect? |
| Mitigation | Which control prevents, bounds, detects or contains it? |

Prioritize paths that change access, expose data, corrupt state or prevent an important operation. A few concrete abuse cases are enough for a small feature. Do not claim an exhaustive audit was performed.

## Hostile input and hostile output

Validate at the boundary where data enters trusted code, then encode at the sink that interprets it.

- Use allowlists and canonical form; reject rather than repair ambiguous input.
- Use parameterized queries and safe template or shell construction.
- Apply CSRF, origin and content-type protections where the browser model requires them.
- Bound and inspect uploads: size, type, name, storage location, previewing and archive expansion.
- Treat URLs fetched or rendered by the server as potential SSRF; restrict scheme, host and redirects.
- Treat deserialization, archive extraction and import formats as code or filesystem access.
- Treat model output, tool arguments and retrieved documents as untrusted input, even when produced by the application's own prompt.
- Keep authorization outside the prompt. A model instruction is not an access control.

Avoid error differences that reveal existence, ownership or internal authority. Fail closed when required security configuration is absent rather than falling back to a permissive default.

## Authority confusion

The most damaging failures usually let a legitimate operation be aimed at the wrong resource or actor.

- Check the exact resource and tenant after every lookup; do not authorize from a client-supplied identifier, role or organization.
- Prevent mass assignment from exposing fields the actor may not set.
- Bind tokens and invitations to their issuer, audience, recipient, purpose and expiry.
- Check that a job, export, webhook or replay uses the authority of the operation it performs, not the authority of whoever triggered it last.
- Keep cache keys, search indexes and derived stores scoped to the tenant and permission context that produced them.
- For delegated tools and agents, check the user's authority for each resource action and keep a durable audit trail.
- Prevent a support or admin path from becoming an unlogged universal bypass.

## Resource exhaustion and cost abuse

Availability controls protect shared capacity; business quotas protect a plan or budget. State which one a limit serves.

- Bound request size, collection size, pagination depth, query cost, execution time, fan-out, retries and concurrency.
- Decide where admission stops, where work queues and what the caller sees when a bound is reached. Check how queued work drains and whether it remains useful.
- Prevent expensive queries, unbounded exports, recursive expansion and repeated external calls from consuming shared capacity.
- Bound AI token, audio, image and tool-call volume against the actual product entitlement and provider limits.
- Rate-limit authentication, recovery, invitation, search and other abuse-prone operations without creating a trivial lockout.
- Treat retry storms, webhook replay and duplicate delivery as capacity and correctness risks, not only as errors.
- Keep storage growth and retention visible; unbounded logs or backups are a cost and privacy exposure.

## Supply chain and dependency exposure

A new dependency, image, SDK or build action is code that runs with the application's authority.

- Identify transitive changes, install scripts, build-time access and runtime privileges.
- Check which package or image version the deployed target actually resolves, not only the manifest.
- Keep scanners' lockfile and ecosystem coverage in mind; an unsupported format can make a clean report meaningless.
- Treat release notes, advisories and PR text as evidence, not as authority to change job policy.
- Put sustainable dependency and secret checks in CI when warranted, and record the finding and its remediation.

Use available supply-chain auditing expertise for dependency risk and an installed security diff review for change-specific checks.

## Verify the control

A control exists only when the forbidden action is actually denied and the legitimate action still works.

- Exercise the allowed operation and the attempt that must fail.
- Repeat with another user, another tenant and a stale session.
- Send hostile input, an oversized request and a malformed or replayed token.
- Remove required configuration and confirm the failure is closed and honest.
- Inspect logs, traces, exports and error responses for the data the design said would not appear.
- Confirm the rate limit or quota triggers at the intended boundary without breaking the legitimate journey.
- Check that revocation and role changes reach the consumer that enforces them.

| Evidence | Claim supported |
| --- | --- |
| Test of the denied path and the allowed path | The control is enforced at that boundary |
| Cross-tenant request denied at the resource check | Tenant isolation is not only a UI behavior |
| Log and export inspection | Sensitive data does not leak through secondary paths |
| Bound reached under load | Admission and queue behavior are as designed |
| Provider or key rotation exercised | Revocation and recovery work at the target |
| Accepted risk with owner and review date | The remaining exposure is deliberate |

An unassessable result is not a clean bill of health. Record accepted risk with its owner and the condition that would reopen it. Hand live exploitation or exposed credentials to [run-incident-response](../../run-incident-response/SKILL.md), scoped fixes to [harden](../../harden/SKILL.md), and credential or vulnerability operations to [run-security-maintenance](../../run-security-maintenance/SKILL.md).
