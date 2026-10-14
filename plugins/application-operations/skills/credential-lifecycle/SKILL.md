---
name: credential-lifecycle
description: Inventory, issue, rotate, revoke, and retire operational secrets, API
  keys, deploy keys, service-account credentials, and certificates, including response
  to leaked credentials.
metadata:
  scope: generic
  invocation: both
  version: '2.0'
  role: task
---

# Credential lifecycle

Maintain one authoritative credential record and a complete map of its consumers. Credential values belong in protected stores, not the report.

## Modes and architecture

In interactive work, explain identity/delivery tradeoffs and resolve ownership and cutover decisions. For setup, implement least-privilege identity and secret delivery in the chosen stack; during feature work review new consumers, privileges and reload behavior. For recurring reviews inspect metadata, expiry, secret references and audit findings; prepare policy-bounded changes without exporting values. Rotate/revoke automatically only when the job explicitly authorizes the affected consumers and verified provider procedure.

Consult [references/secrets-architecture.md](references/secrets-architecture.md) for industry-grounded design, runtime/CI delivery, rotation and recovery for deeper implementation details when needed.

## Discover and document

Read local secret-management instructions and actual references in deployment, CI, integrations, and secret synchronization. Identify provider, account/tenant, environment, purpose, permissions, owner/deputy, authoritative store, consumers, expiry/rotation, and distribution mechanism.

Use [references/credential-record.md](references/credential-record.md) for metadata and scenarios. If ownership or consumers are unknown, investigate references and audit metadata; absence of recent use alone is not proof that retirement is safe.

## Standards

- Issue purpose-bound least-privilege credentials. Separate runtime pull/read access from build push/write or administrative access.
- Prefer a supported scoped workload/app identity or short-lived token over a shared long-lived human credential for automation.
- Include system, scope/tenant, purpose, and environment in names where confusion is possible.
- Maintain one authoritative record shared through appropriate permission boundaries; avoid duplicate copies masquerading as sources of truth.
- Document automatically rotated credentials and the mechanism even when their values are managed elsewhere.
- Record expiry and renewal lead time, with an owner and deputy. For certificates inspect chain, validity, key/store format, and dependent trust configuration.
- Protect values during CLI/API handling. Do not print them, put them in tickets, enable shell tracing around them, or treat base64 as encryption.
- Prefer short-lived workload federation/dynamic leases where supported; validate issuer, audience and subject/target restrictions. Removing a workload does not necessarily revoke an issued credential.
- Generate secrets with a cryptographically suitable provider, encrypt transport/storage, audit metadata-only access and test manager outage/break-glass recovery.
- Keep secrets out of source, images/build layers/arguments, Terraform state outputs and unrestricted artifacts. Kubernetes Secret encoding alone is not encryption or adequate access control.

## Rotate planned credentials

1. Map all consumers, synchronization hops, propagation delay, and reload/restart behavior.
2. Establish a replacement with equivalent required scope, using provider-supported overlap when available.
3. Update the authoritative store and its distribution mapping; avoid hand-edited copies that will be overwritten.
4. Verify each consumer actually loads and uses the replacement. Check authentication, runtime image pulls, CI access, and downstream business completion as applicable.
5. Revoke the old credential after verified migration under the provider's rotation procedure. If overlap is impossible, coordinate a bounded cutover.
6. Update metadata and expiry tracking, and remove obsolete distributed copies/temporary files.

Track partial migrations explicitly; a successful secret update does not prove the running service reloaded it.

## Respond to exposure

Revoke or rotate the exposed access promptly and follow the local security incident process. Record scope and exposure window without reproducing the value. Check use/audit history and all distributed copies.

Remove the value from current files, logs, artifacts, and other affected stores. Repository history cleanup is a separate coordinated operation; it does not invalidate the secret. Check scanner syntax for the installed version, preserve default detection, use narrowly justified false-positive exceptions, and rescan a fresh checkout.

History rewriting needs an explicit scope, protected backup, collaborator coordination, and verification of protected/latest commits and remote references. Do not routinely disable hooks or force-push as part of scanning.

## Retire and report

For obsolete credentials, verify consumers are migrated/removed, revoke provider access, remove distribution references, and retain required audit metadata. Report metadata-only status: discovered, issued, migrated, verified, revoked, or blocked; identify outstanding consumers and owners.
