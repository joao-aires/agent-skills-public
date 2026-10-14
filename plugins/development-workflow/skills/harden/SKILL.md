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

Read [task guidance](../../TASKS.md). Map the affected data, actors, trust boundaries and valuable actions using security-and-privacy-design and relevant stack guidance. Prioritize evidenced risks rather than running every scanner. Apply bounded fixes within the request and verify ownership/tenant denial, invalid inputs, secret handling and affected behavior. Use vulnerability-management for dependency findings, credential-lifecycle for credential authority and specialist reviews within their coverage. Report residual risks and unverified boundaries. Do not rotate live credentials, rewrite authentication, accept risk, merge or claim legal/security certification without the corresponding scope/evidence.
