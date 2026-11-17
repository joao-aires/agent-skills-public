# AWS compute and data

Decision tables for the `aws-platform` method. Choose compute from the workload's runtime and operating model, then choose data services from access pattern, consistency, retention and recovery. Kubernetes resource behavior belongs to `kubernetes-resource-engineering`; infrastructure delivery belongs to `infra-delivery`.

Verify current limits, engine versions and feature support in AWS documentation. No price, quota or version below is a durable fact.

## Compute

| Signal | Lambda | ECS/Fargate | ECS/EC2 | EKS | EC2 |
| --- | --- | --- | --- | --- | --- |
| Event-driven, short work | Strong | Possible but heavier | Possible | Possible | Poor fit |
| Long-running request or stream | Poor beyond limits | Strong | Strong | Strong | Strong |
| Container ecosystem and scheduling | Limited | Good | Good | Strong | Manual |
| Kubernetes APIs/operators required | No | No | No | Yes | Possible, self-managed |
| Host-level control or specialised runtime | No | Limited | Good | Good | Strong |
| Operational burden | Low | Low to medium | Medium | High | Highest |
| Scale to zero | Yes | Task-level | Task-level | Cluster/node overhead | No |
| Stateful workload | Not suitable | Possible with external storage | Possible | StatefulSets with care | Possible |

Decision rules:

- Lambda fits bounded event processing and HTTP handlers without long-lived connections. Check duration, memory, package size, concurrency, cold start, retry semantics and downstream connection limits before committing.
- ECS fits containerized services without a Kubernetes requirement. Fargate removes node operations; EC2 gives more runtime and cost control with patch ownership.
- EKS fits a genuine Kubernetes platform need: operators, custom controllers, portability or an existing cluster operating model. Do not choose it only because the team knows Kubernetes.
- EC2 fits specialised runtimes, licensed software and full host control; it also means you own patching, scaling and availability.
- Lambda retries are not free idempotency. Event sources differ in retry and duplicate behavior; design consumers accordingly.

## Containers and serverless checks

| Concern | Check |
| --- | --- |
| Image provenance | Immutable digest, trusted registry, scanning, no secrets in layers |
| Identity | Task/execution role or pod identity, not node-wide permissions |
| Configuration and secrets | References to secret stores; no plaintext in task definitions or environment blocks |
| Resource sizing | CPU/memory requests and limits aligned with measured use |
| Health and shutdown | Readiness, liveness where appropriate, graceful drain, termination grace |
| Networking | Correct subnet, security group, load balancer target type and health check |
| Autoscaling | Metric, target, cooldown, minimum capacity and scale-in behavior |
| Deployment | Rolling, blue/green or canary; rollback path and in-flight behavior |
| Observability | Logs, metrics, traces and correlation identity from the runtime |

A running task, a successful invocation or a healthy target group does not prove the service handles its intended traffic.

## Relational data

| Decision | RDS | Aurora |
| --- | --- | --- |
| Engine breadth | Broad engine/version choice | Aurora-supported engines |
| Availability | Multi-AZ instance or cluster | Cluster with writer and readers; failover behavior differs by engine |
| Read scaling | Read replicas | Reader instances and endpoints |
| Storage | Provisioned or autoscaling | Distributed storage managed by Aurora |
| Backup | Automated backups and PITR | Continuous backup to a retention window |
| Connection behavior | Instance endpoint; proxy optional | Writer/reader endpoints; failover changes the writer |
| Operational fit | Predictable managed database | Higher throughput/availability needs and Aurora constraints |

Check:

- engine and version support, upgrade path and extension compatibility;
- Multi-AZ versus read replicas: they solve different problems;
- automated backup retention, PITR window and a restore drill;
- parameter group and option group ownership;
- connection pooling and the maximum connections of the instance class;
- failover behavior, endpoint choice and application retry;
- maintenance window and its effect on the workload;
- encryption, network isolation and credential rotation;
- storage growth and the cost of provisioned headroom.

Aurora failover is not instantaneous and the application must handle a writer change. A read replica is not a backup.

## Object storage

