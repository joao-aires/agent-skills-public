# Secret decisions for application configuration

Use this reference with the `application-configuration` method when a value must be protected, delivered, rotated or scanned. It owns the application boundary: how a workload obtains and uses protected material. It is not a vendor secret-manager tutorial, and it does not own the wider credential lifecycle or incident response.

Custody mechanisms differ by provider, but the decisions are portable: classify the material, choose an authority, deliver it through the narrowest channel, test the consumer, and keep evidence without values.

## Classify the material

| Material | Disclosure allows | Typical lifetime | Custody consequence |
| --- | --- | --- | --- |
| User password or recovery code | Account takeover | Long; change on suspicion | Hash in application storage; never reveal or log; reauthentication for sensitive changes |
| Static API key or shared token | Call the issuing API as the holder | Medium to long | Scoped per consumer and environment; rotate with overlap |
| OAuth/client secret | Obtain tokens for a client identity | Medium | Prefer federation where the platform supports it; bind to the exact client |
| Signing key or HMAC secret | Forge or verify claims, webhooks or artifacts | Medium; overlap on rotation | Key identifier plus key material; rotation must preserve verification of retained artifacts |
| Encryption key | Decrypt data or backups | Long; often versioned | Separate from data; retain old decrypt keys while retained data needs them |
| Certificate and private key | Impersonate an endpoint or client | Short; renew before expiry | Renewal covers chain, format and endpoint names; verify reload |
| Connection string | Reach and authenticate to a dependency | Medium | Decompose non-secret host/port from credentials; do not render the whole value into logs |
| Webhook or callback secret | Send accepted events | Medium | Per-endpoint; verify signature and timestamp; rotate with a grace window |

A value that only selects behavior is configuration, even when it is security-sensitive. A value that grants access is a secret. A value that does both should be split.

## Choose custody and delivery

| Channel | Suitable when | Failure modes to design for |
| --- | --- | --- |
| Workload identity / federation | The platform can issue short-lived credentials for the workload | Audience or subject mismatch; trust policy too broad; token unavailable at startup |
| Secret manager SDK at runtime | The workload can authenticate and fetch directly | Store outage; SDK cache; missing reload; secret retrieval in a request path |
| Injected file or volume | The runtime supports protected mounts and the consumer reloads files | Stale mounted content; permissions; accidental inclusion in a backup or image |
| Environment variable | The platform or library only supports it; the value is startup-only | Child-process inheritance, crash dumps, diagnostics, no reload, container inspection |
| Encrypted value in Git (sealed/encrypted secret) | GitOps needs the declaration in the same reviewed repository | Key custody and rotation; decryption key scope; plaintext in history after a mistake |
| Build-time injection | Almost never for runtime credentials | Baked into image layers or build logs; cannot rotate without rebuild |
| Committed plaintext | Never | Permanent history exposure; forks, caches and clones retain it |

Prefer the shortest-lived credential the platform can issue. Prefer direct workload retrieval over routing runtime credentials through CI. Prefer a protected file or identity-based retrieval over an environment variable when the consumer supports it, but choose the mechanism by reload behavior and threat model rather than fashion.

A secret manager is an authority, not automatically a single copy. Several stores can be legitimate when each credential has one declared authority. Uncontrolled copies are the problem.

## Delivery path

```text
workload identity or scoped access
        |
        v
protected store  --->  versioned credential or lease
        |                       |
        |                       v
        |                 authorized consumer
        |                       |
        v                       v
  metadata audit          target dependency
```

The path must answer:

- Which identity may read this secret, for which environment and purpose?
- Is the channel encrypted and access-controlled in transit and at rest?
- Does the consumer fetch directly or receive an injected copy?
- How does the consumer learn that the value changed?
- What is retained in memory, on disk, in a cache or in a crash artifact?
- What happens when the store is unavailable at startup or during reload?

Exclude values from logs, error messages, shell tracing, build arguments, image layers, infrastructure plan/state output, test snapshots and CI artifacts. A masked variable in one tool is not redaction in every downstream system.

## Runtime consumption

- Resolve secrets after configuration validation but before serving dependent traffic; a missing credential should fail readiness, not the first customer request.
- Keep secret values out of the general settings object and its serialization. Use a distinct type or accessor so a debug dump cannot include them accidentally.
- If the runtime caches, set a bound tied to the credential's lease or rotation policy rather than caching forever.
- On rotation, support overlap: accept the new credential, switch consumers, verify authentication, then revoke the old one. Some systems need two valid verification keys during the window.
- For encryption keys, separate the active encrypt key from retained decrypt keys. Revoking a decrypt key can make backups or archived data unreadable.
- On reload failure, retain the last usable credential only within its declared validity; do not extend an expired lease indefinitely.

