# AWS identity and network

Decision tables for the `aws-platform` method. IAM and VPC are the two boundaries most AWS changes cross, so establish them before choosing compute or data services. Verify current behavior in the linked AWS documentation; policy evaluation and service support change.

## Account and organisation model

| Model | Shape | Fit | Trade-off |
| --- | --- | --- | --- |
| Single account | Everything in one account | Experiment, tiny non-production estate | Broad blast radius; weak cost and access separation |
| Environment accounts | Separate development, staging and production | Most production workloads | Cross-account access and shared services need deliberate design |
| Workload accounts | Account per workload or bounded domain | Strong isolation and ownership | More accounts, guardrails and central services |
| OU-based | Organisation units group accounts by policy | Many accounts with shared controls | SCP mistakes apply broadly; OU design needs care |
| Control-tower-style landing zone | Centralised accounts, logging, guardrails | Regulated or multi-team estates | Setup complexity; central team dependency |

Establish at least: where production data lives, which account can read it, where logs and backups go, and how a break-glass identity is reached. Account IDs are configuration and evidence markers; never credentials.

## Human and machine identity

| Principal | Preferred mechanism | Avoid |
| --- | --- | --- |
| Human operator | Federation with MFA and short-lived permission sets | Long-lived IAM users, shared accounts, routine root use |
| CI/CD job | OIDC federation to a scoped role | Static access keys stored in CI |
| ECS task | Task role | Credentials in the task definition or image |
| EKS workload | EKS Pod Identity or IRSA, according to cluster version and current support | Node instance role shared by every pod |
| Lambda function | Execution role | Embedded keys or a broad shared role |
| EC2 instance | Instance profile with a narrow role | Long-lived keys on disk |
| Cross-account automation | Assume-role with trust conditions | Sharing a role secret across accounts |
| Break-glass | Protected, audited, time-bound role | Permanent administrator identity |

Use one role per workload and environment. A role shared by unrelated workloads turns one compromise into many and makes least privilege impossible to reason about.

## Policy layering

| Layer | Applies to | What to check |
| --- | --- | --- |
| SCP | Accounts in an OU | Maximum available permissions; it does not grant access |
| Permission boundary | An identity | Maximum permissions for that identity |
| Identity policy | User or role | Allowed actions and resources |
| Resource policy | Bucket, queue, key, topic, function, secret | Cross-account or service principal access |
| Session policy | A temporary session | Further restriction on an assumed role |
| Explicit deny | Any layer | Overrides every allow |

Review the effective request: principal, action, resource, condition and account. Common mistakes are an allow on `Resource: "*"`, a trust policy that lets any account assume the role, a condition that checks a header but not the intended source, and a policy that passes review while an SCP or boundary silently removes the permission.

Conditions worth using where they fit: `aws:SourceAccount`, `aws:SourceArn`, `aws:PrincipalOrgID`, `aws:PrincipalArn`, MFA, VPC endpoint, and a specific role session name. Do not copy a condition without verifying that the request actually carries the key.

## Workload identity decisions

| Question | Consequence |
| --- | --- |
| Which AWS principal does the workload use? | Determines audit identity and blast radius |
| Is the credential short-lived? | Reduces exposure but does not remove the need for scope |
| Can another workload in the same cluster/account assume it? | Shared node roles and broad trust policies leak identity |
| Does the workload need cross-account access? | Requires trust policy and often a second role |
| How is the secret delivered? | Prefer identity and SDK retrieval over injected static keys |
| What happens on rotation? | Session validity, SDK refresh and consumer reload must be understood |

EKS identity is a separate decision from node identity. A pod that inherits the node role can reach every permission the node has; use the cluster's supported workload identity mechanism and verify the service account-to-role binding.

## VPC design

| Decision | Establish | Failure if skipped |
| --- | --- | --- |
| CIDR | Private range with headroom for subnets, clusters, endpoints and hybrid | Overlap forces re-architecture |
| Availability Zones | At least two for production; three where the objective requires | Single-AZ outage |
| Subnet tiers | Public ingress, private application, isolated data, plus endpoint subnets where used | Unintended public exposure or no egress |
| Egress | NAT, egress-only gateway, proxy or VPC endpoints | Private workloads cannot reach dependencies |
| Endpoints | Gateway and interface endpoints for high-volume or private services | NAT dependency, data transfer cost, public path |
| Security groups | Stateful allow rules by reference and least privilege | Broad CIDR ingress and drift |
| Network ACLs | Stateless rules only where a second layer is justified | Asymmetric ephemeral-port blocks |
| Routing | Route tables, peering, Transit Gateway, VPN/Direct Connect | Black-holed or asymmetric paths |
| DNS | Private hosted zones, resolver rules, endpoint DNS | Name resolution differs from the tested path |
| Logging | Flow logs, retention, destination | No evidence for an investigation |

Security groups are stateful: return traffic is allowed automatically. Network ACLs are stateless: both directions and ephemeral ports need explicit rules. Most application connectivity problems are security-group references, missing routes or DNS, not the absence of an ACL.

## Common topology

```text
internet
   |
 WAF / load balancer
   |
 public subnets (ingress only)
   |
 private application subnets  ---> VPC endpoints / NAT ---> AWS services
   |
 isolated data subnets
```

Adapt the layers to the workload. A serverless application may have no VPC at all; a Lambda in a VPC needs the routes and endpoints its dependencies require. A public subnet is not required for a private service behind a load balancer.

## Failure modes

| Condition | Symptom | Check |
| --- | --- | --- |
| Overly broad role | Any compromised workload can read data or change infrastructure | Effective policy, trust policy, unused-access findings |
| Missing endpoint or route | Private workload times out reaching S3, SQS, Secrets Manager or a registry | Route table, endpoint policy, security group, DNS |
| NAT dependency | Egress works until NAT capacity, cost or AZ failure | Endpoint coverage and NAT AZ redundancy |
| CIDR exhaustion | New subnets or pods cannot get addresses | Current allocation and growth |
| Security-group drift | A manual rule opens a path | Drift comparison and IaC ownership |
| Public bucket or database | Data exposed through misconfiguration | Public-access block, policy, subnet and security group |
| Cross-account trust too broad | Another account assumes the role | Trust policy conditions and CloudTrail |
| Shared node role | Pods inherit node permissions | Workload identity binding and service account |
| DNS mismatch | Works from one network, fails from another | Resolver rules, private zone association, endpoint DNS |
| Flow logs absent | Cannot reconstruct the path during an incident | Log destination and retention |

## Evidence

| Claim | Evidence |
| --- | --- |
| Access is least privilege | Effective policy review plus allowed and denied requests from the actual principal |
| Workload identity is scoped | Role trust, service account binding and a denied cross-workload attempt |
| Network path works | Connection from the actual subnet/security group to the dependency, with DNS and route checked |
| Network is private | Public exposure review and a denied external connection |
| Cross-account access is bounded | Trust conditions, external ID or source account, audit record |
| Change is delivered as code | Declared revision and target comparison, not only console state |

A policy document that looks narrow is not evidence that the effective permission is narrow. Exercise the deny path.
