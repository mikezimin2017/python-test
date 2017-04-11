import json
from pathlib import Path
from collections import OrderedDict

def convert_from_file(file_name):
    content = Path(file_name).read_text()
    return convert(content)

def convert(json_content):
    block = json.loads(json_content, object_pairs_hook=OrderedDict)
    return build_block(block)

def build_block(block):
    if isinstance(block, str):
        return block
    elif isinstance(block, list):
        result = ''
        for element in block:
            result += build_tag('li', build_block(element))
        return build_tag('ul', result)
    elif isinstance(block, OrderedDict):
        result = ''
        for tag, content in block.items():
            result += build_tag(tag, content)
        return result
    
def build_tag(name, content):
    return '<{0}>{1}</{0}>'.format(name, build_block(content))