---
name: harden
description: Assess and address security/privacy weaknesses in the supplied feature,
  diff or repository. Use for a scoped hardening task with evidence-backed fixes and
  verification, preserving accepted architecture and task authority.
user-invocable: true
disable-model-invocation: true
metadata:
  scope: generic
  invocation: user
  role: task
---

# Harden

Read [task guidance](../../TASKS.md). Use [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) for verified remediation and seek matching security/privacy expertise when available. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

## Assess and remediate within scope

Trace how untrusted input reaches the valuable action or sensitive data in scope. Identify the actor the application believes it is serving, how that identity was verified, where permission is checked, and which components can read or change the resulting data. Include alternate routes such as background jobs, direct API calls and exports when they reach the same operation.

Use that trace to identify a plausible failure or abuse path and its impact. Prioritize findings that can change access, expose data, corrupt state or prevent an important operation. Scanners can supply evidence about a particular class of weakness; investigate whether a finding applies to the actual application before selecting a fix.

Apply bounded fixes within the request at the component that owns the protection. Verify both the legitimate operation and the attempt that must fail, including relevant ownership/tenant denial, invalid input and secret handling. A hidden control or a rejected frontend action does not establish that the underlying operation is protected. Use vulnerability prioritization and remediation expertise for dependency findings, credential management expertise for credential authority, and specialist reviews within their coverage.

Report residual risks and unverified boundaries. Live credential rotation, authentication rewrites, risk acceptance, merging and legal/security certification each require the corresponding scope and evidence.
