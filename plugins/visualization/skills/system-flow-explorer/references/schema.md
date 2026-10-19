# Canonical JSON contract (version 1)

`scripts/validate.py` is the executable contract. It rejects unknown fields to catch misspellings. IDs use letters/digits/underscore/hyphen, start with a letter, and are globally unique across sources, nodes, messages, and flows. Empty scenarios and dangling citations are invalid. JSON is strict: no NaN, Infinity, or duplicate object keys.

## Top level

Required: `version: 1`, `title: string`, `summary: string`, `sources: []`, `nodes: []`, `messages: []`, `flows: []`. Optional `assumptions: [string]` and `exploration` settings. At least one node, message, and flow. See `assets/minimal.json` for an executable example.

## Sources

`{id, label, path}`; optional `lines` (string such as `10-35`) and `url` (http/https only). Paths are displayed citations, not silently fetched. Use an actual browsable source URL when available. Paths can reference local code or a supplied design brief. `citations` elsewhere are lists of source IDs.

## Nodes

`{id, label, kind, status, external, citations}`; optional `parent`, `description`.

- `kind`: person, system, container, component.
- `status`: implemented, proposed, unresolved. Implemented nodes/messages require citations.
- `external`: boolean, inherited consistently through a subtree.
- People and systems are roots. Containers require a system parent; components require a container parent. Component-of-component hierarchies are deliberately excluded in version 1.
- External systems are separate roots, not descendants of an internal system. Mark the entire external subtree external. Providers, neighboring services, and their known containers can be modeled explicitly without nesting them inside the consuming runtime.

## Messages

Required: `id`, `label`, `from`, `to`, `status`, `citations`, `note`, `transport`, `payload`, `payloadProvenance`.

Roots have no parent and use person/system/container endpoints. Optional `fromComponent` and `toComponent` attach a finer endpoint within the corresponding root container; root identity and payload remain unchanged.

Children have `parentId` (a root message ID) and `within` (container ID); `from` and `to` must be components within that container, and the root must touch it. No nested child-of-child messages in v1. Child order is array order. Children appear immediately after their parent only when their `within` container is expanded. Child labels are derived as `N.1`, `N.2`, etc.; roots use `N` from scenario order.

`transport`:

- Local: `{kind: "local", action: "function call"}` (action is any nonempty description). No endpoint properties.
- Network: `{kind: "network", protocol, direction, endpoint}`.
- Protocol: http, sse, websocket, grpc, queue, tcp.
- Direction: request, response, event.
- Endpoint: `{status, method, url}`, optional `note`, `route`.
- Status: actual, proposed, unresolved. Method is a nonempty protocol operation (e.g. POST, SSE, Publish); use null for undecided methods only on unresolved endpoints.
- URL: http(s), ws(s), grpc(s), amqp(s), tcp URLs or an absolute route `/...` for actual/proposed endpoints. Use placeholders within an absolute URL if a deployment base is unknown, e.g. `https://{API_HOST}/items`; explain it in the note. Unresolved URL must be null. Scheme must match transport; relative routes are for HTTP/SSE only. Actual endpoints require citations on the message.
- Optional `route` is a clickable http(s) URL or `/...` route, not a citation. Absolute safe URLs are clickable in the inspector; raw route-only URLs remain clickable but resolving against a file artifact may require deployment context. Never invent a local-call URL to populate this field.

`payload` is any JSON value, including null/string/array. `payloadProvenance` is `{kind, citations}` with optional `note` and `fields`. Kind is observed, illustrative, derived, proposed. Observed/derived require citations. Each field is `{pointer, origin, citations}`: pointer is an RFC 6901 JSON pointer into the payload, origin is a readable source/upstream path, citations are source IDs. Pointer existence is checked.

Optional `examples`: array of `{label, kind, value, provenance}` with optional `note`. Kind: context, state, persistence, transform, prompt, tools, request, response. `value` is JSON; provenance follows the same contract, with pointers relative to that value. Examples are separate inspectable JSON values; the default payload is not an invented envelope combining them.

## Flows

`{id, label, kind: "scenario", goal, messageIds: [root IDs]}`. Optional `description`. No repeated root IDs within a flow; every root appears in some flow. A root can belong to more than one scenario, with scenario-local numbering. Scenario subsets can intentionally omit unrelated nodes; the architecture keeps all declared systems/containers for orientation.

## Projection and selection invariants

View is `sequence` or `c4`; global depth is `context`, `container`, or `component`. They are independent UI controls. Component depth expands all modeled containers by default. Local overrides let several regions stay at different levels in either view. Only modeled children are expandable; component-of-component and nested message hierarchies remain outside version 1.

Optional initial settings, chosen by the generating agent when useful:

```json
"exploration": {
  "depth": "container",
  "overrides": {"api": "component"}
}
```

`depth` is required when `exploration` is supplied; without settings the renderer starts at container depth. `overrides` is an optional object keyed by node ID. Systems with modeled containers accept context/container/component; containers with modeled components accept container/component. Unknown IDs, leaf-node overrides, and unsupported levels are invalid. A container inherits its system's level, and a system inherits the global level. A local container choice reveals its owning system at container level even when the global level is context. An explicit context override on that system hides all its internals, including saved container overrides. These reappear when the system is expanded. Changing the global level preserves local choices; Reset local levels clears them. Initial settings affect presentation only, not evidence or canonical identities.

Context projects internal nodes to their system. At component depth, refined endpoints use their declared component; unrefined container endpoints remain aggregate containers. Boundary rectangles name the owning system/container, including external ownership. Local controls are available on sequence participants, C4 nodes, ownership boundaries, and in the Local detail levels panel; the panel also allows choosing inheritance again.

Every root interaction survives every projection, including collapsed self-loops. Child `parentId` maps selection to a root when hidden. The picker, diagram, previous/next, payload, and network inspector derive from the same selected canonical message. Switching views preserves identity and depth choices; collapsing remembers hidden children; switching scenarios resets selection to that scenario's first root while retaining depth choices. Re-expanding restores a remembered child unless the reader has explicitly selected another message.

The Python `project` helper accepts an `overrides` mapping for the same projection. Its legacy `expanded` argument retains single-container component expansion for existing callers.
