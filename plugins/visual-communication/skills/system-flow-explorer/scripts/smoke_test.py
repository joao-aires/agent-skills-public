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
