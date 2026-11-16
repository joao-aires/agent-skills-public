---
name: graphql-design
description: Design a GraphQL schema and API contract covering domain types, nullability, connections, errors, mutations, idempotency, N+1 and cost limits, field authorization, persisted queries, federation boundaries, deprecation, caching and public versus private surfaces. Use before implementing resolvers or changing a schema; not for resolver code or service behavior design.
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

# Design the GraphQL schema as a contract

A GraphQL schema publishes the types, fields and operations clients may depend on. This method owns that published contract and the decisions that make it safe to evolve: nullability, pagination, errors, authorization, cost and federation boundaries. It does not own resolver implementation, datastore access or service behavior.

Use service-contract design (`backend-design`) for operation meaning, authority, invariants, durable effects and completion. Use architecture design (`system-design`) when service, data or client boundaries change. Resolver code, middleware, server configuration and database access belong to the selected stack conventions.

Stop when the schema and its operating rules are reviewable: the SDL or schema artifacts, the error and authorization contract, the cost policy and the verification needs. Implementation follows.

Preserve the existing schema where one is accepted. Extend its naming, identity and directive conventions, and record a consequential deviation rather than introducing a parallel style.

## Model the domain, not the database

Start from the journeys and the concepts consumers need, then define types around them.

- Treat the schema as a public contract even when it is internal. Name types and fields for domain meaning, not table or column names.
- Decide which objects are entities with stable identity and which are value objects owned by a parent. Expose opaque global IDs where clients need to refetch or pass a reference.
- Use interfaces and unions for genuine polymorphism; do not create a union of unrelated types to avoid designing a shape.
- Keep input types close to the mutation that accepts them. A shared "everything" input invites ambiguous combinations and accidental field exposure.
- Avoid untyped JSON scalars for core domain data. They move validation into every client and hide incompatibility from schema checks.
- Write descriptions for types, fields, arguments and enum values. They are the API documentation clients actually see through introspection.
- Decide schema-first (SDL reviewed before code) or code-first deliberately. Either is valid; the composed schema, not the authoring style, is what consumers receive.

## Make nullability a promise

Every field is nullable by default. `!` is a promise that the value will exist, and a broken promise propagates `null` upward to the nearest nullable parent.

- Prefer nullable fields for data that can be missing, denied, stale or supplied by a failing dependency. Apollo's schema guidance recommends starting nullable and adding non-null where the guarantee is real.
- Use non-null for identifiers, required relationships and values whose absence would make the object meaningless.
- Decide list nullability separately: `[Item!]!` fails the whole list if one item errors; `[Item]!` preserves the list and isolates the failure.
- Make mutation inputs non-null where the operation truly requires them. Converting a nullable input to non-null later is a breaking change for callers.
- Remember that field authorization and resolver failures become null propagation. A non-null field can erase an otherwise usable response.
- Do not use non-null to express "should always be present in our database"; express what the API promises under partial failure.

Read [the schema review](references/schema-review.md) for the naming, nullability and mutation checks used at review.

## Design connections as a stable pagination contract

