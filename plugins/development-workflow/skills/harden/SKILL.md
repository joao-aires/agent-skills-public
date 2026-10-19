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

Read [task guidance](../../TASKS.md). Read [security-and-privacy-design](../security-and-privacy-design/SKILL.md) for security and privacy design, [deliver-reliable-changes](../deliver-reliable-changes/SKILL.md) for verified remediation. Load the optional stack/domain guidance selected by task guidance only when relevant and available.

Map the affected data, actors, trust boundaries and valuable actions using security-and-privacy-design and relevant stack guidance. Prioritize evidenced risks rather than running every scanner. Apply bounded fixes within the request and verify ownership/tenant denial, invalid inputs, secret handling and affected behavior. Use vulnerability prioritization and remediation expertise for dependency findings, credential management expertise for credential authority and specialist reviews within their coverage. Report residual risks and unverified boundaries. Do not rotate live credentials, rewrite authentication, accept risk, merge or claim legal/security certification without the corresponding scope/evidence.
