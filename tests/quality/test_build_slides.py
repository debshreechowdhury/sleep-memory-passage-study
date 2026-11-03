"""The slide builder must produce every slide with editable charts from the committed aggregate results."""
import sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"scripts"/"quality"))
try:
    from build_slides import build, fmt_p
    from pptx import Presentation
except ImportError: build=None

@unittest.skipIf(build is None or not (ROOT/"results/quality/quality.json").exists(),"python-pptx or quality results not available")
class Slides(unittest.TestCase):
    def test_six_slides_with_native_charts_and_notes(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/"deck.pptx"
            build(ROOT/"presentation/template.pptx",out)
            deck=Presentation(out)
        self.assertEqual(len(deck.slides),6)
        self.assertEqual(sum(sh.has_chart for s in deck.slides for sh in s.shapes),3)
        self.assertTrue(all(s.has_notes_slide and s.notes_slide.notes_text_frame.text for s in deck.slides))

    def test_design_deck_has_eight_slides_with_native_charts(self):
        sys.path.insert(0,str(ROOT/"scripts"/"detection"))
        from build_design_slides import build as build_design
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/"deck.pptx"
            build_design(ROOT/"presentation/template.pptx",out)
            deck=Presentation(out)
        self.assertEqual(len(deck.slides),8)
        self.assertEqual(sum(sh.has_chart for s in deck.slides for sh in s.shapes),2)

    def test_final_deck_has_twelve_ordered_slides_with_native_charts(self):
        sys.path.insert(0,str(ROOT/"scripts"))
        from build_final_deck import build as build_final, number
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/"deck.pptx"
            build_final(ROOT/"presentation/template.pptx",out)
            deck=Presentation(out)
        self.assertEqual([number(s) for s in deck.slides],list(range(1,13)))
        self.assertEqual(sum(sh.has_chart for s in deck.slides for sh in s.shapes),4)
        self.assertTrue(all(s.notes_slide.notes_text_frame.text.startswith("Presenter: ") for s in deck.slides))

    def test_p_value_format_drops_the_leading_zero(self):
        self.assertEqual(fmt_p(.0036),".0036")
        self.assertEqual(fmt_p(.555),".555")

if __name__=="__main__":unittest.main()
