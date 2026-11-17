# Kubernetes failure modes

Use this reference after the scope and symptom are established. The same state can have different causes across versions, CNIs, storage provisioners and managed distributions; treat each explanation as a hypothesis to discriminate.

## Pod lifecycle

| Observed state | Meaning to verify | Distinguishing evidence | Common causes | Avoid |
| --- | --- | --- | --- | --- |
| `Pending` | The pod is accepted but not placed on a node. | Scheduler events, node allocatable resources, taints/tolerations, affinity/topology, PVC binding, quota. | Insufficient resources, unschedulable constraints, unbound volume, quota, admission delay. | Assuming a node or application fault without reading scheduler events. |
| `ContainerCreating` | The sandbox or volumes are being prepared. | Events for volume attach/mount, image pull, CNI or secret/config mount. | Slow volume attach, image pull, CNI setup, missing secret/config. | Deleting the pod before the preparation error is captured. |
| `ImagePullBackOff` / `ErrImagePull` | The kubelet cannot obtain the image. | Event message, image reference, pull secret, registry reachability, node architecture. | Wrong name/tag/digest, missing or expired credential, registry policy, network, platform mismatch. | Treating a mutable tag as proof that the intended image is running. |
| `CrashLoopBackOff` | A container exits and is restarted with backoff. | Last termination reason, exit code, previous logs, configuration, probe events. | Application error, missing dependency/config, failed migration, OOM kill, liveness kill. | Reading only the current log after the failing process has restarted. |
| Running, not `Ready` | The process runs but is excluded from ready endpoints. | Readiness probe result, startup duration, dependency health, endpoint slices. | Probe too strict or wrong port/path, slow startup, dependency unavailable, application degradation. | Disabling the probe to make the pod look healthy. |
| `Completed` | The main container exited successfully. | Exit code, job/controller condition, output durability. | One-shot job success, or a process intended to run continuously exited. | Treating process exit as proof that the job's external effect completed. |
| `Evicted` | The kubelet reclaimed the pod under pressure. | Pod status reason/message, node conditions, disk/memory/PID pressure. | Node resource pressure, ephemeral-storage exhaustion, policy. | Increasing limits before identifying which resource caused eviction. |
| `OOMKilled` | A container was killed for exceeding a memory boundary. | Last termination reason, limit, working-set behavior, node pressure. | Limit too low, leak, burst, runtime overhead, sidecar/init contribution. | Raising the limit without measuring the actual pattern. |
| `Terminating`, stuck | Deletion is waiting on finalizers, graceful shutdown or volume detach. | Finalizers, `deletionGracePeriodSeconds`, preStop/termination grace, volume attachment, controller events. | Slow drain, finalizer, stuck volume, unreachable node. | Force-deleting without understanding data or controller consequences. |
| `Unknown` | The API cannot currently reach the node/kubelet. | Node conditions, kubelet/system pods, network and provider status. | Node or network failure, kubelet problem, provider maintenance. | Reporting an application failure when the node is unreachable. |

## Probes and startup

| Observation | Interpretation to test | Next evidence |
| --- | --- | --- |
| Probe gets connection refused | Process not listening yet, wrong port or wrong container. | Probe target, container port, startup timing and logs. |
| Probe gets an application error or unauthorized status | The endpoint works but is not a valid health signal. | Probe path/auth contract and application dependency state. |
| Probe times out | Slow initialization, event-loop/thread starvation, network or overload. | Probe timeout versus actual latency, CPU throttling and dependency latency. |
| Pod restarts at a regular interval | Liveness may be killing a busy or temporarily degraded process. | Liveness timing, failure events and whether the process recovers on its own. |
| All replicas restart together | A shared dependency, config rollout or liveness policy may be implicated. | Rollout history, shared config/secret and dependency timeline. |
| Startup probe never succeeds | Initialization is genuinely too slow or blocked. | Startup logs, init containers, dependencies and readiness behavior. |
| Ready, then removed from endpoints | Readiness is failing after serving began. | Readiness event, dependency health and endpoint slice changes. |

Startup probes protect initialization; readiness controls traffic eligibility; liveness restarts a locally unrecoverable process. A probe change is a behavioral change, not a neutral diagnostic action.

## Scheduling and resources

