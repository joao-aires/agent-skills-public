---
name: application-configuration
description: Design, implement or review how an application loads, validates and changes
  configuration and secrets across local, CI and production targets. Use for source
  precedence, typed settings, environment parity, runtime reload, multi-tenant defaults,
  feature-flag boundaries, secret delivery, rotation and scanning.
metadata:
  kind: method
  origin: local
  pack: sdlc
  domain: development
  phase: cross-phase
  scope: generic
  invocation: both
  role: support
user-invocable: true
---

# Own configuration as a typed contract

Configuration is the part of application behavior that is decided per target rather than per build. Secrets are the subset whose disclosure grants access or decrypts data, so they need separate custody, rotation and evidence. Both are interfaces: declared keys, types, defaults, requiredness and failure behavior, not an unstructured bag of environment variables.

Establish the requested boundary first: design a new surface, implement or change an existing one, review a target's effective configuration, or audit custody and exposure. Reading or diagnosing does not authorize a live change, a credential rotation or a secret reveal. Keep the application artifact independent of its environment so the same build can run locally, in CI and in production.

## Map the configuration surface

Find every source that can set a value before choosing a precedence rule. A key with two owners and no declared conflict rule is a defect waiting for an environment.

| Layer | Typical content | Required property |
| --- | --- | --- |
| Built-in defaults | Safe non-secret behavior for an ordinary run | Documented; no environment-specific address, identity or credential |
| Committed configuration | Shared behavior, non-secret limits and endpoints | Reviewable, schema-validated, safe to share |
| Deployed configuration | Target endpoints, capacity, dependency names, security-sensitive switches | Environment-owned; delivered through the accepted target path |
| Runtime overrides | Operational tuning, staged exposure, emergency controls | Bounded, observable, owned and expiring where temporary |
| Secrets | Passwords, tokens, keys, certificates, connection strings | External custody; never in the layers above |

Resolve precedence explicitly and once. Prefer a small ordered set such as defaults, committed file, target configuration, then a narrow runtime override, with a documented rule for conflicting sources. Do not rely on whichever library or shell exports last. Record the winning source by name in diagnostics, never the value.

Environment variables are a transport and a deployment convention, not a data model. Parse them into a typed settings object at one boundary. Variables inherited from a shell, a container image or a CI runner are not evidence that the deployed target received the intended value.

## Type and validate at the boundary

Choose one authoritative schema for the merged result. Generate documentation, environment examples and, where practical, typed accessors from it so the contract cannot drift into three hand-maintained lists.

- Validate type, range, enum, format, length and cross-field consistency. A port, timeout and URL path can each be individually valid while the combination is unusable.
- Distinguish required, optional and defaulted values. Do not let an empty string impersonate absence.
- Validate the merged result, not each source in isolation; a valid file can still produce an invalid combination.
- Run the same validation in tests, local startup, CI configuration checks and the deployed target. CI can validate that every required key is supplied and that examples parse; only the target proves the values are the intended ones.
- Fail before serving traffic. Report key, source and violated constraint, never the secret value.
- Exercise missing, malformed, conflicting and target-specific cases, not only a complete happy-path file.

Strict rejection of unknown keys catches typos that silently disable behavior. Permissive forward compatibility lets an older application ignore a newer key. Choose by who owns the file and whether mixed versions coexist, rather than applying one default everywhere.

## Keep configuration and secrets distinct

Classify by consequence, not by convenience.

| Class | Test | Storage and review |
| --- | --- | --- |
| Non-sensitive behavior | Disclosure is harmless | Versioned configuration, ordinary review |
| Security-sensitive configuration | Not secret alone, but changes exposure or authority — auth mode, trusted origins, allowlists, TLS settings, log redaction | Protected review and target authorization; not hidden in a secret store where it becomes unreviewable |
| Secret | Disclosure grants access, signs, decrypts or impersonates | Secret manager or workload identity; metadata and rotation tracked; never in diffs, logs or artifacts |
| Derived material | Short-lived token, signature or session derived from a secret | Generated at runtime; not persisted as configuration |

