"""Run the three hypothesis tests at a shared Bonferroni threshold; aggregate output only."""
import argparse, csv, json, sys
from pathlib import Path
import numpy as np
from scipy import stats
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from group_power import fisher_power

GROUPS=("International","Domestic")
THRESHOLD=.05/3
SNAPSHOT_ROWS=54

def group_table(rows,reversed_record=lambda r:False):
    table=[]
    for group in GROUPS:
        correct=[(r["detect_correct"]=="1")!=reversed_record(r) for r in rows if r["student_background"]==group]
        table.append([sum(correct),len(correct)-sum(correct)])
    return table

def fisher(table):
    return {"table":table,"p":float(stats.fisher_exact(table).pvalue)}

def group_test(rows):
    """H1: detection accuracy by student background."""
    table=group_table(rows)
    scores=[np.repeat([1.,0.],row) for row in table]
    # The course's interval: Welch t on the 0/1 scores, in place of an odds ratio.
    welch=stats.ttest_ind(scores[0],scores[1],equal_var=False).confidence_interval()
    expected=stats.contingency.expected_freq(table)
    return {"groups":{g:{"correct":a,"incorrect":b,"n":a+b,"proportion":a/(a+b)} for g,(a,b) in zip(GROUPS,table)},
            "difference_in_proportions":float(scores[0].mean()-scores[1].mean()),"difference_ci95_welch_t":[float(welch.low),float(welch.high)],
            "expected_counts":expected.tolist(),"reject_at_threshold":bool(stats.fisher_exact(table).pvalue<THRESHOLD),**fisher(table)}

def quality_test(rows):
    """H2: paired original-minus-AI composite difference."""
    test=stats.ttest_rel([float(r["quality_O"]) for r in rows],[float(r["quality_AI"]) for r in rows])
    return {"t":float(test.statistic),"df":int(test.df),"p":float(test.pvalue),"reject_at_threshold":bool(test.pvalue<THRESHOLD)}

def detection_test(rows,reversed_record=lambda r:False):
    """H3: overall detection accuracy against chance."""
    correct=[(r["detect_correct"]=="1")!=reversed_record(r) for r in rows]
    k=sum(correct);n=len(correct)
    test=stats.chisquare([k,n-k],[n/2,n/2])
    interval=stats.ttest_1samp(np.array(correct,dtype=float),.5).confidence_interval()
    return {"correct":k,"n":n,"proportion":k/n,"proportion_minus_chance":k/n-.5,"ci95_t":[float(interval.low),float(interval.high)],"chi2":float(test.statistic),"df":1,"p":float(test.pvalue),"reject_at_threshold":bool(test.pvalue<THRESHOLD)}

def chi_square_power(n,rate,alpha):
    """Sum binomial probabilities over the counts that the goodness-of-fit test rejects."""
    counts=np.arange(n+1)
    statistic=(counts-n/2)**2/(n/2)*2
    return float(stats.binom.pmf(counts,n,rate)[stats.chi2.sf(statistic,1)<=alpha].sum())

def first_n_with_power(rate,alpha,target=.8):
    return next(n for n in range(2,5000) if chi_square_power(n,rate,alpha)>=target)

def first_n_per_group(rate_1,rate_2,alpha,target=.8):
    return next(n for n in range(2,500) if fisher_power(n,n,rate_1,rate_2,alpha=alpha)>=target)

def confidence_test(rows):
    """Exploratory: confidence for correct versus incorrect choices."""
    good=[float(r["confidence"]) for r in rows if r["detect_correct"]=="1"]
    bad=[float(r["confidence"]) for r in rows if r["detect_correct"]=="0"]
    test=stats.mannwhitneyu(good,bad)
    return {"correct_n":len(good),"correct_mean":float(np.mean(good)),"incorrect_n":len(bad),"incorrect_mean":float(np.mean(bad)),"mean":float(np.mean(good+bad)),"median":float(np.median(good+bad)),"mann_whitney_u":float(test.statistic),"p":float(test.pvalue)}

def summarize(raw):
    rows=[r for r in raw if r["included"]=="1"]
    legacy=lambda r:r["status"]=="Yes"
    position=lambda r:int(r["response_id"].lstrip("R"))
    planned=[r for r in raw if r["student_background"] in GROUPS and r["included_both_wrong_rule"]=="1"]
    n=[sum(r["student_background"]==g for r in rows) for g in GROUPS]
    return {"threshold":THRESHOLD,"n":len(rows),
            "H1_group_difference":group_test(rows),"H2_quality":quality_test(rows),"H3_overall_detection":detection_test(rows),
            "H1_sensitivity":{"planned_both_wrong_rule":fisher(group_table(planned)),"legacy_record_omitted":fisher(group_table([r for r in rows if not legacy(r)])),
                              "legacy_record_reversed":fisher(group_table(rows,legacy)),"status_student_only":fisher(group_table([r for r in rows if r["status"]=="Student"])),
                              "without_responses_after_row_54":fisher(group_table([r for r in rows if position(r)<=SNAPSHOT_ROWS]))},
            "H3_sensitivity":{"planned_both_wrong_rule_students":detection_test(planned),"planned_both_wrong_rule_all_respondents":detection_test([r for r in raw if r["included_both_wrong_rule"]=="1"]),
                              "legacy_record_omitted":detection_test([r for r in rows if not legacy(r)]),"legacy_record_reversed":detection_test(rows,legacy)},
            "confidence_exploratory":confidence_test(rows),
            "H3_power_assumed_rates":[{"rate":x,"first_n_80_at_05":first_n_with_power(x,.05),"first_n_80_at_threshold":first_n_with_power(x,THRESHOLD),"power_at_n_05":chi_square_power(len(rows),x,.05),"power_at_n_threshold":chi_square_power(len(rows),x,THRESHOLD)} for x in (.6,.7,.8)],
            "H1_future_n_per_group_30_vs_60":{"at_05":first_n_per_group(.3,.6,.05),"at_threshold":first_n_per_group(.3,.6,THRESHOLD)},
            "H1_power_assumed_rates":[{"rate_1":a,"rate_2":b,"power_at_05":fisher_power(*n,a,b),"power_at_threshold":fisher_power(*n,a,b,alpha=THRESHOLD)} for a,b in ((.5,.7),(.3,.6),(.5,.8),(.1,.6))]}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True);p.add_argument("--output",required=True)
    a=p.parse_args()
    with open(a.input,newline="") as f: raw=list(csv.DictReader(f))
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(summarize(raw),indent=2,allow_nan=False)+"\n")
if __name__=="__main__":main()
