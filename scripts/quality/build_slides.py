"""Build the data and quality slides from results/quality/, matching the shared template. Charts stay native and editable."""
import argparse, csv, json
from pathlib import Path
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Pt

ROOT=Path(__file__).resolve().parents[2]
FONT="Helvetica Neue"
INK,TEAL,MUTED,GOLD,TINT,GRID=(RGBColor.from_string(x) for x in ("152C35","15616D","536871","AE6A30","F4F7F7","D9E0E3"))
ITEMS=dict(clear="Clarity",engage="Engagement",write="Overall writing")

def fmt_p(p):
    text=f"{p:.2g}" if p<.01 else f"{p:.3g}"
    return text.lstrip("0")

def text(slide,value,x,y,w,h,size=21,color=INK,bold=False,name=None,anchor=None,align=None):
    box=slide.shapes.add_textbox(Pt(x),Pt(y),Pt(w),Pt(h))
    if name: box.name=name
    frame=box.text_frame;frame.word_wrap=True
    if anchor: frame.vertical_anchor=anchor
    for i,line in enumerate(value.split("\n")):
        para=frame.paragraphs[0] if i==0 else frame.add_paragraph()
        if align: para.alignment=align
        para.space_after=Pt(6)
        run=para.add_run();run.text=line
        run.font.size,run.font.name,run.font.bold=Pt(size),FONT,bold
        run.font.color.rgb=color
    return box

def new_slide(deck,title,number,notes):
    slide=deck.slides.add_slide(deck.slide_layouts.get_by_name("Blank"))
    text(slide,title,48,36,864,86,33,INK,True,"Title")
    text(slide,f"{number}  •  Sleep and memory passage study",48,502,864,20,13.5,MUTED,name="Footer")
    slide.notes_slide.notes_text_frame.text=notes
    return slide

def card(slide,x,y,w,h,value,label,name):
    shape=slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Pt(x),Pt(y),Pt(w),Pt(h))
    shape.name=name;shape.adjustments[0]=.06
    shape.fill.solid();shape.fill.fore_color.rgb=TINT;shape.line.fill.background();shape.shadow.inherit=False
    text(slide,value,x+10,y+8,w-20,h*.55,34,TEAL,True,f"{name} value")
    text(slide,label,x+10,y+h*.52,w-20,h*.45,15,INK,name=f"{name} label")

def style_chart(chart,legend):
    chart.font.size=Pt(14);chart.font.name=FONT;chart.font.color.rgb=INK
    chart.has_title=False
    chart.has_legend=legend
    if legend:
        chart.legend.position=XL_LEGEND_POSITION.BOTTOM;chart.legend.include_in_layout=False
    value=chart.value_axis
    value.major_gridlines.format.line.color.rgb=GRID;value.format.line.fill.background()
    value.tick_labels.font.color.rgb=MUTED;chart.category_axis.tick_labels.font.color.rgb=MUTED
    chart.category_axis.format.line.color.rgb=MUTED

def column_chart(slide,x,y,w,h,categories,series,name,number_format,low=None,high=None,axis_title=None,gap=60,axis_format=None,major_unit=None):
    data=CategoryChartData();data.categories=categories
    for label,values,_ in series: data.add_series(label,values)
    chart=slide.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED,Pt(x),Pt(y),Pt(w),Pt(h),data)
    chart.name=name
    chart=chart.chart;style_chart(chart,len(series)>1)
    plot=chart.plots[0];plot.gap_width=gap;plot.overlap=-5;plot.has_data_labels=True
    labels=plot.data_labels;labels.number_format=number_format;labels.number_format_is_linked=False;labels.position=XL_LABEL_POSITION.OUTSIDE_END;labels.font.size=Pt(13);labels.font.color.rgb=INK
    for plotted,(_,_,color) in zip(plot.series,series):
        plotted.format.fill.solid();plotted.format.fill.fore_color.rgb=color
    axis=chart.value_axis
    if low is not None: axis.minimum_scale=low
    if high is not None: axis.maximum_scale=high
    if major_unit: axis.major_unit=major_unit
    axis.tick_labels.number_format=axis_format or number_format;axis.tick_labels.number_format_is_linked=False
    if axis_title:
        axis=chart.category_axis;axis.has_title=True;axis.axis_title.text_frame.text=axis_title
        run=axis.axis_title.text_frame.paragraphs[0].runs[0];run.font.size=Pt(13);run.font.bold=False;run.font.color.rgb=MUTED
    return chart

