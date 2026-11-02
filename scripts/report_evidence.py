"""Analyze private export; write aggregate results only. No identifiers in outputs."""
import argparse,csv,json,sys,hashlib,collections,math
from pathlib import Path
import numpy as np
from scipy import stats
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--input',required=True)
parser.add_argument('--output',required=True)
args=parser.parse_args()
p=Path(args.output).parent
p.mkdir(parents=True,exist_ok=True)
sys.path.insert(0,str(Path(__file__).resolve().parent))
from clean import clean_row
from analyze import alpha
rawpath=Path(args.input)
with rawpath.open(encoding='utf-8-sig',newline='') as f:
 reader=csv.reader(f);headers=next(reader);raw=list(reader)
expected=json.loads((Path(__file__).resolve().parents[1]/'config/report_export_headers.json').read_text())
if headers != expected:
    raise ValueError('Export schema changed; review the report column mapping before analysis')
rows=[]
for i,r in enumerate(raw,1):
 x=dict(response_id=f'R{i:03}',order='AI first',status=r[1],consent=r[2],detect=r[13],confidence=r[14],check_1=r[8],check_2=r[12])
 for pos,start in ((1,5),(2,9)):
  for j,item in enumerate(('clear','engage','write')):x[f'{item}_{pos}']=r[start+j]
 rows.append(clean_row(x))

def summarize(rs):
 ai=np.array([r['quality_AI'] for r in rs]);orig=np.array([r['quality_O'] for r in rs]);d=ai-orig
 test=stats.ttest_rel(ai,orig);ci=test.confidence_interval()
 correct=np.array([r['detect_correct'] for r in rs]);k=int(correct.sum());n=len(rs)
 exact=stats.binomtest(k,n,.5);pci=exact.proportion_ci();chi=stats.chisquare([k,n-k],[n/2,n/2])
 w=stats.wilcoxon(np.round(d,10),method='approx')
 dif3=[]
 for item in ('clear','engage','write'):
  a=np.array([r[f'{item}_AI'] for r in rs]);o=np.array([r[f'{item}_O'] for r in rs]);t=stats.ttest_rel(a,o);c=t.confidence_interval()
  dif3.append(dict(item=item,mean_AI=float(a.mean()),sd_AI=float(a.std(ddof=1)),mean_O=float(o.mean()),sd_O=float(o.std(ddof=1)),difference=float((a-o).mean()),p=float(t.pvalue),ci95=[float(c.low),float(c.high)]))
 confidence=np.array([r['confidence'] for r in rs]);corr=stats.spearmanr(confidence,correct)
 return dict(n=n,quality_AI_mean=float(ai.mean()),quality_O_mean=float(orig.mean()),quality_AI_sd=float(ai.std(ddof=1)),quality_O_sd=float(orig.std(ddof=1)),AI_minus_O=float(d.mean()),difference_sd=float(d.std(ddof=1)),t=float(test.statistic),df=n-1,p=float(test.pvalue),ci95=[float(ci.low),float(ci.high)],cohen_dz=float(d.mean()/d.std(ddof=1)),original_higher=int(sum(d<0)),AI_higher=int(sum(d>0)),ties=int(sum(d==0)),cronbach_alpha={v:alpha([[r[f'{x}_{v}'] for x in ('clear','engage','write')] for r in rs]) for v in ('AI','O')},shapiro_differences=dict(statistic=float(stats.shapiro(d).statistic),p=float(stats.shapiro(d).pvalue)),difference_range=[float(d.min()),float(d.max())],wilcoxon_sensitivity=dict(statistic=float(w.statistic),p=float(w.pvalue),note='Exploratory normal approximation; ties/zeros present; two-sided; differences rounded to 10 decimals to preserve mathematical ties'),items_exploratory=dif3,detection=dict(correct=k,incorrect=n-k,accuracy=k/n,exact_p=float(exact.pvalue),ci95=[float(pci.low),float(pci.high)],chi2=float(chi.statistic),chi2_p=float(chi.pvalue),cohen_w=float(math.sqrt(chi.statistic/n))),confidence=dict(mean=float(confidence.mean()),correct_mean=float(confidence[correct==1].mean()),incorrect_mean=float(confidence[correct==0].mean()),spearman_r=float(corr.statistic),spearman_p=float(corr.pvalue)),status_counts=dict(collections.Counter(r['status'] for r in rs)))
keep=[r for r in rows if r['included']]
no_legacy=[r for r in keep if r['status']!='Yes']
reverse=[dict(r) for r in keep]
for r in reverse:
 if r['status']=='Yes':
  for item in ('clear','engage','write','quality'):r[f'{item}_AI'],r[f'{item}_O']=r[f'{item}_O'],r[f'{item}_AI']
  r['detect_correct']=1-r['detect_correct']
result=dict(source_sha256=hashlib.sha256(rawpath.read_bytes()).hexdigest(),raw_n=len(raw),both_wrong_excluded=len(rows)-len(keep),missing_core=0,assumption='Current form AI first; legacy first response version uncertain',filtered_current_mapping=summarize(keep),sensitivity_without_legacy=summarize(no_legacy),sensitivity_legacy_original_first=summarize(reverse),unfiltered=summarize(rows))
Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
print(f'Wrote aggregate statistics for {len(raw)} submissions to {args.output}')
