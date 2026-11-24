---
name: harden
description: Assess and address security/privacy weaknesses in the supplied feature,
  diff or repository. Use for a scoped hardening task with evidence-backed fixes and
  verification, preserving accepted architecture and task authority.
user-invocable: true
disable-model-invocation: true
metadata:
  kind: activity
  domain: development
  phase: cross-phase
  scope: generic
  invocation: user
---

# Harden

Remove or bound a concrete security or privacy weakness in the requested scope, and stop at verified remediation or a reported gap.

Read [activity system](../activity-system/SKILL.md) for scope and stopping point. Use [verification](../test/SKILL.md) for verified remediation and seek matching security/privacy expertise when available. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

## Assess and remediate within scope

Trace how untrusted input reaches the valuable action or sensitive data in scope. Identify the actor the application believes it is serving, how that identity was verified, where permission is checked, and which components can read or change the resulting data. Include alternate routes such as background jobs, direct API calls and exports when they reach the same operation.

For a security-sensitive diff, read [security diff review](references/security-diff-review.md) for the change-specific checks, removed-code history, blast radius and coverage gaps. Remediation and verification stay in this activity.

Use that trace to identify a plausible failure or abuse path and its impact. Prioritize findings that can change access, expose data, corrupt state or prevent an important operation. Scanners can supply evidence about a particular class of weakness. Investigate whether a finding applies to the actual application before selecting a fix.

Apply bounded fixes within the request at the component that owns the protection. Verify both the legitimate operation and the attempt that must fail, including relevant ownership/tenant denial, invalid input and secret handling. A hidden control or a rejected frontend action does not establish that the underlying operation is protected.

Use vulnerability prioritization and remediation expertise for dependency findings, credential management expertise for credential authority, and specialist reviews within their coverage.

Report residual risks and unverified boundaries. Live credential rotation, authentication rewrites, risk acceptance, merging and legal/security certification each require the corresponding scope and evidence.
