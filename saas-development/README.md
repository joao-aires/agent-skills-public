# SaaS development plugin: tenancy, commercial state and the operating product

The `saas-development` plugin carries the product-level contracts a hosted product needs beyond authentication and a subscription form: who the tenant is, what the customer bought, who may administer it, which supporting services it depends on, what operators can see, and whether a specific rollout is ready.

It does not implement authentication, billing-provider SDKs, dashboards, infrastructure or release. Those belong to the selected stack and the established delivery authority.

## Purpose

Use this package when a hosted-product decision crosses identity, commercial and operating boundaries. Each method owns one contract; together they keep the tenant model, paid access, organization authority and scoped readiness from collapsing into one another.

## Conceptual model

| Question | Owner |
| --- | --- |
| Who is the customer, what is the tenant boundary, and how does the lifecycle transition? | [saas-design](skills/saas-design/SKILL.md) |
| What did the customer buy, and what does the product permit right now? | [saas-billing](skills/saas-billing/SKILL.md) |
| Who belongs to the organization, what may they do, and how is that revoked? | [saas-identity-and-access](skills/saas-identity-and-access/SKILL.md) |
| Which non-differentiating capabilities must exist, and how are they integrated? | [saas-supporting-services](skills/saas-supporting-services/SKILL.md) |
| What should customers and operators see and do in the dashboard? | [saas-dashboard-design](skills/saas-dashboard-design/SKILL.md) |
| Is this launch or customer cohort ready against its actual commitments? | [saas-readiness](skills/saas-readiness/SKILL.md) |

Four facts stay separate throughout: the tenant and its lifecycle, the commercial promise and entitlement, organization authority, and observed evidence. Provider objects are evidence for those facts, not replacements for them.

## Responsibilities

| Skill | Type | Owns | Stops at | Not for |
| --- | --- | --- | --- | --- |
| [saas-design](skills/saas-design/SKILL.md) | method | Customer and organization lifecycle, tenancy model, isolation, tenant context, closure and migration | A hosted-product contract and transition rules | Billing-provider mechanics, authentication libraries or framework choice |
| [saas-billing](skills/saas-billing/SKILL.md) | method | Plans, prices, entitlements, trials, upgrades, dunning, cancellation, refunds, tax and provider-event reconciliation | A commercial and entitlement contract with provider mapping | General ledger, legal tax advice or organization roles |
| [saas-identity-and-access](skills/saas-identity-and-access/SKILL.md) | method | Membership, roles, invitations, ownership transfer, SSO/SCIM, machine identity, support access, tenant isolation and revocation | An organization authority model with reviewable grants | Sign-in, session or policy-enforcement mechanics |
| [saas-supporting-services](skills/saas-supporting-services/SKILL.md) | method | Capability map, build/buy/adopt/defer decision, integration contract, failure behavior and exit | A requirement-led acquisition and integration contract | Billing, identity or the product's differentiating architecture |
| [saas-dashboard-design](skills/saas-dashboard-design/SKILL.md) | method | Customer and operator dashboard information architecture, metrics meaning, tables, actions, tenant context and interface states | Decision-oriented dashboard design and acceptance needs | Generic visual system, framework components or server-side enforcement |
| [saas-readiness](skills/saas-readiness/SKILL.md) | method | Commitment-to-evidence trace for a named cohort, gap classification and prioritized next actions | A scoped verdict with precise gaps | Universal enterprise checklist or release authorization |

## How it materialized

| Model element | Implementation |
| --- | --- |
| Lifecycle and tenancy | [lifecycle](skills/saas-design/references/lifecycle.md), [multi-tenancy](skills/saas-design/references/multi-tenancy.md) |
| Commercial state and provider events | [entitlements](skills/saas-billing/references/entitlements.md), [provider events](skills/saas-billing/references/provider-events.md), [provider notes](skills/saas-billing/references/provider-notes.md) |
| Organization and delegated authority | [organization model](skills/saas-identity-and-access/references/organization-model.md), [enterprise identity](skills/saas-identity-and-access/references/enterprise-identity.md), [support access](skills/saas-identity-and-access/references/support-access.md) |
| Supporting-service requirements and integration | [capability map](skills/saas-supporting-services/references/capability-map.md), [selection criteria](skills/saas-supporting-services/references/selection-criteria.md), [integration contract](skills/saas-supporting-services/references/integration-contract.md) |
| Dashboard decisions | [dashboard decisions](skills/saas-dashboard-design/references/dashboard-decisions.md) |
| Inspected starters, limits and pins | [sources](references/sources.md) |

## Reading paths

1. **New hosted product** → [saas-design](skills/saas-design/SKILL.md) for tenant and lifecycle → [saas-identity-and-access](skills/saas-identity-and-access/SKILL.md) → [saas-billing](skills/saas-billing/SKILL.md) → [saas-supporting-services](skills/saas-supporting-services/SKILL.md).
2. **Launch or customer rollout** → [saas-readiness](skills/saas-readiness/SKILL.md) for the cohort and evidence trace → the owning method for each gap.
3. **Paid access defect** → [saas-billing](skills/saas-billing/SKILL.md) for provider, entitlement and usage reconciliation → [saas-design](skills/saas-design/SKILL.md) if the lifecycle rule is wrong.
4. **Enterprise or support request** → [saas-identity-and-access](skills/saas-identity-and-access/SKILL.md) for organization authority and revocation → [saas-readiness](skills/saas-readiness/SKILL.md) when a commitment is being claimed.
5. **Customer or operator surface** → [saas-dashboard-design](skills/saas-dashboard-design/SKILL.md) for task and data semantics → the frontend interface method for visual and interaction refinement.

## Boundaries

- **Authentication and security.** Sign-in, sessions, enforcement mechanics, privacy and threat modeling belong to the `sdlc` security methods (`design-security`, `run-security-maintenance`). This package decides organization authority and tenant isolation requirements.
- **Product and architecture.** Product direction, service boundaries, data contracts and release authorization belong to `sdlc` and the domain packages. SaaS methods consume those decisions.
- **Pricing and packaging.** `design-business-model` in `strategy` decides the pricing metric, packaging and economic model before the SDLC; `saas-billing` owns the commercial and entitlement state that implements an accepted model. Live price changes need the relevant authority.
- **Commercial lifecycle.** `saas-design` owns tenant lifecycle and closure; `saas-billing` owns plan, entitlement and payment transitions, including dunning, cancellation and refund mechanics. A transition that changes tenant access must be reconciled across both.
- **Frontend and infrastructure.** Dashboard visual craft belongs to frontend design; hosting, queues and observability implementation belong to their platform packages.
- **Readiness scope.** `saas-readiness` assesses a named cohort against actual commitments. It does not certify a universal maturity level or authorize release.
- **Evidence.** Inspected open-source starters are research examples. They do not establish that a pattern meets a particular product's security, accessibility or operating requirements.

## Authority and optional tools

The package declares no MCP servers and no provider accounts. Contacting a customer, changing a price, issuing a refund, enabling SSO, migrating a tenant or publishing a readiness verdict requires scope from the request and the relevant authority. Legal, tax and formal compliance determinations remain outside it.

## Maintenance

Owning sources are `skills/*/SKILL.md`, their references and [sources](references/sources.md). Update this README when the responsibility split, a provider note or the boundary with security and frontend changes. Validate with `scripts/validate_plugins.py`, `scripts/check_collection.py` and the repository tests.
