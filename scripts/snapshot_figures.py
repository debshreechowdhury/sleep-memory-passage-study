"""Create report figures and slide chart inputs solely from aggregate results/."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def main():
    result=json.loads((ROOT/'results/snapshot_group_statistics.json').read_text())
    primary=json.loads((ROOT/'results/report_statistics.json').read_text())
    assert result['source_sha256']==primary['source_sha256']
    figures=ROOT/'results/figures';figures.mkdir(exist_ok=True)
    detection=primary['filtered_current_mapping']['detection']
    plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
    fig,ax=plt.subplots(figsize=(7.6,3.2),layout='constrained')
    value=detection['accuracy'];low,high=detection['ci95']
    ax.errorbar([value],[0],xerr=[[value-low],[high-value]],fmt='o',capsize=6,color='#15616D',markersize=9)
    ax.axvline(.5,color='#777777',linestyle='--',label='Chance (50%)')
    ax.set(xlim=(0,1),ylim=(-.5,.5),yticks=[],xlabel='Proportion correctly identifying the AI passage',title='18 of 49 correct; exact 95% interval includes chance')
    ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1));ax.legend(loc='upper right')
    fig.savefig(figures/'detection.png',dpi=180);plt.close(fig)
    fig,axes=plt.subplots(1,2,figsize=(10,4.1),layout='constrained')
    for ax,key,title in zip(axes,['student_background','participant_status'],['Self-reported student background','Current participant status']):
        groups=result[key]['groups'];values=np.array([g['accuracy'] for g in groups]);cis=np.array([g['ci95'] for g in groups])
        ax.errorbar(values,[1,0],xerr=[values-cis[:,0],cis[:,1]-values],fmt='o',capsize=5,color='#15616D')
        ax.set(yticks=[1,0],yticklabels=[f"{g['label']} ({g['correct']}/{g['n']})" for g in groups],xlim=(0,1),ylim=(-.6,1.6),title=title,xlabel='Detection accuracy')
        ax.axvline(.5,color='#999999',linestyle='--');ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(1))
    fig.savefig(figures/'detection_groups.png',dpi=180);plt.close(fig)
    confidence=result['confidence'];levels=confidence['levels']
    data=dict(chart_precision='Proportions rounded to 12 decimal places for portable editable Excel chart data; statistical outputs retain full precision',source_sha256=result['source_sha256'],retained_n=result['retained_n'],
              detection=dict(categories=['Correct','Incorrect'],counts=[detection['correct'],detection['incorrect']],accuracy=detection['accuracy'],ci95=detection['ci95'],exact_p=detection['exact_p']),
              groups={key:dict(categories=[g['label'] for g in result[key]['groups']],values=[round(g['accuracy'],12) for g in result[key]['groups']],counts=[g['n'] for g in result[key]['groups']],fisher_p=result[key]['fisher_two_sided_p']) for key in ('student_background','participant_status')},
              confidence=dict(categories=[str(x['level']) for x in levels],correct=[x['correct'] for x in levels],incorrect=[x['incorrect'] for x in levels],rho=confidence['spearman_rho'],permutation_p=confidence['permutation_p']))
    (ROOT/'results/presentation_chart_data.json').write_text(json.dumps(data,indent=2)+'\n')
    print('Wrote report figures and editable slide chart inputs under results/')
if __name__=='__main__':main()
