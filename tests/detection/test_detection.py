"""Detection script runs on the synthetic fixture; values are not participant results."""
import csv, json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FIXTURE=ROOT/'tests'/'fixtures'/'synthetic_analysis.csv'

class Detection(unittest.TestCase):
    def test_counts_only_included_rows(self):
        with open(FIXTURE,newline='') as f: rows=[r for r in csv.DictReader(f) if r['included']=='1']
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'detection.json'
            subprocess.run([sys.executable,str(ROOT/'scripts'/'detection'/'detection.py'),'--input',str(FIXTURE),'--output',str(out)],check=True,capture_output=True)
            x=json.loads(out.read_text())
        self.assertEqual(x['detection']['n'],len(rows))
        self.assertEqual(x['detection']['correct'],sum(r['detect_correct']=='1' for r in rows))
if __name__=='__main__':unittest.main()
