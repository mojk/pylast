#!/usr/bin/env python
"""
Unit tests for pylast.py
"""
import sys
import unittest

import pytest


@pytest.mark.skipif(sys.version_info.major >= 3, reason="Requires Python 2")
class TestPyLastPython2(unittest.TestCase):
    def test_python2(self):

        with self.assertRaises(ImportError) as e:
            import pylast  # noqa
        self.assertIn(
            "pylast 3.0 and above are no longer compatible with Python 2",
            str(e.exception),
        )


if __name__ == "__main__":
    unittest.main(failfast=True)