def table(slide,x,y,widths,rows,name,size=15,row_height=36):
    shape=slide.shapes.add_table(len(rows),len(widths),Pt(x),Pt(y),Pt(sum(widths)),Pt(row_height*len(rows)))
    shape.name=name
    grid=shape.table;grid.horz_banding=False
    for i,width in enumerate(widths): grid.columns[i].width=Pt(width)
    for r,row in enumerate(rows):
        grid.rows[r].height=Pt(row_height)
        for c,value in enumerate(row):
            cell=grid.cell(r,c);cell.vertical_anchor=MSO_ANCHOR.MIDDLE
            cell.fill.solid();cell.fill.fore_color.rgb=TINT if r==0 else RGBColor(255,255,255)
            para=cell.text_frame.paragraphs[0];para.alignment=PP_ALIGN.LEFT if c==0 else PP_ALIGN.RIGHT
            run=para.add_run();run.text=value
            run.font.size,run.font.name,run.font.bold=Pt(size),FONT,r==0
            run.font.color.rgb=INK

def limit_cards(slide,points):
    for i,(head,body) in enumerate(points):
        x,y=48+(i%2)*444,142+(i//2)*170
        shape=slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Pt(x),Pt(y),Pt(420),Pt(152));shape.name=f"Limit card {i+1}";shape.adjustments[0]=.06
        shape.fill.solid();shape.fill.fore_color.rgb=TINT;shape.line.fill.background();shape.shadow.inherit=False
        text(slide,head,x+12,y+10,396,36,21,TEAL,True,f"Limit {i+1} heading")
        text(slide,body,x+12,y+52,396,92,18,INK,name=f"Limit {i+1} text")

def remove_template_slides(deck):
    ids=deck.slides._sldIdLst
    for slide_id in list(ids):
        deck.part.drop_rel(slide_id.rId);ids.remove(slide_id)

