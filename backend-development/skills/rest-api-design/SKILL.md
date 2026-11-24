---
name: rest-api-design
description: Design a REST/HTTP API contract covering resources, method and status semantics, representations, errors, collections, idempotency, conditional requests, versioning, caching, authorization boundaries, rate limits and OpenAPI. Use before implementing or changing an HTTP interface; not for service behavior design or framework setup.
user-invocable: true
metadata:
  kind: method
  domain: backend
  phase: design
  scope: generic
  invocation: both
---

# Design the HTTP contract

REST API design decides what an HTTP interface exposes, what each exchange promises, and how it survives retries, concurrency, caching and change. This method owns that contract, not the behavior behind it: use service-contract design (`backend-design`) for operations, authority, invariants and durable effects, and architecture design when service, data or client boundaries change. Router, serializer, driver and deployment mechanics belong to the selected stack conventions.

Stop when the contract and its verification needs are reviewable, usually an OpenAPI document plus the identity, error and compatibility rules. Preserve accepted project conventions: when an existing API or stack convention already decides a detail, follow it and record only the consequential deviation.

## Start from behavior, then name resources

Read the accepted journeys before naming endpoints. A resource is a thing with identity and observable state, not a database table, screen or handler.

- List the operations each caller needs, the state each changes and the response each can act on. Let service-contract design decide what the operation means, who may perform it and when it completes.
- Give resources stable identities and name collections and members with stable plural nouns. Prefer server-generated opaque identifiers; a natural key in the URL becomes part of the contract and may later stop being unique or immutable. Model a genuine command or transition as a documented action sub-resource, and say why replacing resource state does not express it.
- Decide nesting and aggregation deliberately. One projection may serve a screen, but it must not expose another service's tables, ownership or a second authority path.
- Treat bulk and long-running work as first-class contracts. Bulk operations need per-item outcomes and a partial-failure rule; deferred work needs a status resource and the completion meaning accepted in service design.

| Shape | Use when | Contract obligations |
| --- | --- | --- |
| Member CRUD | The thing has identity, state and an owner | Stable identifier, representation, conditional update |
| Sub-resource | Its lifecycle is owned by a parent | Parent authorization, cascade or detach behavior |
| Action | A command cannot be expressed by replacing state | Documented semantics, retry safety, resulting state |
| Bulk | Many independent items share one call | Per-item status, ordering, partial failure, limits |
| Long-running | Completion is not bounded by the request | Acceptance status, status location, polling, terminal states |

## Decide method safety and status behavior

HTTP defines safe and idempotent method properties that clients, caches and retry libraries rely on ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) §9.2). A state change under `GET` breaks prefetching, caching and automatic retry, and answering a failed request with `200` and an error body misleads every generic HTTP layer.

| Intent | Method | Decisions the contract must record |
| --- | --- | --- |
| Read | `GET`, `HEAD` | Safe; validators support cheap revalidation |
| Create or replace at a caller-chosen URI | `PUT` | Full representation, idempotent; creation returns the new location |
| Create in a collection | `POST` | Not idempotent; needs a retry rule and a created or accepted outcome |
| Partial update | `PATCH` | Name the patch media type and its merge semantics |
| Delete | `DELETE` | Repeating it must not create a new effect |

