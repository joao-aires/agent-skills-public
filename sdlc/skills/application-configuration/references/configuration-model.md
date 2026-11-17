# Configuration model decisions

Stable decision tables for the `application-configuration` method. Use this reference when the open question is source precedence, schema strictness, parity, reload, tenant layering or failure behavior. Secret custody and rotation are in [secrets](secrets.md).

## Source precedence

| Model | Resolution | Use when | Cost or failure mode |
| --- | --- | --- | --- |
| Single environment store | One source supplies every key | Small service; one deployment shape | Local and CI need a parallel mechanism; no reviewable shared defaults |
| Layered | Built-in defaults, committed file, target values, narrow runtime override | Most applications with several environments | A later layer can obscure a missing earlier value; needs source reporting |
| Profile-based | Named profiles select a bundle of values | A few fixed deployment shapes | Profile drift duplicates keys and hides the effective set |
| Remote configuration service | Central service supplies values with targeting | Many targets or tenants need changes without deployment | Availability, cache, failure and authorization become part of configuration |
| Per-tenant override | Global defaults plus tenant/plan records | Tenant-specific behavior or limits | Unbounded records, isolation bugs and cache invalidation |
| Flag evaluation | Targeting service decides a bounded exposure | Temporary rollout or kill path | Becomes permanent configuration with no owner if not retired |

Rules that apply to every model:

- One declared owner per key. If two sources can set the same key, state which wins and why.
- Resolve once into an immutable effective settings object; do not let different modules re-read and disagree.
- Report `key -> source` for diagnostics. Never report the resolved value for a secret.
- Treat absence and empty string as different states unless the schema explicitly normalizes them.
- A source that is unreachable at startup needs a declared behavior: fail, use a bounded cache, or use a documented safe default.

### Illustrative precedence

```text
built-in safe default
  < committed non-secret defaults
  < target configuration (staging/production)
  < bounded runtime override (owner, expiry, audit)
```

Secrets are not a precedence layer. They are resolved separately through a workload identity or protected store and must not be shadowed by a non-secret default with the same key name.

## Schema and strictness

| Decision | Strict | Permissive |
| --- | --- | --- |
| Unknown keys | Reject; catches typos and stale keys | Ignore; tolerates mixed application versions |
| Missing optional | Apply documented default | Leave absent; code must handle both |
| Type coercion | Require the declared type; reject ambiguous strings | Accept common coercions |
| Cross-field rules | Validate combinations and target invariants | Validate fields independently |
| Renamed keys | Fail with migration guidance | Accept old and new with a deprecation window |
| Sensitive values | Redact in errors, logs and schema output | Same; never relax this for convenience |

Pick one policy per surface. Mixed versions of the application, shared configuration with other services, and an external config file you do not control favor a measured permissive window with a deprecation date. A single-owner service and a small key set favor strict rejection. In either case, validate the merged result and test the negative path.

A useful schema covers:

- type and nullability;
- range or duration and its unit;
- enum or closed set;
- format where a parser exists (URL, CIDR, email, key identifier);
- relational rules between keys;
- target-only invariants that cannot be checked at build time.

## Environment parity

| Difference | Acceptable | Verify |
| --- | --- | --- |
| Host names, endpoints, account IDs, cluster names | Yes, target-owned | Effective value in the named target |
| Capacity, replicas, timeouts, log level | Yes, within reviewed bounds | Value and its operational effect |
| Secret values | Yes, independently held | Presence, scope and authentication; never the value |
| Key names or schema shape | No, unless the application genuinely differs | Key-set comparison |
| Security mode, trusted origins, redaction | Variation is security-sensitive | Protected review and target authorization |
| Feature exposure | Yes, intentional | Owner and kill path |
| Local-only debug bypasses | Only when impossible in production | Compile-time or explicit non-production guard |

Parity checks compare key sets and schema versions, not values. A service that silently ignores a production key is worse than a startup failure.

## Reload model

