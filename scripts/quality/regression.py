"""Exploratory regression of the original-minus-AI difference on collected predictors; aggregate output only."""
import argparse, csv, json
from pathlib import Path
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats

PREDICTORS=("international","detect_correct","confidence")

def design(rows):
    y=np.array([float(r["quality_O"])-float(r["quality_AI"]) for r in rows])
    x=np.array([[float(r["student_background"]=="International"),float(r["detect_correct"]),float(r["confidence"])] for r in rows])
    return y,x

def fit(rows):
    y,x=design(rows)
    model=sm.OLS(y,sm.add_constant(x)).fit()
    return model

def summarize(rows):
    model=fit(rows)
    ci=model.conf_int()
    names=("intercept",)+PREDICTORS
    shapiro=stats.shapiro(model.resid)
    bp=het_breuschpagan(model.resid,model.model.exog)
    return {"outcome":"original minus AI composite","n":int(model.nobs),"df_residual":int(model.df_resid),"r_squared":float(model.rsquared),"adjusted_r_squared":float(model.rsquared_adj),
            "f":float(model.fvalue),"f_p":float(model.f_pvalue),
            "coefficients":[{"term":n,"estimate":float(model.params[i]),"se":float(model.bse[i]),"t":float(model.tvalues[i]),"p":float(model.pvalues[i]),"ci95":[float(ci[i][0]),float(ci[i][1])]} for i,n in enumerate(names)],
            "residual_shapiro":{"statistic":float(shapiro.statistic),"p":float(shapiro.pvalue)},"breusch_pagan":{"lm":float(bp[0]),"p":float(bp[1])}}

def eligible(path):
    with open(path,newline="") as f: rows=list(csv.DictReader(f))
    return [r for r in rows if r["included"]=="1" and r["quality_AI"] and r["quality_O"] and r["detect_correct"]!="" and r["confidence"]]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True);p.add_argument("--output",required=True)
    a=p.parse_args()
    result=summarize(eligible(a.input))
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(result,indent=2,allow_nan=False)+"\n")
if __name__=="__main__":main()
