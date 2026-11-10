"""Deterministic ECR structural checker regression tests."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "plugins/development/skills/engineering-artifacts/scripts/check_ecr.py"
spec = importlib.util.spec_from_file_location("check_ecr", MODULE)
check_ecr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_ecr)


def example():
    return "\n".join(
        f"## {index}. {heading}\n\n"
        + ("Pending" if index in (4, 5, 6) else "Evidence, outcome and linked decision.")
        for index, heading in enumerate(check_ecr.SECTIONS, 1)
    )


class TestEcrContract(unittest.TestCase):
    def test_valid_ecr_with_pending_sections(self):
        self.assertEqual(check_ecr.validate(example()), [])

    def test_accept_ampersand_variant(self):
        self.assertEqual(
            check_ecr.validate(example().replace("Overview and lifecycle", "Overview & lifecycle")),
            [],
        )

    def test_reject_missing_or_out_of_order_section(self):
        missing = example().replace("## 4. Solution design\n\nPending\n", "")
        self.assertTrue(any("seven unique" in msg for msg in check_ecr.validate(missing)))
        out_of_order = example().replace("## 2. Problem and scope", "## 6. Problem and scope")
        self.assertTrue(check_ecr.validate(out_of_order))

    def test_reject_blank_section(self):
        damaged = example().replace("## 4. Solution design\n\nPending", "## 4. Solution design\n\n")
        self.assertTrue(any("empty" in msg for msg in check_ecr.validate(damaged)))

    def test_reject_unexplained_na_and_blocker(self):
        damaged = example().replace("## 4. Solution design\n\nPending", "## 4. Solution design\n\nNot applicable")
        self.assertTrue(any("needs a reason" in msg for msg in check_ecr.validate(damaged)))
        damaged = example().replace("## 5. Implementation strategy\n\nPending", "## 5. Implementation strategy\n\nBlocked")
        self.assertTrue(any("reason" in msg for msg in check_ecr.validate(damaged)))

    def test_ignore_fake_headers_in_code_fences(self):
        content = example().replace(
            "## 2. Problem and scope",
            "```md\n## 7. Decision history and references\n```\n## 2. Problem and scope",
        )
        self.assertEqual(check_ecr.validate(content), [])

    def test_cli_machine_readable_result(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "ecr.md"
            path.write_text(example(), encoding="utf-8")
            self.assertEqual(check_ecr.main([str(path), "--json"]), 0)
            path.write_text("# Missing sections\n", encoding="utf-8")
            self.assertEqual(check_ecr.main([str(path), "--json"]), 1)


if __name__ == "__main__":
    unittest.main()