Use the most specific status callers can act on, and keep the set small enough to document. The full catalogue belongs to [RFC 9110 §15](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes) and [RFC 6585](https://www.rfc-editor.org/rfc/rfc6585.html); only these choices change client behavior:

| Status | Client-facing decision |
| --- | --- |
| `201`, `202`, `204` | Created, accepted or empty body; pair creation with `Location` and deferred work with a status resource |
| `400` versus `422` | Malformed request versus semantically invalid content; one meaning per status, applied everywhere |
| `401` versus `403` versus `404` | Credential challenge, permitted-but-denied or deliberately hidden; one disclosure policy across reads, lists, writes and related resources |
| `409`, `412`, `428` | State conflict, failed precondition or missing precondition; the client must re-read, rebase or send a conditional write |
| `429` | Back off rather than retry immediately; include `Retry-After` |
| `5xx` | Whether a retry is safe depends on the method and the documented idempotency rule |

## Define representation and the error contract

Choose the media type and represent it consistently. A top-level JSON object leaves room for additive fields; a bare array is harder to evolve.

- Fix conventions for field naming, identifiers, timestamps, money, enums, null and absent values, and state which fields are always present and what `null` means. Return the resource state the caller may rely on, not a dump of persistence columns, and keep output-only and input-only fields distinct.
- Give every error a stable machine-readable code, a human-readable message, and a location when a specific field caused it. [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) `application/problem+json` is a sound default; clients must ignore unknown extension members.
- Keep status, code and documented meaning aligned: one condition, one code, on every endpoint, without stack traces, SQL, internal hosts or another tenant's identifiers. Treat the error shape as compatibility — new codes are additive only if clients were told to handle unknown codes, and changing a code's meaning is a breaking change.

Read [the contract checklist](references/rest-contract-checklist.md) before review. It turns these rules into concrete pass/fail checks.

## Design collections as a query contract

Pagination, filtering and sorting are API surface, not implementation details. Decide them before the first list endpoint ships; the contract checklist records the cursor-versus-offset signals.

- Prefer cursor pagination when data changes or the collection is large; use offset pagination only when stable, random access and a meaningful total justify it.
- Define a deterministic total order with a unique tie-breaker. A page boundary that moves between requests produces duplicates and gaps even with a correct page size.
- Allowlist filterable and sortable fields; a caller-supplied expression over arbitrary columns invites unbounded scans and exposes internal schema.
- Cap page size and reject absurd requests rather than silently truncating them. Return a next-page link or cursor rather than making clients construct one, and state defaults, maximums and end-of-list behavior in the specification. Treat totals, facets and aggregate counts as separate costs: omit them or make them opt-in when they require a second scan.
- Apply the same filter, ordering and authorization rules to every page; a cursor must not let a caller escape a tenant or permission boundary.

## Make retries and concurrency explicit

Method semantics alone do not make a `POST` safe to retry. A client that times out cannot know whether the server committed.

- For a retryable non-idempotent operation, accept an idempotency key with a defined scope, lifetime and request fingerprint. Replaying the same key and payload returns the original outcome; a different payload under that key is an error; a concurrent duplicate may be rejected while the first attempt is unresolved. `Idempotency-Key` is an active IETF draft, so document the behavior you implement.
- Distinguish the identity of the logical operation from the identity of an individual attempt. Durable deduplication and the decision that an effect is complete belong to service-contract design; the API exposes the key, the observable result and, for work continuing after the response, a status resource stating what polling returns, which terminal states exist and how long results remain available.
- Use a strong entity tag plus `If-Match` for lost-update protection, rejecting an unconditional overwrite rather than silently applying it, and require the precondition when the client omitted it.
- Decide what a second writer sees — rejected conflict, merged result or last-writer-wins — and choose last-writer-wins only when the accepted product behavior permits silent loss. Make bulk retries safe per item.

## Version and evolve the contract

Prefer compatible evolution to a new version. Add optional response fields, endpoints and enum values only where clients were told to tolerate them; do not change a field's type, meaning, nullability, default, ordering or error behavior in place. Read [versioning and compatibility](references/versioning-and-compatibility.md) for change classification, version placement and the deprecation sequence; a schema diff is not consumer evidence.

- When a breaking change is unavoidable, version at the boundary that actually changes: a path major version, a media type, or a date-based parameter. Pick one convention, document it and apply it to the whole surface; do not version every route reflexively.
- Deprecate with a date and a migration path. `Deprecation` ([RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html)) and `Sunset` ([RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html)) headers communicate intent when clients surface them; documentation and direct notice still carry the obligation.
- Measure who still uses the old surface before removal, and record supported versions and tested consumer combinations in the compatibility matrix.

## Cache with the same care as authorization

- A cache can answer without reaching the service ([RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html)), so caching is part of the contract. Set explicit freshness for cacheable `GET`/`HEAD` responses and validators so a stale entry can be revalidated cheaply.
- Mark authenticated or tenant-specific responses `private` or `no-store` unless the representation is genuinely shared. A shared cache keyed only by URL can serve one user's data to another.
- Use `Vary` for any request header that changes the representation, and verify behavior through the actual CDN or proxy configuration rather than origin headers alone.
- A successful unsafe request invalidates cached representations of the target URI; do not assume a write refreshes every derived cache. Do not use caching to compensate for missing authorization or an expensive query.

## Put authorization at the resource boundary

Authentication establishes who is calling; authorization decides what this request may do to this resource. "The endpoint requires a token" is not a resource-level rule. Authority and data-flow review remain with service and security design; this method makes the HTTP boundary and its denial semantics visible.

- Check authority for reads, lists, writes, exports, bulk items and nested resources. Access to a parent does not imply access to every child or referenced record.
- Derive tenant and owner from verified identity, not a caller-supplied field, and apply the same rule to filters, cursors, aggregates and batch keys. Scopes are coarse gates: a scope permits a class of operation, not ownership of a particular object.
- Keep credentials out of URLs, do not treat CORS as authorization, protect cookie-authenticated mutations against CSRF, and rate-limit per identity and tenant as well as per route.

## Make OpenAPI the reviewed contract

[OpenAPI 3.1](https://spec.openapis.org/oas/v3.1.0.html) aligns the Schema Object with JSON Schema 2020-12 and supports webhooks. Use the version your tooling supports, and pin it.

- Give each operation a stable `operationId` and describe success and error responses, security schemes, parameters, examples and deprecation in the same document. Generated clients and audit tooling depend on the identifiers; an undocumented error is not part of the contract anyone can test.
- Keep specification and implementation in the same change, lint the document and diff it in review. A schema diff is the cheapest place to notice a breaking change; drift is a defect, not documentation debt.
- Use provider validation and contract tests against a running service. A valid document proves neither behavior nor compatibility, and a regenerated client that changes types or defaults is evidence to inspect.

## Observe, document and hand off

Instrument request and correlation identifiers, consumer identity and version, route template rather than raw path, status class, latency, payload size, saturation and rate-limit rejections. Log authorization denials as policy events without secrets or full personal data. Document authentication, scopes, pagination, filtering, error codes, idempotency, retries, rate limits, versioning, deprecation, examples and a sandbox path; a changelog and support route are part of the interface.

Record the design where the project already keeps decisions: a design proposal or ECR section, with C4 when boundaries changed, a sequence view when ordering or failure matters, a state machine for long-running work, and a compatibility matrix; do not create a second API-design document or artifact type.

Verification must exercise the contract, not just the happy path: real consumer shapes, denied access, duplicate submission, concurrent update, cache behavior, page boundaries, deprecation notices and the old/new version combination. Generated types and a green schema diff do not establish semantic compatibility.

## Composition

| Need | Use |
| --- | --- |
| Operation meaning, authority, invariants, durable effects, retries and completion | `backend-design` in this package |
| Service, data, client or deployment boundaries; option comparison | Installed system architecture guidance |
| Design record, options, C4, sequence, state and compatibility artifacts | The artifact system's design-proposal, C4, sequence, state-machine and compatibility-matrix guides |
| Framework routing, validation, serialization, sessions and deployment | The selected stack conventions, for example the Python/FastAPI guidance |
| Identity, tokens, scopes, threat modeling, metrics, traces, SLOs and alerting | Installed security, identity and observability guidance |
| Verification strategy and release evidence | The project's test and change-verification guidance |

## Sources and fit

This method is original guidance informed by:

- [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html) and [RFC 9111](https://www.rfc-editor.org/rfc/rfc9111.html) for method properties, status semantics, validators and caching; [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) for problem details; [RFC 6585](https://www.rfc-editor.org/rfc/rfc6585.html) for `428` and `429`; [RFC 8594](https://www.rfc-editor.org/rfc/rfc8594.html) and [RFC 9745](https://www.rfc-editor.org/rfc/rfc9745.html) for `Sunset` and `Deprecation`. Checked 2026-11-16.
- [OpenAPI Specification 3.1.0](https://spec.openapis.org/oas/v3.1.0.html) for the contract document; the [release page](https://github.com/OAI/OpenAPI-Specification/releases) shows later 3.1 and 3.2 revisions, so match the exact version to tooling support.
- [Google API Improvement Proposals](https://google.aip.dev/general) (AIP-158, -160, -132, -151, -155, -180, -193) for a coherent resource-oriented convention set; they are an opinionated house style, not HTTP requirements. [Microsoft's](https://github.com/microsoft/api-guidelines) and [Zalando's](https://opensource.zalando.com/restful-api-guidelines/) guidelines differ on version placement and error shape, so choose one deliberately rather than blending them.
- [The Idempotency-Key HTTP Header Field](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) (IETF draft, October 2026) for replay, fingerprint and duplicate handling. It and the [RateLimit header fields draft](https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/) are works in progress, so treat their semantics as documented conventions, not settled standards.

These sources provide protocol constraints and common conventions. They do not define this project's authority model, product behavior, artifact homes or compatibility promises; no text is copied.
