"""Write paired rating and detection statistics from cleaned data."""
import argparse, csv, json, math
from pathlib import Path
import numpy as np
from scipy import stats

def alpha(items):
    x=np.asarray(items,dtype=float)
    if len(x)<2: return None
    total=np.var(x.sum(axis=1),ddof=1)
    return float(1.5*(1-np.var(x,axis=0,ddof=1).sum()/total)) if total>0 else None

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True);p.add_argument("--output",required=True)
    a=p.parse_args()
    with open(a.input,newline="") as f: raw=list(csv.DictReader(f))
    rows=[r for r in raw if r["included"]=="1"]
    paired=[r for r in rows if r["quality_AI"] and r["quality_O"]]
    output={"raw_n":len(raw),"eligible_n":len(rows),"paired_n":len(paired),
            "difference_direction":"AI minus original", "alpha_nominal":0.05,
            "multiplicity":"Unadjusted co-primary p-values; interpretation policy remains to be finalized"}
    if len(paired)>=2:
        ai=np.array([float(r["quality_AI"]) for r in paired])
        orig=np.array([float(r["quality_O"]) for r in paired])
        d=ai-orig; sd=d.std(ddof=1)
        result={"mean_AI":float(ai.mean()),"mean_O":float(orig.mean()),"mean_difference":float(d.mean()),"sd_difference":float(sd)}
        if sd>0:
            test=stats.ttest_rel(ai,orig); ci=test.confidence_interval()
            result.update(t=float(test.statistic),df=len(d)-1,p=float(test.pvalue),ci95=[float(ci.low),float(ci.high)],cohen_dz=float(d.mean()/sd))
        else: result["warning"]="Zero variance in differences; t inference and standardized effect undefined"
        result["difference_values_for_diagnostics"]=d.tolist()
        result["assumption_review"]="Inspect differences for outliers and approximate normality; independence depends on recruitment and duplicate review"
        output["ratings"]=result
        output["cronbach_alpha"]={v:alpha([[float(r[f"{x}_{v}"]) for x in ("clear","engage","write")] for r in paired]) for v in ("AI","O")}
    else: output["ratings"]={"warning":"Fewer than two complete pairs"}
    detected=[int(r["detect_correct"]) for r in rows if r["detect_correct"]!=""]
    if detected:
        n=len(detected); k=sum(detected); exact=stats.binomtest(k,n,p=0.5);ci=exact.proportion_ci()
        detection={"n":n,"correct":k,"incorrect":n-k,"accuracy":k/n,"accuracy_minus_chance":k/n-0.5,"exact_binomial_p":float(exact.pvalue),"exact_ci95":[float(ci.low),float(ci.high)]}
        if n/2>=5:
            test=stats.chisquare([k,n-k],f_exp=[n/2,n/2]); detection.update(chi2=float(test.statistic),chi2_df=1,chi2_p=float(test.pvalue),cohen_w=float(math.sqrt(test.statistic/n)))
        else: detection["chi2_warning"]="Expected counts below 5; chi-square omitted; report exact test"
        output["detection"]=detection
    def finite(obj):
        if isinstance(obj,float) and not math.isfinite(obj): return None
        if isinstance(obj,dict): return {k:finite(v) for k,v in obj.items()}
        if isinstance(obj,list): return [finite(v) for v in obj]
        return obj
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(finite(output),indent=2,allow_nan=False)+"\n")
if __name__=="__main__":main()
