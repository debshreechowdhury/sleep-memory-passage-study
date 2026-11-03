"""Paired-t sensitivity scenarios under assumed effects; not observed/post hoc power."""
import argparse, csv, math
from pathlib import Path
from scipy import stats, optimize

def power(n,dz,alpha):
    critical=stats.t.isf(alpha/2,n-1)
    return float(stats.nct.sf(critical,n-1,dz*math.sqrt(n))+stats.nct.cdf(-critical,n-1,dz*math.sqrt(n)))
def minimum_detectable_dz(n,alpha,target):
    # Widen from a small bracket: nct returns NaN at the very large noncentralities a fixed upper bound can reach.
    upper=.5
    while power(n,upper,alpha)<target: upper*=2
    return float(optimize.brentq(lambda d:power(n,d,alpha)-target,.001,upper))
def scenarios(pairs,alphas,target):
    rows=[]
    for alpha in alphas:
        for dz in (.3,.5,.8):
            n=2
            while power(n,dz,alpha)<target and n<100000: n+=1
            rows.append(dict(assumed_dz=dz,alpha=alpha,target_power=target,required_complete_pairs=n,planned_pairs=pairs,power_at_planned_n=power(pairs,dz,alpha),minimum_detectable_dz=minimum_detectable_dz(pairs,alpha,target)))
    return rows
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n",type=int,default=30);p.add_argument("--alpha",type=float,nargs="+",default=[.05])
    p.add_argument("--target",type=float,default=.8);p.add_argument("--output",required=True)
    a=p.parse_args()
    if a.n<2 or not all(0<x<a.target<1 for x in a.alpha): raise ValueError("Invalid power parameters")
    rows=scenarios(a.n,a.alpha,a.target)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
if __name__=="__main__":main()