- Requests drive scheduling; limits constrain runtime. Compare both, plus init/sidecar requests and the node's allocatable capacity.
- CPU throttling can look like application latency; memory limits can produce `OOMKilled` without node pressure.
- Ephemeral-storage exhaustion may evict pods even when CPU and memory look adequate. Tmpfs consumes memory rather than disk.
- Taints, affinity, topology spread, node selectors and PVC topology can make capacity unusable even when total free capacity exists.
- ResourceQuota and LimitRange can reject creation or force defaults. A pending pod with adequate nodes may be blocked by quota or admission.
- PodDisruptionBudgets constrain voluntary eviction, not scheduling or every involuntary failure.
- Cluster autoscaling may be bounded by node groups, quotas, availability zones or scale-up latency. A pending pod does not prove the autoscaler is broken.
- Priority and preemption can explain why a lower-priority workload waits while another runs.

## Service, DNS and network

| Symptom | Check first | Common cause |
| --- | --- | --- |
| Service has no endpoints | Selector/labels, pod readiness, target port, namespace. | Selector mismatch, unready pods, wrong port name/number. |
| Connection refused at a Service | Endpoint slices, pod listening port, Service port mapping. | No healthy endpoint, wrong target port, process not listening. |
| Name does not resolve in a pod | CoreDNS/system pods, service name and namespace, search path/`ndots`, egress policy. | DNS component failure, wrong name, search-path surprise, blocked egress. |
| Some peers reach a service, others do not | NetworkPolicy peers and direction, CNI enforcement, namespace labels. | Additive policy, missing DNS/egress allowance, label or namespace selector mismatch. |
| External traffic fails but in-cluster works | Ingress/Gateway status, class, TLS, backend service, controller logs. | Routing/controller issue, certificate, backend mismatch. |
| Intermittent timeouts | Endpoint count, retries, conntrack, proxy, dependency latency, policy. | One bad endpoint, saturation, packet loss or retry amplification. |

NetworkPolicy is additive. A permissive rule in another policy can defeat the intended restriction, and denying egress without allowing DNS breaks name resolution. An object's presence does not prove the CNI enforces it.

## Storage

- `Pending` PVC: missing or unsupported storage class, no provisioner, insufficient capacity, topology mismatch, access mode, quota or delayed binding.
- Attach or mount failure: volume attachment conflict, multi-attach with a non-shared access mode, node/CSI problem, filesystem or permission mismatch.
- A mounted volume can still be read-only, full or owned by an unexpected identity. Check the workload's write path, not only the PVC phase.
- StatefulSet volume claim templates and retention policy determine what survives pod replacement. Deleting a PVC can destroy the only copy.
- A successful mount does not prove application-consistent data or a recoverable backup.

## Nodes, control plane and managed clusters

- Node `NotReady` can come from kubelet, container runtime, disk/memory/PID pressure, network or provider maintenance. Read node conditions and system-namespace pods before blaming workloads.
- API errors, throttling, admission-webhook failures and controller backlog can look like application failures. Check the error code and the layer that returned it.
- Managed control planes expose different logs, metrics and node access than self-managed clusters. Use provider diagnostics and state which evidence is unavailable locally.
- Provider maintenance, node-image upgrades and add-on lifecycle can change behavior without a workload deployment.
- Do not infer control-plane health from a single application failure, or application health from a healthy control plane.

## Configuration and change

- ConfigMap or Secret updates are not automatically reloaded by every application. Environment variables, `subPath` mounts and mounted-file refresh behave differently.
- A mutable image tag can point to a different artifact than the one reviewed. Prefer immutable identity when the evidence depends on it.
- CRD, controller and admission-webhook changes can alter validation, defaults or reconciliation without a workload diff.
- Expired credentials, rotated secrets, service-account token projection and RBAC changes can produce authorization failures that look like application bugs.
- Job retries, concurrency policy and deadline settings can duplicate or suppress work. Process success is not the same as durable external effect.

## What looks like what

| Appearance | Alternative explanation to rule out |
| --- | --- |
| Application timeout | DNS, NetworkPolicy, missing endpoint, proxy or dependency saturation. |
| Pod crash | Liveness kill, OOM kill, failed init container or configuration error. |
| Service outage | Empty endpoints, wrong target port or unready pods rather than a dead application. |
| Storage failure | Scheduling, topology, quota or attachment rather than the provisioner alone. |
| Node failure | Provider maintenance or network partition rather than a workload defect. |
| Permission denied | RBAC, admission policy, expired token or wrong service account. |
| Recent deployment caused it | Pre-existing drift, dependency change or capacity trend that the deployment exposed. |

## References

- [Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- [Liveness, readiness and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Assigning pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [Taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [Node conditions](https://kubernetes.io/docs/concepts/architecture/nodes/)
- [DNS for services and pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Storage classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [Debug services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
