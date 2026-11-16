# GraphQL security and cost

Use this reference when designing the access and capacity controls around a GraphQL schema. The schema decides what is reachable; these controls decide who may reach it and how much work one request can cause.

## Name the threat before choosing a control

| Threat | What it looks like | Primary control |
| --- | --- | --- |
| Unauthorized field access | A nested field returns data the caller may not see | Field and type authorization, resource checks |
| Enumeration through introspection | Schema shape and internal type names exposed | Schema surface choice, production introspection policy |
| Query amplification | Aliases, fragments or broad root fields multiply work | Alias, root-field, depth and cost limits |
| Deep recursion | Nested connections walk far beyond the intended UI | Depth limit, page-size cap, per-field cost |
| Expensive field abuse | One field triggers a scan, export or remote fan-out | Field cost, timeout, precomputation, removal from public schema |
| N+1 collapse | A modest query produces thousands of datastore calls | DataLoader, query counts, trace review |
| Persisted-query poisoning | A client registers an arbitrary operation at runtime | Registered allowlist, not APQ alone |
| Error leakage | Stack traces, SQL, host names or other tenants' IDs in `errors` | Error masking, correlation IDs |
| Injection through arguments | Unvalidated filter or sort reaches storage | Input validation, allowlisted operators, parameterized access |
| CSRF or method abuse | Cookie-authenticated mutation triggered cross-site, or mutation over `GET` | CSRF protection, method and content-type rules |
| Federation boundary bypass | A subgraph is reachable directly, or entity representations are spoofed | Network isolation, signed/trusted routing, no public subgraphs |
| Cache authority mismatch | Cached result served after permissions changed | Scoped caching, revalidation, no shared cache for private data |

## Layer the controls

No single control covers the list. Design them together:

1. **Authenticate** every request and bind identity to a trusted context.
2. **Authorize** at the field, type and resource boundary, including nested and federated fields.
3. **Restrict the operation surface** with persisted operations or an allowlist where the audience permits it.
4. **Bound the request shape** with depth, height, alias, root-field, byte and page-size limits.
5. **Bound total work** with cost analysis, timeouts and concurrency limits.
6. **Rate-limit** by identity, tenant and operation cost.
7. **Observe** rejections, expensive operations and authorization filtering as separate signals.
8. **Reduce exposure** by keeping internal fields out of public contract variants.

## Make authorization decisions at the right boundary

| Mechanism | Enforces | Does not establish |
| --- | --- | --- |
| Authentication middleware | Who is calling | Permission for a specific object |
| Root-field check | Access to the entry point | Access to nested fields or connected records |
| `@authenticated` | Presence of an authenticated context | Ownership, tenancy or scope |
| `@requiresScopes` | Claim-based scope requirement | Object-level ownership |
| `@policy` | A custom policy decision | That every resolver path uses the same policy |
| Resolver or data-layer check | The specific resource rule | Coverage of every field unless consistently applied |
| Contract variant / `@inaccessible` | Schema exposure | Data access if the field is reachable another way |

- Apply checks to every path that can reach the data: direct fields, connections, aggregates, mutations, batch loaders and federated reference resolvers.
- Derive tenant, owner and role from verified claims or server-side state. Never trust a caller-supplied tenant ID, role or "as user" argument.
- Decide the failure shape. Apollo's authorization directives filter fields and rely on null propagation; a non-null field can turn a single denial into a null parent. If that is unacceptable, choose an operation-level rejection or a schema surface that cannot request the field.
- Treat introspection separately. Authorization directives do not hide field names from introspection, so a sensitive schema needs a contract variant or an explicit production introspection decision.
- Apply authorization before caching. A cached result scoped to the wrong authority is an access breach, not a performance bug.

Use service and security design for the authority model, tenancy and threat boundaries; this reference covers the GraphQL enforcement points.

## Build a cost model that matches the schema

Static limits catch shape abuse cheaply; dynamic cost catches expensive values.

| Control | Catches | Misses |
| --- | --- | --- |
| Depth | Deep nesting | Wide aliases, large pages, expensive single fields |
| Height | Total selection breadth | Repeated fragments and list multipliers |
| Alias count | Alias amplification | Expensive fields without aliases |
| Root-field count | Batch-style queries in one document | Nested fan-out |
| Page-size cap | Unbounded connections | Expensive filters and sorts |
| Static field weights | Predictable expensive fields | Cost driven by argument values |
| Variable-aware cost | Large limits, ranges or ID lists | Unknown cardinality in the datastore |
| Timeout and concurrency limit | Runaway execution | Work already performed before cancellation |
| Persisted-operation allowlist | Unknown operations entirely | Approved but expensive operations |

