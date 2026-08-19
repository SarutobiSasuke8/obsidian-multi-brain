import tempfile
import unittest
from pathlib import Path

from scripts import validate


class ValidatorTests(unittest.TestCase):
    def test_repository_contract_passes(self) -> None:
        self.assertEqual([], validate.run_checks())

    def test_frontmatter_parser_reads_scalar_contract(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            note = Path(temporary_directory) / "note.md"
            note.write_text("---\ntype: agent-context\ntier: public-safe\n---\n", encoding="utf-8")
            fields, error = validate.parse_frontmatter(note)
        self.assertIsNone(error)
        self.assertEqual("agent-context", fields["type"])
        self.assertEqual("public-safe", fields["tier"])

    def test_private_home_path_is_rejected(self) -> None:
        self.assertTrue(validate.contains_private_path("C:\\Users\\example\\Private Vault"))
        self.assertTrue(validate.contains_private_path("/home/example/private-vault"))
        self.assertFalse(validate.contains_private_path("[absolute path to the satellite]"))

    def test_credential_shape_is_rejected(self) -> None:
        fake_key = "api_key=" + ("x" * 24)
        self.assertIsNotNone(validate.CREDENTIAL_SHAPE.search(fake_key))
        self.assertIsNone(validate.CREDENTIAL_SHAPE.search("credentials stay outside the vault"))


if __name__ == "__main__":
    unittest.main()
