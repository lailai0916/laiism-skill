import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("checker", ROOT / "scripts/check_repository.py")
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class RepositoryTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "positions.json").read_text(encoding="utf-8"))

    def test_existing_material(self):
        self.assertEqual(checker.check_positions(self.data), [])

    def test_confirmation_is_required(self):
        self.data["positions"][0].pop("confirmation")
        self.assertTrue(checker.check_positions(self.data))

    def test_migration_does_not_ratify(self):
        self.data["positions"][0]["doctrine_status"] = "ratified"
        self.assertTrue(checker.check_positions(self.data))

    def test_distinct_doctrinal_approval(self):
        item = self.data["positions"][0]
        item["doctrine_status"] = "ratified"
        item["ratification"] = copy.deepcopy(item["confirmation"])
        self.assertTrue(checker.check_positions(self.data))
        item["ratification"] = {
            "date": "2026-01-01",
            "statement": "Synthetic approval fixture, not a real user statement.",
            "approved_by": "lailai",
            "scope": "doctrine",
            "content_sha256": checker.content_digest(item),
        }
        self.assertEqual(checker.check_positions(self.data), [])
        item["personal_status"] = "unconfirmed"
        self.assertTrue(checker.check_positions(self.data))

    def test_ratification_is_bound_to_text(self):
        item = self.data["positions"][0]
        item["doctrine_status"] = "ratified"
        item["ratification"] = {
            "date": "2026-01-01",
            "statement": "Synthetic approval fixture, not a real user statement.",
            "approved_by": "lailai",
            "scope": "doctrine",
            "content_sha256": checker.content_digest(item),
        }
        self.assertEqual(checker.check_positions(self.data), [])
        item["content"] += " Changed claim."
        self.assertTrue(checker.check_positions(self.data))

    def test_invalid_or_duplicate_id(self):
        self.data["positions"].append(copy.deepcopy(self.data["positions"][0]))
        self.assertTrue(checker.check_positions(self.data))
        self.data["positions"][-1]["id"] = 42
        self.assertTrue(checker.check_positions(self.data))

    def test_bad_status_and_source(self):
        for field, value in (("personal_status", "maybe"), ("personal_status", []), ("doctrine_status", "maybe"), ("source", None)):
            with self.subTest(field=field):
                data = copy.deepcopy(self.data)
                data["positions"][0][field] = value
                self.assertTrue(checker.check_positions(data))

    def test_brand_case(self):
        self.assertEqual(checker.check_text("note.txt", "laiism\n"), [])
        for spelling in ("laiism".capitalize(), "laiism".upper()):
            self.assertTrue(checker.check_text("note.txt", spelling + "\n"))
            self.assertTrue(checker.check_text(spelling + ".txt", "content\n"))

    def test_links_and_newline(self):
        self.assertTrue(checker.check_text("README.md", "[missing](does-not-exist.md)\n"))
        self.assertEqual(checker.check_text("README.md", "[entry](SKILL.md)\n"), [])
        self.assertTrue(checker.check_text("note.txt", "no final newline"))

    def test_readme_publication_boundary(self):
        path = ROOT / "README.md"
        self.assertEqual(checker.check_readme(path, "lailai0916/laiism-skill", False, True), [])
        self.assertTrue(checker.check_readme(path, "lailai0916/laiism-skill", False, False))
        with tempfile.TemporaryDirectory() as directory:
            other = Path(directory) / "README.md"
            other.write_text(path.read_text(encoding="utf-8").replace("<h1>laiism</h1>", "<h1>other</h1>"), encoding="utf-8")
            self.assertTrue(checker.check_readme(other, "lailai0916/laiism-skill", False, True))

    def test_project_tree_comment_alignment(self):
        for name in ("README.md", "README.zh-Hans.md"):
            path = ROOT / name
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.startswith(("├", "└")) and "#" in line:
                    self.assertEqual(line.index("#"), checker.TREE_COMMENT_MIN_INDEX)


if __name__ == "__main__":
    unittest.main()
