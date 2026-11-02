"""Prospective paired-t sensitivity scenarios; not observed/post hoc power."""
import argparse, csv, math
from pathlib import Path
from scipy import stats, optimize

def power(n,dz,alpha):
    critical=stats.t.isf(alpha/2,n-1)
    return float(stats.nct.sf(critical,n-1,dz*math.sqrt(n))+stats.nct.cdf(-critical,n-1,dz*math.sqrt(n)))
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n",type=int,default=30);p.add_argument("--alpha",type=float,default=.05)
    p.add_argument("--target",type=float,default=.8);p.add_argument("--output",required=True)
    a=p.parse_args()
    if a.n<2 or not 0<a.alpha<a.target<1: raise ValueError("Invalid power parameters")
    rows=[]
    for dz in (.3,.5,.8):
        n=2
        while power(n,dz,a.alpha)<a.target and n<100000: n+=1
        rows.append(dict(assumed_dz=dz,alpha=a.alpha,target_power=a.target,required_complete_pairs=n,planned_pairs=a.n,power_at_planned_n=power(a.n,dz,a.alpha)))
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    print(f"Minimum detectable dz at n={a.n}: {optimize.brentq(lambda d:power(a.n,d,a.alpha)-a.target,.001,10):.4f}")
if __name__=="__main__":main()
