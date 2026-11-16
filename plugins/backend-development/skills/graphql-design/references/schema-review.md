# GraphQL schema review

Use this checklist when reviewing an SDL change, a composed supergraph or a proposed schema for a new graph. Review the schema as a contract: resolvers can be fixed later, but published field meanings and nullability are hard to change.

Record the schema revision reviewed and whether it is the subgraph SDL, the composed supergraph or a contract variant. A review of the wrong artifact proves nothing about what clients receive.

## 1. Naming and domain shape

- [ ] Types and fields use domain language, not table, ORM or transport names.
- [ ] One concept has one type; near-duplicate types are justified by different ownership or lifecycle.
- [ ] Entity identity is stable and exposed as an opaque ID where clients need to refetch or pass a reference.
- [ ] Value objects that cannot exist independently are not given root queries or mutations.
- [ ] Interfaces and unions represent real polymorphism, not a workaround for an unfinished shape.
- [ ] No generic `JSON` scalar carries core domain data without a documented shape and validation rule.
- [ ] Field, argument and enum names follow one casing convention and avoid abbreviations only the team knows.
- [ ] Types, fields, arguments and enum values have descriptions that state meaning, units and edge cases.

## 2. Nullability

- [ ] Every non-null response field has a guarantee the API can keep under dependency failure, denial and partial data.
- [ ] Customer-supplied or third-party data is nullable unless a real invariant makes absence impossible.
- [ ] List and item nullability are chosen separately: one failing item does not erase the list unless that is intended.
- [ ] Non-null fields do not sit below a field that can be denied, or the resulting null propagation is accepted.
- [ ] Mutation inputs are non-null where the operation genuinely requires them, and optional inputs have documented defaults.
- [ ] Changing nullable to non-null on a response is treated as usually compatible but reviewed for new null propagation.
- [ ] Changing non-null to nullable is treated as breaking.
- [ ] No field uses `null` to mean several different things: absent, not found, denied, unknown and empty are distinguished where clients must act differently.

| Data source | Default | Make non-null when |
| --- | --- | --- |
| Identifier or key | Non-null | The object cannot exist without it |
| Required relationship | Decide per failure behavior | The parent is meaningless without it and resolution is local |
| Optional relationship | Nullable | Never, unless the domain guarantees it |
| Third-party or federated field | Nullable | A verified contract and fallback guarantee it |
| Computed aggregate | Nullable | The aggregate is always defined for an existing object |
| Authorization-sensitive field | Nullable | Never; denial must be representable |
| List of independent items | Nullable items | Every item is required for the list to be meaningful |

## 3. Queries and connections

- [ ] Every collection field returns a connection or another bounded pagination shape.
- [ ] A connection has `edges` and non-null `pageInfo`; edges have `node` and `cursor`.
- [ ] `pageInfo` exposes `hasNextPage`, `hasPreviousPage`, `startCursor` and `endCursor` with the documented semantics.
- [ ] Page-size arguments have defaults and maximums; negative values are rejected.
- [ ] Ordering is deterministic with a unique tie-breaker and is consistent forward and backward.
- [ ] Cursors are opaque, stable for the same order and scoped to the filter and caller.
- [ ] Filter and sort arguments use bounded enums or documented input types, not arbitrary expressions.
- [ ] `totalCount` is absent or explicitly documented as potentially expensive.
- [ ] Nested connections are bounded and do not multiply into unbounded fan-out.

## 4. Mutations

- [ ] Each mutation names one intent and returns a payload with the affected entity and any user-facing outcome.
- [ ] Input types are specific to the mutation and do not expose fields the caller may not set.
- [ ] The mutation distinguishes not-found, conflict, validation failure and permission failure.
- [ ] A retried mutation does not create a second effect, or the contract documents how the client supplies an idempotency key.
- [ ] Partial success is not reported as a successful whole; either the operation is atomic or the payload reports per-item outcomes.
- [ ] Exactly-one inputs use `@oneOf` where the runtime and clients support the September 2025 edition.
- [ ] The payload does not require a second query for data the client needs to update its cache.
- [ ] Root mutation fields do not bypass the authority checks of the underlying operation.