| Model | Behavior | Good fit | Evidence |
| --- | --- | --- | --- |
| Startup-only | Value is read once; change requires restart/rollout | Stable target settings; simple lifecycle | New revision serves; old revision drained |
| File watch | Consumer observes a mounted file change | Sidecar or file-based configuration with explicit reload support | File version changed and consumer acknowledged it |
| Periodic poll | Consumer re-reads on an interval | Slow-moving operational values | Version change observed within the bound |
| Push notification | Store publishes a change event | Fast control with a reliable consumer | Event received and applied; missed event recovered by poll |
| Dual-read/overlap | Old and new credentials valid during cutover | Rotation without downtime | New authenticates; old revoked after cutover |

A reload path is incomplete without:

- validation before the swap;
- a single atomic version, not per-key application;
- cache invalidation for settings-derived objects;
- bounded retry and a last-known-good policy;
- a signal that exposes the active version and the failure;
- a test that changes a value and observes the effect on work in flight.

An update in the store is not a reload. Mounted files may update on a delay, environment variables generally do not update in a running process, and a client may cache the old value indefinitely.

## Multi-tenant resolution

| Layer | Example | Must not do |
| --- | --- | --- |
| Platform default | Safe quota, retention, feature availability | Contain a tenant credential |
| Plan or entitlement | Limits attached to a purchased plan | Be inferred from a client-supplied plan name |
| Tenant override | Tenant-specific integration, branding, limits | Weaken a mandatory safety or isolation rule |
| Operational override | Temporary relief for one tenant | Become an unaudited permanent bypass |

Resolution rules:

1. Establish tenant identity from verified authentication and membership.
2. Load defaults, plan, tenant and operational layers in the declared order.
3. Validate the merged tenant view; reject or isolate an invalid override.
4. Bind caches to tenant identity and configuration version.
5. Enforce limits and feature availability in the serving path, not only in the display layer.
6. Audit who changed a tenant override and why.

Tenant isolation is a security property. A configuration lookup keyed only by a client-provided value, a cache without tenant in the key, or a fallback to a global tenant can cross the boundary even when each tenant's record is individually valid.

## Flags versus configuration

| Test | Configuration | Feature flag |
| --- | --- | --- |
| Would the value still be correct in a year? | Configuration | Flag |
| Does it select durable target behavior? | Configuration | Flag only during transition |
| Does it vary by cohort for an experiment? | Configuration if stable segments | Flag |
| Does it grant permission or entitlement? | Neither; authorization owns it | Neither |
| Is there an owner and a removal date? | Owner, no date required | Both required |
| Must it be identical everywhere? | Often yes | Usually no |
| Is a startup failure acceptable? | Usually yes | No; flag needs a default |

A flag whose removal depends on an unnamed future event is permanent configuration with weaker review. A configuration key whose only purpose is a temporary rollout is a flag with no kill path.

## Failure modes

| Condition | Preferred behavior | Avoid |
| --- | --- | --- |
| Required key absent | Fail before readiness; name key and source | Silent default that disables a control |
| Value invalid after merge | Fail with constraint and source | Coercing to a nearby valid value |
| Unknown key | Follow the declared strictness policy | Library-specific ignore/throw surprise |
| Secret store unreachable | Fail closed for access; bounded cache only where designed | Unbounded reuse of an old credential |
| Reload validation fails | Keep last known good; signal; no partial swap | Applying the valid subset |
| One tenant override invalid | Isolate that tenant; deny or safe default | Use another tenant's values |
| Config service slow | Bound the wait; use declared cache policy | Block startup indefinitely |
| Runtime override left behind | Detect, expire and reconcile to source | Let the next deployment silently restore it |

For each failure, state the user-visible effect. A startup crash, a read-only degradation and a cross-tenant fallback are not interchangeable.

## Evidence

| Claim | Sufficient evidence | Insufficient evidence |
| --- | --- | --- |
| Schema is valid | Parser/schema check over the merged example and negative cases | File exists |
| Target received a value | Effective source/value read from the target, or a behavior that depends on it | CI variable was set |
| Reload works | Change observed, active version reported, in-flight behavior checked | Store update timestamp |
| Rotation completed | New credential authenticates and old one is rejected | New version created |
| Tenant isolation holds | Cross-tenant read/write attempts denied through the application path | Separate records exist |
| Secret exposure handled | Credential revoked/rotated and scope assessed | File deleted |
| Environment parity holds | Key-set and schema comparison with deliberate differences listed | Same template rendered |

Report authored, validated, applied and observed states separately. The target's own behavior is the only proof that the effective configuration is the intended one.
