# Supporting capability map

Use this map to turn a product need into a capability with requirements. It is not a
vendor catalogue and does not imply that every hosted product needs every row. Select the
rows the product's promises actually depend on.

Columns describe the recurring decision, not an exhaustive checklist. The integration
questions behind failure, tenancy and exit are in
[the integration contract](integration-contract.md).

| Capability | Requirement question | Product consequence | Data and tenancy concern | Failure and exit concern |
| --- | --- | --- | --- | --- |
| Analytics | Which user and tenant actions must be understood, and what decision follows? | Onboarding, retention, pricing and support priorities | Event/person/group identity, PII, cross-tenant aggregation, region | Missing or duplicated events, sampling bias, consent withdrawal, export and deletion |
| Email | Which transactional messages are required, and is marketing consent separate? | Sign-in, invitations, receipts, alerts and campaigns | Recipient data, tenant branding, suppression list, region | Bounce/complaint handling, duplicate sends, deliverability, provider change |
| Observability | Which errors, traces, metrics and business events must be seen, by whom and how quickly? | Detection, diagnosis, recovery and customer communication | Log payloads, PII scrubbing, tenant correlation, access to production data | Sampling and quota loss, alert routing, vendor outage, retention and export |
| Hosting and edge | What must run where, with which build, routing, caching and rollback behavior? | Availability, latency, preview environments and deployment safety | Secrets, environment separation, regional routing, request logs | Quota/limit changes, build lock-in, cache invalidation, DNS and rollback |
| Marketing and social automation | Which external audiences and channels matter, and who approves publishing? | Acquisition, announcements, scheduling and inbox response | Account connection tokens, audience data, content policy, region | Rate limits, platform policy change, scheduling time zones, token revocation |
| Search | Which records must be found, with what relevance, freshness and permission scope? | Discoverability, productivity and support load | Index tenancy, field-level exposure, deletion propagation, region | Stale index, cross-tenant leakage, reindex cost, query limits and exit |
| Queues and background work | Which work must leave the request path, with what ordering, retry and delay? | Reliability, latency and long-running jobs | Payload sensitivity, tenant fairness, job ownership | Poison messages, duplicate effects, backlog growth, replay and migration |
| Notifications | Which channels are required, and what counts as delivered or acknowledged? | Activation, alerts and time-sensitive actions | Contact data, channel preferences, tenant routing, region | Duplicate/late delivery, opt-out enforcement, provider fallback and cost |
| Support | How do customers get help, and how is the conversation and knowledge managed? | Resolution time, trust and retention | Conversation data, attachments, tenant routing, retention | Missed escalation, vendor outage, export and deletion |

The support row covers the helpdesk/conversation capability. Privileged staff access to
customer state and impersonation is an authority decision owned by
`saas-identity-and-access`; a helpdesk integration is not the support-access control.

## Acquisition tendencies by capability

For each selected capability, still apply all eight criteria in
[selection criteria](selection-criteria.md). The table records which shapes usually deserve
comparison and which criteria tend to discriminate; it does not excuse the rest or recommend
a winner.

| Capability | Shapes worth comparing | Criteria that usually discriminate | Defer when |
| --- | --- | --- | --- |
| Analytics | Managed product-analytics service; existing platform analytics; self-hosted analytics | Data/residency, PII, event volume and cost, identity/group model | No product decision depends on the data yet. |
| Email | Managed transactional provider; platform email service; self-hosted mail transfer | Deliverability, bounce/complaint handling, consent/compliance, operational burden | The product has no email promise or a manual path is adequate. |
| Observability | Managed error/trace service; platform monitoring; self-hosted stack | Data sensitivity, volume/retention cost, on-call capability, alert integration | The service has no operator or no detection promise. |
| Hosting and edge | Managed edge platform; infrastructure as a service; self-managed runtime | Residency, build/routing lock-in, rollback, operational burden | The deployment target is already accepted and sufficient. |
| Marketing and social automation | Managed publishing API; direct platform integrations; manual publishing | Coverage, token lifecycle, approval/scheduling needs, vendor maturity | There is no external publishing commitment or volume. |
| Search | Database-native search; managed search service; self-hosted search | Relevance requirement, index tenancy, scale/cost, deletion propagation | Existing database queries meet the actual findability need. |
| Queues and background work | Durable job table; managed queue; self-hosted broker | Delivery/ordering guarantees, replay/DLQ needs, operational burden, cost | Work fits safely in the request path or a simple scheduled job. |
| Notifications | In-product only; managed multi-channel service; platform push/chat integration | Channel promise, consent/opt-out, delivery evidence, fallback and cost | The product has no time-sensitive or external notification promise. |
| Support | Hosted helpdesk; in-product support; shared inbox and process | Customer data exposure, SLA/volume, integration with identity/tenancy, cost | The cohort has no support commitment beyond direct contact. |

## Adjacent capabilities with other owners

| Capability | Owner | Why it is separate |
| --- | --- | --- |
| Billing and entitlements | `saas-billing` | Commercial state, provider events and entitlement decisions carry their own reconciliation and authority rules. |
| Organization and identity access | `saas-identity-and-access` | Membership, enterprise identity, machine credentials and support access define who may act, not which vendor sends a message. |
| Tenancy and lifecycle | `saas-design` | Isolation, customer lifecycle and offboarding are product contracts that every supporting service must preserve. |

## Reading the map

A capability can appear under more than one product feature. Label the requirement by the
outcome it serves rather than by the first screen that needs it: "notify a user that an
import finished" may use in-product notifications, email or both, with different consent
and failure expectations.

Distinguish a capability from a provider. "Search" does not imply a separate search
cluster; a database index may satisfy the requirement. "Queues" does not imply a broker;
a durable job table may be sufficient. The acquisition decision belongs in
[selection criteria](selection-criteria.md).

For each selected row, record the requirement, the chosen shape, the integration owner,
the degraded behavior and the exit path. A capability without an owner is an unowned
failure surface, even when a provider operates it.
