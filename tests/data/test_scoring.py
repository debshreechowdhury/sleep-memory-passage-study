"""Synthetic validation of order reversal, missingness and exclusions."""
import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts'/'data'))
from clean import analysis_row, clean_row

def row(order='AI first'):
    return dict(response_id='synthetic',order=order,status='Student',consent='Yes, I agree',check_1='90 minutes',check_2='60 minutes',detect='Passage 1',clear_1='7',engage_1='6',write_1='5',clear_2='1',engage_2='2',write_2='3')

class Scoring(unittest.TestCase):
    def test_order_reversal_changes_versions_and_detection(self):
        a=clean_row(row());b=clean_row(row('Original first'))
        self.assertEqual((a['quality_AI'],a['quality_O'],a['detect_correct']),(6,2,1))
        self.assertEqual((b['quality_AI'],b['quality_O'],b['detect_correct']),(2,6,0))
    def test_both_wrong_excluded_one_correct_kept(self):
        r=row();self.assertEqual(clean_row(r)['included'],1)
        r['check_1']='30 minutes';self.assertIn('both_checks_wrong',clean_row(r)['exclusion_reason'])
    def test_missing_rating_does_not_become_zero(self):
        r=row();r['clear_1']='';self.assertIsNone(clean_row(r)['quality_AI'])
    def test_missing_check_flagged(self):
        r=row();r['check_2']='';self.assertIn('missing_comprehension_review',clean_row(r)['exclusion_reason'])
    def test_study_rule_keeps_students_with_both_checks_correct(self):
        r=row();r.update(check_2='90 minutes',student_background='International student')
        self.assertEqual(analysis_row(r)['included'],1)
        self.assertEqual(analysis_row(r)['student_background'],'International')
    def test_study_rule_excludes_non_students(self):
        r=row();r.update(check_2='90 minutes',student_background='Not applicable — not currently a student')
        x=analysis_row(r);self.assertEqual(x['included'],0);self.assertIn('not_a_student',x['exclusion_reason'])
    def test_study_rule_excludes_one_wrong_check_but_keeps_earlier_flag(self):
        r=row();r['student_background']='Domestic student'
        x=analysis_row(r);self.assertEqual(x['included'],0);self.assertIn('one_check_wrong',x['exclusion_reason'])
        self.assertEqual(x['included_both_wrong_rule'],1)
    def test_unknown_background_rejected(self):
        r=row();r['student_background']='Something else'
        with self.assertRaises(ValueError):analysis_row(r)
    def test_no_identifiers_leak(self):
        r=row();r['name']='Synthetic Name';r['email']='example@example.com'
        self.assertNotIn('name',clean_row(r));self.assertNotIn('email',clean_row(r))
    def test_invalid_rating_and_order_rejected(self):
        r=row();r['clear_1']='8'
        with self.assertRaises(ValueError):clean_row(r)
        r=row('Unknown')
        with self.assertRaises(ValueError):clean_row(r)
if __name__=='__main__':unittest.main()
