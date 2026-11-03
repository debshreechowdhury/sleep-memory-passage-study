"""Write detection statistics from cleaned data."""
import argparse, csv, json
from pathlib import Path
from scipy import stats

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True);p.add_argument("--output",required=True)
    a=p.parse_args()
    with open(a.input,newline="") as f: raw=list(csv.DictReader(f))
    rows=[r for r in raw if r["included"]=="1"]
    output={"raw_n":len(raw),"eligible_n":len(rows),"alpha_three_tests_bonferroni":0.05/3}
    detected=[int(r["detect_correct"]) for r in rows if r["detect_correct"]!=""]
    if detected:
        n=len(detected); k=sum(detected); 
        detection={"n":n,"correct":k,"incorrect":n-k,"accuracy":k/n,"accuracy_minus_chance":k/n-0.5}
        if n/2>=5:
            test=stats.chisquare([k,n-k],f_exp=[n/2,n/2]); detection.update(chi2=float(test.statistic),chi2_df=1,chi2_p=float(test.pvalue))
        else: detection["chi2_warning"]="Expected counts below 5; chi-square omitted"
        output["detection"]=detection
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(output,indent=2,allow_nan=False)+"\n")
if __name__=="__main__":main()
