"""Regression coefficients on clearly synthetic rows; not participant results."""
import random, sys, unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"scripts"/"quality"))
try: from regression import summarize
except ImportError: summarize=None

@unittest.skipIf(summarize is None,"statsmodels not installed")
class Regression(unittest.TestCase):
    def setUp(self):
        rng=random.Random(1)
        self.rows=[]
        for i in range(40):
            group,correct,confidence=rng.choice(("International","Domestic")),rng.randint(0,1),rng.randint(1,5)
            d=.5+.25*(group=="International")-.5*correct+.1*confidence+rng.gauss(0,.2)
            self.rows.append(dict(student_background=group,detect_correct=str(correct),confidence=str(confidence),quality_AI=str(4+d),quality_O="4"))

    def test_matches_least_squares(self):
        y=np.array([float(r["quality_AI"])-4 for r in self.rows])
        x=np.array([[1,r["student_background"]=="International",float(r["detect_correct"]),float(r["confidence"])] for r in self.rows],dtype=float)
        expected=np.linalg.lstsq(x,y,rcond=None)[0]
        result=summarize(self.rows)
        for term,value in zip(result["coefficients"],expected): self.assertAlmostEqual(term["estimate"],value)
        self.assertEqual(result["df_residual"],36)
        self.assertIn("p",result["breusch_pagan"])

if __name__=="__main__":unittest.main()
