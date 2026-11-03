"""Temporary synthetic exports exercise mapping and analysis without publishing data."""
import csv,json,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class Pipeline(unittest.TestCase):
 def test_private_columns_removed_and_statistics_match(self):
  with tempfile.TemporaryDirectory() as d:
   d=Path(d);raw=d/'raw.csv';mapped=d/'mapped.csv';clean=d/'clean.csv';quality=d/'quality.json';detection=d/'detection.json'
   headers=['Name','Consent','Status','Background','Clear','Engage','Write','Check','Clear','Engage','Write','Check','Detection']
   with raw.open('w',newline='') as f:
    w=csv.writer(f);w.writerow(headers)
    for i in range(12):
     w.writerow(['SYNTHETIC PRIVATE NAME','Yes','Student','International student',str(2+i%3),str(3+i%3),str(4+i%3),'90 minutes','2','3','4','90 minutes','Passage 1' if i<9 else 'Passage 2'])
   manifest={'sources':[dict(path='raw.csv',order='AI first',expected_headers=headers,columns=dict(consent=1,status=2,student_background=3,clear_1=4,engage_1=5,write_1=6,check_1=7,clear_2=8,engage_2=9,write_2=10,check_2=11,detect=12))]}
   (d/'manifest.json').write_text(json.dumps(manifest))
   for script,args in [('data/import_forms',['--manifest',str(d/'manifest.json'),'--output',str(mapped)]),('data/clean',['--input',str(mapped),'--output',str(clean)]),('quality/quality',['--input',str(clean),'--output',str(quality)]),('detection/detection',['--input',str(clean),'--output',str(detection)])]:
    subprocess.run([sys.executable,str(ROOT/'scripts'/f'{script}.py')]+args,check=True,capture_output=True)
   self.assertNotIn('PRIVATE NAME',mapped.read_text())
   x=json.loads(quality.read_text());self.assertEqual(x['paired_n'],12)
   self.assertAlmostEqual(x['ratings']['mean_difference'],1)
   x=json.loads(detection.read_text());self.assertEqual(x['detection']['correct'],9)
   self.assertAlmostEqual(x['detection']['chi2'],3)
   manifest['sources'][0]['expected_headers']=['wrong']
   (d/'manifest.json').write_text(json.dumps(manifest))
   r=subprocess.run([sys.executable,str(ROOT/'scripts/data/import_forms.py'),'--manifest',str(d/'manifest.json'),'--output',str(mapped)],capture_output=True)
   self.assertNotEqual(r.returncode,0)
if __name__=='__main__':unittest.main()
