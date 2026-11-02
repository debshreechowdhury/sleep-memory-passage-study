"""Verify the exact-tail shortcut against enumerated binomial tests."""
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from scipy import stats
from report_power import detection_power
class Power(unittest.TestCase):
 def test_exact_rejection_tail_matches_enumeration(self):
  for n in (20,30,49):
   for alpha in (.05,.025):
    expected=sum(stats.binom.pmf(k,n,.7) for k in range(n+1) if stats.binomtest(k,n,.5).pvalue<=alpha)
    self.assertAlmostEqual(detection_power(n,.7,alpha),expected,places=12)
if __name__=='__main__':unittest.main()
