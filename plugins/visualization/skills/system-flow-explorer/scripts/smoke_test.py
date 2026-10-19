#!/usr/bin/env python3
"""Behavioral structural checks, including deliberately malformed models."""
import copy
import json
import unittest
from pathlib import Path
from render import render
from validate import ModelError, load, project, validate

ROOT = Path(__file__).resolve().parents[1]


class ModelTests(unittest.TestCase):
    def setUp(self):
        self.data = load(ROOT / "assets" / "minimal.json")

    def test_all_parent_interactions_survive_every_depth(self):
        validate(self.data)
        for flow in self.data["flows"]:
            for depth in ("context", "container", "component"):
                items = project(self.data, flow["id"], depth, "api")
                self.assertEqual([m["id"] for m in items if m["id"] == m["parentId"]], flow["messageIds"])
                for item in items:
                    self.assertIn(item["parentId"], flow["messageIds"])
                    if item["id"] != item["parentId"]:
                        self.assertRegex(item["number"], r"^\d+\.\d+$")
        items = project(self.data, "understand", "component", "api")
        self.assertIn({"id": "modelCall", "parentId": "modelCall", "number": "6", "from": "adapter", "to": "provider"}, items)

    def test_independent_local_depth_and_system_collapse(self):
        base = dict(flow_id="find", depth="container")
        api = project(self.data, **base, overrides={"api": "component"})
        self.assertIn("read", [m["id"] for m in api])
        self.assertNotIn("selectDocument", [m["id"] for m in api])
        both = project(self.data, **base, overrides={"api": "component", "client": "component"})
        self.assertIn("read", [m["id"] for m in both])
        self.assertIn("selectDocument", [m["id"] for m in both])
        self.assertEqual([m["id"] for m in both if m["id"] == m["parentId"]], self.data["flows"][0]["messageIds"])
        collapsed = project(self.data, **base, overrides={"library": "context", "api": "component"})
        self.assertEqual([m["id"] for m in collapsed], self.data["flows"][0]["messageIds"])
        self.assertEqual(next(m for m in collapsed if m["id"] == "lookup")["to"], "library")
        self.assertEqual(project(self.data, "find", "context", overrides={"api": "component"}), api)
        global_components = project(self.data, "find", "component")
        self.assertEqual(global_components, both)
        summarized_client = project(self.data, "find", "component", overrides={"client": "container"})
        self.assertEqual(summarized_client, api)

    def test_initial_exploration_settings_and_invalid_overrides(self):
        self.data["exploration"] = {"depth": "context", "overrides": {"api": "component"}}
        validate(self.data)
        rendered = render(self.data)
        embedded = rendered.split('<script id="flow-model" type="application/json">')[1].split('</script>')[0]
        self.assertEqual(json.loads(embedded)["exploration"], self.data["exploration"])
        for settings in (
            {}, {"depth": "code"}, {"depth": "container", "unknown": True},
            {"depth": "container", "overrides": []},
            {"depth": "container", "overrides": {"missing": "component"}},
            {"depth": "container", "overrides": {"reader": "context"}},
            {"depth": "container", "overrides": {"provider": "container"}},
            {"depth": "container", "overrides": {"api": "context"}},
        ):
            with self.subTest(settings=settings):
                self.data["exploration"] = settings
                with self.assertRaises(ModelError):
                    validate(self.data)

    def test_reject_invalid_identity_hierarchy_and_transport(self):
        mutations = [
            lambda d: d["nodes"].append(copy.deepcopy(d["nodes"][0])),
            lambda d: d["nodes"][4].update(parent="provider"),
            lambda d: d["nodes"][-1].update(parent="api"),
            lambda d: d["nodes"][4].update(external=True),
            lambda d: d["messages"][2].update(parentId="read"),
            lambda d: d["messages"][2].update(to="provider"),
            lambda d: d["messages"][1].update(toComponent="reader"),
            lambda d: d["messages"][7]["transport"]["endpoint"].update(url="https://invented.test"),
            lambda d: d["messages"][0]["transport"].update(endpoint={}),
            lambda d: d["messages"][1]["transport"]["endpoint"].update(url="javascript:alert(1)"),
            lambda d: d["messages"][1]["transport"].update(protocol="websocket"),
            lambda d: d["messages"][1].update(citations=[]),
            lambda d: d["flows"][0].update(kind="runtime"),
            lambda d: d["flows"][0]["messageIds"].append("read"),
            lambda d: d["messages"][3]["payloadProvenance"]["fields"][0].update(pointer="/missing"),
        ]
        for mutation in mutations:
            data = copy.deepcopy(self.data)
            mutation(data)
            with self.subTest(mutation=mutation):
                with self.assertRaises(ModelError):
                    validate(data)

    def test_safe_json_injection_preserves_exact_value(self):
        malicious = '</script><script>window.injected=true</script><img src=x onerror="alert(1)">\u2028 &'
        self.data["title"] = malicious
        self.data["messages"][0]["payload"] = {"text": malicious}
        html = render(self.data)
        embedded = html.split('<script id="flow-model" type="application/json">')[1].split('</script>')[0]
        self.assertNotIn('<', embedded)
        self.assertEqual(json.loads(embedded)["messages"][0]["payload"]["text"], malicious)
        self.assertNotIn('__FLOW_MODEL_JSON__', html)


if __name__ == "__main__":
    unittest.main(verbosity=2)
