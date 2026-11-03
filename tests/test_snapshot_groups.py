import sys
import unittest
from pathlib import Path
import numpy as np
from scipy import stats
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'scripts'))
from group_power import fisher_power
from snapshot_group_analysis import group_comparison

class GroupEvidence(unittest.TestCase):
    def test_fisher_power_matches_exhaustive_tables(self):
        for n1,n2 in ((3,4),(6,5)):
            expected = 0
            for a in range(n1+1):
                for b in range(n2+1):
                    if stats.fisher_exact([[a,n1-a],[b,n2-b]]).pvalue <= .05+1e-12:
                        expected += stats.binom.pmf(a,n1,.3)*stats.binom.pmf(b,n2,.7)
            self.assertAlmostEqual(fisher_power(n1,n2,.3,.7), expected, places=12)

    def test_group_denominator_and_odds_direction(self):
        rows = [dict(group=g,detect_correct=c) for g,answers in [('A',[1]*7+[0]*4),('B',[1]+[0]*5),('NA',[1])]
                for c in answers]
        result = group_comparison(rows,'group',['A','B'])
        self.assertEqual(result['table'],[[7,4],[1,5]])
        self.assertEqual(result['excluded_from_comparison'],1)
        self.assertGreater(result['conditional_odds_ratio_first_vs_second'],1)
        self.assertAlmostEqual(result['fisher_two_sided_p'],stats.fisher_exact([[7,4],[1,5]]).pvalue)

if __name__ == '__main__': unittest.main()
