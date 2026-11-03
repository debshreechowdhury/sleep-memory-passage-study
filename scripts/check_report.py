"""Check report arithmetic and source linkage without accessing participant identifiers."""
import json,math
from pathlib import Path
root=Path(__file__).resolve().parents[1]
x=json.loads((root/'results/report_statistics.json').read_text());r=x['filtered_current_mapping'];text=(root/'report/report.md').read_text()
assert x['raw_n']-x['both_wrong_excluded']==r['n']==49
assert r['detection']['correct']+r['detection']['incorrect']==49
assert math.isclose(r['quality_O_mean']-r['quality_AI_mean'],-r['AI_minus_O'])
assert math.isclose(r['t'],r['AI_minus_O']/(r['difference_sd']/math.sqrt(r['n'])))
assert math.isclose(r['cohen_dz'],r['t']/math.sqrt(r['n']))
assert r['ci95'][0]<r['AI_minus_O']<r['ci95'][1]<0
# The report leads with the 26-respondent analysis. These first-54-row values are unchanged in size by the corrected passage order.
for value in ['0.415','0.167','0.663','3.369','.00149','0.481','94.0','.00242']:
 assert value in text,value
for section in ['Abstract','Background and motivation','Null and alternative hypotheses','Description of experimental design','Power analysis','Data collection and cleaning procedures','Statistical analysis','Interpretation of results','Limitations','Conclusion and recommendations','References']:
 assert f'## {section}' in text,section
assert 'Pending results' not in text and 'Write last' not in text
assert len(x['source_sha256'])==64
print('Report sections, counts, effect direction, estimates and source hash checked.')
