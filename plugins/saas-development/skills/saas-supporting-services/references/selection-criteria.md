# Selection criteria for supporting services

Use when a capability needs an acquisition decision. The goal is a defensible choice at
the product's actual scale, not a complete comparison of the market.

## Turn the requirement into constraints

Before comparing candidates, record the facts that would change the answer:

| Fact | Why it changes the choice |
| --- | --- |
| Users, tenants, events or messages, with growth range | Determines whether a free tier, per-unit price or self-hosted baseline is credible. |
| Peak and sustained latency | Separates an interactive dependency from asynchronous work that can queue. |
| Availability and recovery expectation | Sets whether a provider outage must degrade, queue, fail over or block. |
| Data class and sensitivity | Restricts providers, regions, retention and access paths. |
| Tenancy model | Requires per-tenant isolation, credentials, metadata or sharding. |
| Residency and contractual regions | Excludes providers or configurations regardless of feature fit. |
| Team operating capability and on-call | Makes self-hosting a staffing decision, not only a licensing one. |
| Budget shape and unit economics | Distinguishes a fixed platform cost from a usage curve that grows with customers. |
| Exit expectation and customer commitments | Determines export, deletion and parallel-run requirements. |

If a fact is unknown, record the assumption and the cost of being wrong. Do not invent a
volume, a residency requirement or an uptime promise to make a comparison look complete.

## Compare acquisition shapes

| Shape | Suitable when | Main cost or risk | Evidence to seek |
| --- | --- | --- | --- |
| Build in-house | The capability is small, stable and differentiating; the team can own security, failure and evolution. | Engineering and maintenance displace product work; hidden operational burden. | Design for the failure path, not only the happy path; ownership and on-call. |
| Managed provider | The capability is commodity; demand is variable; the provider's limits and contract fit. | Recurring cost, dependency, data location, plan and API changes. | Current docs, contract/DPA, export and deletion behavior, status history. |
| Open-source, self-hosted | Data control, customization or scale economics justify operating it. | Patching, upgrades, capacity, backups, monitoring and expertise. | Version, license, upgrade path, backup/restore, security advisories. |
| Existing platform service | The platform already supplies enough and the product accepts its coupling. | Limited control, feature gaps, migration cost if the platform changes. | Actual plan limits, configuration, isolation, support and exit. |
| Defer | The need is speculative, a manual process is adequate, or a product decision is unresolved. | The workaround becomes permanent without a review trigger. | Named owner, user-visible behavior, review date or trigger. |

A hybrid is common: use a managed provider for delivery while keeping a local queue,
mapping or fallback that preserves the product's contract. State which part is owned
locally and which part is delegated.

## Evaluate the eight criteria

| Criterion | Questions that expose a real difference |
| --- | --- |
| Fit | Does it satisfy the required outcome, not merely a similar feature? Which required behavior is missing, and can the product work around it without changing the promise? |
| Data, privacy and residency | Which data leaves the boundary, for what purpose, to which locations and subprocessors? What retention and access controls apply? Can the product meet its notices and deletion commitments? |
| Identity and integration | How are credentials issued, scoped and rotated? Can the provider express tenant and environment separation? Which API, webhook, SDK or protocol is required, and is it stable? |
| Failure and reconciliation | What happens on timeout, duplicate, late or missing events? Which side is authoritative? How does the product detect drift and recover without repeating effects? |
| Cost | What drives the bill, how does it behave at the expected growth, and who owns the budget? Are there fixed commitments, overage cliffs or egress charges? |
| Compliance | Which obligations and customer commitments apply to this data and processing? Does the provider offer the contract, evidence and configuration needed, within its actual scope? |
| Lock-in and exit | Can data and configuration be exported in a usable form? How long would migration take? What is the parallel-run and cutover path? |
| Operational burden | Who pages, upgrades, patches, rotates secrets and handles provider incidents? Which work moves from the product team to an operator or vendor? |

Cost belongs in the comparison, but a lower visible price can hide integration,
egress, migration and on-call work. Compliance belongs in the comparison, but a provider
certificate or region setting does not cover the application's own controls.

## Decide and record

Choose the smallest sufficient shape that meets the constraints and preserves a credible
exit. Prefer reuse of an already-operated capability when its limits fit; prefer a new
dependency when reusing the old one would distort the product or its isolation.

Record:

- the requirement and the constraints that decided it;
- the considered shapes and why the selected one fits;
- the accepted limits and the unresolved decisions;
- the integration owner and the degraded behavior;
- the exit trigger, export format and review date.

Pilots should use representative data, tenants and failure conditions. A demo that shows
the happy path establishes that the provider can be called, not that the product can
depend on it.

## Avoid comparison theater

A weighted score across every criterion can conceal the one constraint that matters. If a
residency requirement, a customer contract or a recovery target is non-negotiable, apply
it as a gate before scoring. If two candidates remain close, choose on reversibility and
operating ownership rather than on an invented precision.

Do not encode current prices, quotas or plan names as durable guidance. Record the date and
source of any commercial fact, and re-check it when the decision is executed.
