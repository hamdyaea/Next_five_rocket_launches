# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from RocketLaunch import summarize, fetch_launches

class RocketTests(unittest.TestCase):
    def test_nested_fields(self):
        result = summarize({"rocket": {"configuration": {"full_name": "Test Rocket"}},
                            "mission": None, "net": "2026-01-01"})
        self.assertEqual(result["Rocket"], "Test Rocket")
        self.assertEqual(result["Mission"], "")
    def test_https_only(self):
        with self.assertRaises(ValueError):
            fetch_launches("http://example.com/data.json")
    def test_missing_fields(self):
        result = summarize({})
        self.assertTrue(all(v == "" for v in result.values()))

if __name__ == "__main__":
    unittest.main()
