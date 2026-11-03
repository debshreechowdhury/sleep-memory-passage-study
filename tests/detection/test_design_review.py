"""Protect the distinction between the administered archive and corrected reference."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'scripts/detection'))
from check_design_review import check

class DesignReview(unittest.TestCase):
    def test_archive_and_current_deck_match_reviewed_evidence(self):
        check()

if __name__=='__main__':unittest.main()
