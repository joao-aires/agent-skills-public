# Versioning and compatibility

Use this reference when deciding whether an HTTP API change is compatible, where to place a version, and how to retire a surface. It applies to the wire contract, not to internal code, database schema or deployment versions. Header and status semantics come from [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), `Deprecation` from [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html) and `Sunset` from [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html); the classification below is this collection's review tool.

## What counts as the contract

The contract includes more than paths and JSON fields:

- method, path and query semantics, media types, status codes and headers;
- field names, types, formats, nullability, defaults and ordering;
- error codes, their meanings and the status they arrive with;
- authentication, authorization, pagination, filtering, sorting and rate-limit behavior;
- idempotency, retry semantics and documented limits: page size, payload, timeout and quota.

A change can compile and still break a consumer through any of these.

## Classify the change

| Change | Classification | Condition or note |
| --- | --- | --- |
| Add an endpoint | Compatible | No existing consumer behavior changes |
| Add an optional response field | Compatible | Clients were told to ignore unknown fields |
| Add an optional request field with a safe default | Compatible | Omitting it preserves the previous behavior |
| Add a required request field | Breaking | Existing callers cannot supply it |
| Add a required request header | Breaking | Unless the server can derive it |
| Remove or rename a field, parameter or endpoint | Breaking | Deprecate and measure first |
| Change a field type, precision or format | Breaking | Even when the JSON shape looks similar |
| Change response nullability from non-null to nullable | Breaking | Clients assumed a value was present |
| Change response nullability from nullable to non-null | Usually compatible | Verify clients handle the new guarantee |
| Change a request field from optional to required | Breaking | The previous omission no longer works |
| Change a request field from required to optional | Compatible | As long as the default is documented |
| Change a default value | Breaking behavior | The same request now produces a different result |
| Change field ordering or collection ordering | Breaking when relied upon | Make order explicit in the contract |
| Add an enum value | Compatible only with an unknown-value rule | Strict clients otherwise fail |
| Remove an enum value | Breaking | Persisted or replayed values may still use it |
| Tighten validation or add a new rejection | Breaking | Previously accepted requests now fail |
| Change an error code, its meaning or its status | Breaking | Client branching depends on it |
| Change a status for the same condition | Breaking | Includes `200` to `201` or `404` to `403` |
| Change authentication or required scope | Breaking operationally | Coordinate with identity and consumers |
| Change pagination default or maximum | Behavior change | May break clients that rely on full traversal |
| Lower a rate limit materially | Behavior change | Treat as a compatibility event |
| Change the versioning scheme itself | Breaking | Do not mix schemes on one surface |
| Remove a deprecated surface after its sunset | Breaking, by plan | Only after the announced date and evidence |

When uncertain, test the change against a recorded consumer request and response. A schema diff that reports "non-breaking" is a tool opinion; it does not know how a consumer uses the field.

## Choose where the version lives

| Placement | Example | Strengths | Costs |
| --- | --- | --- | --- |
| Path major | `/v2/orders` | Obvious, easy to route and cache | Duplicated paths; invites versioning every route |
| Media type | `application/vnd.example.v2+json` | Keeps one URL; content negotiation | Harder for browsers, gateways and documentation |
| Query parameter | `?api-version=2026-01-01` | Date-based, good for frequent cloud releases | Easy to omit; every link and cache key must preserve it |
| Custom header | `X-Api-Version: 2` | Keeps URLs clean | Invisible in links and browser access; proxy behavior varies |

Pick one convention for the surface and document it in the OpenAPI servers, examples and error guidance. A date-based scheme suits continuously released services; a major path segment suits a product with a small number of long-lived API generations. Do not combine a path major with a media-type minor and a date parameter unless each has a distinct, documented job.

Prefer compatible evolution over a new major version. Reserve a new major for changes that cannot be made additive, and keep the previous major working for a stated overlap period.

## Deprecate in a sequence

1. Name the surface, the reason, the replacement and the last supported date.
2. Mark it deprecated in OpenAPI and in the consumer documentation.
3. Add `Deprecation` and, when a removal date is committed, `Sunset` response headers; link the migration guide.
4. Instrument usage by consumer identity and version, separating first-party, partner and unknown traffic.
5. Notify affected consumers directly and provide a migration path with examples.
6. Keep both surfaces working through the overlap; verify the replacement behaves under the old consumer's real requests.
7. Remove only after the sunset date and after usage is zero or explicitly accepted by the owner.

| Signal | What it proves |
| --- | --- |
| OpenAPI `deprecated: true` | Intent only |
| `Deprecation`/`Sunset` headers | The response told the caller, if the caller or intermediary surfaces it |
| Request logs by client and version | Who still calls it, within the logging retention |
| Successful replacement traffic from the same consumer | Migration actually happened |
| A support confirmation for an opaque partner | The remaining caller is accounted for |

Headers do not replace notice. Many clients and proxies ignore them, and a header on a `404`-only path may never be seen.

## Preserve consumers across the transition

- Keep stable `operationId` values and document the old and new surface together during the overlap.
- Run contract tests with the oldest supported consumer shape, not only the current client.
- Test the combinations you claim: old client/new server, new client/old server where rolling deployment allows it, and both versions during the overlap.
- Record the tested versions, platforms, dates and evidence in the compatibility matrix. "Latest" is not a version.
- Watch error rate, latency and retry volume after the change; a compatibility break often appears as a spike in `400`/`422` or repeated `409`.
- Distinguish an API rollback from a data rollback. Reverting the route does not reverse writes, migrations or emitted events.

## Common failures

- Calling a change compatible because the response still validates against the old schema, while a field's meaning or default changed.
- Versioning every route at birth, then maintaining versions nobody can distinguish.
- Adding an enum value with no instruction for unknown values.
- Using `PATCH` semantics that silently replace a whole object, so older clients erase fields they never knew about.
- Removing a field after "no usage in the last 24 hours" on a weekly or monthly client.
- Shipping `Deprecation` headers without a migration guide, owner or removal date.
- Keeping two versions alive indefinitely because no one owns the retirement.
- Treating an OpenAPI diff as proof that consumers still work.
- Forgetting query parameters, headers and error codes in the versioning decision.
