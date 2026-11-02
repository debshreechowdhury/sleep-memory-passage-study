"""Planning sensitivity at declared effects; calculated after collection began."""
import argparse,json
from pathlib import Path
from scipy import stats
from power import power

def detection_power(n,p,alpha):
    # Under p0=.5 the exact two-sided rejection tails are symmetric.
    upper=int(stats.binom.isf(alpha/2,n,.5))+1
    lower=n-upper
    return float(stats.binom.cdf(lower,n,p)+stats.binom.sf(upper-1,n,p))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',required=True);a=parser.parse_args()
    result={'timing':'Retrospective planning sensitivity, not a prospective calculation or observed power','target':.8,'paired':[],'detection':[]}
    for significance in (.05,.025):
        for effect in (.3,.5,.8):
            n=2
            while power(n,effect,significance)<.8:n+=1
            result['paired'].append(dict(alpha=significance,assumed_dz=effect,required_complete_pairs=n,power_at_30=power(30,effect,significance)))
        for accuracy in (.6,.7,.8):
            n=2
            while detection_power(n,accuracy,significance)<.8:n+=1
            result['detection'].append(dict(alpha=significance,assumed_accuracy=accuracy,first_n_with_80_percent_power=n,power_at_30=detection_power(30,accuracy,significance)))
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':main()
