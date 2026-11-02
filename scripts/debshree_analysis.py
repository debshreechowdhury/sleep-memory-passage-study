"""Exploratory detection groups and confidence; aggregate output only."""
import argparse
import json
from pathlib import Path
import numpy as np
from scipy import stats
from study_export import load_export


def group_comparison(rows, field, labels):
    groups = [[r for r in rows if r[field] == label] for label in labels]
    table = [[sum(r['detect_correct'] for r in group), sum(1-r['detect_correct'] for r in group)] for group in groups]
    if any(not group for group in groups):
        raise ValueError('Both declared groups need responses')
    test = stats.fisher_exact(table, alternative='two-sided')
    odds = stats.contingency.odds_ratio(table, kind='conditional')
    ci = odds.confidence_interval()
    summaries = []
    for label, group, (correct, incorrect) in zip(labels, groups, table):
        interval = stats.binomtest(correct, len(group)).proportion_ci()
        summaries.append(dict(label=label, n=len(group), correct=correct, incorrect=incorrect,
                              accuracy=correct/len(group), ci95=[float(interval.low), float(interval.high)]))
    return dict(field=field, groups=summaries, table_columns=['correct', 'incorrect'], table=table,
                excluded_from_comparison=len(rows)-sum(map(len, groups)), fisher_two_sided_p=float(test.pvalue),
                conditional_odds_ratio_first_vs_second=float(odds.statistic), odds_ratio_ci95=[float(ci.low), float(ci.high)],
                risk_difference_first_minus_second=summaries[0]['accuracy']-summaries[1]['accuracy'])


def confidence_summary(rows):
    good = np.array([r['confidence'] for r in rows if r['detect_correct'] == 1])
    bad = np.array([r['confidence'] for r in rows if r['detect_correct'] == 0])
    test = stats.mannwhitneyu(good, bad, alternative='two-sided', method='asymptotic', use_continuity=True)
    x = np.array([r['confidence'] for r in rows]); y = np.array([r['detect_correct'] for r in rows])
    rho = stats.spearmanr(x, y)
    # A fixed-seed permutation avoids relying only on Spearman's small-sample approximation.
    ranks = stats.rankdata(x); centered = ranks-ranks.mean(); yc = y-y.mean()
    observed = float(np.dot(centered, yc)/np.sqrt(np.dot(centered, centered)*np.dot(yc, yc)))
    rng = np.random.default_rng(510); extreme = 0; repetitions = 99999
    for start in range(0, repetitions, 1000):
        permuted = np.array([rng.permutation(yc) for _ in range(min(1000, repetitions-start))])
        values = np.sum(permuted * centered, axis=1) / np.sqrt(np.dot(centered, centered)*np.dot(yc, yc))
        extreme += int(np.sum(np.abs(values) >= abs(observed)-1e-12))
    return dict(n=len(rows), mean=float(x.mean()), median=float(np.median(x)),
                correct=dict(n=len(good), mean=float(good.mean()), median=float(np.median(good))),
                incorrect=dict(n=len(bad), mean=float(bad.mean()), median=float(np.median(bad))),
                mann_whitney_u_correct=float(test.statistic), mann_whitney_p=float(test.pvalue),
                rank_biserial_correct_minus_incorrect=float(2*test.statistic/(len(good)*len(bad))-1),
                spearman_rho=float(rho.statistic), spearman_asymptotic_p=float(rho.pvalue),
                permutation_p=(extreme+1)/(repetitions+1), permutation_repetitions=repetitions, seed=510,
                levels=[dict(level=level, correct=sum(r['confidence']==level and r['detect_correct']==1 for r in rows),
                             incorrect=sum(r['confidence']==level and r['detect_correct']==0 for r in rows)) for level in range(1, 6)])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True); parser.add_argument('--output', required=True)
    args = parser.parse_args(); rows, digest = load_export(args.input)
    keep = [r for r in rows if r['included']]
    result = dict(source_sha256=digest, raw_n=len(rows), retained_n=len(keep),
                  analysis_status='Retrospective exploratory; H3 group definition awaits team confirmation',
                  student_background=group_comparison(keep, 'student_background', ['International', 'Domestic']),
                  student_background_strict_student=group_comparison([r for r in keep if r['status']=='Student'], 'student_background', ['International', 'Domestic']),
                  participant_status=group_comparison(keep, 'status', ['Student', 'Working professional']),
                  confidence=confidence_summary(keep))
    no_legacy = [r for r in keep if r['status']!='Yes']
    reverse = [dict(r, detect_correct=1-r['detect_correct']) if r['status']=='Yes' else r for r in keep]
    result['legacy_sensitivity'] = {}
    for name, selected in [('omit', no_legacy), ('reverse', reverse)]:
        result['legacy_sensitivity'][name] = dict(student_background=group_comparison(selected, 'student_background', ['International','Domestic']),
                                                 participant_status=group_comparison(selected,'status',['Student','Working professional']),
                                                 confidence=confidence_summary(selected))
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(f'Wrote aggregate group/confidence evidence for {len(keep)} retained responses')

if __name__ == '__main__':
    main()
