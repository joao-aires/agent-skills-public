---
name: security-and-privacy-design
description: Design, implement or review features with security and privacy built
  into data flows, authorization and integrations. Apply to changes involving identities,
  user data, external inputs, dependencies or new trust boundaries; revisit protections
  as the application evolves.
metadata:
  scope: generic
  invocation: both
  role: support
user-invocable: false
---

# Design secure features

## Start with the changed boundary

Read the feature, architecture and existing security decisions. Identify valuable data/actions, actors, entrypoints and trust boundaries; examine how the change can expose data, bypass authority, exhaust resources or produce unwanted side effects. Keep this proportional: a few documented abuse cases often suffice for a small feature. Use [OWASP threat modeling](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) and relevant cheat sheets for the actual risk. Do not turn every change into an exhaustive audit or claim one was performed.

- Derive identity and tenant context from verified authentication; enforce authorization on server-side reads and writes, including background jobs, exports and MCP/AI tools.
- Validate inputs at boundaries, use parameterized queries and appropriate browser protections, and fail closed when required security configuration is absent.
- Avoid fallback secrets and permissive production defaults.
- Keep privileges narrow and separate environments.
- Bound uploads, expensive queries, external calls and retries to prevent trivial abuse.

## Check meaningful resource operations

Trace an operation across the trust boundary rather than treating every route as an interchangeable read or write. Identify the actor and exact resource, the state in which the action is allowed, the permission required, and the effect that must be recorded. Include what happens when the request conflicts with another change or is repeated after an uncertain result.

Use a small operation matrix when several actions need comparison: actor, exact resource, lifecycle conditions, authority, effect, transaction/history, conflict/retry and user-visible outcome. The purpose is to expose differences in authority and consequences that a generic endpoint checklist would miss.

- Do not assume every resource permits generic CRUD.
- Publishing, finalizing, amending, revoking and correcting can have different authority and retention rules.
- Keep intended state, observed records and authorized transitions distinct.
- Keep business requirements separate from API implementation choices; scope the analysis to affected resources rather than invent a universal workflow engine.

## Collect and retain deliberately

For each new personal-data field or telemetry event, identify its purpose, who needs access, where it flows and how long it is retained.

- Prefer minimal fields, aggregation and redaction over capturing raw messages, audio, tokens or search contents.
- Include providers, logs, analytics, caches, exports and backups in the data flow; check regional storage and transfer requirements against the actual service configuration.
- Do not equate an EU deployment region with legal compliance.

Preserve the application's access, deletion and export behavior across integrations.

- Explain how retention/deletion interacts with immutable backups and restoration, including preventing deleted records from silently returning to active use.
- Check applicable requirements with authoritative sources; escalate unresolved legal/product choices rather than inventing a lawful basis or presenting engineering checks as certification.
- For EU personal data, consult the current [GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

Treat model output and tool arguments as untrusted. Keep authorization outside the prompt; minimize data sent to providers and avoid giving a model broad credentials. Apply the project's AI/tool guidance where relevant.

### Trace credential ownership and recipients

Choose credential ownership from the actual deployment. Distributed client code cannot keep a confidential application secret merely by receiving it through a build variable. User-supplied credentials have different exposure, storage and revocation tradeoffs; they do not automatically require a new server or make remote processing private.

Trace the chosen credential to its recipient and operations, including redirects or delegated processors where relevant. When recipients, purposes or stored access change, reassess the applicable disclosure, authorization and consent basis. An old setup may not cover an expansion, while an ordinary technical edit may need no new prompt.

## Reuse specialists for the actual question

Choose specialist review according to the question:

- Use available security-sensitive differential-review expertise for affected changes.
- Use compatible dependency supply-chain auditing expertise for dependency risk. Check the auditor's declared lockfile coverage, especially for pnpm/yarn, and use ecosystem-native tools when unsupported.

An unassessable result is not a clean bill of health. Neither review replaces feature threat modeling or privacy decisions. Choose further specialist tools only when their scope matches the application and the user request.

## Keep improvements connected to delivery

Translate concrete risks into focused checks: cross-user/tenant requests, invalid or hostile inputs, missing configuration, privileged operations and accidental sensitive logging. Put sustainable dependency/secret checks in CI when warranted, record actual findings and remediation, and define when accepted risks will be revisited. Reassess on new integrations, changed exposure/data use and relevant advisories rather than continuously running an invented background audit.

Keep affected architecture, data-flow, retention and decision notes synchronized with the change. Report what was checked, what improved and what remains uncertain; do not label an application secure or compliant solely because scans pass.

Seek available credential management expertise for identity issuance/rotation/revocation and vulnerability prioritization and remediation expertise for findings through deployed remediation. Keep telemetry redaction and collection access aligned with privacy requirements using observability expertise. These are targeted follow-ups, not prerequisites for every edit.
