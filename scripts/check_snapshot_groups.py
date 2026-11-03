"""Verify cross-output counts, source provenance, assembly and slide evidence."""
import json
from pathlib import Path
from scipy import stats
ROOT=Path(__file__).resolve().parents[1]
a=json.loads((ROOT/'results/snapshot_group_statistics.json').read_text())
b=json.loads((ROOT/'results/report_statistics.json').read_text())
c=json.loads((ROOT/'results/presentation_chart_data.json').read_text())
assert a['source_sha256']==b['source_sha256']==c['source_sha256']
assert a['retained_n']==b['filtered_current_mapping']['n']==49
for key in ('student_background','participant_status'):
    group=a[key]
    assert sum(sum(r) for r in group['table'])+group['excluded_from_comparison']==49
    assert abs(stats.fisher_exact(group['table']).pvalue-group['fisher_two_sided_p'])<1e-12
    assert sum(g['correct'] for g in group['groups'])==sum(r[0] for r in group['table'])
confidence=a['confidence']
assert sum(r['correct'] for r in confidence['levels'])==18
assert sum(r['incorrect'] for r in confidence['levels'])==31
assert c['detection']['counts']==[18,31]
assert c['groups']['student_background']['counts']==[11,6]
text=(ROOT/'report/report.md').read_text()
for phrase in ('H1:','H2:','H3:','5/14','11/12','.0053','.239','.1312','retrospective'):
    assert phrase in text, phrase
assert not (ROOT/'report/figures').exists()
print('Detection/group/confidence counts, Fisher p-values, provenance and report checked.')
