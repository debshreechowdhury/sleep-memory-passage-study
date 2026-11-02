"""Assemble owner-written sections in course order; fail on missing/empty input."""
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def assemble():
    report = ROOT/'report'
    manifest = json.loads((report/'sections.json').read_text())
    chunks = []
    for section in manifest:
        if section['heading']:
            chunks.append('## '+section['heading'])
        for filename in section['files']:
            path = report/filename
            text = path.read_text().strip()
            if not text:
                raise ValueError(f'Empty section: {filename}')
            chunks.append(text)
    text = '\n\n'.join(chunks)+'\n'
    for target in re.findall(r'!\[[^]]*\]\(([^)]+)\)',text):
        if not (report/target).resolve().is_file():
            raise ValueError(f'Missing figure: {target}')
    (report/'report.md').write_text(text)
    print('Assembled report/report.md from owner files')

if __name__=='__main__': assemble()
