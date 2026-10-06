---
name: design-secure-features
description: Design, implement or review features with security and privacy built into data flows, authorization and integrations. Apply to changes involving identities, user data, external inputs, dependencies or new trust boundaries; revisit protections as the application evolves.
---

# Design secure features

## Start with the changed boundary

Read the feature, architecture and existing security decisions. Identify valuable data/actions, actors, entrypoints and trust boundaries; examine how the change can expose data, bypass authority, exhaust resources or produce unwanted side effects. Keep this proportional: a few documented abuse cases often suffice for a small feature. Use [OWASP threat modeling](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html) and relevant cheat sheets for the actual risk. Do not turn every change into an exhaustive audit or claim one was performed.

Derive identity and tenant context from verified authentication; enforce authorization on server-side reads and writes, including background jobs, exports and MCP/AI tools. Validate inputs at boundaries, use parameterized queries and appropriate browser protections, and fail closed when required security configuration is absent. Avoid fallback secrets and permissive production defaults. Keep privileges narrow and separate environments. Bound uploads, expensive queries, external calls and retries to prevent trivial abuse.

## Collect and retain deliberately

For each new personal-data field or telemetry event, identify its purpose, who needs access, where it flows and how long it is retained. Prefer minimal fields, aggregation and redaction over capturing raw messages, audio, tokens or search contents. Include providers, logs, analytics, caches, exports and backups in the data flow; check regional storage and transfer requirements against the actual service configuration. Do not equate an EU deployment region with legal compliance.

Preserve the application's access, deletion and export behavior across integrations. Explain how retention/deletion interacts with immutable backups and restoration, including preventing deleted records from silently returning to active use. Check applicable requirements with authoritative sources; escalate unresolved legal/product choices rather than inventing a lawful basis or presenting engineering checks as certification. For EU personal data, consult the current [GDPR text](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

Treat model output and tool arguments as untrusted. Keep authorization outside the prompt; minimize data sent to providers and avoid giving a model broad credentials. Apply the project's AI/tool guidance where relevant.

## Reuse specialists for the actual question

Use installed `differential-review` for security-sensitive changes and `supply-chain-risk-auditor` for dependency risk. The auditor supports particular lockfiles; check its declared coverage, especially for pnpm/yarn, and use ecosystem-native tools when unsupported. An unassessable result is not a clean bill of health. Neither skill replaces feature threat modeling or privacy decisions. Choose further specialist tools only when their scope matches the application and the user request.

## Keep improvements connected to delivery

Translate concrete risks into focused checks: cross-user/tenant requests, invalid or hostile inputs, missing configuration, privileged operations and accidental sensitive logging. Put sustainable dependency/secret checks in CI when warranted, record actual findings and remediation, and define when accepted risks will be revisited. Reassess on new integrations, changed exposure/data use and relevant advisories rather than continuously running an invented background audit.

Keep affected architecture, data-flow, retention and decision notes synchronized with the change. Report what was checked, what improved and what remains uncertain; do not label an application secure or compliant solely because scans pass.