Start from measured operation profiles. Take the heaviest legitimate client operations, set limits above them with headroom, and verify the limits against real traffic rather than copying another graph's numbers. Apollo Router's request limits (`max_depth`, `max_height`, `max_aliases`, `max_root_fields`) are one implementation of the static layer; treat its defaults as defaults, not as a security decision.

Make the cost unit explicit: field resolutions, datastore calls, bytes, or a weighted score. If the unit cannot be explained to a client author, it cannot guide them when a request is rejected.

## Control amplification

- Cap `first`/`last` on every connection and cap nested list fields in resolvers. Depth limits do not bound a list multiplied at each level.
- Count aliases and fragment-expanded fields, not only the text a client typed.
- Reject query batching or bound its size if the server enables it; a batch can multiply an otherwise acceptable operation.
- Bound ID lists, filter value counts and date ranges. A filter that accepts ten thousand IDs is a bulk endpoint with no bulk contract.
- Disable or tightly bound arbitrary `GET` operations. Mutations must not be executable through `GET`, and cookie-authenticated requests need CSRF protection.
- Inspect query plans for federated operations; a plan that fans out to every subgraph for each entity is a cost bug in the schema or resolver design.

## Roll out persisted operations safely

| Stage | Behavior | Use |
| --- | --- | --- |
| Allow IDs | Clients may send an ID or a full operation | Latency benefit only |
| Audit | Unknown operations are logged but executed | Discover clients before enforcement |
| Safelist | Unregistered operations are rejected | Public or high-risk graphs |
| IDs only | Free-form operations are rejected entirely | Mature first-party clients |

Generate the manifest from client sources in CI, publish it with the client release, and keep prior operation IDs valid while older app versions are supported. Verify that a rejected operation returns a documented error and that client telemetry distinguishes it from a schema validation failure.

APQ is not a security control: any client can register an operation at runtime. Use it for request size, not for trust.

## Protect errors, logs and schema metadata

- Mask internal error messages in production. Keep the original in logs with a correlation ID.
- Do not put tokens, passwords, full personal records or another tenant's identifiers in `extensions`, paths or variable logs.
- Decide whether production introspection is enabled and document the decision. A schema registry can serve developer exploration without exposing the runtime endpoint.
- Strip deprecated, internal and experimental fields from public contract variants rather than relying on documentation alone.
- Treat the schema itself as sensitive where field names reveal unreleased features, internal org structure or security posture.

## Isolate federation boundaries

- Do not expose subgraph endpoints to untrusted networks. The router's authorization and limits are meaningless if a caller can reach a subgraph directly.
- Treat entity representations as untrusted input. Validate `@key` values and resolve only entities the caller is allowed to see.
- Keep authorization requirements consistent across subgraphs that contribute fields to the same entity; composition can merge requirements in ways that surprise one team.
- Verify that contract variants and `@inaccessible` remove fields from the artifact clients actually receive.
- Record subgraph ownership and trust direction in the architecture notes; a new subgraph is a boundary change.

## Observe and tune

Track, per operation and client version:

- request count, rejection reason and limit that fired;
- latency and resolver/datastore time;
- query count per operation and N+1 indicators;
- response size and list lengths;
- authorization-filtered paths and denials;
- persisted-query status and unknown-operation rate;
- cost distribution, not only the average.

Alert on a shift in the cost distribution or on a new operation dominating execution time. A limit that never rejects may be too loose; a limit that rejects legitimate clients is a product defect, not a security win.

## Common failures

- Relying on depth alone while aliases or page sizes multiply the work.
- Setting limits from a blog post instead of measured client operations.
- Enforcing authorization only on root fields and assuming nested fields are safe.
- Using a non-null field for protected data and turning a denial into a null parent.
- Leaving introspection on and assuming field-level filtering hides the schema.
- Treating APQ as an allowlist.
- Publishing a new client before its operation manifest reaches the router.
- Exposing subgraphs directly and expecting the router's policy to apply.
- Logging full variables to debug a cost problem, including credentials and personal data.
- Caching personalized results at a shared edge because the operation "looks public".
- Setting a timeout without cancelling work or bounding concurrency, so overload continues after the client gives up.
