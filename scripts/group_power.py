"""Retrospective exact Fisher power scenarios; assumed rates, never observed power."""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy import stats


def fisher_power(n1, n2, p1, p2, alpha=.05):
    total = n1+n2
    reject_probability = 0.0
    for successes in range(total+1):
        a = np.arange(max(0, successes-n2), min(n1, successes)+1)
        conditional = stats.hypergeom.pmf(a, total, successes, n1)
        # Two-sided probability ordering used by scipy.stats.fisher_exact.
        sorted_p = np.sort(conditional)
        cumulative = np.cumsum(sorted_p)
        indices = np.searchsorted(sorted_p, conditional*(1+1e-12), side='right')-1
        reject = cumulative[indices] <= alpha+1e-12
        joint = stats.binom.pmf(a, n1, p1)*stats.binom.pmf(successes-a, n2, p2)
        reject_probability += float(joint[reject].sum())
    return reject_probability


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True); args = parser.parse_args()
    scenarios = []
    for p1,p2 in ((.4,.6),(.3,.6),(.3,.7)):
        for n in (15,30,50,100):
            scenarios.append(dict(n_per_group=n, assumed_accuracy_group_1=p1, assumed_accuracy_group_2=p2,
                                  alpha=.05, exact_fisher_power=fisher_power(n,n,p1,p2)))
    result = dict(timing='Retrospective illustrative planning; no rates estimated from observed groups',
                  test='Two-sided Fisher exact, probability-ordered tails; independent binomial groups',
                  target_power=.8, scenarios=scenarios)
    Path(args.output).write_text(json.dumps(result, indent=2)+'\n')

if __name__ == '__main__':
    main()
