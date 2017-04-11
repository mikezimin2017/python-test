import json
from pathlib import Path
from collections import OrderedDict

def convert_from_file(file_name):
    content = Path(file_name).read_text()
    return convert(content)

def convert(json_content):
    blocks = json.loads(json_content, object_pairs_hook=OrderedDict)
    ul_content = ''
    for block in blocks:
        li_content = ''
        for tag, content in block.items():
            li_content += build_tag(tag, content)
        ul_content += build_tag('li', li_content)
    return build_tag('ul', ul_content)
    
def build_tag(name, content):
    return '<{0}>{1}</{0}>'.format(name, content)
