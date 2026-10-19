#!/usr/bin/env python3
"""Strict, dependency-free model validation and deterministic projections."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit


class ModelError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ModelError(message)


def shape(value, required, optional=(), at="object"):
    require(isinstance(value, dict), f"{at}: expected object")
    require(set(required) <= value.keys(), f"{at}: missing {sorted(set(required) - value.keys())}")
    require(value.keys() <= set(required) | set(optional), f"{at}: unknown fields {sorted(value.keys() - set(required) - set(optional))}")


def text(value, at):
    require(isinstance(value, str) and bool(value.strip()), f"{at}: expected nonempty string")


def array(value, at):
    require(isinstance(value, list), f"{at}: expected array")


def safe_url(value, schemes, relative=False):
    if not isinstance(value, str) or not value or re.search(r"[\s<>\x00-\x1f]", value):
        return False
    if relative and value.startswith("/") and not value.startswith("//"):
        return True
    try:
        parsed = urlsplit(value)
    except ValueError:
        return False
    return parsed.scheme.lower() in schemes and bool(parsed.netloc)


def load(path):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, f"duplicate JSON key: {key}")
            result[key] = value
        return result

    def constant(value):
        raise ModelError(f"non-JSON constant: {value}")

    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=pairs, parse_constant=constant)


def validate(data):
    shape(data, ("version", "title", "summary", "sources", "nodes", "messages", "flows"), ("assumptions", "exploration"), "model")
    require(type(data["version"]) is int and data["version"] == 1, "version: expected 1")
    text(data["title"], "title")
    text(data["summary"], "summary")
    for name in ("sources", "nodes", "messages", "flows"):
        array(data[name], name)
        require(name == "sources" or data[name], f"{name}: must not be empty")
    array(data.get("assumptions", []), "assumptions")
    for value in data.get("assumptions", []):
        text(value, "assumption")
    used = set()

    def identify(item):
        ident = item.get("id")
        require(isinstance(ident, str) and re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", ident), "invalid ID")
        require(ident not in used, f"duplicate ID: {ident}")
        used.add(ident)
        text(item.get("label"), f"{ident}.label")

    sources = {}
    for source in data["sources"]:
        shape(source, ("id", "label", "path"), ("lines", "url"), "source")
        identify(source)
        text(source["path"], "source.path")
        if "lines" in source:
            text(source["lines"], "source.lines")
        if "url" in source:
            require(safe_url(source["url"], {"http", "https"}), "unsafe source URL")
        sources[source["id"]] = source

    def citations(values, at, needed=False):
        array(values, at)
        require(all(isinstance(x, str) and x in sources for x in values), f"{at}: unknown citation")
        require(len(values) == len(set(values)), f"{at}: repeated citation")
        require(not needed or values, f"{at}: evidence required")

    def status(item):
        require(item["status"] in ("implemented", "proposed", "unresolved"), f"{item['id']}: invalid status")
        citations(item["citations"], f"{item['id']}.citations", item["status"] == "implemented")

    nodes = {}
    for node in data["nodes"]:
        shape(node, ("id", "label", "kind", "status", "external", "citations"), ("parent", "description"), "node")
        identify(node)
        status(node)
        require(node["kind"] in ("person", "system", "container", "component"), "invalid node kind")
        require(type(node["external"]) is bool, "external must be boolean")
        if "description" in node:
            text(node["description"], "node.description")
        if "parent" in node:
            text(node["parent"], "node.parent")
        nodes[node["id"]] = node
    for node in nodes.values():
        expected = {"container": "system", "component": "container"}.get(node["kind"])
        if expected:
            parent = nodes.get(node.get("parent"))
            require(parent is not None and parent["kind"] == expected, f"{node['id']}: invalid containment")
            require(parent["external"] == node["external"], f"{node['id']}: external ownership differs from parent")
        else:
            require("parent" not in node, f"{node['id']}: root cannot have parent")

    if "exploration" in data:
        exploration = data["exploration"]
        shape(exploration, ("depth",), ("overrides",), "exploration")
        require(exploration["depth"] in ("context", "container", "component"), "invalid exploration depth")
        overrides = exploration.get("overrides", {})
        require(isinstance(overrides, dict), "exploration.overrides: expected object")
        for ident, depth in overrides.items():
            node = nodes.get(ident)
            require(node is not None and node["kind"] in ("system", "container"), "depth override needs a system or container")
            allowed = ("context", "container", "component") if node["kind"] == "system" else ("container", "component")
            require(depth in allowed, "invalid local depth")
            require(any(n.get("parent") == ident for n in nodes.values()), "depth override needs modeled children")

    def provenance(value, payload, at):
        shape(value, ("kind", "citations"), ("note", "fields"), at)
        require(value["kind"] in ("observed", "illustrative", "derived", "proposed"), f"{at}: invalid provenance")
        citations(value["citations"], at, value["kind"] in ("observed", "derived"))
        if "note" in value:
            text(value["note"], at + ".note")
        array(value.get("fields", []), at + ".fields")
        for field in value.get("fields", []):
            shape(field, ("pointer", "origin", "citations"), at="provenance field")
            text(field["origin"], "field.origin")
            citations(field["citations"], "field.citations", True)
            pointer = field["pointer"]
            require(isinstance(pointer, str) and (pointer == "" or pointer.startswith("/")), "invalid JSON pointer")
            current = payload
            for part in pointer.split("/")[1:] if pointer else []:
                require(not re.search(r"~(?![01])", part), "invalid JSON pointer escape")
                part = part.replace("~1", "/").replace("~0", "~")
                if isinstance(current, list):
                    require(re.fullmatch(r"0|[1-9][0-9]*", part) is not None and int(part) < len(current), "pointer array index missing")
                    current = current[int(part)]
                else:
                    require(isinstance(current, dict) and part in current, "pointer field missing")
                    current = current[part]

    messages = {}
    for message in data["messages"]:
        shape(message, ("id", "label", "from", "to", "status", "citations", "note", "transport", "payload", "payloadProvenance"), ("parentId", "within", "fromComponent", "toComponent", "examples"), "message")
        identify(message)
        status(message)
        text(message["note"], "message.note")
        require(all(isinstance(message[key], str) and message[key] in nodes for key in ("from", "to")), f"{message['id']}: unknown endpoint node")
        for key in ("parentId", "within", "fromComponent", "toComponent"):
            if key in message:
                text(message[key], f"message.{key}")
        transport = message["transport"]
        require(isinstance(transport, dict), "transport must be object")
        if transport.get("kind") == "local":
            shape(transport, ("kind", "action"), at="local transport")
            text(transport["action"], "transport.action")
        else:
            shape(transport, ("kind", "protocol", "direction", "endpoint"), at="network transport")
            require(transport["kind"] == "network", "invalid transport kind")
            protocols = {"http": {"http", "https"}, "sse": {"http", "https"}, "websocket": {"ws", "wss"}, "grpc": {"grpc", "grpcs", "http", "https"}, "queue": {"amqp", "amqps"}, "tcp": {"tcp"}}
            require(isinstance(transport["protocol"], str) and transport["protocol"] in protocols, "invalid network protocol")
            require(transport["direction"] in ("request", "response", "event"), "invalid network direction")
            endpoint = transport["endpoint"]
            shape(endpoint, ("status", "method", "url"), ("note", "route"), "endpoint")
            require(endpoint["status"] in ("actual", "proposed", "unresolved"), "invalid endpoint status")
            if endpoint["status"] == "unresolved":
                require(endpoint["url"] is None, "unresolved URL must be null")
                if endpoint["method"] is not None:
                    text(endpoint["method"], "endpoint.method")
            else:
                text(endpoint["method"], "endpoint.method")
                require(safe_url(endpoint["url"], protocols[transport["protocol"]], transport["protocol"] in ("http", "sse")), "URL incompatible with transport")
            if endpoint["status"] == "actual":
                citations(message["citations"], "actual endpoint citations", True)
            if "note" in endpoint:
                text(endpoint["note"], "endpoint.note")
            if "route" in endpoint:
                require(safe_url(endpoint["route"], {"http", "https"}, True), "unsafe clickable route")
        provenance(message["payloadProvenance"], message["payload"], "payloadProvenance")
        array(message.get("examples", []), "examples")
        for example in message.get("examples", []):
            shape(example, ("label", "kind", "value", "provenance"), ("note",), "example")
            text(example["label"], "example.label")
            require(example["kind"] in ("context", "state", "persistence", "transform", "prompt", "tools", "request", "response"), "invalid example kind")
            if "note" in example:
                text(example["note"], "example.note")
            provenance(example["provenance"], example["value"], "example.provenance")
        messages[message["id"]] = message
    for message in messages.values():
        if "parentId" in message:
            parent = messages.get(message["parentId"])
            require(parent is not None and "parentId" not in parent, "child must map to a root message")
            container = nodes.get(message.get("within"))
            require(container is not None and container["kind"] == "container", "child needs within container")
            require(container["id"] in (parent["from"], parent["to"]), "child container not touched by parent")
            require(all(nodes[message[k]]["kind"] == "component" and nodes[message[k]].get("parent") == container["id"] for k in ("from", "to")), "internal child must stay within container")
            require("fromComponent" not in message and "toComponent" not in message, "child cannot refine endpoint")
        else:
            require("within" not in message, "root cannot have within")
            require(all(nodes[message[k]]["kind"] != "component" for k in ("from", "to")), "root endpoint must not be component")
            for key in ("from", "to"):
                component = message.get(key + "Component")
                if component is not None:
                    require(component in nodes and nodes[component]["kind"] == "component" and nodes[component].get("parent") == message[key], "refined endpoint must belong to parent container")
    covered = set()
    for flow in data["flows"]:
        shape(flow, ("id", "label", "kind", "goal", "messageIds"), ("description",), "flow")
        identify(flow)
        require(flow["kind"] == "scenario", "flow tabs are user scenarios only")
        text(flow["goal"], "flow.goal")
        if "description" in flow:
            text(flow["description"], "flow.description")
        array(flow["messageIds"], "flow.messageIds")
        require(flow["messageIds"], "scenario must contain messages")
        require(all(isinstance(x, str) and x in messages and "parentId" not in messages[x] for x in flow["messageIds"]), "flow must reference root messages")
        require(len(set(flow["messageIds"])) == len(flow["messageIds"]), "repeated flow message")
        covered.update(flow["messageIds"])
    require(covered == {m["id"] for m in messages.values() if "parentId" not in m}, "orphan root message")
    # Ensure values passed directly by callers are also finite JSON.
    try:
        json.dumps(data, allow_nan=False)
    except (ValueError, TypeError) as error:
        raise ModelError(f"not valid JSON: {error}") from error
    return data


def project(data, flow_id, depth, expanded=None, overrides=None):
    """Project global depth and local overrides without changing canonical messages.

    The optional expanded argument retains the old single-container projection API.
    New callers use overrides; component depth then expands every modeled container.
    """
    require(depth in ("context", "container", "component"), "invalid depth")
    nodes = {n["id"]: n for n in data["nodes"]}
    messages = {m["id"]: m for m in data["messages"]}
    flow = next(f for f in data["flows"] if f["id"] == flow_id)
    overrides = dict(overrides or {})
    if expanded is not None and depth == "component":
        overrides = {n["id"]: "component" if n["id"] == expanded else "container"
                     for n in nodes.values() if n["kind"] == "container"} | overrides

    def system_depth(node):
        if node["id"] in overrides:
            return overrides[node["id"]]
        if depth == "context" and any(n.get("parent") == node["id"] and n["id"] in overrides for n in nodes.values()):
            return "container"
        return depth

    def container_depth(node):
        parent_depth = system_depth(nodes[node["parent"]])
        return "context" if parent_depth == "context" else overrides.get(node["id"], parent_depth)

    def node_id(ident):
        node = nodes[ident]
        if node["kind"] == "component":
            parent = nodes[node["parent"]]
            if container_depth(parent) != "component":
                node = parent
        if node["kind"] == "container" and container_depth(node) == "context":
            node = nodes[node["parent"]]
        return node["id"]

    result = []
    for index, ident in enumerate(flow["messageIds"], 1):
        root = messages[ident]
        endpoints = {key: node_id(root.get(key + "Component", root[key])) for key in ("from", "to")}
        result.append({"id": ident, "parentId": ident, "number": str(index), **endpoints})
        children = [m for m in data["messages"] if m.get("parentId") == ident]
        for child_index, child in enumerate(children, 1):
            if container_depth(nodes[child["within"]]) == "component":
                result.append({"id": child["id"], "parentId": ident, "number": f"{index}.{child_index}", "from": node_id(child["from"]), "to": node_id(child["to"])})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model")
    args = parser.parse_args()
    try:
        data = validate(load(args.model))
    except (ModelError, json.JSONDecodeError, OSError) as error:
        parser.exit(1, f"INVALID: {error}\n")
    print(f"VALID: {len(data['nodes'])} nodes, {len(data['messages'])} messages, {len(data['flows'])} scenarios")


if __name__ == "__main__":
    main()