def add_slides(deck):
    q=json.loads((ROOT/"results/quality/quality.json").read_text())
    reg=json.loads((ROOT/"results/quality/regression.json").read_text())
    with open(ROOT/"results/quality/power_achieved.csv",newline="") as f: power=list(csv.DictReader(f))
    flow,r=q["exclusion_flow"],q["ratings"]
    group,sens=q["group_comparison"],q["sensitivity"]
    corr=q["item_correlations"]
    at=lambda alpha:[r for r in power if float(r["alpha"])==alpha]
    n=int(power[0]["planned_pairs"])
    mde=lambda alpha:float(at(alpha)[0]["minimum_detectable_dz"])

    s=new_slide(deck,f"H2, and what {n} pairs can detect",4,"The quality half of the shared hypotheses slide. Source: results/quality/power_achieved.csv; report section Power analysis. These are assumed effects at the achieved sample size, not observed power. H2 is exploratory. Merge with the H1 half in the final deck.")
    text(s,f"H2, exploratory question\nH0: mean AI-minus-original quality difference = 0\nAlternative: the difference is not 0\nTwo-sided paired t-test\n\nSmallest effect detectable at 80% power:\ndz = {mde(.05):.2f} at α = .05",51,136,410,350,20,name="Hypotheses")
    column_chart(s,480,136,432,350,[f"dz = {float(x['assumed_dz']):.1f}" for x in at(.05)],[("α = .05",[float(x["power_at_planned_n"]) for x in at(.05)],TEAL)],"Power by assumed effect","0%",0,1)

    s=new_slide(deck,f"From {flow['submissions']} responses to {flow['included']} students",5,f"Source: results/quality/quality.json exclusion_flow; report section Data collection and cleaning. The student restriction follows from the international versus domestic comparison planned before collection. The stricter check rule was chosen on November 2 after the 54-response results had been seen, so the planned both-wrong rule stays in the report as a sensitivity analysis. By stated status, retained respondents were {flow['included_by_status']['Student']} Student, {flow['included_by_status']['Working professional']} Working professional and {flow['included_by_status']['Yes']} legacy record.")
    width=264
    for i,(value,label) in enumerate(((str(flow["submissions"]),"submissions\nAll affirmed consent"),(str(flow["students"]),f"reported a student background\n{flow['not_a_student']} non-students removed"),(str(flow["included"]),f"had both checks correct\n{flow['students_both_checks_wrong']+flow['students_one_check_wrong']} students removed"))):
        card(s,48+i*(width+36),150,width,170,value,label,f"Flow step {i+1}")
        if i<2:
            arrow=s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,Pt(48+i*(width+36)+width+7),Pt(225),Pt(22),Pt(20));arrow.name=f"Flow arrow {i+1}"
            arrow.fill.solid();arrow.fill.fore_color.rgb=MUTED;arrow.line.fill.background();arrow.shadow.inherit=False
    groups=flow["included_by_background"]
    text(s,f"{groups['International']} international and {groups['Domestic']} domestic students\nCheck rule: 90 minutes on both comprehension questions\nThe stricter check rule was set after earlier results and is disclosed as retrospective",51,345,851,140,20,name="Flow notes")

    s=new_slide(deck,"H2: students rated the AI rewrite higher",7,f"Source: results/quality/quality.json ratings; report section Statistical analysis. AI minus original {r['mean_difference']:.3f}, 95% CI [{r['ci95'][0]:.3f}, {r['ci95'][1]:.3f}], t({r['df']}) = {abs(r['t']):.3f}, p = {fmt_p(r['p'])}, dz = {abs(r['cohen_dz']):.3f}. It is below .05, so we reject H0 for H2, but this analysis is exploratory. AI higher for {r['AI_higher']}, original higher for {r['original_higher']}, tied for {r['ties']}. Say clearly that the AI rewrite was always second, so this does not prove that authorship caused the difference.")
    outcomes=[(ITEMS[x["item"]],x) for x in q["items"]]+[("Composite",r)]
    column_chart(s,48,136,520,352,[o for o,_ in outcomes],[("AI rewrite",[x["mean_AI"] for _,x in outcomes],GOLD),("Original",[x["mean_O"] for _,x in outcomes],TEAL)],"Mean ratings by version","0.00",1,7,axis_format="0",major_unit=1)
    card(s,592,136,320,112,f"+{r['mean_difference']:.2f} points",f"AI minus original, 95% CI [{r['ci95'][0]:.2f}, {r['ci95'][1]:.2f}], on a 1–7 scale","Effect")
    text(s,f"t({r['df']}) = {abs(r['t']):.2f}, p = {fmt_p(r['p'])}\ndz = {abs(r['cohen_dz']):.2f}\n\n{r['AI_higher']} rated the AI rewrite higher\n{r['original_higher']} rated the original higher\n{r['ties']} rated them equally",592,262,320,226,19,name="Test result")

    s=new_slide(deck,"Composite holds up; single items are less stable",8,f"Sources: results/quality/quality.json ratings, items and sensitivity. Shapiro-Wilk on the composite differences W = {r['shapiro']['statistic']:.3f}, p = {fmt_p(r['shapiro']['p'])}; Wilcoxon p = {fmt_p(r['wilcoxon']['p'])}. Bonferroni for three items sets the threshold at .0167. Under the planned check rule the composite was {sens['earlier_rule_all_respondents']['mean_difference']:.3f} with p = {fmt_p(sens['earlier_rule_all_respondents']['p'])}. In the 49-response snapshot, engagement and overall writing passed and clarity did not, so do not single out one item. Correlations between items were descriptive: clarity and overall writing were {corr['AI']['clear_write']:.2f} for the AI rewrite and {corr['O']['clear_write']:.2f} for the original; engagement and overall writing were {corr['AI']['engage_write']:.2f} and {corr['O']['engage_write']:.2f}.")
    counts=q["AI_minus_original_counts"]
    column_chart(s,48,136,430,352,[f"{c['thirds_of_a_point']/3:+.1f}" if c["thirds_of_a_point"] else "0" for c in counts],[("Respondents",[c["respondents"] for c in counts],TEAL)],"Paired difference counts","0",0,None,"AI minus original (points)",35)
    rows=[["Item","Diff.","Bonf. p","Wilcoxon p"]]+[[ITEMS[x["item"]],f"{x['mean_difference']:.2f}",fmt_p(x["bonferroni_p"]),fmt_p(x["wilcoxon"]["p"])] for x in q["items"]]
    table(s,498,142,[164,70,80,100],rows,"Item tests")
    earlier=sens["earlier_rule_all_respondents"]
    text(s,f"Shapiro-Wilk p = {fmt_p(r['shapiro']['p'])}; Wilcoxon p = {fmt_p(r['wilcoxon']['p'])}\nPlanned check rule (n = {earlier['n']}): +{earlier['mean_difference']:.2f}, p = {fmt_p(earlier['p'])}\nWhich item passes changes with the sample",498,300,414,190,18,name="Assumption notes")

    s=new_slide(deck,"No predictor reliably explained the difference",9,f"Sources: results/quality/regression.json and quality.json group_comparison. The AI-use and English questions were not collected, so the proposed regression could not be fitted; this one uses collected predictors and is exploratory. F(3, {reg['df_residual']}) = {reg['f']:.3f}, p = {fmt_p(reg['f_p'])}. Residual Shapiro-Wilk p = {fmt_p(reg['residual_shapiro']['p'])}; Breusch-Pagan p = {fmt_p(reg['breusch_pagan']['p'])}. Nonsignificant does not mean no relationship at this sample size. Welch t({group['welch']['df']:.1f}) = {group['welch']['t']:.3f}, p = {fmt_p(group['welch']['p'])}.")
    labels=dict(intercept="Intercept",international="International",detect_correct="Correct detection",confidence="Confidence")
    rows=[["Term","Estimate","95% CI","p"]]+[[labels[c["term"]],f"{c['estimate']:.2f}",f"[{c['ci95'][0]:.2f}, {c['ci95'][1]:.2f}]",fmt_p(c["p"])] for c in reg["coefficients"]]
    table(s,51,142,[190,90,150,70],rows,"Regression terms",16)
    text(s,f"Outcome: AI minus original, n = {reg['n']}\nAdjusted R² = {reg['adjusted_r_squared']:.2f}, model p = {fmt_p(reg['f_p'])}\nResidual checks passed",51,335,500,150,18,name="Regression notes")
    by=group["by_group"]
    card(s,580,142,332,130,f"+{by['International']['mean_difference']:.2f} vs +{by['Domestic']['mean_difference']:.2f}",f"AI advantage: international vs domestic\nWelch p = {fmt_p(group['welch']['p'])}","Subgroups")
    text(s,"Both groups lean the same way, so there is no Simpson's reversal\nThe AI-use and English questions were not collected",580,290,332,200,18,name="Subgroup notes")

    s=new_slide(deck,"Limits on the rating results",10,"The rating half of the shared limitations slide, from report section Limitations. Merge with the stimulus and sampling points in the final deck.")
    points=(("Fixed order","The AI rewrite was always second, so version and position cannot be separated."),("Exclusions",f"The student restriction cut the sample from {flow['submissions']} to {flow['students']}, and a stricter check rule set after earlier results left {flow['included']}."),("Measurement","Ratings are bounded and subjective, and the three items agreed only partly, especially clarity."),("Data checks","Duplicate responses could not be verified, and AI-use and English were not collected."))
    limit_cards(s,points)

def build(template,output):
    deck=Presentation(template);remove_template_slides(deck)
    add_slides(deck)
    Path(output).parent.mkdir(parents=True,exist_ok=True)
    deck.save(output)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--template",required=True);p.add_argument("--output",required=True)
    a=p.parse_args();build(a.template,a.output)
if __name__=="__main__":main()
