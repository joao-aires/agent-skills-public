# Security and privacy in design

This reference routes security and privacy work from architecture to the method that owns it. It deliberately does not restate threat modeling, authorization design, privacy analysis or remediation; those methods have their own scope, evidence and failure modes. Read the one that matches the question instead of applying a generic security checklist to the design.

## What design-system owns

Architecture decides, and the security methods then assess in depth:

- **Trust boundaries.** Where untrusted input, a different identity domain or a delegated provider crosses into code we control, and what validates that crossing.
- **Authority placement.** Where the application verifies subject, resource, action and tenant before an effect. Jobs, exports, support tools and AI/tool actions share the requirement even when they have no HTTP route.
- **Data flow and exposure.** Which data classes cross the changed boundary, for what purpose, to which recipient, stored where and retained for how long. Include logs, caches, backups and model providers.
- **Delegation.** What a platform or provider can see and do on our behalf, which credentials it holds and what happens when its terms or capabilities change.
- **Denial and failure behavior.** Fail closed where required, avoid leaking existence or authority through error differences, and keep the user-visible outcome honest.
- **Credential ownership.** Which component holds which credential, for which operations, with what rotation and revocation path. A build-time variable in distributed client code is not a secret.
- **Tradeoffs.** Security against usability, latency, cost, offline capability and recovery. State the accepted risk and who accepted it.

A design that names these without deciding them has not addressed security; it has only listed topics.

## Route the question

| Question | Method |
| --- | --- |
| Abuse cases, trust boundaries, data flow, retention and provider exposure for a feature | [Design security](../../design-security/SKILL.md) |
| Authentication, sessions, federation, passkeys, machine identity, tenant and resource authorization | [Design security](../../design-security/SKILL.md) |
| Applicable legal or contractual obligation, control mapping, assurance evidence | [Run compliance assessment](../../run-compliance-assessment/SKILL.md) |
| Dependency and supply-chain risk, lockfile coverage, update remediation | [Dependencies](../../run-dependency-maintenance/SKILL.md) and installed supply-chain auditing expertise |
| Credential inventory, rotation, vulnerability triage and deployed remediation | [Run security maintenance](../../run-security-maintenance/SKILL.md) |
| Security-focused review of an actual diff | [Security diff review](../../harden/references/security-diff-review.md) |
| Telemetry redaction and collection access | [Observability and monitoring](observability-and-monitoring.md) with the privacy method |

Compliance is not a synonym for security, and neither is established by the other. `run-compliance-assessment` establishes applicability and control evidence; `design-security` establishes the engineering protections. A provider's certification describes the provider, not our service.

## Questions to settle before handoff

- Which new trust boundary does this change create or move, and who validates what crosses it?
- Where is each new action authorized, and does the check use server-derived identity and the actual resource rather than a client-supplied label?
- Which data classes are newly collected, exposed, logged, exported or sent to a provider, and does the accepted purpose and retention cover them?
- What does the user see when the action is denied, the check cannot be evaluated or a provider is unavailable?
- Which credential, key or token is introduced, who can use it and how is it revoked?
- Which security question remains unresolved, and which method or owner will answer it?

Carry the answers into the design record and the affected data-flow views. Do not claim that a design is secure because it mentions security, and do not claim compliance because scans or a provider attestation exist.
