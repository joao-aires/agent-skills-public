---
name: rest-api-design
description: Design a REST/HTTP API contract covering resources, method and status semantics, representations, errors, collections, idempotency, conditional requests, versioning, caching, authorization boundaries, rate limits and OpenAPI. Use before implementing or changing an HTTP interface; not for service behavior design or framework setup.
user-invocable: true
metadata:
  kind: method
  origin: local
  pack: technical
  domain: backend
  phase: design
  scope: generic
  invocation: both
  role: support
---

# Design the HTTP contract

REST API design decides what an HTTP interface exposes, what each exchange promises, and how it survives retries, concurrency, caching and change. This method owns that contract. It does not own the behavior behind it: use service-contract design (`backend-design`) for operations, authority, invariants and durable effects, and architecture design (`system-design`) when service, data or client boundaries change. Router, serializer, driver and deployment mechanics belong to the selected stack conventions.

Stop when the contract and its verification needs are reviewable, usually as an OpenAPI document plus the identity, error and compatibility rules. Implementation remains with the hosting activity.

Preserve accepted project conventions. When an existing API, style guide or stack convention already decides a detail, follow it and record only the consequential deviation rather than replacing an established contract with this method's defaults.

## Start from behavior, then name resources

Read the accepted journeys and operations before naming endpoints. A resource is a thing with identity and observable state, not a database table, screen or handler.

- List the operations each caller needs, the state each changes and the response each caller can act on. Let service-contract design decide what the operation means, who may perform it and when it completes.
- Give resources stable identities. Prefer server-generated opaque identifiers; a natural key in the URL becomes part of the contract and may later stop being unique or immutable.
- Name collections and members with stable plural nouns. Model a genuine command or transition as a documented action sub-resource, and say why replacing resource state does not express it.
- Decide nesting and aggregation deliberately. One projection may serve a screen, but it must not expose another service's tables or ownership.
- Treat bulk and long-running work as first-class contracts. Bulk operations need per-item outcomes and a partial-failure rule; deferred work needs a status resource and the completion meaning accepted in service design.
- Keep internal entities private. Do not expose a table, or add an endpoint whose only justification is client convenience, if it creates a second authority path or an operation no accepted consumer needs.

| Shape | Use when | Contract obligations |
| --- | --- | --- |
| Member CRUD | The thing has identity, state and an owner | Stable identifier, representation, conditional update |
| Sub-resource | Its lifecycle is owned by a parent | Parent authorization, cascade or detach behavior |
| Action | A command or transition cannot be expressed by replacing state | Documented semantics, retry safety, resulting state |
| Bulk | Many independent items share one call | Per-item status, ordering, partial failure, limits |
| Long-running | Completion is not bounded by the request | `202`, status location, polling guidance, terminal states |

## Apply HTTP method and status semantics

HTTP defines safe and idempotent method properties that clients, caches and retry libraries rely on ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) §9.2). A state change performed under `GET` breaks prefetching, caching and automatic retry. Never answer a failed request with `200` and an error body: generic HTTP software reads only the status.

| Intent | Method | Typical success | Notes |
| --- | --- | --- | --- |
| Read one or list | `GET`, `HEAD` | `200`, `304` with a validator | Safe; no side effects |
| Create or replace at a caller-chosen URI | `PUT` | `201` on creation, `200`/`204` on replace | Idempotent; full representation; `Location` on creation |
| Create in a collection | `POST` | `201` plus `Location`, or `202` | Not idempotent; needs a retry rule |
| Partial update | `PATCH` | `200` or `204` | Choose JSON Merge Patch or JSON Patch and document it |
| Delete | `DELETE` | `200`, `202` or `204` | Repeating it must not create a new effect |
| Deferred command | `POST` | `202` plus status location | Acceptance is not completion |

Use the most specific status that callers can act on, and keep the set small enough to document.

