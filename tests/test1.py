# -*- coding: utf-8 -*-

from .context import jsontohtml
from pathlib import Path
import unittest


class TestSuite1(unittest.TestCase):
    """Advanced test cases."""

    def test_convert(self):
        # self.assertIsNone(False)
        result = jsontohtml.convert_from_file('tests/test1-source.json')
        assert result == Path('tests/test1-result.html').read_text()

if __name__ == '__main__':
    unittest.main()