Do not promote a value into a secret store merely because it is inconvenient to review, and do not move a credential into configuration because the secret path is awkward. A secret that also selects behavior — a connection string containing a host and credentials — should be decomposed so the non-secret part remains reviewable. Read [secrets](references/secrets.md) for custody, delivery, rotation, scanning and failure decisions.

Credential lifecycle authority remains with the installed security maintenance capability; this method owns how the application consumes the result. Identity and authorization decisions remain with the identity capability.

## Make environments comparable

Parity means the same keys, schema and shape, not the same values. Differences should be deliberate and visible.

- Keep one schema and one key vocabulary across local, CI, staging and production. Environment-specific values belong to the target; environment-specific code paths do not.
- Provide a local example containing key names and safe placeholders. A working production secret in an example file is a leak, not onboarding.
- Give CI only the configuration and credentials its stage needs. Fork or untrusted pull-request builds must not receive production or publication secrets.
- Build the artifact configuration-free. The same immutable artifact is promoted; the target supplies values and credentials.
- Do not let production configuration exist only as console edits. Deliver it from reviewed source or an authorized operator path with an audit trail.
- Compare environments by key set, schema version and source, never by revealing secret values. A missing key and a deliberately different value are different findings.

Feature-flag targeting legitimately differs by environment. Record it as intentional rather than forcing flag parity.

## Decide reload behavior

Startup-only configuration is a valid, simpler choice: a change then requires a restart or rollout. Reload is justified when a restart is too costly or a control must change faster than a deployment. Either way, define the observable effect.

| Change | Suitable mechanism | Evidence required |
| --- | --- | --- |
| Target address, dependency identity, resource shape | Restart or rollout | New revision serves; old and new values were not mixed |
| Bounded operational tuning | Atomic reload with validation | Old and new values observed; in-flight work remains correct |
| Credential rotation | Overlapping credentials, then revoke the old | Consumers authenticate with the new value; old access is rejected after cutover |
| Staged exposure | Flag evaluation | Intended audience sees the new path; kill path works |

A reload must validate before swapping, apply as one version, invalidate consumer caches and expose which version is active. Watching a mounted file, polling a store and receiving a push all fail differently: a store update is not evidence that the consumer noticed it. Bound retries and keep the last known good version when a reload fails, but fail closed for security-relevant settings. Never half-apply a change or let one failed key leave a mixed configuration.

## Resolve multi-tenant configuration

Derive the tenant from verified identity and application membership, not solely from a client-supplied header, path segment or query parameter. Then resolve the intended layering, for example platform defaults, plan or entitlement, tenant override, and a bounded operational override.

- Declare precedence and conflict behavior. A tenant override must not silently erase a mandatory platform or safety setting.
- Validate tenant configuration when it is written and again when it is loaded. One malformed tenant override must not break other tenants or fall back to another tenant's values.
- Isolate tenant secrets, keys, storage prefixes, rate limits and quotas. Cache entries must include tenant identity and configuration version.
- Treat entitlements as product/authorization state, not as an unstructured flag. A tenant's plan is not proof that a client may call a paid operation.
- Keep per-tenant limits enforceable in the serving path; a stored number alone is not enforcement.
- Bound the number and size of tenant overrides so configuration does not become an unaudited extension of the database.

## Separate feature flags from configuration

| Question | Configuration | Feature flag |
| --- | --- | --- |
| Lifetime | Durable target behavior | Temporary exposure decision |
| Ownership | Service or platform owner | Named owner with a removal condition |
| Variation | Environment and tenant values | Audience or cohort targeting |
| Failure | Invalid value blocks startup or reload | Declared default and kill path |
| Authority | Can influence behavior, not permission | Never authorization or entitlement |
| Retirement | Changed through reviewed configuration | Flag and its dead code path are removed |

A flag needs a purpose, audience, default, evaluation-failure behavior, tested relevant states and an expiry or removal trigger. Test the states that matter — on, off and the interaction with tenant or plan — rather than every combination. Prefer a tested kill path over an untested matrix. Do not use flags as a permanent substitute for configuration, and do not leave retired branches in the serving path.

