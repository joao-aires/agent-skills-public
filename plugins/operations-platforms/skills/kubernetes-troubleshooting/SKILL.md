---
name: kubernetes-troubleshooting
description: >-
  Expertise and methods for Kubernetes troubleshooting. Diagnose a running Kubernetes workload
  or cluster problem from observed state. Use for pod lifecycle, events, current and previous
  logs, probes, resources and scheduling, DNS and Service endpoints, network policy, storage,
  and control-plane or managed-cluster differences. It does not provision clusters or design
  manifests. It informs the activity that composes it; that activity owns the decision and
  stopping point.
metadata:
  kind: method
  domain: platform
  phase: maintenance
  scope: stack-specific
  stack: Kubernetes
  invocation: both
user-invocable: true
---

# Kubernetes troubleshooting

Diagnose a live or reported Kubernetes problem from the state the cluster actually reports. This method owns evidence gathering, discrimination among plausible failure modes and a precise next action. It does not own manifest, chart or overlay design, cluster provisioning, upgrades or application repair outside the diagnosed scope.

Commands here are starting points, not portable syntax. Field names, log access, event retention, CNI enforcement, storage behavior and control-plane visibility vary by Kubernetes version, distribution and provider. Use current first-party documentation for exact syntax and the installed distribution's guidance for managed components.

## Evidence discipline

Establish the cluster and distribution, version, active context, namespace, affected object, symptom, first and last observation, affected population and recent changes. Identify whether access is read-only or includes a granted mutation, and preserve that boundary.

- Read object status, conditions, events and logs before proposing a cause.
- Record the exact command, context and namespace, UTC timestamp and relevant output. Redact secrets, tokens and personal data.
- Separate reported fact, live observation, inference and unavailable evidence.
- Do not claim a live cluster fact from a manifest, a repository value, another environment or a provider status page.
- A recent deployment or configuration change is a correlation, not proof of cause or remedy.
- Managed control planes may hide etcd, controller and node evidence. Provider diagnostics can fill part of that gap; they do not establish application behavior.

## Diagnostic order

Work from impact and controller evidence toward narrower runtime evidence. Skip a step only when earlier evidence makes it irrelevant, and say so.

| Step | Question | First evidence |
| --- | --- | --- |
| Scope | Which users, workloads and dependencies are affected, and since when? | Workload status, endpoints, alerts, dependent-service symptoms and recent rollout history. |
| Events and conditions | What did the scheduler, kubelet, controllers or admission report? | Namespace and object events in timestamp order; object `status.conditions`. |
| Pod lifecycle | Is the pod scheduled, pulling, starting, running, ready, completing or terminating? | Pod phase, container statuses, restart count, last termination state and waiting reason. |
| Logs | What did the application, init containers and sidecars emit, now and before the last restart? | Current and previous container logs with timestamps and the container name. |
| Probes and traffic | Is it alive but not ready, ready but failing, or restarted by a probe? | Probe configuration and events, readiness transitions, Service endpoints and serving path. |
| Resources and scheduling | Do requests, limits, quota, node pressure, taints, affinity or disruption settings explain the state? | Pod and node descriptions, QoS class, quota and limit ranges, autoscaler and controller events. |
| DNS and network | Does the name resolve, does the Service select the pod, and do policy and routing allow the path? | Endpoint slices, in-pod resolution, Service ports, NetworkPolicy, ingress/gateway status. |
| Storage | Is the volume bound, attached, mounted and writable by the workload identity? | PVC/PV status, storage class, volume attachment, mount and permission evidence. |
| Control plane and nodes | Are nodes, system components, admission or the API healthy? | Node conditions, system-namespace pods, API errors, webhook and provider diagnostics. |
| Change correlation | What changed in the workload, configuration, credentials, policy, CRD, controller or cloud resource? | Revision history, rendered configuration, secret/config version and provider events. |

Use [diagnostic workflow](references/diagnostic-workflow.md) for the triage matrix and command ladder. Use [failure modes](references/failure-modes.md) for the meaning of lifecycle states and common causes.

## Convert evidence into a next action

Stop at a supported diagnosis or a precise evidence gap. Do not prescribe a restart, deletion, probe change or resource increase merely to make the symptom disappear.

- Prefer the least destructive discriminating check. Preserve events and logs before a restart or replacement when practical.
- A rollout restart or pod deletion can mitigate an effect while erasing evidence; label it as mitigation, not cause.
- Mutate only within granted authority. Deleting pods, PVCs or namespaces, changing probes or policy, scaling and failing over have different consequences.
- If the cause is intended-state design, hand off to `kubernetes-resource-engineering`; if data is lost or corrupted, use continuity/disaster-recovery expertise; if customers are affected now, use run-incident-response.
- Verify the result through the original workload path and independent signals, not only a pod becoming Ready.

## Distribution and access limits

- Managed control planes expose different logs and metrics than self-managed clusters. Use the provider's control-plane diagnostics where local inspection is unavailable, and state that boundary.
- NetworkPolicy objects do not prove CNI enforcement. Verify the installed CNI and test the actual direction and peer.
- PVC behavior depends on the provisioner, storage class, topology and access mode; `Pending` is not automatically a storage fault.
- Admission webhooks, controllers and CRDs can mutate or deny requests. An API error may be policy rather than application failure.
- Node-level and host-runtime diagnosis needs host access and provider support. Windows and other runtimes differ.
- Do not transplant commands, paths or guarantees across distributions. Link the version-appropriate Kubernetes documentation for exact syntax.

## Report

Return the symptom and impact, cluster/context/version/namespace, observed facts with their commands and timestamps, the supported interpretation, alternatives ruled out, remaining hypotheses, the safe next action and owner, any mutation and its result, and unavailable evidence. A manifest or a healthy pod is not a substitute for a live cluster observation.
