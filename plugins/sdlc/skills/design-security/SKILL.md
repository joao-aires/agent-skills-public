---
name: design-security
description: Design security into a feature or system boundary — trust boundaries, data flow, authority placement, privacy, delegation and abuse resistance, including authentication, sessions, federation, machine identity and tenant/resource access. Use when a change introduces identities, user data, external inputs, integrations or new authority; not for scoped remediation, credential operations or compliance assessment.
metadata:
  kind: method
  domain: security
  phase: cross-phase
  scope: generic
  invocation: both
user-invocable: true
---

# Design security into the boundary

Read [activity system](../activity-system/SKILL.md) for scope and stopping point.

Security design decides where trust changes, who may do what, which data may move and what happens under abuse. It is not a checklist applied after the architecture is settled. Read the feature, architecture, accepted data flows and prior decisions. Name the valuable data or action, the actors, each entrypoint, and the boundary this change creates or moves.

[Security in design](../design-system/references/security.md) owns the design constraints and routes security questions. This method owns the in-depth design. Scoped remediation belongs to [harden](../harden/SKILL.md), credential lifecycle and vulnerability operations to [run-security-maintenance](../run-security-maintenance/SKILL.md), and applicability and evidence to [run-compliance-assessment](../run-compliance-assessment/SKILL.md). Compliance is not a security outcome, and a provider attestation describes the provider.

## Trace what crosses the boundary

For each crossing, establish what is accepted, what validates it and what happens when validation fails. Follow input, identity, commands, model output and provider responses in both directions. A boundary that is named but has no enforcement point is a hope, not a control.

Read [trust boundaries and data flow](references/boundaries-and-data-flow.md) for the operation matrix, data lifecycle, delegation and exposure through logs, caches, exports, backups and providers.

Collect and retain deliberately. For each new personal-data field or telemetry event, record purpose, recipients, storage, retention and access. Include analytics, caches, exports, backups and model providers. Do not equate a deployment region with a legal basis; escalating an unresolved legal or product choice is part of the design.

## Put authority where the effect happens

Derive identity and tenant context from verified authentication. Enforce authorization in trusted code that controls the actual resource, action and lifecycle state — not in the client, a prompt or a presentation layer. Cover HTTP/API calls, background jobs, exports, support tools and AI/MCP actions. Listing, search, related resources and bulk operations need the same semantics as a single read or write. Default-deny unknown operations, and treat client-supplied role, tenant and entitlement fields as input to verify.

Read [identity and access](references/identity-and-access.md) when the change introduces or moves authentication, sessions, federation, passkeys, machine identity or resource and tenant permissions. Follow authority-changing events into existing sessions and caches: membership, role, entitlement, expiry, recovery, linking and deprovisioning.

## Treat delegation as exposure

A credential, token or provider integration extends the application's authority to another party. Establish which component holds it, for which operations, under whose terms, and how it is rotated or revoked. Trace it to the recipient and to redirects or delegated processors. User-supplied credentials have different storage and revocation tradeoffs; they do not automatically make processing private.

Choose credential ownership from the deployment. Distributed client code cannot keep a confidential secret merely because a build variable supplied it. Keep privileges narrow, separate environments, and avoid fallback secrets or permissive production defaults. When recipients, purposes or stored access change, reassess the disclosure and authorization basis rather than assuming the old arrangement still covers it.

Treat model output and tool arguments as untrusted. Keep authorization outside the prompt, minimize data sent to providers, and avoid granting a model broad credentials.

## Resist abuse proportionately

Identify what an attacker, a careless client or a runaway integration can make happen, and who bears the cost. Bound uploads, expensive queries, external calls, retries and fan-out so a small request cannot exhaust shared capacity. Fail closed when required security configuration is absent, and avoid error differences that reveal existence or authority.

Read [threat and abuse](references/threat-and-abuse.md) for abuse cases, hostile input, authority confusion, resource exhaustion and the checks that distinguish a control from a claim. Use [OWASP threat modeling](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) and the relevant cheat sheet for the actual risk. A few documented abuse cases often suffice for a small feature; an exhaustive audit is a different job.

## Verify and keep the design connected

Exercise the behaviors that settle the design:

- Allowed and denied operations, including cross-user and cross-tenant requests.
- Expiry, logout, revocation, recovery, linking and privilege changes.
- Missing configuration, hostile input and a necessary provider outage.
- Stale caches and existing sessions against the accepted revocation window.

Translate concrete risks into focused checks rather than a generic security test list. Use [security diff review](../harden/references/security-diff-review.md) for an affected change and available supply-chain auditing expertise for dependency risk. An unassessable result is not a clean bill of health. Choose further specialist tools only when their scope matches the application and the request.

Keep architecture, data-flow, retention and decision notes synchronized with the change. Record what was checked, what changed and what remains uncertain. Do not label an application secure or compliant because scans pass. Hand live incident impact to [run-incident-response](../run-incident-response/SKILL.md), implementation changes to the relevant activity, and unresolved risk to a named owner with a review point.

Sources and project interpretation are recorded in [sources](references/sources.md).
