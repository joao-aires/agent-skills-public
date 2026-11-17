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

Stop when the schema and its operating rules are reviewable: the SDL or schema artifacts, the error and authorization contract, the cost policy and the verification needs. Preserve an accepted schema's naming, identity and directive conventions; record a consequential deviation rather than introducing a parallel style.

## Model the domain, not the database

- Treat the schema as a public contract even when it is internal. Name types and fields for domain meaning, not table or column names. Decide which objects are entities with stable identity and which are value objects owned by a parent, and expose opaque global IDs where clients need to refetch or pass a reference.
- Use interfaces and unions for genuine polymorphism; do not create a union of unrelated types to avoid designing a shape.
- Keep input types close to the mutation that accepts them; a shared "everything" input invites ambiguous combinations and accidental field exposure. Avoid untyped JSON scalars for core domain data, which move validation into every client and hide incompatibility from schema checks.
- Write descriptions for types, fields, arguments and enum values, since they are the documentation clients see through introspection. Choose schema-first or code-first deliberately: the composed schema, not the authoring style, is what consumers receive.

## Make nullability a promise

Every field is nullable unless marked otherwise, and a broken non-null promise propagates null upward to the nearest nullable parent.

- Prefer nullable fields for data that can be missing, denied, stale or supplied by a failing dependency. Use non-null for identifiers, required relationships and values whose absence would make the object meaningless — not to express "always present in our database". Decide list and item nullability separately: one failing item either erases the list or is isolated as a null element, so choose which failure the consumer can tolerate.
- Make mutation inputs non-null where the operation truly requires them. Converting a nullable input to non-null later is a breaking change for callers.
- Field authorization and resolver failures become null propagation. A non-null field can erase an otherwise usable response, so express what the API promises under partial failure.

Read [the schema review](references/schema-review.md) for the naming, nullability and mutation checks used at review.

## Design connections as a stable pagination contract

