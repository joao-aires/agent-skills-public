# Dated vendor notes

**Reviewed:** 2026-11-16. **Basis:** public documentation only; no accounts, paid plans,
consoles or reliability tests were used. Prices, quotas, plan gating and regional
availability were not verified and are not recorded as durable facts.

These notes describe integration mechanics to investigate. They are not a recommendation,
a ranking or a substitute for the account's current terms. Re-check the provider's
documentation, contract and actual configuration at the point of commitment.

| Provider | Capability area | Main integration questions |
| --- | --- | --- |
| PostHog | Product analytics, flags, experiments, replay | Event and identity taxonomy, region, PII, self-host parity, flag evaluation |
| Resend | Transactional email | Domain authentication, bounce/complaint webhooks, idempotency, suppression |
| Sentry | Error and performance monitoring | Environment DSNs, release/source maps, sampling, PII scrubbing, quotas |
| Cloudflare Pages | Hosting and edge | Build configuration, previews, functions, rollback, plan limits, routing lock-in |
| Hetzner | Infrastructure as a service | Region, network, firewall, snapshots, API token scope, managed-service gaps |
| Supabase | Postgres-centric backend platform | Row-level security, auth, storage, pooler, migrations, backup/PITR |
| Zernio | Social and marketing publishing | Account connection, scheduling, webhook verification, token rotation, coverage |

## PostHog

Public docs cover product analytics, session replay, feature flags and experiments.
Events, persons and groups form the identity model; funnels, retention and insights are
derived from that model. US and EU cloud regions exist, and self-hosting is offered with
some feature differences.

Verify before use:

- the event taxonomy and the group key that represents an organization/tenant;
- where persons are identified and how anonymous-to-identified merging behaves;
- PII in event properties, URLs, replay masks and reverse-proxy configuration;
- the actual data region, retention and deletion behavior for the selected plan;
- whether flags and experiments are evaluated server-side or client-side, and how
  exposure is recorded.

A product analytics tool is not an audit log or a billing meter. Confirm that the events
used for product decisions are not also being treated as authoritative financial or
security records.

## Resend

Public docs cover transactional email, domain verification, templates, webhooks and
idempotency keys. Domain authentication involves SPF, DKIM and DMARC records; delivery,
bounce and complaint events arrive through webhooks.

Verify before use:

- which domain and From/Reply-To identities are authorized for which environment;
- how bounces, complaints and suppressions are received and applied to future sends;
- whether an idempotency key is supported for the send path and how long it is retained;
- rate limits, shared versus dedicated IP behavior and the provider's current plan terms;
- how unsubscribe and marketing consent are handled separately from transactional mail.

Deliverability is not guaranteed by correct DNS records. The sender remains responsible
for consent, content, list hygiene and applicable email law. Test the bounce and complaint
path, not only successful delivery.

## Sentry

Public docs cover error events, releases, source maps, tracing, sampling, quotas, spike
protection, PII scrubbing and alert rules. A DSN identifies the project and environment.

Verify before use:

- a distinct DSN and project per environment, with release and source-map upload in the
  build;
- sampling and quota behavior, including what is dropped when the quota is reached;
- PII scrubbing for request bodies, headers, user identifiers and breadcrumbs;
- alert ownership and routing, including cron or heartbeat monitors where used;
- retention and access for the selected plan, and the difference between SaaS and
  self-hosted feature parity.

Error monitoring observes failures; it does not establish that a customer journey
succeeded. Keep business outcome evidence separate from error volume.

## Cloudflare Pages

Public docs cover Git integration or direct upload, build configuration, preview
deployments, Pages Functions, custom domains, headers/redirects and rollbacks. Pages
Functions run on the Workers runtime; Cloudflare also documents Workers static assets as
an alternative for new projects.

Verify before use:

- build command, output directory, environment variables and secret handling per
  environment;
- whether preview deployments are protected and whether they can reach production data;
- function bindings, runtime limits and request/response size limits;
- custom domain, DNS, TLS and redirect behavior, including apex and www handling;
- rollback behavior and whether a previous deployment remains addressable;
- current plan limits for builds, files, requests and functions.

Hosting choices create coupling at the build and routing layer. Keep the build reproducible
outside the provider where the exit path matters, and test a rollback rather than assuming
the dashboard button restores the previous behavior.

## Hetzner

Public docs cover cloud servers, volumes, private networks, load balancers, firewalls,
snapshots/backups, API tokens and regions. Hetzner Cloud and dedicated/Robot products are
separate offerings with different APIs and terms.

Verify before use:

- the region and availability-zone behavior that the product's residency or recovery
  promise depends on;
- server type, volume, snapshot and backup coverage, including restore testing;
- private network and firewall rules, and whether the default exposure is acceptable;
- API token scope, rotation and the actions each token can perform;
- the managed-service gap: databases, queues, object storage and observability may need
  separate providers or self-operation.

A lower infrastructure price does not include the operational work of patching, backup
verification, monitoring and failover. Record who owns that work.

## Supabase

Public docs cover Postgres, row-level security (RLS), Auth, Storage, Edge Functions,
Realtime, migrations, connection pooling and backups/PITR. It is a platform around
Postgres, not a transparent proxy to a self-managed database.

Verify before use:

- RLS enabled on every exposed table and policy behavior tested for each role and tenant;
- the service-role key's blast radius, storage and server-only use;
- connection pooler mode and its interaction with migrations, prepared statements and
  long-running jobs;
- migration workflow and schema drift between local, preview and production;
- backup/PITR availability and restore procedure for the selected plan;
- extension availability, project pause behavior and current limits.

RLS is a common breach path when a policy is missing or a service key bypasses it. Test
cross-tenant reads and writes through the actual client path, not only in the dashboard.

## Zernio

Public docs describe a single API for social posting, scheduling, inbox and ads across
multiple platforms, with API-key authentication, webhooks, SDKs and agent-oriented
tooling. The public material is comparatively young and some coverage claims are
inconsistent across pages.

Verify before use:

- which platforms and actions are actually supported for the account, at the time of use;
- how platform accounts are connected, which tokens are stored and how they are rotated or
  revoked;
- scheduling behavior across time zones, approvals and platform rate limits;
- webhook authenticity, retry behavior and event ordering;
- content policy, platform review requirements and failure handling when a post is
  rejected;
- export, deletion and what happens to scheduled content if the relationship ends.

Treat coverage, reliability and commercial terms as unverified until tested against the
actual account and platforms. Do not make this provider the product's only path for a
customer-critical announcement without an exit and a fallback.

## Using these notes

For each provider, record the exact documentation page, retrieval date and the account plan
that was inspected. A public doc page can describe a feature that the account cannot use.
When the decision depends on a contractual term, read the agreement rather than the
marketing page.

No note here establishes security, residency, compliance or availability for a particular
deployment. Those conclusions require the actual configuration, contract and exercised
behavior.
