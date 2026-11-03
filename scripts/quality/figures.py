"""Create quality figures from cleaned data; no identifiers or response IDs appear."""
import argparse, json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from regression import eligible, fit

BLUE,INK,MUTED,GRID="#315a9b","#1f2933","#5f6c76","#d9dee3"
plt.rcParams.update({"font.size":10,"axes.edgecolor":MUTED,"axes.labelcolor":INK,"axes.titlesize":11,"axes.titleweight":"bold","axes.spines.top":False,"axes.spines.right":False,
                     "axes.grid":True,"grid.color":GRID,"grid.linewidth":.6,"axes.axisbelow":True,"xtick.color":MUTED,"ytick.color":MUTED,"text.color":INK})

def qq(ax,values):
    (theoretical,ordered),(slope,intercept,_)=stats.probplot(values,dist="norm")
    ax.plot(theoretical,slope*theoretical+intercept,color=MUTED,linewidth=1.2)
    ax.scatter(theoretical,ordered,s=26,color=BLUE,edgecolor="white",linewidth=.6,zorder=3)
    ax.set_xlabel("Theoretical normal quantile")

def difference_diagnostics(d,path):
    fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout="constrained")
    ax=axes[0];ax.hist(d,bins=np.arange(-1.5,2.84,1/3),color=BLUE,edgecolor="white",linewidth=1.5)
    ax.axvline(0,color=MUTED,linestyle="--",linewidth=1);ax.grid(axis="x",visible=False)
    ax.set_xlabel("Original minus AI quality (points)");ax.set_ylabel("Respondents");ax.set_title("Paired differences")
    ax=axes[1];qq(ax,d);ax.set_ylabel("Ordered differences");ax.set_title("Normal quantile plot")
    fig.savefig(path,dpi=220);plt.close(fig)

def item_intervals(statistics,path):
    rows=[("Composite",statistics["ratings"])]+[(dict(clear="Clarity",engage="Engagement",write="Overall writing")[x["item"]],x) for x in statistics["items"]]
    fig,ax=plt.subplots(figsize=(7.2,3),layout="constrained")
    for y,(label,x) in enumerate(reversed(rows)):
        low,high=-x["ci95"][1],-x["ci95"][0];mean=-x["mean_difference"]
        ax.plot([low,high],[y,y],color=BLUE,linewidth=2,solid_capstyle="round")
        ax.scatter(mean,y,s=48,color=BLUE,edgecolor="white",linewidth=1,zorder=3)
        ax.annotate(f"{mean:.2f}",(mean,y),xytext=(0,8),textcoords="offset points",ha="center",fontsize=9)
    ax.set_yticks(range(len(rows)),[label for label,_ in reversed(rows)]);ax.set_ylim(-.6,len(rows)-.3)
    ax.axvline(0,color=MUTED,linestyle="--",linewidth=1);ax.grid(axis="y",visible=False)
    ax.set_xlabel("Original minus AI (points), unadjusted 95% CI")
    fig.savefig(path,dpi=220);plt.close(fig)

def residual_diagnostics(rows,path):
    model=fit(rows)
    fig,axes=plt.subplots(1,2,figsize=(10,3.6),layout="constrained")
    ax=axes[0];ax.scatter(model.fittedvalues,model.resid,s=26,color=BLUE,edgecolor="white",linewidth=.6,zorder=3)
    ax.axhline(0,color=MUTED,linestyle="--",linewidth=1);ax.set_xlabel("Fitted difference (points)");ax.set_ylabel("Residual (points)");ax.set_title("Residuals versus fitted")
    ax=axes[1];qq(ax,model.resid);ax.set_ylabel("Ordered residuals");ax.set_title("Normal quantile plot")
    fig.savefig(path,dpi=220);plt.close(fig)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True);p.add_argument("--statistics",required=True);p.add_argument("--output-dir",required=True)
    a=p.parse_args();out=Path(a.output_dir);out.mkdir(parents=True,exist_ok=True)
    rows=eligible(a.input)
    d=np.array([float(r["quality_O"])-float(r["quality_AI"]) for r in rows])
    difference_diagnostics(d,out/"difference_diagnostics.png")
    item_intervals(json.loads(Path(a.statistics).read_text()),out/"item_differences.png")
    residual_diagnostics(rows,out/"regression_residuals.png")
if __name__=="__main__":main()