| Concern | Decision |
| --- | --- |
| Access pattern | Frequent, infrequent, archive; retrieval time and minimum duration |
| Consistency | S3 provides strong read-after-write consistency for object operations; list and overwrite behavior still needs application reasoning |
| Versioning | Enable where overwrite/delete recovery matters; understand cost and lifecycle interaction |
| Lifecycle | Transition and expiration rules; incomplete multipart upload cleanup |
| Encryption | SSE-S3 or SSE-KMS by requirement; key policy and cross-account access |
| Public access | Block public access unless a reviewed exception exists |
| Policy | Bucket policy, IAM, ACLs (avoid unless required); least privilege and condition keys |
| Retention | Object Lock only where the compliance requirement is real; understand irreversibility |
| Replication | Asynchronous; versioning prerequisite and failover implications |
| Events | Notification destination, duplicate delivery and consumer idempotency |
| Logging | Server access logs or CloudTrail data events, retention and cost |

A bucket policy that allows `s3:*` on `arn:aws:s3:::*` is not made safe by a private network alone.

## Messaging

| Concern | SQS standard | SQS FIFO | SNS |
| --- | --- | --- | --- |
| Delivery | At least once | Exactly-once processing intent within a message group | At least once to subscribers |
| Ordering | Best effort | Per message group | Not guaranteed |
| Throughput | High, distributed | Constrained by group and region | Fanout, per-subscription delivery |
| Deduplication | Consumer must be idempotent | Deduplication ID or content-based dedupe | Consumer must be idempotent |
| Failure handling | Visibility timeout, DLQ, max receive count | Same, plus group-level blocking | Subscription retry and endpoint behavior |
| Best fit | Work queue with idempotent consumers | Ordered work within a key | Broadcast to multiple consumers |

Check:

- visibility timeout relative to actual processing time, including retries;
- dead-letter queue and an alarm on its depth;
- idempotency key and duplicate window;
- message size and payload claim-check pattern;
- long polling rather than tight receive loops;
- FIFO message-group design: one slow message blocks its group;
- SNS filtering and subscription endpoints; delivery to an unhealthy endpoint is not consumption;
- encryption, access policy and cross-account subscription.

At-least-once means duplicates are normal. An idempotent consumer is required even with FIFO.

## Availability and recovery

| Objective | Mechanism | Verify |
| --- | --- | --- |
| Survive an AZ failure | Multi-AZ deployment, spread subnets, replicated data | Failover exercise or documented provider behavior |
| Survive a region failure | Cross-region backup/replica, DNS or global entry point | Restore or failover drill |
| Recover accidental deletion | Versioning, backup, PITR, Object Lock where required | Restore drill and access path |
| Recover a bad application release | Previous artifact and compatible data | Rollback or forward fix on the target |
| Recover a credential compromise | Revocation, rotation, audit | Old credential denied; scope assessed |

A backup is not a recovery strategy until a restore has been exercised. Cross-region replication is asynchronous; state the acceptable data-loss window.

## Failure modes

| Condition | Symptom | Check |
| --- | --- | --- |
| Lambda timeout or concurrency ceiling | Dropped or throttled events | Duration, reserved concurrency, downstream limits, retry policy |
| Lambda duplicate delivery | Repeated side effects | Idempotency, event source semantics, DLQ |
| ECS task cannot reach dependency | Health check fails or requests time out | Security group, subnet route, endpoint, DNS, task role |
| EKS add-on or version skew | Pods fail after a cluster upgrade | Add-on compatibility, API deprecations, node drain |
| Database connection exhaustion | Intermittent connection errors under load | Pool size, max connections, proxy, scale |
| Aurora writer change | Writes fail during failover | Endpoint use, retry/backoff, DNS TTL |
| S3 public exposure | Data reachable outside the intended boundary | Public-access block, bucket policy, ACL, account-level block |
| SQS visibility too short | Duplicate processing while a message is retried | Visibility timeout versus processing time |
| FIFO group blocking | One failing message stalls a key | Group design, DLQ, retry policy |
| Backup unrestored | Recovery objective unproven | Restore drill, permissions, cross-account/region copy |

## Evidence

| Claim | Evidence |
| --- | --- |
| Compute handles the workload | Load or event test at representative shape, with timeouts and retries observed |
| Identity is per workload | Task/pod/function role and a denied cross-workload action |
| Data is durable | Backup/PITR configuration plus restore result |
| Failover works | Exercised or provider-documented behavior with application retry |
| Queue is reliable | Duplicate and poison-message handling, DLQ alarm |
| Storage is private | Public-access review and denied external access |
| Cost is attributable | Tag coverage and a cost view, with the date checked |

Distinguish configured, deployed and observed behavior. A successful deployment is not a capacity or recovery test.
