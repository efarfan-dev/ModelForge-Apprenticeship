import sys
import unittest
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "exercises" / "python")
)

from assessment_01 import count_occurrences


class AssessmentTests(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(count_occurrences([]), {})

    def test_counts(self):
        self.assertEqual(
            count_occurrences(["a", "b", "a"]),
            {"a": 2, "b": 1}
        )

    def test_case_sensitive(self):
        self.assertEqual(
            count_occurrences(["Cat", "cat"]),
            {"Cat": 1, "cat": 1}
        )

    def test_unchanged(self):
        items = ["a", "a"]
        count_occurrences(items)
        self.assertEqual(items, ["a", "a"])
