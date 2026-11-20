
import unittest
from app import analyze_log


class TestLogAnalysis(unittest.TestCase):

    def test_error_and_critical_count(self):
        counts, issues = analyze_log("sample.log")

        self.assertEqual(counts["ERROR"], 1)
        self.assertEqual(counts["CRITICAL"], 1)
        self.assertEqual(len(issues), 2)

    def test_warning_count(self):
        counts, issues = analyze_log("sample.log")

        self.assertEqual(counts["WARNING"], 1)


if __name__ == "__main__":
    unittest.main()