## Rotation

| Credential | Overlap strategy | Completion evidence |
| --- | --- | --- |
| Password | Create new, distribute, verify sign-in, revoke old sessions as required | New authenticates; old rejected; dependent sessions handled |
| Static API key | Issue second key, move consumers, revoke first | Every consumer uses the new key; first key denied |
| Signing key | Publish new verification key before signing with it | New signatures verify; retained old signatures still verify |
| Encryption key | Introduce new key; re-encrypt or retain old for decryption | New writes use new key; old data remains recoverable |
| Certificate | Renew before expiry; deploy chain and key together | Served chain and hostname valid; consumers reloaded |
| Database credential | Create role/password, update pool, verify connections, drop old | New connections succeed; old credential fails |

Rotation is a state machine, not a single update. Create/set/test/promote may happen in separate invocations, so keep durable version state rather than relying on a local variable. Make retries idempotent and verify the target or credential identity before changing it.

Automated rotation must not rotate the wrong resource. Record which secret, environment and consumer it targets, and stop on an identity mismatch.

## Secret scanning

| Stage | What it can find | Limit |
| --- | --- | --- |
| Pre-commit / staged diff | Accidental credential in the next commit | Bypassed hooks; unstaged or generated files |
| CI working tree | Current source and configuration | Shallow checkout may miss history |
| Full history | Old commits, deleted files, branches | Rewriting history does not revoke access |
| Image and artifact scan | Baked layers, build output, package caches | Runtime-generated files are absent |
| Log and telemetry scan | Printed values, URLs with tokens, crash output | Retention and access to the logs themselves |
| Infrastructure/config repository scan | Rendered manifests, state, encrypted blobs, example files | Encrypted values cannot be judged by content alone |

Use more than one detector where their failure modes differ: known-format matching, provider validity checks and entropy heuristics catch different things. Verify a finding before declaring an incident; a valid-format token may be revoked or a test fixture.

Exceptions need a path, reason, owner and expiry. A repository-wide ignore is not an exception.

When a secret is exposed:

1. Revoke or rotate first; deleting the file does not revoke access.
2. Assess scope and use from provider audit evidence.
3. Remove it from logs, artifacts, caches and reachable history as hygiene.
4. Add a check or narrow rule that would catch the same path, without encoding the incident story into every skill.

## Failure modes

| Condition | Consequence | Design response |
| --- | --- | --- |
| Store unavailable at startup | Workload cannot authenticate | Fail readiness; bounded bootstrap credential or break-glass path with explicit authority |
| Store unavailable during rotation | Old credential remains in use past the intended window | Bound cache/lease; alert; complete rotation when restored |
| Consumer does not reload | New version exists but old is still used | Verify consumer reload, not store update; restart if reload unsupported |
| Secret in environment | Leaks through dumps, child processes or diagnostics | Redact; prefer file/identity; keep out of crash reports |
| Encrypted secret committed with weak key control | Anyone with repo plus key can decrypt | Scope decryption identity; rotate key; treat as custody, not just encoding |
| Broad read policy | One compromised workload reads many secrets | Per-secret, per-environment access; audit and alert on unusual reads |
| Overlap omitted | Rotation causes an outage | Dual-valid window; test cutover and rollback |
| Old decrypt key revoked too early | Backups or archives become unreadable | Retain decrypt keys for the data retention period; separate from access tokens |
| CI receives production credentials | Fork or compromised build exfiltrates them | Environment-scoped federation; no production secrets in untrusted builds |

## Evidence

| Claim | Evidence |
| --- | --- |
| Secret is not in source or artifact | Scan scope and result, including history and built layers where relevant |
| Consumer authenticates with the intended credential | Successful target authentication and, where available, provider audit identity |
| Rotation completed | New version in use, old rejected, consumers reloaded |
| Custody is scoped | Read policy and identity reviewed; access exercise denied outside the intended path |
| Exposure is contained | Revocation confirmed; scope assessed; remaining copies handled |
| Failure behavior works | Store outage or missing credential exercised in a safe environment |

Never include secret values in reports, tickets, logs or evaluation fixtures. Record identifiers, versions, timestamps, status and scope instead.
