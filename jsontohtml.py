import json
from pathlib import Path
from collections import OrderedDict

def convert_from_file(file_name):
    content = Path(file_name).read_text()
    return convert(content)

def convert(json_content):
    blocks = json.loads(json_content, object_pairs_hook=OrderedDict)
    html = ''
    for block in blocks:
        for tag, content in block.items():
            html += build_tag(tag, content)
    return html
    
def build_tag(name, content):
    return '<{0}>{1}</{0}>'.format(name, content)
