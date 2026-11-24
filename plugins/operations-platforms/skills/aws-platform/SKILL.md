---
name: aws-platform
description: Design, implement or review AWS workloads across identity, network, compute,
  data, messaging, observability, cost, continuity and edge security. Use for IAM,
  VPC, ECS/EKS/Lambda, RDS/Aurora, S3, SQS/SNS, CloudWatch, budgets, Backup, Route 53,
  WAF and Secrets Manager decisions; verify service detail against current AWS docs.
metadata:
  kind: method
  domain: platform
  phase: cross-phase
  scope: stack-specific
  invocation: both
  stack: AWS
user-invocable: true
---

# Build on AWS without losing the workload

AWS guidance is service-fragmented: IAM, network, compute, data, messaging, observability, cost and continuity each have their own documentation and failure modes. This method owns the common decisions that connect them, and routes the long tail to current service documentation rather than reproducing it.

Establish the workload, its data classification, availability target, operating model, account boundary, region and budget before selecting services. Reuse the organisation's existing accounts, network, identity and tagging standards. Prefer a managed service when it fits the workload and the team can operate its lifecycle; do not add a service merely because it exists.

Use AWS Well-Architected as a review lens, not a certification or a checklist to complete. The pillars — operational excellence, security, reliability, performance efficiency, cost optimization and sustainability — generate questions and risks; they do not prove the workload is well designed.

## Read the identity and account boundary first

| Decision | Establish |
| --- | --- |
| Account structure | Organisation, OU, environment and workload accounts; separation for production and data |
| Human access | Federation, MFA, permission sets, break-glass path; no long-lived root use |
| Workload identity | Role per workload; ECS task role, EKS Pod Identity or IRSA, Lambda execution role, EC2 instance profile |
| Policy layering | Identity policy, resource policy, permission boundary, SCP, session policy; explicit deny wins |
| Cross-account access | Trust policy, external ID or source condition, narrow role, audit trail |
| Secret access | Workload identity to Secrets Manager or Parameter Store; per-secret scope |
| Detection | Access Analyzer, CloudTrail, GuardDuty or the organisation's accepted equivalents |

Policy evaluation is subtle. An explicit deny overrides an allow; an SCP caps what an account can do; a permission boundary caps an identity; a resource policy participates in the same request. Review the effective path for the actual principal, action and resource rather than reading one policy document.

Read [identity and network](references/identity-and-network.md) for the IAM and VPC decision tables.

## Design the network before placing resources

- Plan CIDR with headroom for growth, clusters, endpoints and hybrid ranges; overlapping ranges are expensive to fix.
- Spread subnets across Availability Zones and separate public ingress from private workloads.
- Decide the egress path explicitly: NAT, egress-only gateway, proxy or endpoints. A private subnet without a working egress path fails at the first dependency call.
- Prefer VPC endpoints for high-volume or private AWS service access when they reduce NAT dependency, cost or exposure.
- Use security groups as the primary stateful control; network ACLs are stateless and add a second, easily inconsistent layer.
- Record peering, Transit Gateway and hybrid connections with their route and policy ownership.
- Enable flow logs where the investigation value justifies the volume and retention.

Default VPCs, broad security groups and public buckets are convenience defaults, not architecture.

## Choose compute and data by workload

| Workload signal | Likely fit | Verify before committing |
| --- | --- | --- |
| Short event handler, variable traffic, minimal runtime control | Lambda | Duration, concurrency, cold start, packaging, retry semantics, downstream connection limits |
| Container with a service lifecycle, predictable operations | ECS on Fargate or EC2 | Task networking, load balancing, autoscaling, secrets, logging, image provenance |
| Kubernetes platform and ecosystem requirements | EKS | Add-on lifecycle, node strategy, identity, ingress, upgrade cadence, operational ownership |
| Full host or specialised runtime control | EC2 | Patch ownership, scaling, availability and cost of idle capacity |
| Managed relational workload | RDS or Aurora | Engine/version, Multi-AZ versus replicas, backup/PITR, connection pooling, failover behavior |
| Durable object storage | S3 | Access pattern, retention, versioning, encryption, lifecycle, replication, request/egress cost |
| Queue or pub/sub decoupling | SQS or SNS | Delivery semantics, ordering, visibility, DLQ, idempotency, fanout and filtering |

