# -*- coding: utf-8 -*-

from .context import jsontohtml
from pathlib import Path
import unittest


class TestSuite5(unittest.TestCase):

    def test_convert(self):
        result = jsontohtml.convert_from_file('tests/test5-source.json')
        assert result == Path('tests/test5-result.html').read_text()

    def test_simple_convert(self):
        result = jsontohtml.convert('{"p":"hello1"}')
        assert result == '<p>hello1</p>'

if __name__ == '__main__':
    unittest.main()
