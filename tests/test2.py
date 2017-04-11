# -*- coding: utf-8 -*-

from .context import jsontohtml
from pathlib import Path
import unittest


class TestSuite2(unittest.TestCase):
    """Advanced test cases."""

    def test_convert(self):
        result = jsontohtml.convert_from_file('tests/test2-source.json')
        assert result == Path('tests/test2-result.html').read_text()

if __name__ == '__main__':
    unittest.main()