| Status | Meaning in an API contract |
| --- | --- |
| `400` | Malformed syntax, invalid parameter encoding or unparseable body |
| `401` | Missing, invalid or expired credentials; include the challenge |
| `403` | Authenticated but not permitted, where revealing that fact is acceptable |
| `404` | The resource does not exist, or its existence is deliberately hidden |
| `405` | Method not supported for this resource; include `Allow` |
| `406`, `415` | The requested or supplied media type cannot be served |
| `409` | The request conflicts with current state, including an unresolved duplicate |
| `412` | A conditional request failed its precondition |
| `422` | Syntactically valid content that is semantically invalid; do not use it as a synonym for `400` |
| `428` | The server requires a conditional request to protect an update |
| `429` | A quota or rate limit was exceeded; include `Retry-After` ([RFC 6585](https://www.rfc-editor.org/rfc/rfc6585.html)) |
| `500` | An unexpected server fault; do not expose internals |
| `502`, `503`, `504` | An upstream failed, the service is shedding load, or a dependency timed out |

`401` versus `403` versus `404` is a disclosure decision, not a style preference. Choose one policy for inaccessible resources and apply it consistently across reads, lists, writes and related resources.

## Define representation and the error contract

Choose the media type and represent it consistently. A top-level JSON object leaves room for additive fields; a bare array is harder to evolve.

- Fix conventions for field naming, identifiers, timestamps, money, enums, null and absent values. State which fields are always present and what `null` means where it appears.
- Return the resource state the caller may rely on, not a dump of persistence columns. Keep output-only and input-only fields distinct.
- Give every error a stable machine-readable code, a human-readable message, and a location when a specific field caused it. [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) `application/problem+json` is a sound default; clients must ignore unknown extension members.
- Keep the status, the code and the documented meaning aligned. Do not encode the same condition with different codes on different endpoints.
- Include a correlation identifier that support can use, without exposing stack traces, SQL, internal host names or another tenant's identifiers.
- Treat the error shape as part of compatibility. New codes are additive only if clients are told to handle unknown codes; changing a code's meaning is a breaking change.

Read [the contract checklist](references/rest-contract-checklist.md) before review. It turns these rules into concrete pass/fail checks.

## Design collections as a query contract

Pagination, filtering and sorting are API surface, not implementation details. Decide them before the first list endpoint ships.

- Prefer cursor pagination when data changes or the collection is large; use offset pagination only when stable, random access and a meaningful total justify it.
- Define a deterministic total order with a unique tie-breaker. A page boundary that moves between requests produces duplicates and gaps even with a correct page size.
- Allowlist filterable and sortable fields. A caller-supplied expression over arbitrary columns invites unbounded scans and exposes internal schema.
- Cap page size and reject absurd requests rather than silently truncating them. State defaults and maximums in the specification.
- Return a next-page link or cursor rather than requiring clients to construct one. Do not return an empty `next` value at the end if the contract says the field is absent.
- Treat totals, facets and aggregate counts as separate costs. Omit them or make them opt-in when they require a second scan.
- Apply the same filter, ordering and authorization rules to every page; a cursor must not let a caller escape a tenant or permission boundary.

| Choice | Prefer when | Main risk |
| --- | --- | --- |
| Cursor | Large or changing collections, feeds, exports | No random access; cursors must be opaque and tamper-resistant |
| Offset and limit | Small, stable, admin-style tables with page numbers | Drift, duplicates and gaps under concurrent writes |
| Server-driven next link | The service owns ordering and query state | Opaque query state can hide unbounded work if not validated |

## Make retries and concurrency explicit

Method semantics alone do not make a `POST` safe to retry. A client that times out cannot know whether the server committed.

- For a non-idempotent operation that a caller may retry, accept an idempotency key with a defined scope, lifetime and request fingerprint. Replaying the same key and payload returns the original outcome; reusing the key with a different payload is an error; a concurrent duplicate may return `409` while the first attempt is unresolved. The `Idempotency-Key` header is an active IETF draft, not a published standard, so document the behavior you implement.
- Distinguish the identity of the logical operation from the identity of an individual attempt. Durable deduplication, reconciliation and the decision that an effect is complete belong to service-contract design; the API exposes the key and the observable result.
- Use `202` with a status resource for work that continues after the response. State what polling returns, what terminal states exist and how long results remain available.
- Use entity tags and conditional requests for lost-update protection. `If-Match` with a strong `ETag` makes an update conditional; failure is `412`. `If-None-Match` supports efficient reads and `304` responses. Require a precondition with `428` when an unconditional overwrite is unacceptable.
- Decide what a second writer sees: rejected conflict, merged result or last-writer-wins. Only choose last-writer-wins when the accepted product behavior permits silent loss.
- Make bulk retries safe per item. A retried bulk request must not repeat successful items merely because one item failed.

## Version and evolve the contract

Prefer compatible evolution to a new version. Add optional response fields, new endpoints and new enum values only where clients were told to tolerate them; do not change a field's type, meaning, nullability, default, ordering or error behavior in place.

- When a breaking change is unavoidable, version at the boundary that actually changes: a path major version, a media type, or a date-based query parameter. Pick one convention, document it and apply it to the whole surface.
- Do not version every route reflexively. A version that no consumer can distinguish adds cost without protecting anyone.
- Deprecate with a date and a migration path. `Deprecation` ([RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html)) and `Sunset` ([RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)) headers communicate intent when your clients and intermediaries support them; documentation and direct notice still carry the obligation.
- Measure who still uses the old surface before removal. A deprecation without consumer evidence is a hope.
- Record supported versions, tested consumer combinations and the evidence in the project's compatibility matrix.

Read [versioning and compatibility](references/versioning-and-compatibility.md) for the compatibility table, versioning placement decision and deprecation sequence.

## Cache with the same care as authorization

Caching is part of the contract because a cache can answer without reaching the service ([RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html)).

- Set explicit freshness for cacheable `GET`/`HEAD` responses; use validators so a stale entry can be revalidated cheaply.
- Mark authenticated or tenant-specific responses `private` or `no-store` unless the representation is genuinely shared. A shared cache keyed only by URL can serve one user's data to another.
- Use `Vary` for any request header that changes the representation, and verify the behavior through the actual CDN or proxy configuration.
- Remember that a successful unsafe request invalidates cached representations of the target URI. Do not assume a write immediately refreshes every derived cache.
- Do not use caching to compensate for missing authorization or to hide an expensive query that should be fixed.
- Treat `ETag` as both a cache validator and a concurrency token; weak validators are not safe for `If-Match` update protection.

## Put authorization at the resource boundary

Authentication establishes who is calling; authorization decides what this request may do to this resource. Saying "the endpoint requires a token" is not a resource-level rule.

- Check authority for reads, lists, writes, exports, bulk items and nested resources. Access to a parent does not imply access to every child or referenced record.
- Derive tenant and owner from verified identity, not from a caller-supplied field. Apply the same rule to filters, cursors and aggregate results.
- Treat scopes as coarse gates. A scope permits a class of operation; it does not prove ownership of a particular object.
- Choose and document the `403`/`404` disclosure policy, and keep it consistent across direct access and collection membership.
- Keep credentials out of URLs and query strings. Do not treat CORS as authorization, and protect cookie-authenticated mutations against CSRF.
- Apply rate limits and quotas per identity and tenant as well as per route; otherwise one caller can exhaust the service for everyone.

Authorization design and data-flow review remain with service and security design; this method makes the HTTP boundary and its denial semantics visible.

## Make OpenAPI the reviewed contract

[OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0.html) aligns the Schema Object with JSON Schema 2020-12 and supports webhooks. Use the version your tooling actually supports, and pin it.

- Give every operation a stable `operationId`; generated clients and audit tooling depend on it.
- Describe success and error responses, security schemes, parameters, examples and deprecation in the same document. An undocumented error is not part of the contract anyone can test.
- Lint the document and diff it in review. A schema diff is the cheapest place to notice a breaking change.
- Keep the specification and the implementation in the same change. Drift between them is a defect, not documentation debt.
- Use provider validation and contract tests against a running service. A valid OpenAPI document proves neither behavior nor compatibility.
- Generate clients deliberately; a regenerated client that changes types or defaults is evidence to inspect, not a mechanical update.

## Observe, document and hand off

Instrument the boundaries callers experience: request and correlation identifiers, consumer identity and version, route template rather than raw path, status class, latency, payload size, saturation and rate-limit rejections. Log authorization denials as policy events without recording secrets or full personal data.

Document what a consumer needs to succeed: authentication, scopes, pagination, filtering and sorting, error codes, idempotency, retries and backoff, rate limits, versioning, deprecation, examples and a sandbox or test path. A changelog and a support route are part of the interface.

Record the design where the project already keeps decisions: a design proposal or ECR section, with a C4 view when boundaries changed, a sequence view when ordering or failure matters, a state machine for long-running work, and a compatibility matrix for versions and consumers. Do not create a second API-design document or a new artifact type for this.

Verification must exercise the contract, not just the happy path: real consumer shapes, denied access, duplicate submission, concurrent update, cache behavior, page boundaries, deprecation notices and the old/new version combination. Generated types and a green schema diff do not establish semantic compatibility.

## Composition

| Need | Use |
| --- | --- |
| Operation meaning, authority, invariants, durable effects, retries and completion | `backend-design` in this package |
| Service, data, client or deployment boundaries; option comparison | `system-design` when installed |
| Design record, options, C4, sequence, state and compatibility artifacts | The artifact system's design-proposal, C4, sequence, state-machine and compatibility-matrix guides |
| Framework routing, validation, serialization, sessions and deployment | The selected stack conventions, for example the Python/FastAPI guidance |
| Identity, tokens, scopes and threat modeling | Installed security and identity guidance |
| Metrics, traces, SLOs and alerting | Installed observability guidance |
| Verification strategy and release evidence | The project's test and change-verification guidance |

## Sources and fit

This method is original guidance informed by:

- [RFC 9110: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html), [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html), [RFC 9112: HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112.html) and [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html) for method properties, status semantics, validators, caching and transport framing. Checked 2026-11-16.
- [RFC 9457: Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) for a machine-readable error shape; [RFC 6585](https://www.rfc-editor.org/rfc/rfc6585.html) for `428` and `429`; [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) and [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html) for `Sunset` and `Deprecation`. Checked 2026-11-16.
- [OpenAPI Specification 3.1.0](https://spec.openapis.org/oas/v3.1.0.html) for the contract document; the [OpenAPI release page](https://github.com/OAI/OpenAPI-Specification/releases) shows later 3.1 and 3.2 revisions, so match the exact version to tooling support.
- [Google API Improvement Proposals](https://google.aip.dev/general), especially AIP-158 (pagination), AIP-160 (filtering), AIP-132 (ordering), AIP-151 (long-running operations), AIP-155 (request identification), AIP-180 (backwards compatibility) and AIP-193 (errors), for a coherent resource-oriented convention set. Google's conventions are an opinionated house style, not HTTP requirements.
- [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines) for the historical conventions. The general guide is now deprecated in favor of the [Azure REST API Guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md) and [Microsoft Graph guidelines](https://github.com/microsoft/api-guidelines/blob/vNext/graph/GuidelinesGraph.md); those differ on version placement, paging and error shape, so choose one deliberately rather than blending them.
- [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/) for resource naming, problem JSON, pagination, deprecation headers, compatibility and OpenAPI practice. Its rules are a company standard with explicit MUST/SHOULD levels; use the reasoning, not the mandatory list, unless the project adopts it.
- [The Idempotency-Key HTTP Header Field](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) (IETF draft, October 2026) for replay, fingerprint and duplicate-request handling. It is a work in progress, so treat its header semantics as a convention to document, not a settled standard. The [RateLimit header fields draft](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/) is likewise not final.

These sources provide protocol constraints and common conventions. They do not define this project's authority model, product behavior, artifact homes or compatibility promises; no text is copied.
