"""Create aggregate report figures without names or response identifiers."""
import argparse,csv,json
from pathlib import Path
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--input',required=True);p.add_argument('--statistics',required=True);p.add_argument('--output-dir',required=True)
a=p.parse_args();out=Path(a.output_dir);out.mkdir(parents=True,exist_ok=True)
x=json.loads(Path(a.statistics).read_text())['filtered_current_mapping']
fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout='constrained')
d=-x['AI_minus_O'];lo=-x['ci95'][1];hi=-x['ci95'][0]
ax=axes[0];ax.errorbar(d,0,xerr=[[d-lo],[hi-d]],fmt='o',color='#315a9b',capsize=6);ax.axvline(0,color='gray',linestyle='--');ax.set_yticks([]);ax.set_xlim(-.1,.8);ax.set_xlabel('Original minus AI quality');ax.set_title('Mean difference and 95% CI')
y=x['detection'];v=y['accuracy'];lo,hi=y['ci95'];ax=axes[1];ax.errorbar(v,0,xerr=[[v-lo],[hi-v]],fmt='o',color='#a36a26',capsize=6);ax.axvline(.5,color='gray',linestyle='--');ax.set_yticks([]);ax.set_xlim(0,1);ax.xaxis.set_major_formatter(PercentFormatter(1));ax.set_xlabel('Correct AI identification');ax.set_title('Accuracy and exact 95% CI')
fig.suptitle('49 retained responses under current passage mapping',fontsize=12)
fig.savefig(out/'paired_results.png',dpi=220);plt.close(fig)
with open(a.input,encoding='utf-8-sig',newline='') as f:
 r=csv.reader(f);next(r);rows=list(r)
d=np.array([sum(map(int,r[9:12]))/3-sum(map(int,r[5:8]))/3 for r in rows if r[8]=='90 minutes' or r[12]=='90 minutes'])
fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout='constrained')
axes[0].hist(d,bins=np.arange(-1.5,3.2,1/3),color='#315a9b',edgecolor='white');axes[0].axvline(0,color='gray',linestyle='--');axes[0].set_xlabel('Original minus AI quality');axes[0].set_ylabel('Responses');axes[0].set_title('Paired difference distribution')
stats.probplot(d,dist='norm',plot=axes[1]);axes[1].set_title('Normal quantile plot');axes[1].set_ylabel('Ordered differences');axes[1].set_xlabel('Theoretical normal quantiles')
fig.savefig(out/'difference_diagnostics.png',dpi=220)