## Define failure behavior

Decide what happens before an incident forces the choice:

- Missing required value: fail fast before readiness, naming the key and expected source.
- Invalid value: fail with the constraint and source; do not coerce silently.
- Secret unavailable or expired: fail closed for authentication and authorization; allow only bounded, explicitly designed degradation elsewhere.
- Reload failure: retain the last known good version, emit a signal and keep serving only if that state is safe.
- Unknown key: reject or warn according to the declared compatibility policy, not library accident.
- Tenant failure: isolate the affected tenant and deny or use a safe documented default; never substitute another tenant's configuration.
- Optional value absent: use a documented default whose safety has been reviewed.

A fallback that restores service by disabling authentication, signature verification or tenant checks is an outage of a different kind.

## Detect exposed secrets

Scanning is detection, not custody. Cover the stages where material can escape: the working tree and staged diff, CI history and pull-request content, built images and artifacts, generated configuration, logs and telemetry, and infrastructure/configuration repositories.

- Verify findings before declaring an incident; entropy alone produces noise, while a known credential format still needs scope and validity checked.
- Keep exceptions narrow, owned and expiring. A blanket path exclusion hides the next leak.
- A finding is not closed by deleting a file or rewriting history. Revoke or rotate the credential, then clean the remaining copies and artifacts as needed. Revocation is the security action; history cleanup is hygiene.
- Never print suspected values in the report. Record location, type, status and remediation.

Hand an exposed credential to incident response when impact is live, and use installed security maintenance guidance for the credential lifecycle.

## Report evidence

Return the configuration contract and the actual evidence, separating what was authored from what a target observed:

- keys, types, defaults, requiredness, owners and the declared precedence;
- environment matrix showing which keys are supplied where, deliberate differences and gaps;
- schema, startup and negative-case results, with the commands that produced them;
- reload or rotation exercise: what changed, which version became active and how consumers responded;
- secret scan scope, findings and exceptions, without values;
- secret custody and rotation metadata, without values;
- unresolved target authority, unreachable providers and unverified live behavior.

A schema pass, a rendered ConfigMap, a green CI check or a manager update proves only its own stage. It does not prove that the running target loaded the intended value or that a rotated credential is in use.

## Composition

Use installed guidance by capability; absence changes the depth, not the outcomes above.

| Need | Capability |
| --- | --- |
| Release boundary, target authorization and served-state verification | `release` |
| Repository layout, local setup, examples and configuration checks | `project-conventions` |
| Security-sensitive choices, trust boundaries and data exposure | `security-and-privacy-design` |
| Credential inventory, rotation, revocation and scanning operations | `security-maintenance` |
| Identity, sessions, tokens and tenant authority | `security-auth-development` |
| Environment separation, artifact identity and gate design | `ci-cd-pipelines` |
| Selected provider's configuration and secret-store mechanics | `tooling-conventions` |
| Kubernetes ConfigMap/Secret consumption and workload reload | `kubernetes-resource-engineering` |
| Infrastructure-delivered configuration and desired-state reconciliation | `infra-delivery` |
| AWS-native configuration and secret services | `aws-platform` |
| Signals that reveal effective configuration and failed reloads | `observability` |
| Behavior tests for startup, reload and tenant isolation | `test` |

## Sources

These are primary references for constraints, not project authority. Checked 2026-11-16.

- [The Twelve-Factor App: Config](https://12factor.net/config) establishes environment-based configuration and strict separation from code. It does not define a schema, precedence among target sources or secret custody.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) covers custody, distribution, rotation and exposure response.
- [Kubernetes ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) and [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) documentation describe consumption and reload limits; [good practices for Secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/) states that base64 encoding is not encryption.
- [OpenFeature specification](https://openfeature.dev/specification/) defines provider-neutral flag evaluation concepts; it does not define this application's audience, defaults or authority.
- [CWE-798](https://cwe.mitre.org/data/definitions/798.html) covers hardcoded credentials; [NIST SP 800-57 Part 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) provides key-management vocabulary.
