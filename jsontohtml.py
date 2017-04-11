import json
from pathlib import Path
from collections import OrderedDict
import html
import re

def convert_from_file(file_name):
    content = Path(file_name).read_text()
    return convert(content)

def convert(json_content):
    block = json.loads(json_content, object_pairs_hook=OrderedDict)
    return build_block(block)

def build_block(block):
    if isinstance(block, str):
        return html.escape(block, quote=False)
    elif isinstance(block, list):
        result = ''.join(
            build_tag('li', build_block(element))
            for element in block
        )
        return build_tag('ul', result)
    elif isinstance(block, OrderedDict):
        result = ''.join(
            build_tag(tag, build_block(content))
            for tag, content in block.items()
        )
        return result
    
def build_tag(tag, text):
    name = re.search(r"[\w\d\-]+", tag).group(0)
    id = re.search(r"\#([\w\d\-]+)", tag)
    id_attr = ' id="{0}"'.format(id.group(1)) if id else ''
    classes = re.findall(r"\.([\w\d\-]+)", tag)
    classes_attr = ' class="{0}"'.format(' '.join(classes)) if classes else ''
    return '<{0}{2}{3}>{1}</{0}>'.format(name, text, id_attr, classes_attr)