import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("skill_graph", ROOT / "scripts/skill_graph.py")
skill_graph = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(skill_graph)
SCHEMA_SPEC = importlib.util.spec_from_file_location("skill_schema", ROOT / "scripts/skill_schema.py")
skill_schema = importlib.util.module_from_spec(SCHEMA_SPEC)
SCHEMA_SPEC.loader.exec_module(skill_schema)

DOCUMENT = skill_graph.build()
NODES = {node["id"]: node for node in DOCUMENT["nodes"]}


class GraphModelTests(unittest.TestCase):
    def test_every_edge_is_a_move_or_a_record_link(self):
        relations = {edge["relation"] for edge in DOCUMENT["edges"]}
        self.assertLessEqual(relations, skill_graph.RELATIONS)
        self.assertLessEqual(relations, set(DOCUMENT["model"]["moves"]) | set(DOCUMENT["model"]["record_links"]))

    def test_every_node_is_an_abstraction(self):
        abstractions = {node["abstraction"] for node in DOCUMENT["nodes"]}
        self.assertLessEqual(abstractions, set(DOCUMENT["model"]["abstractions"]))

    def test_every_edge_endpoint_exists(self):
        for edge in DOCUMENT["edges"]:
            self.assertIn(edge["source"], NODES, edge["id"])
            self.assertIn(edge["target"], NODES, edge["id"])

    def test_mentions_are_not_edges(self):
        pairs = {(edge["source"], edge["target"]) for edge in DOCUMENT["edges"]}
        for mention in DOCUMENT["mentions"]:
            self.assertNotIn((mention["from"], mention["to"]), pairs)

    def test_composition_does_not_cross_packages(self):
        for edge in DOCUMENT["edges"]:
            if edge["relation"] != "compose":
                continue
            self.assertEqual(
                NODES[edge["source"]]["plugin"],
                NODES[edge["target"]]["plugin"],
                edge["id"],
            )

    def test_handoff_connects_work_states_only(self):
        handoffs = [edge for edge in DOCUMENT["edges"] if edge["relation"] == "handoff"]
        self.assertTrue(handoffs)
        for edge in handoffs:
            self.assertEqual(NODES[edge["source"]]["abstraction"], "work", edge["id"])
            self.assertEqual(NODES[edge["target"]]["abstraction"], "work", edge["id"])

    def test_every_relation_has_a_declaration_site(self):
        for edge in DOCUMENT["edges"]:
            self.assertTrue(edge["provenance"]["file"], edge["id"])
            self.assertIn(edge["confidence"], {"declared", "derived"}, edge["id"])

    def test_counts_match_the_collections(self):
        counts = DOCUMENT["counts"]
        self.assertEqual(counts["edges"], len(DOCUMENT["edges"]))
        self.assertEqual(counts["mentions"], len(DOCUMENT["mentions"]))
        self.assertEqual(counts["capabilities"], sum(1 for node in DOCUMENT["nodes"] if node["abstraction"] == "capability"))
        self.assertEqual(counts["records"], sum(1 for node in DOCUMENT["nodes"] if node["abstraction"] == "record"))
        self.assertEqual(counts["work"], sum(1 for node in DOCUMENT["nodes"] if node["abstraction"] == "work"))
        self.assertEqual(sum(counts["by_relation"].values()), counts["edges"])

    def test_edge_ids_are_unique(self):
        ids = [edge["id"] for edge in DOCUMENT["edges"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_capability_phases_use_the_schema_vocabulary(self):
        for node in DOCUMENT["nodes"]:
            if node["abstraction"] == "capability":
                self.assertIn(node["phase"], skill_schema.PHASES, node["id"])

    def test_record_links_are_present(self):
        counts = DOCUMENT["counts"]["by_relation"]
        self.assertGreater(counts.get("produces", 0), 0)
        self.assertGreater(counts.get("guided-by", 0), 0)

    def test_build_is_deterministic(self):
        self.assertEqual(skill_graph.comparable(DOCUMENT), skill_graph.comparable(skill_graph.build()))

    def test_routers_are_the_only_route_edges(self):
        for edge in DOCUMENT["edges"]:
            if edge["relation"] == "route":
                self.assertEqual(edge["mechanism"], "alias", edge["id"])
                self.assertTrue(NODES[edge["source"]]["explicit"], edge["id"])


if __name__ == "__main__":
    unittest.main()
