# AWS operations and cost

Checklists for the `aws-platform` method: observability, cost allocation, backup, DNS, edge security, secret rotation and the Well-Architected lens. Verify prices, quotas, regional availability and feature support in current AWS documentation; they are not durable facts and are intentionally absent here.

## Observability

| Signal | Establish | Failure if skipped |
| --- | --- | --- |
| Metrics | The metric that represents the user outcome, its dimensions and aggregation | Healthy hosts while requests fail |
| Alarms | Threshold or anomaly, evaluation periods, missing-data behavior, owner | Alert storms or silent failure |
| Logs | Group, retention, structure, correlation identity, redaction | Unbounded cost or no evidence |
| Dashboards | Audience and decision, not every available metric | Pretty screens with no operational use |
| Traces | Sampling, service identity and propagation across async work | Cannot locate the slow or failing boundary |
| Composite alarms | Dependency-aware health where a single metric misleads | Duplicate pages for one incident |
| Cross-account observability | Central log/metric destination and access | Per-account blind spots |

Alarms need an owner and a response. An alarm with no runbook or destination is a notification, not an operating control. Custom metrics and high-cardinality dimensions have cost implications; design dimensions for decisions.

CloudWatch is not the only valid choice. If the organisation uses another observability platform, this method still owns the AWS signals that must be exported or queried.

## Cost

| Capability | Use | Check |
| --- | --- | --- |
| Cost Explorer | Explore spend by service, account, tag and time | Data latency; it is not a billing system of record |
| Budgets | Threshold and forecast alerts per account/workload | Owner, action and whether the budget includes commitments |
| Anomaly detection | Unexpected spend pattern | Baseline, seasonality and alert routing |
| Cost allocation tags | Attribute spend to workload, environment and owner | Tags must be activated; activation is not always retroactive |
| Cost categories | Map accounts/services to business structures | Maintenance as the organisation changes |
| CUR / Data Exports | Detailed, queryable cost and usage at scale | Storage, schema and refresh latency |
| Savings Plans / Reserved capacity | Reduce steady-state cost | Coverage, utilization, term, expiry and break-even |
| Split cost allocation | Container-level allocation for ECS/EKS | Feature/service coverage limits; opt-in |
| Unit economics | Cost per customer, order, request or tenant | Allocation keys are judgement calls |

A tag schema is part of the platform contract: required keys, allowed values, owner and enforcement. Untagged or shared cost needs an explicit allocation rule, not an unexplained remainder.

Do not optimize a cost line without connecting it to reliability, performance, security and contractual constraints. A cheaper architecture that misses the recovery objective is not an improvement.

## Backup and continuity

| Element | Establish |
| --- | --- |
| Scope | Which resources are protected, and which are deliberately excluded |
| Plan | Schedule, retention, lifecycle and copy to another region/account |
| Vault | Access policy, lock where required, encryption key |
| Recovery objective | RPO/RTO per workload, not one number for everything |
| Restore | Who can restore, where, how long, and how the application is validated |
| Dependencies | Identity, network, DNS, keys and secrets needed to use restored data |
| Drill | Last exercised restore and the result |

AWS Backup coverage differs by service. A resource being "managed by AWS" does not mean it is in a backup plan. Backups also need protection from deletion; a compromised account can delete both data and backups if the vault policy permits it.

## DNS and edge

| Concern | Decision |
| --- | --- |
| Hosted zone | Public, private or both; ownership and delegation |
| Routing policy | Simple, weighted, latency, failover, geolocation or multivalue; match the actual objective |
| Health check | Endpoint, protocol, interval, failure threshold and dependent behavior |
| TTL | Low enough for recovery, high enough to avoid query cost and instability |
| Certificate | Region and endpoint scope; renewal and chain |
| WAF | Managed rule groups, rate-based rules, bot control, custom rules; logging and false-positive review |
| Origin protection | Restrict origin access so WAF cannot be bypassed by direct addressing |
| Logging | WAF logs, access logs and retention |

A DNS failover record does not make a stateless application stateful-safe or move data. It changes where traffic is sent. WAF rules need an owner and a review path; an unmanaged managed-rule update can change behavior.

## Secrets

| Need | Approach |
| --- | --- |
| Workload credential | Prefer short-lived role credentials from the workload identity |
| Secret that must persist | Secrets Manager with scoped access and rotation where supported |
| Configuration parameter | Parameter Store; distinguish String, StringList and SecureString |
| Cross-account secret | Resource policy, KMS key policy and narrow principal |
| Rotation | Lambda or service-managed rotation, overlap, consumer reload and verification |
| Break-glass | Protected, audited and tested path independent of the primary store |
| Exposure | Revoke/rotate first, assess use, then clean copies |

Secrets Manager and Parameter Store have different features, limits and cost models. Choose by requirement, not by which name appears first in a tutorial. Base64 or encrypted-at-rest storage does not remove the need for access control.

Application-side consumption, precedence and reload belong to `application-configuration`; the wider credential lifecycle belongs to security maintenance.

## Well-Architected lens

| Pillar | Review question | Evidence |
| --- | --- | --- |
| Operational excellence | Can the team deploy, observe, diagnose and recover this without a hero? | Runbook, deployment record, alarm response |
| Security | Who can access what, and how is that detected? | Effective policy, denied path, logging |
| Reliability | What fails, what is the blast radius, and what recovery was tested? | Failure exercise, restore result, RTO/RPO |
| Performance efficiency | What is the measured bottleneck and headroom? | Load test or production signal |
| Cost optimization | What drives spend and who owns the tradeoff? | Allocation view, budget, decision record |
| Sustainability | Is idle or redundant capacity justified? | Utilization and demand evidence |

Use the lens to generate a small set of risks with owners. Do not present a questionnaire score as an audit result or a compliance claim.

## Failure modes

| Condition | Symptom | Check |
| --- | --- | --- |
| Alarm without owner | Incident discovered by a customer | Alarm destination, runbook, escalation |
| Missing-data treated as healthy | Silent outage | `treatMissingData` and evaluation behavior |
| Log retention infinite | Surprise cost and data exposure | Retention per group, redaction, archive |
| Tag coverage gap | Cost cannot be attributed | Required tags, activation, untagged-cost rule |
| Budget without action | Alert ignored | Owner, threshold, documented response |
| Backup outside the plan | Resource unrecoverable | Coverage inventory and restore test |
| Backup deletable by the workload account | Ransomware or mistake removes recovery | Vault lock, cross-account copy, least privilege |
| DNS failover to an unhealthy target | Traffic moves but service does not recover | Health check semantics and dependency readiness |
| WAF bypassed by direct origin | Edge rules ineffective | Origin access control and network restriction |
| Rotation without reload | New secret exists; workload uses old | Consumer reload and old-credential denial |

## Evidence

| Claim | Evidence |
| --- | --- |
| Workload is observable | Signal, alarm, owner and a triggered or simulated alert |
| Cost is attributable | Tag coverage and an allocation view with the date |
| Backup is usable | Restore performed and application validated |
| Failover works | Exercise or documented behavior plus application retry |
| Edge protection is effective | Denied direct-origin request and reviewed WAF logs |
| Secret rotation works | New credential in use; old denied; consumer reloaded |
| Well-Architected risks are owned | Risk list with owner, decision and follow-up |

Report checked, configured, deployed and verified states separately. A console setting or a passing review is not an exercised recovery path.
