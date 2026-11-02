"""Quality script runs on the synthetic fixture; values are not participant results."""
import csv, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FIXTURE=ROOT/'tests'/'fixtures'/'synthetic_analysis.csv'

class Quality(unittest.TestCase):
    def test_counts_only_included_complete_pairs(self):
        with open(FIXTURE,newline='') as f: rows=list(csv.DictReader(f))
        expected=sum(r['included']=='1' and bool(r['quality_AI']) and bool(r['quality_O']) for r in rows)
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'quality.json'
            subprocess.run([sys.executable,str(ROOT/'scripts'/'quality'/'quality.py'),'--input',str(FIXTURE),'--output',str(out)],check=True,capture_output=True)
            x=json.loads(out.read_text())
        self.assertEqual(x['raw_n'],len(rows))
        self.assertEqual(x['paired_n'],expected)
        self.assertIn('ci95',x['ratings'])
if __name__=='__main__':unittest.main()
