"""Regenerate synthetic_analysis.csv through analysis_row. SYNTHETIC: never analyze as participant data."""
import csv, random, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"scripts"/"data"))
from clean import analysis_row

def mapped_row(i,rng):
    row=dict(response_id=f"SYNTHETIC-{i:03}",order="AI first",consent="Yes, I agree",
             status=rng.choice(("Student","Working professional","Other")),
             student_background=rng.choice(("International student","Domestic student","Not applicable")),
             check_1="90 minutes",check_2="90 minutes",detect=rng.choice(("Passage 1","Passage 2")),
             confidence=str(rng.randint(1,5)),ai_use=str(rng.randint(1,5)),english=str(rng.randint(1,7)))
    for pos in (1,2):
        for item in ("clear","engage","write"): row[f"{item}_{pos}"]=str(rng.randint(1,7))
    return row

def main():
    rng=random.Random(20261102)
    rows=[mapped_row(i,rng) for i in range(1,31)]
    rows[0].update(check_1="30 minutes",check_2="60 minutes")
    rows[1].update(clear_2="",student_background="Domestic student")
    rows[2].update(check_2="60 minutes",student_background="International student")
    cleaned=[analysis_row(r) for r in rows]
    with open(Path(__file__).with_name("synthetic_analysis.csv"),"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(cleaned[0]));w.writeheader();w.writerows(cleaned)
if __name__=="__main__":main()
