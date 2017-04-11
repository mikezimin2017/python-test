import json
from pathlib import Path

def convert_from_file(fileName):
    content = Path(fileName).read_text()
    return convert(content)

def convert(jsonContent):
    blocks = json.loads(jsonContent)
    html = ''.join([
        build_tag('h1', block['title']) + build_tag('p', block['body'])
        for block in blocks    
    ])
    return html
    
def build_tag(name, content):
    return '<{0}>{1}</{0}>'.format(name, content)
