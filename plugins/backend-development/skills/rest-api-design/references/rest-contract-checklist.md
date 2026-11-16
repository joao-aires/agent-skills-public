# REST contract checklist

Use this checklist to review an HTTP interface before implementation or before accepting a change. Review the surface once for cross-cutting rules, then each operation. Record pass, fail or not-applicable with the evidence you inspected; a checked box without a link to the specification, test or observed response is only an opinion.

## 1. Resources and operations

- [ ] Every resource has a stable identity and a stated owner.
- [ ] Identifiers are opaque to clients unless the contract deliberately exposes a natural key.
- [ ] Collections and members use consistent plural nouns; path segments use one casing convention.
- [ ] Each operation has a named consumer and a journey it supports.
- [ ] Action-style endpoints are limited to commands that cannot be expressed as a state replacement, and each documents its resulting state.
- [ ] Sub-resource depth and aggregation are deliberate; no internal table or another service's record is exposed.
- [ ] Bulk operations define per-item results, partial failure and an item limit.
- [ ] No endpoint creates a second path to the same authority decision.

## 2. Methods and statuses

- [ ] `GET` and `HEAD` are safe and free of state changes, including analytics writes that affect behavior.
- [ ] `PUT` and `DELETE` are idempotent; repeating them does not create a second effect.
- [ ] `POST` and `PATCH` have a documented retry rule when callers may retry them.
- [ ] Creation returns `201` with `Location` when the new URI is known.
- [ ] Deferred work returns `202` with a status resource, not a fabricated final result.
- [ ] No success status carries an error payload.
- [ ] `405` includes `Allow`; `401` includes the appropriate challenge.
- [ ] `429` includes `Retry-After`; `503` used for load shedding includes it when a retry delay is known.

### Resolve ambiguous status choices

| Situation | Use | Avoid |
| --- | --- | --- |
| Body is malformed JSON or an unparseable value | `400` | `422` with a parser message |
| Body parses but violates a domain rule | `422`, or `409` if current state causes it | `400` for everything |
| Create with a client-supplied ID that already exists | `409` | `500`, or silently replacing |
| Update targets a stale representation | `412` with `If-Match` | Silent overwrite, `409` without a precondition |
| Update requires a precondition but none was sent | `428` | Accepting the write anyway |
| Duplicate idempotency key with a different payload | `422` or `400` per documented convention | Replaying the old response |
| Duplicate idempotency key while the first attempt is unresolved | `409` with a retry hint | Blocking indefinitely, or executing twice |
| Resource is absent or must not be disclosed | `404` | `403` that confirms existence, inconsistently applied |
| Caller is authenticated but lacks the permission and disclosure is acceptable | `403` | `401` |
| Method is valid elsewhere but not on this resource | `405` | `404` |
| A gateway's upstream did not answer in time | `504`, with guidance on whether the request may have succeeded | `500` that implies nothing happened |

## 3. Representation

- [ ] The media type and charset are explicit; the top-level JSON value has room for additive fields.
- [ ] Field naming, identifier format, timestamp format and timezone, money representation and enum casing are consistent across the surface.
- [ ] `null` and absent have documented, distinct meanings where both occur.
- [ ] Output-only fields cannot be written; input-only fields do not appear as resource state.
- [ ] The representation exposes only concepts consumers may depend on.
- [ ] Collections are not returned as unbounded arrays without pagination.
- [ ] Binary or large content uses an appropriate media type and a size limit, not a base64 field by default.

## 4. Errors

- [ ] Every documented failure has a status, a stable machine code and a human-readable message.
- [ ] Field-level validation identifies the offending location with a JSON Pointer or an equivalent stable path.
- [ ] The error shape is the same across endpoints, or the difference is documented and justified.
- [ ] Clients are told to ignore unknown error codes and extension members.
- [ ] No stack trace, SQL, internal host, secret, token or other tenant's identifier appears in an error.
- [ ] A correlation identifier is returned and can be found in server logs.
- [ ] The same condition does not map to different codes on different endpoints.
- [ ] Changing a code, its meaning or its status is treated as a compatibility change.

## 5. Collections

- [ ] Pagination is present on every collection that can grow.
- [ ] The total order is deterministic and ends with a unique tie-breaker.
- [ ] Cursors are opaque, tamper-resistant and scoped to the filter, sort and caller.
- [ ] Filter and sort fields are allowlisted; unknown values are rejected or ignored by a documented rule.
- [ ] Page size has a default and a hard maximum; oversized requests are rejected, not silently clamped without notice.
- [ ] The next-page mechanism preserves filter, sort and version parameters.
- [ ] Totals and facets are opt-in or omitted when their cost is material.
- [ ] Page two applies the same authorization and tenant constraints as page one.
- [ ] Concurrent inserts or updates cannot cause a record to appear twice or vanish across a full traversal without a documented consistency rule.

### Cursor or offset

| Signal | Cursor | Offset |
| --- | --- | --- |
| Collection changes while paging | Yes | Avoid |
| Deep pages or large data | Yes | Avoid |
| Random access or numbered pages required | No | Yes |
| Stable, small admin table | Either | Acceptable |
| A truthful total is required | Usually no | Yes, with a cost note |
| Export or feed traversal | Yes | Avoid |