Use the [Relay cursor connections specification](https://relay.dev/graphql/connections.htm) when clients need consistent pagination, rather than inventing a page shape per field.

- Keep cursors opaque and stable for the same ordering. Do not expose raw offsets, primary keys or filter state that clients can forge. Define one deterministic order with a unique tie-breaker, and keep forward and backward traversal consistent.
- Require a page-size argument with a default and a hard maximum, rejecting negative or excessive values rather than silently changing them.
- Expose ordering and filtering as explicit arguments with bounded, documented vocabularies, not arbitrary expressions against storage. Treat totals as optional and potentially expensive.
- Apply the same authorization and tenant constraints to every page and nested connection.

## Treat errors as data plus a stable code

GraphQL can return partial data and errors together. Design for that instead of forcing every failure into a top-level HTTP status.

- Use the response error list for request and execution errors, with a stable machine-readable code in extensions and a usable path. Follow the [GraphQL specification](https://spec.graphql.org/September2025/) and [GraphQL over HTTP](https://http-spec.graphql.org/) for status and media-type behavior, and document what the server actually implements. Give each code one meaning and document the client action; do not reuse one code for every failure.
- Separate expected domain outcomes from defects. A sold-out item, a denied field and a validation error are normal results; a null dereference or an unreachable database is not.
- Mask internal messages, stack traces and dependency details in production, keeping the correlation identifier in extensions or logs.
- Consider mutation payloads with explicit user-facing errors for recoverable business outcomes, and reserve the error list for failures. Do not return both a success flag and a silently discarded error.

## Design mutations around intent and safe retries

- Name mutations for the intent (`cancelOrder`, not `updateOrderStatus`) and return a payload containing the affected entity plus any user-facing outcome. Distinguish "not found", "already in that state" and "not allowed"; returning null for all three forces clients to guess.
- One mutation should represent one business intent. A large input that can create, update and delete in one call is hard to authorize and hard to retry, and a mutation that exists only for one screen's convenience must not bypass the operation's invariants.
- Root mutation fields execute serially, but serial execution does not make a retried request safe. A client that times out still does not know whether the effect committed. Accept an idempotency key or client-generated operation identity where retries matter, and let service design own durable deduplication.

## Resolve without N+1 and with bounded execution

- A nested field can multiply queries. Use request-scoped batching and caching (for example DataLoader) so one parent list produces one batched lookup per relationship, not one per row. Scope loader caches to a request or an authorized tenant context; a cache shared across requests can leak data.
- Count queries per operation in tests and traces. An N+1 that is invisible at ten rows becomes an incident at ten thousand.
- In federation, reference resolution runs per entity representation; batch it and expect repeated calls for one query. Bound resolver time and dependency calls: a field that can trigger unbounded remote fan-out needs a cap, a precomputed value or removal.

## Authorize at the field and type boundary

Root-level checks are not enough: the same entity is reachable through many paths, and a field may reveal more than its parent.

- Check authority for every field that returns protected data, including nested fields, connections, aggregates and mutations.
- Enforce resource-level rules in the resolver or data layer as well as in any schema directive. A directive that filters a field name is not a substitute for checking the specific object.
- Decide whether an unauthorized request gets a null field with an error, a whole-operation rejection, or a filtered schema. Document it, because clients see different shapes, and schema directives that filter fields rely on null propagation. Introspection does not apply authorization filtering: if field names or types are sensitive, use a contract variant or remove them from the exposed schema.
- Apply tenant and ownership checks to IDs, cursors, filters and batch keys. A global ID must not become a cross-tenant lookup. Authority and threat modeling remain with service and security design; this method makes the schema's enforcement points explicit.

Read [security and cost](references/security-and-cost.md) for the threat checklist and limit design.

## Bound cost and the operation surface

GraphQL lets a client choose the shape and size of the response. Treat that as a capacity and abuse surface.

- Set static request limits: maximum depth, height, aliases, root fields and request bytes. Apollo's [request limits](https://www.apollographql.com/docs/graphos/routing/security/request-limits) are one implementation, not a security decision.
- Cap page sizes and nested list sizes; depth alone does not bound breadth. Add cost analysis where variable-driven arguments or repeated fragments produce work that static limits miss, charging the operation rather than only the request.
- Require persisted operations or an allowlist for public or high-risk graphs. Automatic persisted queries reduce request size but are not a trust control, because any client can register an operation at runtime. Generate the manifest from client sources, publish it with the client release, keep old operation IDs valid, and treat a rejected operation as a distinct, documented failure.
- Set timeouts and concurrency limits per operation and per client, and rate-limit by identity, tenant and operation cost. Return a documented error code and retry guidance rather than an opaque timeout.

## Draw federation boundaries around ownership

Federation is an architecture choice, not a schema decoration. Use architecture design to decide service boundaries first.

- Define an entity key when fields of one logical object are owned by more than one subgraph and each contributing subgraph can resolve a reference from that key. Key fields must uniquely identify the entity and should be non-null.
- Give each field one owning subgraph. Duplicating the same field with different semantics in two subgraphs produces composition conflicts or surprising merge behavior. Keep shared value types, enums and scalars small and stable; changing one affects every subgraph and client.
- Account for composition rules, entity resolution and query planning — a schema that composes is not automatically efficient.
- Use contract variants to keep internal fields out of a partner or public surface, and verify that the filtered schema is the one clients actually introspect. Treat a new subgraph as a boundary change and record its ownership and dependency.

## Evolve the schema without silent breaks

- Prefer additive change: new types, fields, arguments with defaults, enum values with an unknown-value rule, and optional inputs.
- Removing a field, changing its type or meaning, making a non-null response field nullable, making an optional argument required or changing a default are breaking. Making a response field non-null is usually compatible but changes how errors propagate, so verify it rather than assuming it is free. For inputs, adding a required argument or input field is breaking; making a required input optional is usually compatible when the new default preserves behavior.
- Deprecate with a reason and a replacement. Introspection and generated clients surface the reason; documentation and direct notice still matter.
- Measure field usage by client and operation before removal; a deprecated field with active traffic is not removable. Check the schema diff and run the consumer's operations against the proposed schema: a composed schema and a valid SDL do not prove a client still works.
- Keep operation names and IDs stable across releases; persisted-query manifests depend on them.

## Cache with explicit ownership

- HTTP caching works for GraphQL mainly with `GET` and persisted operations. Without a trusted operation ID and a controlled cache key, a URL cannot establish that the response is shareable.
- Use CDN or gateway caching only for operations whose result is genuinely shareable; authenticated or tenant-specific responses need `private` or `no-store`. Field-level cache hints are an implementation-specific optimization with a freshness rule, not correctness.
- Client normalized caches need stable IDs and sensible invalidation after mutations; returning a different object shape or ID for the same entity defeats them. Never let a cache serve data after a permission change.

## Separate public and private surfaces

One graph for every audience is rarely the right contract. Internal admin fields, experimental types and partner-only data widen the attack and compatibility surface.

- Use a contract variant, a filtered schema or a separate graph when audiences differ in authority or stability expectations.
- Decide whether production introspection is enabled. It aids tooling and also reveals the schema; disabling it is a common control, not a security boundary by itself.
- Document authentication, operation allowlists, rate limits, error codes, pagination and deprecation for each public surface. Keep a schema registry or reviewed SDL as the source of truth, and check that published documentation matches the deployed schema.

## Record and verify the design

Put the contract and decisions in the project's design record: the design proposal or ECR section, with a sequence view for ordering and failure, a state machine for long-running work and a compatibility matrix for clients and schema versions. Do not add a second API-design document.

Observe operation name or hash, client name and version, persisted-query status, field paths, error codes, latency, resolver and datastore time, query count and response size. Separate schema validation errors, authorization filtering and resolver failures so an alert points at the right cause, and redact variables and personal data.

Verification should exercise the schema, not only resolver unit tests: representative client operations, unauthorized fields and types, partial failure and null propagation, nested pagination boundaries, N+1 query counts, depth and cost rejection, persisted-query rejection, deprecated field usage and old/new client combinations.

## Composition

| Need | Use |
| --- | --- |
| Operation meaning, authority, invariants, durable effects, retries and completion | `backend-design` in this package |
| Service, data, client or deployment boundaries; federation topology | `system-design` when installed |
| Design record, C4, sequence, state and compatibility artifacts | The artifact system's design-proposal, C4, sequence, state-machine and compatibility-matrix guides |
| Server, resolver, middleware, datastore and deployment mechanics | The selected stack conventions |
| Identity, tokens, scopes, threat modeling, metrics, traces, SLOs and alerting | Installed security, identity and observability guidance |
| Consumer-driven verification and release evidence | The project's test and change-verification guidance |

## Sources and fit

This method is original guidance informed by:

- [GraphQL Specification, September 2025](https://spec.graphql.org/September2025/) for the type system, null propagation, serial mutation execution and response errors. Checked 2026-11-16.
- [GraphQL over HTTP](https://http-spec.graphql.org/) (draft) for request methods, media types and status conventions; it is still a draft, so document what the server implements.
- [Relay cursor connections](https://relay.dev/graphql/connections.htm) for the connection, edge, cursor and page-info contract.
- [Apollo nullability](https://www.apollographql.com/docs/graphos/schema-design/guides/nullability), [Federation entities](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro), [GraphOS authorization](https://www.apollographql.com/docs/graphos/routing/security/authorization), [request limits](https://www.apollographql.com/docs/graphos/routing/security/request-limits), [persisted queries](https://www.apollographql.com/docs/graphos/platform/security/persisted-queries), [server error handling](https://www.apollographql.com/docs/apollo-server/data/errors) and [DataLoader](https://github.com/graphql/dataloader) for implementation examples, directive behavior, request-size caching versus an approval list, and request-scoped batching. Apollo material describes one implementation and one hosted platform; verify directive and policy support in the chosen runtime.

These sources describe protocol and vendor behavior. They do not define this project's authority model, product behavior or compatibility promises; no text is copied.
