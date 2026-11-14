# Credential record

```text
System / account or tenant / environment:
Purpose and credential type:
Non-secret identifier or fingerprint:
Owner / deputy:
Permissions and intended boundaries:
Authoritative protected-store reference:
Consumers and distribution paths:
Expiry / rotation mechanism / renewal lead time:
Creation or rotation procedure reference:
Reload behavior and verification per consumer:
Old credential revocation evidence:
Retirement condition / next review:
```

## Naming examples

- Store item: `<system>: "<scope> / <purpose> / <environment>" - <credential-type>`.
- Secret variable: `REGISTRY_REGION_TENANT_PULL_TOKEN`, `GH_APP_ID_PRIVATE_KEY`, or `SERVICE_ENV_CLIENT_CERT`, adapted to project conventions.
- Service account: `<tenant>.<service>.<environment>` where the provider supports that convention.

Provider IDs, installation IDs, public fingerprints, and metadata are distinct from secret values. Private keys and tokens remain protected. If a vault's collection is the permission boundary, share the same item across authorized collections and record one accountable owner.

## Acceptance scenarios

1. **Rotate a registry token used by CI and runtime clusters.** Expect consumer inventory, separation of push/pull privileges where appropriate, authoritative-store propagation, actual consumer verification, and old-token revocation.
2. **A scanner reports an API key in old commits.** Expect prompt revocation/rotation, exposure/audit review, cleanup separated from invalidation, narrow false-positive handling, and no credential reproduced in the report.

## Architecture reference

Read [secrets-architecture.md](secrets-architecture.md) for design, distribution, industry grounding and recovery. Store references are metadata; values remain in protected stores.
