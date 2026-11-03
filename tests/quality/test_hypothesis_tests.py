"""The three planned tests on clearly synthetic rows; not participant results."""
import sys, unittest
from pathlib import Path
from scipy import stats
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"scripts"/"quality"))
from hypothesis_tests import THRESHOLD, chi_square_power, confidence_test, first_n_with_power, summarize

def row(i,group,correct,status="Student",included="1",earlier="1"):
    return dict(response_id=f"R{i:05}",student_background=group,detect_correct=str(correct),status=status,included=included,included_both_wrong_rule=earlier,quality_AI=str(4+(i%3)),quality_O="4",confidence=str(1+i%5))

class HypothesisTests(unittest.TestCase):
    def setUp(self):
        answers=[("International",1)]*9+[("International",0)]*5+[("Domestic",1)]*1+[("Domestic",0)]*11
        self.rows=[row(i+1,g,c) for i,(g,c) in enumerate(answers)]
        self.rows.append(row(100,"Not applicable",1,"Working professional","0","1"))
        self.rows.append(row(101,"International",0,"Student","0","1"))
        self.result=summarize(self.rows)

    def test_threshold_covers_three_planned_tests(self):
        self.assertAlmostEqual(THRESHOLD,.05/3)

    def test_group_comparison_uses_included_students_only(self):
        x=self.result["H1_group_difference"]
        self.assertEqual(x["table"],[[9,5],[1,11]])
        self.assertAlmostEqual(x["p"],stats.fisher_exact([[9,5],[1,11]]).pvalue)
        self.assertAlmostEqual(x["difference_in_proportions"],9/14-1/12)

    def test_planned_rule_adds_one_check_failures_but_not_non_students(self):
        self.assertEqual(self.result["H1_sensitivity"]["planned_both_wrong_rule"]["table"],[[9,6],[1,11]])

    def test_overall_detection_is_chi_square_against_half(self):
        x=self.result["H3_overall_detection"]
        self.assertEqual((x["correct"],x["n"]),(10,26))
        self.assertAlmostEqual(x["p"],stats.chisquare([10,16],[13,13]).pvalue)

    def test_chi_square_power_counts_only_rejected_outcomes(self):
        self.assertAlmostEqual(chi_square_power(10,.5,.05),stats.binom.pmf([0,1,9,10],10,.5).sum())
        self.assertLessEqual(chi_square_power(first_n_with_power(.7,.05),.7,.05),1)
        self.assertGreaterEqual(chi_square_power(first_n_with_power(.7,.05),.7,.05),.8)

    def test_confidence_uses_correct_versus_incorrect_groups(self):
        rows=[dict(r,confidence=str(1+i%5)) for i,r in enumerate(self.rows) if r["included"]=="1"]
        x=confidence_test(rows)
        self.assertEqual((x["correct_n"],x["incorrect_n"]),(10,16))

if __name__=="__main__":unittest.main()
