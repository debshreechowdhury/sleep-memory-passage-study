"""Write paired rating statistics from cleaned data; aggregate output only."""
import argparse, csv, hashlib, json, math
from collections import Counter
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy import stats

ITEMS=("clear","engage","write")

def alpha(items):
    # Used only by scripts/report_evidence.py for the 54-response snapshot; not in the course material, so not reported here.
    x=np.asarray(items,dtype=float)
    if len(x)<2: return None
    total=np.var(x.sum(axis=1),ddof=1)
    return float(1.5*(1-np.var(x,axis=0,ddof=1).sum()/total)) if total>0 else None

def item_correlations(rows):
    """Descriptive Pearson correlations between the items within each version."""
    result={}
    for version in ("AI","O"):
        result[version]={f"{a}_{b}":float(np.corrcoef(column(rows,f"{a}_{version}"),column(rows,f"{b}_{version}"))[0,1]) for a,b in combinations(ITEMS,2)}
    return result

def wilcoxon(d):
    # Rounding preserves mathematical ties between averages of three items.
    d=np.round(d,10)
    if not np.any(d): return None
    test=stats.wilcoxon(d,method="approx")
    return {"statistic":float(test.statistic),"p":float(test.pvalue)}

def paired(ai,orig):
    """All differences are AI minus original."""
    d=ai-orig; sd=d.std(ddof=1)
    result={"n":len(d),"mean_AI":float(ai.mean()),"mean_O":float(orig.mean()),"sd_AI":float(ai.std(ddof=1)),"sd_O":float(orig.std(ddof=1)),
            "mean_difference":float(d.mean()),"sd_difference":float(sd),"original_higher":int(np.sum(np.round(d,10)<0)),"AI_higher":int(np.sum(np.round(d,10)>0)),"ties":int(np.sum(np.round(d,10)==0))}
    if sd>0:
        test=stats.ttest_rel(ai,orig); ci=test.confidence_interval()
        result.update(t=float(test.statistic),df=len(d)-1,p=float(test.pvalue),ci95=[float(ci.low),float(ci.high)],cohen_dz=float(d.mean()/sd),wilcoxon=wilcoxon(d))
        if len(d)>=3:
            test=stats.shapiro(d);result["shapiro"]={"statistic":float(test.statistic),"p":float(test.pvalue)}
    else: result["warning"]="Zero variance in differences; t inference and standardized effect undefined"
    return result

def column(rows,name): return np.array([float(r[name]) for r in rows])

def composite(rows,swap=lambda r:False):
    ai=np.array([float(r["quality_O" if swap(r) else "quality_AI"]) for r in rows])
    orig=np.array([float(r["quality_AI" if swap(r) else "quality_O"]) for r in rows])
    return paired(ai,orig)

def item_tests(rows):
    tests=[{"item":x,**paired(column(rows,f"{x}_AI"),column(rows,f"{x}_O"))} for x in ITEMS]
    for test in tests:
        if "p" in test: test["bonferroni_p"]=min(1.,test["p"]*len(ITEMS))
    return tests

def group_comparison(rows):
    """International versus domestic on the paired difference; a subgroup check on the composite result."""
    groups={g:[r for r in rows if r.get("student_background")==g] for g in ("International","Domestic")}
    if min(len(x) for x in groups.values())<2: return {"warning":"Fewer than two complete pairs in a group"}
    a,b=[column(x,"quality_AI")-column(x,"quality_O") for x in groups.values()]
    welch=stats.ttest_ind(a,b,equal_var=False);ci=welch.confidence_interval()
    levene=stats.levene(a,b);mann=stats.mannwhitneyu(a,b)
    return {"by_group":{g:composite(x) for g,x in groups.items()},"welch":{"t":float(welch.statistic),"df":float(welch.df),"p":float(welch.pvalue),"ci95":[float(ci.low),float(ci.high)]},
            "levene":{"statistic":float(levene.statistic),"p":float(levene.pvalue)},"mann_whitney":{"statistic":float(mann.statistic),"p":float(mann.pvalue)}}

def repeated_patterns(rows):
    """Count distinct answer patterns shared by more than one row; a match does not establish a repeated participant."""
    fields=[f"{x}_{v}" for v in ("AI","O") for x in ITEMS]+["check_1","check_2","detect_correct","confidence"]
    counts=Counter(tuple(r[f] for f in fields) for r in rows)
    return sum(c>1 for c in counts.values())

def exclusion_flow(raw):
    reasons=lambda r:r["exclusion_reason"].split(";")
    students=[r for r in raw if "not_a_student" not in reasons(r)]
    return {"submissions":len(raw),"not_a_student":len(raw)-len(students),"students":len(students),
            "students_both_checks_wrong":sum("both_checks_wrong" in reasons(r) for r in students),
            "students_one_check_wrong":sum("one_check_wrong" in reasons(r) for r in students),
            "repeated_answer_patterns":repeated_patterns(raw),"repeated_answer_patterns_included":repeated_patterns([r for r in raw if r["included"]=="1"]),
            "included":sum(r["included"]=="1" for r in raw),
            "included_by_background":{g:sum(r["included"]=="1" and r.get("student_background")==g for r in raw) for g in ("International","Domestic")},
            "included_by_status":{s:sum(r["included"]=="1" and r["status"]==s for r in raw) for s in sorted({r["status"] for r in raw})}}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True);p.add_argument("--output",required=True);p.add_argument("--source")
    a=p.parse_args()
    with open(a.input,newline="") as f: raw=list(csv.DictReader(f))
    complete=lambda r:r["quality_AI"] and r["quality_O"]
    paired_rows=[r for r in raw if r["included"]=="1" and complete(r)]
    output={"raw_n":len(raw),"eligible_n":sum(r["included"]=="1" for r in raw),"paired_n":len(paired_rows),
            "difference_direction":"AI minus original","alpha_nominal":0.05,"alpha_two_test_bonferroni":0.025,"alpha_item_bonferroni":0.05/len(ITEMS),
            "exclusion_flow":exclusion_flow(raw) if raw and "student_background" in raw[0] else None}
    if a.source: output["source_sha256"]=hashlib.sha256(Path(a.source).read_bytes()).hexdigest()
    if len(paired_rows)>=2:
        output["ratings"]=composite(paired_rows)
        steps=Counter(round((float(r["quality_O"])-float(r["quality_AI"]))*3) for r in paired_rows)
        output["original_minus_AI_counts"]=[{"thirds_of_a_point":k,"respondents":steps[k]} for k in range(min(steps),max(steps)+1)]
        output["items"]=item_tests(paired_rows)
        output["group_comparison"]=group_comparison(paired_rows)
        legacy=lambda r:r["status"]=="Yes"
        earlier=[r for r in raw if r.get("included_both_wrong_rule")=="1" and complete(r)]
        output["sensitivity"]={"without_legacy_record":composite([r for r in paired_rows if not legacy(r)]),"legacy_record_reversed":composite(paired_rows,legacy),
                               "earlier_rule_all_respondents":composite(earlier) if len(earlier)>=2 else None}
        output["item_correlations"]=item_correlations(paired_rows)
    else: output["ratings"]={"warning":"Fewer than two complete pairs"}
    def finite(obj):
        if isinstance(obj,float) and not math.isfinite(obj): return None
        if isinstance(obj,dict): return {k:finite(v) for k,v in obj.items()}
        if isinstance(obj,list): return [finite(v) for v in obj]
        return obj
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(finite(output),indent=2,allow_nan=False)+"\n")
if __name__=="__main__":main()
