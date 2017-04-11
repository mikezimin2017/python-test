# -*- coding: utf-8 -*-

from .context import jsontohtml
from pathlib import Path
import unittest


class TestSuite3(unittest.TestCase):

    def test_convert(self):
        result = jsontohtml.convert_from_file('tests/test4-source.json')
        assert result == Path('tests/test4-result.html').read_text()

if __name__ == '__main__':
    unittest.main()