## 6. Idempotency and retries

- [ ] Each retryable non-idempotent operation documents whether a key is required or optional.
- [ ] The key's scope, format, lifetime and storage are documented.
- [ ] A request fingerprint prevents a key from being reused with a different payload.
- [ ] Replay returns the original status and body, or a documented equivalent.
- [ ] Concurrent duplicates have a defined outcome.
- [ ] A client timeout does not cause a second business effect.
- [ ] Retry guidance distinguishes retryable statuses from permanent failures.
- [ ] Bulk retries do not repeat items that already succeeded.
- [ ] `202` polling is safe and does not re-execute the command.

## 7. Concurrency

- [ ] Strong `ETag` values change when the representation changes and are stable when it does not.
- [ ] `If-Match` protects updates where lost updates are possible; failure is `412`.
- [ ] `If-None-Match` supports `304` for reads where revalidation is useful.
- [ ] Weak validators are not used for update preconditions.
- [ ] `Vary` covers every request header that selects a different representation.
- [ ] The contract states the outcome of two concurrent writers: conflict, merge or last-writer-wins.
- [ ] A precondition is evaluated against the same state the write mutates.

## 8. Caching

- [ ] Cacheable responses have explicit freshness or a revalidation strategy.
- [ ] Authenticated or tenant-specific responses are `private` or `no-store`.
- [ ] Shared caches cannot key on a URL that returns different users' data.
- [ ] Unsafe requests invalidate the affected representation, or the staleness is documented and acceptable.
- [ ] The CDN or proxy configuration was checked, not only the origin headers.
- [ ] Sensitive data is not cached in shared storage or logs.

## 9. Authorization and tenancy

- [ ] Each read, write, list, export and bulk item checks authority at the resource boundary.
- [ ] Parent access does not silently grant child or referenced-record access.
- [ ] Tenant and owner come from verified identity, not from a request field.
- [ ] Filters, cursors and aggregate results cannot cross a tenant boundary.
- [ ] The `403`/`404` disclosure policy is consistent across direct and collection access.
- [ ] Credentials are not accepted in URLs.
- [ ] Cookie-authenticated mutations have CSRF protection; CORS is not treated as authorization.
- [ ] Rate limits and quotas exist per identity and tenant, not only per route.

## 10. Limits and abuse

- [ ] Request body, header, page size, filter complexity, export size and timeout limits are documented and enforced.
- [ ] Expensive filters or sorts cannot be used to trigger unbounded scans.
- [ ] Rate-limit rejection is distinguishable from an internal failure.
- [ ] Quota headers or documentation tell a well-behaved client how to back off.
- [ ] Abuse controls do not reveal whether a hidden resource exists.

## 11. OpenAPI and consumer evidence

- [ ] The document states `openapi`, `info.version` and each server.
- [ ] Every operation has a stable `operationId`, summary and description.
- [ ] Success and error responses, parameters, examples and security schemes are described.
- [ ] Deprecated operations and parameters are marked.
- [ ] The document passes linting and the diff was reviewed for breaking changes.
- [ ] The specification matches the deployed or intended service.
- [ ] At least one representative consumer shape was tested against the real response.
- [ ] Denied, duplicate, conflicting, empty, oversized and rate-limited paths were exercised.
- [ ] The supported version and consumer matrix records what was actually tested.

## 12. Common failures

| Failure | Why it breaks |
| --- | --- |
| `200` with `{"error": ...}` | Proxies, caches, retry libraries and generated clients treat it as success |
| `403` on an item but `200` with a filtered list elsewhere | Confirms existence and makes the policy untestable |
| `ETag` derived from `updated_at` with second precision | Two writes in the same second can pass the same precondition |
| `If-Match` compared with a weak validator | Semantically different representations can satisfy the precondition |
| Offset pagination sorted by a non-unique column | Records duplicate or disappear between pages |
| A cursor that encodes a raw offset | Defeats the reason for choosing cursors |
| Idempotency key stored per route only | The same logical operation can run twice through another route |
| Replaying an idempotency key with a different payload returns the old result | Hides a client bug and may apply the wrong intent |
| Retrying a `202` re-executes the command | Acceptance was mistaken for completion |
| `Vary` missing `Authorization` or a tenant header | A shared cache can serve another user's representation |
| Totals computed across all tenants | Leaks volume and existence through an aggregate |
| `429` without `Retry-After` | Clients retry immediately and amplify the overload |
| Error code reused with a new meaning | Client branching silently changes behavior |
| Adding an enum value without an unknown-value rule | Strict clients fail on an otherwise compatible addition |
| OpenAPI omits `4xx`/`5xx` | Generated clients and contract tests cannot see the real failure surface |
| "latest" version in documentation | No consumer can tell which contract was tested |

## 13. Review evidence

Record what supports the review:

- the OpenAPI revision and the commit or deployment it describes;
- the consumer or client revision used for the contract test;
- the observed status, headers and body for success, denial, conflict and retry;
- the cache and proxy configuration inspected;
- the compatibility matrix entry for old and new consumers;
- the checks that could not run and what remains unverified.
