"""Power scenarios use assumed effects only; no participant data."""
import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"scripts"/"quality"))
from power import minimum_detectable_dz, power, scenarios

class Power(unittest.TestCase):
    def test_required_pairs_match_the_report_table(self):
        self.assertEqual([r["required_complete_pairs"] for r in scenarios(30,[.05,.025],.8)],[90,34,15,109,41,18])

    def test_minimum_detectable_effect_reaches_target_power(self):
        for n,alpha in ((30,.05),(49,.025)):
            self.assertAlmostEqual(power(n,minimum_detectable_dz(n,alpha,.8),alpha),.8,places=6)

    def test_matches_course_power_tool(self):
        try: from statsmodels.stats.power import TTestPower
        except ImportError: self.skipTest("statsmodels not installed")
        self.assertAlmostEqual(power(49,.5,.025),TTestPower().power(.5,49,.025),places=6)

if __name__=="__main__":unittest.main()
