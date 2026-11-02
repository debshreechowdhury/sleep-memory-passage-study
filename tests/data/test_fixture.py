"""The synthetic fixture must keep the same columns as real cleaned data."""
import csv, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'/'data'))
from clean import clean_row

class Fixture(unittest.TestCase):
    def test_columns_match_clean_output(self):
        row=dict(response_id='synthetic',order='AI first',status='Student',consent='Yes, I agree',check_1='90 minutes',check_2='60 minutes',detect='Passage 1',clear_1='7',engage_1='6',write_1='5',clear_2='1',engage_2='2',write_2='3')
        with open(ROOT/'tests'/'fixtures'/'synthetic_analysis.csv',newline='') as f:
            self.assertEqual(next(csv.reader(f)),list(clean_row(row)))
    def test_every_row_is_labeled_synthetic(self):
        with open(ROOT/'tests'/'fixtures'/'synthetic_analysis.csv',newline='') as f:
            self.assertTrue(all(r['response_id'].startswith('SYNTHETIC-') for r in csv.DictReader(f)))
if __name__=='__main__':unittest.main()