EKS resource semantics — manifests, charts, probes, controllers, storage and rendered validation — belong to `kubernetes-resource-engineering`. This method owns the AWS account, identity, network, managed-service and operating context around the cluster.

Read [compute and data](references/compute-and-data.md) for detailed tables and failure modes.

## Observe, budget and protect

- Define the signals that represent the workload's outcome, not only host CPU. Use CloudWatch metrics, logs, alarms and dashboards with owners and missing-data behavior.
- Set log retention deliberately. Infinite retention is a cost and privacy decision, not a default.
- Put a budget and anomaly detection on every workload account, and tag for allocation before spend needs to be explained.
- Use AWS Backup plans, vaults and cross-region copies where the recovery objective requires them; a backup plan without a restore drill is a hypothesis.
- Design DNS failover and health checks if availability requires them; a low TTL is not a recovery strategy.
- Put WAF in front of public HTTP entry points where the threat model justifies it, with logging and rule ownership.
- Use Secrets Manager rotation and scoped access for credentials that must exist; prefer short-lived identity where the service supports it.

Read [operations and cost](references/operations-and-cost.md) for the checklists.

## Review with Well-Architected questions

Use the lens proportionally:

| Pillar | Questions worth asking |
| --- | --- |
| Operational excellence | Who owns this? How is it deployed, observed and recovered? What runbook exists? |
| Security | What is the identity, least privilege, encryption, network exposure and detection path? |
| Reliability | What fails, what is the blast radius, what is the recovery objective and has it been tested? |
| Performance efficiency | What is the bottleneck, how does it scale, and what is the measured headroom? |
| Cost optimization | What drives spend, who owns it, and which commitments or architecture changes fit? |
| Sustainability | Is capacity proportionate to demand, and is idle or redundant resource justified? |

Record risks with owners and a decision, not a score. A Well-Architected review is not an audit, a compliance certification or evidence that the workload behaves correctly.

## Keep service detail and reuse disciplined

AWS changes service behavior, quotas, regional availability and pricing. Do not treat any of those as durable facts in guidance or in a design document. Verify the current documentation for the selected region and service before committing a limit, price or feature.

Reuse reviewed material as reference, not as imported instructions:

- `github/awesome-copilot`'s AWS plugin is a reference for Well-Architected review shape, read-only query boundaries and skill decomposition;
- `wshobson/agents`' cloud-infrastructure material is a reference for Terraform module and platform patterns;
- AWS official documentation is authoritative for mechanics;
- an optional read-only AWS MCP server can inspect accounts without mutation, within least-privilege credentials.

Do not acquire action-heavy AWS skills raw, do not reproduce every service, and do not let a reference's provider versions or pricing claims become this collection's defaults. See [reuse and sources](references/reuse-and-sources.md).

## Boundaries

| Concern | Owner |
| --- | --- |
| Infrastructure delivery, IaC choice, GitOps, drift and recovery | `infra-delivery` |
| Kubernetes resource semantics and rendered behavior | `kubernetes-resource-engineering` |
| Pipeline stages, gates, artifact identity and promotion | `ci-cd-pipelines` |
| Release authorization and served-outcome verification | `release` |
| Application configuration and secret consumption | `application-configuration` |
| Capacity, scaling and unit-cost tradeoffs | `analyze-capacity-cost` |
| Backup, restore and data-recovery design | continuity and disaster-recovery design, `guide-runbook` |
| IAM/network threat modeling and credential lifecycle | security design and maintenance capabilities |
| Provider-neutral observability and SLO design | `design-system` observability guidance |

## Report evidence

Separate designed, planned, deployed and observed states. Report the account, region, workload identity, network path, selected services, the checks actually run, and any price, quota or regional claim with the date and source used. State which failure and recovery paths were exercised. A service configuration, a passing IaC plan or a running task is not proof that the workload serves its intended outcome.

## Sources

Primary references; verify the current version and regional availability at use time. Checked 2026-11-16.

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/wellarchitected-framework.html) for review dimensions and design principles.
- [IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) and [VPC overview](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
- [ECS best practices](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/intro.html), [EKS user guide](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) and [EKS best practices](https://docs.aws.amazon.com/eks/latest/best-practices/).
- [RDS user guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html), [Aurora high availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html), [S3 durability](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html).
- [SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) and [SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).
- [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), [Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html), [tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html).
- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html), [Route 53 routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html), [WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html), [Secrets Manager rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).