## 5. Errors

- [ ] Expected domain outcomes are representable in the schema or a documented payload, not only as thrown errors.
- [ ] Each `extensions.code` has one meaning and a documented client action.
- [ ] Errors include a usable `path` and, where relevant, a field pointer or argument name.
- [ ] Internal exceptions are masked; no stack trace, SQL or dependency detail reaches clients.
- [ ] The server's HTTP status behavior is documented: `200` for executed operations, `400` for parse/validation, `5xx` for request-level faults.
- [ ] Null propagation caused by an error is acceptable for every affected non-null field.
- [ ] Clients are told to handle unknown error codes and unknown enum values.

## 6. Schema evolution

| Change | Verdict | Note |
| --- | --- | --- |
| Add a type, field or optional argument | Compatible | Watch cost and authorization on new fields |
| Add an enum value | Compatible with an unknown-value rule | Strict clients otherwise fail |
| Add a non-null argument without a default | Breaking | Existing operations omit it |
| Remove a field or enum value | Breaking | Deprecate and measure first |
| Rename a field | Breaking | Use a new field and deprecate the old one |
| Change a field type or scalar | Breaking | Even when values currently serialize the same |
| Nullable to non-null on output | Usually compatible | Clients see a stronger guarantee; confirm error propagation is acceptable |
| Non-null to nullable on output | Breaking | Clients assumed a value |
| Optional to required input | Breaking | Existing operations become invalid |
| Required to optional input | Compatible | Document the default |
| Change a default value | Breaking behavior | Same operation, different result |
| Deprecate a field | Compatible | Removal is the breaking event |
| Change `@key` fields | Breaking for federation | Affects composition and entity resolution |

- [ ] Breaking changes are detected against the previous published schema, not only against the current branch.
- [ ] Deprecated fields have a reason, a replacement and usage evidence by client.
- [ ] Old persisted operations still validate against the new schema while their clients are supported.
- [ ] The schema registry or reviewed SDL records which revision is deployed.

## 7. Federation and surface

- [ ] Each entity has a resolvable `@key`; key fields are non-null where possible.
- [ ] Each field has one owning subgraph; no field has conflicting semantics across subgraphs.
- [ ] Reference resolvers are expected to be called repeatedly and are batched.
- [ ] Shared enums, scalars and value types are stable across subgraphs.
- [ ] Contract variants or `@inaccessible` remove internal fields from partner and public surfaces.
- [ ] The published schema, documentation and introspection target the intended audience.
- [ ] Authorization directives are applied per field rather than to a shared root operation type.

## 8. Common failures

| Failure | Consequence |
| --- | --- |
| Non-null field backed by a flaky dependency | One dependency error nulls a large part of the response |
| Null used for not-found, denied and empty | Clients cannot choose the right UI or retry behavior |
| Offset disguised as a cursor | Duplicates and gaps under concurrent writes |
| Page size without a maximum | One query can request the whole table |
| `totalCount` on every connection | Hidden second scan and a false performance promise |
| Large shared input on one mutation | Ambiguous combinations, over-posting and hard authorization |
| Mutation returns only a boolean | Clients must refetch and races become visible |
| `@deprecated` without usage data | Removal breaks an unknown client |
| Authorization only on root fields | Nested fields leak data through another path |
| Introspection assumed to hide protected fields | Schema shape leaks even when values are filtered |
| Persisted query manifest not versioned with the client | New clients fail against an old allowlist, or vice versa |
| A shared loader cache across requests | Cross-user data exposure |
| Depth limit without breadth or cost limits | Wide queries bypass the depth guard |
| Composed schema reviewed instead of the contract variant | The public surface is never actually checked |

## 9. Review evidence

- the SDL or supergraph revision and the surface reviewed;
- the previous schema used for the diff;
- representative client operations, including persisted IDs;
- denied and partial-failure responses with paths;
- query counts and depth/cost results for the heaviest operations;
- the client versions still supported and the persisted operations they use.
