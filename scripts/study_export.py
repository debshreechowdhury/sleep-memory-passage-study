"""Verified Forms loader. Identifiers and optional free text never enter analytic rows."""
import csv
import hashlib
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent/'data'))
from clean import clean_row


def load_export(path):
    path = Path(path)
    with path.open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.reader(handle)
        headers = next(reader)
        expected = json.loads((Path(__file__).resolve().parents[1] / 'config/report_export_headers.json').read_text())
        if headers != expected:
            raise ValueError('Export schema changed; review mapping before analysis')
        rows = []
        for i, raw in enumerate(reader, 1):
            if len(raw) != len(headers):
                raise ValueError('Malformed response width')
            item = dict(response_id=f'R{i:03}', order='AI first', status=raw[1], consent=raw[2],
                        detect=raw[13], confidence=raw[14], check_1=raw[8], check_2=raw[12])
            for pos, start in ((1, 5), (2, 9)):
                for j, name in enumerate(('clear', 'engage', 'write')):
                    item[f'{name}_{pos}'] = raw[start+j]
            scored = clean_row(item)
            text = raw[3].strip().lower()
            if text.startswith('international'):
                scored['student_background'] = 'International'
            elif text.startswith('domestic'):
                scored['student_background'] = 'Domestic'
            elif text.startswith('not applicable'):
                scored['student_background'] = 'Not applicable'
            else:
                raise ValueError('Unexpected student-background category; review mapping')
            rows.append(scored)
    return rows, hashlib.sha256(path.read_bytes()).hexdigest()
