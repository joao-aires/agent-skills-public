---
name: saas-design
description: Design or evolve SaaS tenancy, organization/customer lifecycle, entitlements
  and administration independently of framework or billing provider. Use when hosted-product
  behavior crosses identity, commercial and operating boundaries.
license: MIT
metadata:
  scope: generic
  invocation: both
  role: support
  references: ../../references/sources.md
user-invocable: true
---

# Define the hosted product's contracts

Start with who uses the product, who pays for it and which groups share resources. Define the user account, organization/workspace, tenant isolation boundary, billing customer and deployment separately before deciding how they relate. A single person may belong to several organizations; a customer may pay for more than one workspace; a deployment may serve many tenants. The application needs explicit ownership and access rules for the relationships it actually supports. Preserve an adequate accepted design and keep depth proportional to the requested feature. Read [lifecycle decisions](references/lifecycle.md) for commercial or tenant transitions and [research sources](../../references/sources.md) for inspected project patterns and their limits.

## Establish the tenancy and authority model

Define resource ownership, membership, organization switching and privileged administration.

- Choose shared, isolated or hybrid deployment/storage from isolation, operating cost, customization and recovery requirements, rather than treating every B2B product as a dedicated deployment.
- Carry verified tenant context through queries, caches, files, search, jobs, exports, integrations and AI/tool calls.
- Authentication, membership, resource permission and paid entitlement answer different questions.

Model invitations, role changes, ownership transfer and tenant closure as domain operations with accepted rules. Support operators need scoped, attributable access and recovery procedures, not an unbounded hidden superuser. Use available identity/access and data expertise to deepen the reasoning; missing specialists do not remove these boundaries or select a framework.

## Connect commercial state to service behavior

Establish what the plan promises, what is metered and which entity owns usage and invoices.

- Keep provider/payment state, local subscription/entitlement state and observed service usage distinct.
- Define trials, grace periods, upgrades/downgrades, failed payments, cancellation and reactivation only where relevant.
- Ask about unresolved customer commitments; do not invent grace periods or silently remove access/data.

### Payment and integration failure boundaries

Decide which system owns each commercial fact and how the application learns that it changed. A provider can confirm a payment while the local entitlement update is still pending. A user redirect can arrive before that update, and a delivered event can be repeated or arrive after a more recent state change. The design must explain what access the application permits during those conditions.

Verify the event's authenticity and actual account/environment mapping before using it. Record enough durable progress to distinguish receiving an event from completing its business effects. If local state changes and remote work cannot commit together, define how interrupted work is found and resumed without repeating a consequential effect. Event deduplication alone does not establish that the intended work finished.

Resolve out-of-order or conflicting information against the source responsible for the fact. Give reconciliation a bounded retry policy and an operator or customer recovery path when it cannot settle the result. A successful checkout redirect is not authoritative proof of paid access.

## Design the operating product

Define usable onboarding and offboarding, including import/export, retention/deletion, integrations and active work.

- Quotas and abuse protection should preserve fair service and an understandable user outcome.
- Assess noisy neighbors, per-tenant attribution and capacity/recovery against actual commitments.
- Enterprise identity, regional hosting, audit export or contractual support belong only when the target customers require them.

Specify customer administration, self-service and support boundaries. Include useful task/activation signals with deliberate privacy/retention. Seek applicable security, governance, reliability and delivery expertise by capability; their absence does not imply readiness or require installation.

## Verify transitions and deliver the requested slice

Connect representative allowed/denied journeys, concurrent/replayed operations, interrupted processing, stale entitlements and tenant closure/recovery to observable outcomes.

Include the actual service/database/provider boundary when making integration claims. Return accepted/proposed contracts, consequential choices, implementation/verification needs and evidence limits.

A design request stops at design; provider accounts, billing configuration and live publication need their own authorized actions.
