# Diagnostic workflow

## Triage matrix

| Symptom | First checks | Discriminating evidence | Likely boundary |
| --- | --- | --- | --- |
| No pods for a workload | Controller status, desired/ready replicas, events, quota. | Replica-set or job condition versus an admission, quota or scheduling rejection. | Controller, quota or API. |
| Pod `Pending` | Scheduler events, node resources, taints/tolerations, affinity, PVC, quota. | Event text such as insufficient resources, untolerated taint, unbound volume or exceeded quota. | Scheduler, capacity, storage or policy. |
| `ImagePullBackOff` / `ErrImagePull` | Image reference and tag/digest, pull secret, registry reachability, node architecture. | Event detail: auth denied, not found, timeout or platform mismatch. | Registry, credential, network or image identity. |
| `CrashLoopBackOff` | Previous logs, exit code, last termination reason, configuration and probes. | Process exits before serving, or starts and is killed by liveness/OOM. | Application, configuration, resources or probe. |
| Running but not `Ready` | Readiness probe result, startup duration, logs, endpoint membership. | Probe failure detail versus a dependency or application error. | Application, probe or dependency. |
| Ready but requests fail | Service selector and ports, endpoint slices, ingress/gateway, application logs. | Request reaches the pod or fails before it; TLS/status detail. | Service, routing, policy or application. |
| Intermittent timeout | Endpoint count, latency/error signals, retries, dependency health, policy. | One failing peer or path versus broad saturation or packet loss. | Network, dependency, capacity or application. |
| DNS failure | CoreDNS/system pods, search path and `ndots`, NetworkPolicy egress, service name. | In-pod resolution result versus host resolution and policy drops. | DNS, network policy or configuration. |
| Volume not usable | PVC/PV status, storage class, events, attachment, mount path, permissions. | Provisioning, attach, mount, capacity or access-mode failure. | Storage provisioner, topology or workload. |
| Job or CronJob failure | Pod logs, retries/backoff, deadline, concurrency, service account. | Application exit versus deadline, duplicate run, permission or unschedulable pod. | Application, job policy or authority. |
| Node `NotReady` | Node conditions, kubelet/system pods, disk/memory pressure, network. | Pressure or runtime condition with the affected node and time window. | Node, runtime, network or provider. |
| API errors | API server reachability, admission webhooks, CRDs, provider status, RBAC. | Error code and message, webhook failure, throttling or authorization denial. | Control plane, policy or client identity. |

## Command ladder

These are common starting points. Replace placeholders, confirm the context and namespace, and use version-appropriate syntax from the linked documentation.

```bash
kubectl config current-context
kubectl get pods -n <namespace> -o wide
kubectl describe pod <pod> -n <namespace>
kubectl get events -n <namespace> --sort-by=.lastTimestamp
kubectl logs <pod> -n <namespace> -c <container> --timestamps
kubectl logs <pod> -n <namespace> -c <container> --previous
kubectl get deployment,statefulset,daemonset,job,cronjob -n <namespace>
kubectl rollout history deployment/<name> -n <namespace>
kubectl get service,endpointslice -n <namespace>
kubectl get networkpolicy -n <namespace>
kubectl get pvc,pv -n <namespace>
kubectl describe pvc <pvc> -n <namespace>
kubectl get nodes -o wide
kubectl describe node <node>
kubectl auth can-i --list -n <namespace>
```

Some objects, event fields, endpoint APIs and log options depend on version and RBAC. A forbidden response is an access boundary, not evidence that the object is absent.

## Order of discrimination

1. Confirm the context, namespace and object identity. A correct command against the wrong cluster creates a false finding.
2. Read controller and object conditions before pod-level detail. The controller may already name the rejected reason.
3. Read events in time order and compare their timestamps with the symptom window.
4. For a pod, separate scheduling, image, startup, readiness, liveness and termination evidence.
5. Read current and previous logs, including init containers and sidecars. A restarted container's current log may not contain the failure.
6. Check the Service and endpoint path before blaming the application for a connection failure.
7. Check policy, quota, admission and identity before treating a denial as an application defect.
8. Check storage and node evidence before deleting or recreating a stateful resource.
9. For managed clusters, identify which layer the provider owns and which evidence it exposes before claiming a control-plane cause.
10. Stop when one explanation accounts for the observations. Record alternatives that remain possible.

## Evidence capture

```text
Context/cluster/version:
Namespace/object and observed revision:
Symptom, impact and UTC window:
Commands and UTC timestamps:
Observed facts:
Ruled out, with evidence:
Remaining hypotheses:
Mutations and authority:
Next action and owner:
Unavailable evidence or access boundary:
```

Keep this in the incident, change or ticket record already in use; it is not a separate artifact type.

## References

- [Debug pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-pods/)
- [Debug a running pod](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/)
- [Determine the reason for pod failure](https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/)
- [Debug services](https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/)
- [Troubleshoot clusters](https://kubernetes.io/docs/tasks/debug/debug-cluster/)
- [Pod lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)
- [Liveness, readiness and startup probes](https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/)
- [Resource management for pods and containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [DNS for services and pods](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/)
- [Service](https://kubernetes.io/docs/concepts/services-networking/service/)
- [Network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