Use the [Relay cursor connections specification](https://relay.dev/graphql/connections.htm) when clients need consistent pagination: a `Connection` type with `edges` and `pageInfo`, an `Edge` type with `node` and `cursor`, and `PageInfo` with `hasNextPage`, `hasPreviousPage`, `startCursor` and `endCursor`.

- Keep cursors opaque and stable for the same ordering. Do not expose raw offsets, primary keys or filter state that clients can forge.
- Define one deterministic order with a unique tie-breaker, and keep forward and backward traversal consistent.
- Require a page-size argument with a default and a hard maximum. Reject negative or excessive values rather than silently changing them.
- Expose ordering and filtering as explicit arguments with bounded, documented vocabularies. Do not accept arbitrary expressions against storage.
- Treat `totalCount` as optional and potentially expensive; a connection need not promise a cheap total.
- Apply the same authorization and tenant constraints to every page and to nested connections.

## Treat errors as data plus a stable code

GraphQL can return partial data and errors together. Design for that instead of forcing every failure into a top-level HTTP status.

- Use the response `errors` array for execution and request errors, with `message`, `path`, `locations` and an `extensions.code` carrying a stable machine-readable reason. Follow the [GraphQL specification](https://spec.graphql.org/September2025/) and the [GraphQL over HTTP](https://http-spec.graphql.org/) conventions for status and media type.
- Return `200` when an operation executed and only field errors occurred; use `400` for parse or validation failure and reserve `5xx` for request-level faults. Do not make clients branch on an HTTP status that describes GraphQL execution.
- Separate expected domain outcomes from defects. A sold-out item, a denied field and a validation error are normal results; a null dereference or an unreachable database is not.
- Give each code one meaning and document the client action. Do not reuse `BAD_USER_INPUT` for every failure.
- Mask internal messages, stack traces and dependency details in production; keep the correlation identifier in extensions or logs.
- Consider mutation payload types with explicit user-facing errors for recoverable business outcomes, and reserve the `errors` array for failures. Do not return both a success flag and a silently discarded error.

## Design mutations around intent and safe retries

- Name mutations for the intent (`cancelOrder`, not `updateOrderStatus`) and return a payload containing the affected entity plus any user-facing outcome.
- One mutation should represent one business intent. A large input that can create, update and delete in one call is hard to authorize and hard to retry.
- Mutation root fields execute serially, but serial execution does not make a retried request safe. A client that times out still does not know whether the effect committed. Accept an idempotency key or client-generated operation identity where retries matter, and let service design own the durable deduplication.
- Use `@oneOf` input objects, available since the [September 2025 specification edition](https://spec.graphql.org/September2025/), when exactly one of several inputs is valid. Verify that the server and client tooling support the edition before relying on it.
- Distinguish "not found", "already in that state" and "not allowed". Returning `null` for all three forces clients to guess.
- Do not expose a mutation that exists only to serve one screen's convenience if it bypasses the operation's invariants.

## Resolve without N+1 and with bounded execution

Schema design decides which traversals are possible; resolver design decides their cost. Keep the contract honest about both.

- A nested field can multiply queries. Use request-scoped batching and caching (for example DataLoader) so one parent list produces one batched lookup per relationship, not one per row.
- Scope loader caches to a request or an authorized tenant context. A cache shared across requests can leak data.
- Count queries per operation in tests and in traces. An N+1 that is invisible at ten rows becomes an incident at ten thousand.
- In federation, reference resolvers are called per entity representation; batch them and expect repeated calls for one query.
- Bound resolver time and dependency calls. A schema field that can trigger an unbounded remote fan-out needs a cap, a precomputed value or removal.

## Authorize at the field and type boundary

Root-level checks are not enough: the same entity is reachable through many paths, and a field may reveal more than its parent.

- Check authority for every field that returns protected data, including nested fields, connections, aggregates and mutations.
- Enforce resource-level rules in the resolver or data layer as well as any schema directive. A directive that filters a field name is not a substitute for checking the specific object.
- Apollo's `@authenticated`, `@requiresScopes` and `@policy` directives are one implementation; they filter unauthorized fields and rely on null propagation. That behavior differs from returning a hard denial, so choose it deliberately.
- Decide whether an unauthorized request gets a null field with an error, a whole-operation rejection, or a filtered schema. Document it, because clients see different shapes.
- Apply tenant and ownership checks to IDs, cursors, filters and batch keys. A global ID must not become a cross-tenant lookup.
- Remember that introspection does not apply authorization filtering. If field names or types are sensitive, use a contract variant or remove them from the exposed schema.
- Use service and security design for the authority model and threat boundaries; this method makes the schema's enforcement points explicit.

Read [security and cost](references/security-and-cost.md) for the threat checklist and limit design.

## Bound query cost before production

GraphQL lets a client choose the shape and size of the response. Treat that as a capacity and abuse surface.

- Set static request limits: maximum depth, height, aliases, root fields and request bytes. Apollo Router exposes these as request limits (`max_depth`, `max_height`, `max_aliases`, `max_root_fields`).
- Cap page sizes and nested list sizes. Depth alone does not bound breadth.
- Add cost analysis where variable-driven arguments or repeated fragments can produce work that static limits miss. Charge the operation, not only the request.
- Require persisted operations or an allowlist for public or high-risk graphs, and roll out safelisting in audit mode before enforcing it.
- Set timeouts and concurrency limits per operation and per client. A single expensive query should not consume the service's whole budget.
- Rate-limit by identity, tenant and operation cost. Return a documented error code and retry guidance rather than an opaque timeout.

## Use persisted queries and trusted documents deliberately

Automatic persisted queries (APQ) cache an operation after a client sends it. A persisted query list (PQL) or trusted-document manifest registers approved operations at build time and can reject everything else.

| Mechanism | Protects against | Limit |
| --- | --- | --- |
| APQ | Repeated request size | Does not safelist; clients can register arbitrary operations |
| Registered operation allowlist | Unknown or handcrafted operations | Requires build and release discipline for every client |
| Audit mode | Unknown operations during migration | Detects but does not block |
| ID-only safelisting | Free-form operations entirely | Requires every client to ship operation IDs |

Use a manifest generated from client sources, publish it with the client release, and keep old operation IDs available while old app versions remain in use. A new schema that rejects an old client's operation is a compatibility break even if the fields still exist.

## Draw federation boundaries around ownership

Federation is an architecture choice, not a schema decoration. Use architecture design to decide service boundaries first.

- Define an entity with `@key` when fields of one logical object are owned by more than one subgraph and each contributing subgraph can resolve a reference from the key. Key fields must uniquely identify the entity and should be non-null.
- Give each field one owning subgraph. Duplicating the same field with different semantics in two subgraphs produces composition conflicts or surprising merge behavior.
- Keep shared value types small and stable; changing a shared enum or scalar affects every subgraph and client.
- Account for composition rules, entity resolution and query planning in the design. A schema that composes is not automatically efficient.
- Use contract variants or `@inaccessible` to keep internal fields out of a partner or public surface, and verify that the filtered schema is the one clients actually introspect.
- Treat a new subgraph as a boundary change: record the ownership and dependency in the project's C4 or architecture notes.

## Evolve the schema without silent breaks

- Prefer additive change: new types, fields, arguments with defaults, enum values with an unknown-value rule, and optional inputs.
- Removing a field, changing its type or meaning, making a response field nullable where it was non-null, making an optional argument required or changing a default are breaking. Making a response field non-null is usually compatible for clients but changes how errors propagate, so verify it rather than assuming it is free.
- For inputs, adding a required argument or input field is breaking; making a required input optional is usually compatible when the new default preserves behavior.
- Deprecate with `@deprecated(reason: "...")` and a replacement. Introspection and generated clients surface the reason; documentation and direct notice still matter.
- Measure field usage by client and operation before removal. A deprecated field with active traffic is not removable.
- Check the schema diff and run the consumer's operations against the proposed schema. Composition success and a valid SDL do not prove a client still works.
- Keep operation names and IDs stable across releases; persisted query manifests depend on them.

## Cache with explicit ownership

- HTTP caching works for GraphQL mainly with `GET` and persisted operations. Without a trusted operation ID and a controlled cache key, a URL cannot establish that the response is shareable.
- Use CDN or gateway caching only for operations whose result is genuinely shareable. Authenticated or tenant-specific responses need `private` or `no-store`.
- Field-level cache hints are implementation-specific. Treat them as an optimization with a freshness and invalidation rule, not as correctness.
- Client normalized caches need stable IDs and sensible invalidation after mutations. Returning a different object shape or ID for the same entity defeats them.
- Do not let a cache serve data after a permission change. Authorization decisions belong at execution time unless the cached artifact is scoped to the same authority.

## Observe the graph as consumers experience it

Record operation name or hash, client name and version, persisted-query status, field paths, error codes, latency, resolver and datastore time, query count and response size. Separate schema validation errors, authorization filtering and resolver failures so an alert points at the right cause.

Trace the query plan for federated operations. The slow part is often a subgraph fan-out or an unbatched entity lookup, not the gateway. Redact variables and personal data from logs; retain enough correlation to reproduce a request.

## Separate public and private surfaces

One graph for every audience is rarely the right contract. Internal admin fields, experimental types and partner-only data create a wider attack and compatibility surface.

- Use a contract variant, a filtered schema or a separate graph when audiences differ in authority or stability expectations.
- Decide whether production introspection is enabled. It aids tooling and also reveals the schema; disabling it is a common control, not a security boundary by itself.
- Document authentication, operation allowlists, rate limits, error codes, pagination and deprecation for each public surface.
- Keep a schema registry or reviewed SDL as the source of truth, and make sure the published documentation matches the deployed schema.

## Record and verify the design

Put the contract and decisions in the project's design record: the design proposal or ECR section, with a sequence view for ordering and failure, a state machine for long-running work and a compatibility matrix for clients and schema versions. Do not add a second API-design document.

Verification should exercise the schema, not only the resolver unit tests: representative client operations, unauthorized fields and types, partial failure and null propagation, nested pagination boundaries, N+1 query counts, depth and cost rejection, persisted-query rejection, deprecated field usage and old/new client combinations. A composed schema and a green type check do not prove any of that.

## Composition

| Need | Use |
| --- | --- |
| Operation meaning, authority, invariants, durable effects, retries and completion | `backend-design` in this package |
| Service, data, client or deployment boundaries; federation topology | `system-design` when installed |
| Design record, C4, sequence, state and compatibility artifacts | The artifact system's design-proposal, C4, sequence, state-machine and compatibility-matrix guides |
| Server, resolver, middleware, datastore and deployment mechanics | The selected stack conventions |
| Identity, tokens, scopes and threat modeling | Installed security and identity guidance |
| Metrics, traces, SLOs and alerting | Installed observability guidance |
| Consumer-driven verification and release evidence | The project's test and change-verification guidance |

## Sources and fit

This method is original guidance informed by:

- [GraphQL Specification, September 2025](https://spec.graphql.org/September2025/) for the type system, null propagation, serial mutation execution, response errors and `@oneOf`. Checked 2026-11-16.
- [GraphQL over HTTP](https://http-spec.graphql.org/) (draft) for request methods, media types and status conventions. It is still a draft; document the behavior your server actually implements.
- [Relay cursor connections specification](https://relay.dev/graphql/connections.htm) for the connection, edge, cursor and `PageInfo` contract.
- [Apollo schema design: nullability](https://www.apollographql.com/docs/graphos/schema-design/guides/nullability) for nullable-first guidance, non-null tradeoffs and null propagation.
- [Apollo Federation entities](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro) for `@key`, entity resolution and N+1 risk; [GraphOS authorization](https://www.apollographql.com/docs/graphos/routing/security/authorization) for `@authenticated`, `@requiresScopes`, `@policy`, field filtering and introspection behavior.
- [Apollo Router request limits](https://www.apollographql.com/docs/graphos/routing/security/request-limits) for depth, height, alias and root-field limits; [persisted queries and safelisting](https://www.apollographql.com/docs/graphos/platform/security/persisted-queries) for PQL, APQ differences and incremental adoption.
- [Apollo Server error handling](https://www.apollographql.com/docs/apollo-server/data/errors) for error codes, extensions and HTTP status practice; [DataLoader](https://github.com/graphql/dataloader) for request-scoped batching and caching.

Apollo material describes one implementation and one hosted platform; the schema decisions remain valid with other servers, but verify directive and policy support in the chosen runtime. No text is copied.
