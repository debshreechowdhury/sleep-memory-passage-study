"""Combine both member decks into the 11-slide presentation order, merging the shared slides. Charts stay native and editable."""
import argparse, csv, json, sys
from pathlib import Path
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.util import Pt
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/"scripts"/"quality"),str(ROOT/"scripts"/"detection")]
import build_design_slides, build_slides
from build_slides import INK, MUTED, TEAL, TINT, new_slide, remove_template_slides, text

PRESENTERS={1:"Debshree",2:"Debshree",3:"Debshree",4:"Both",5:"Kuba",6:"Debshree",7:"Kuba",8:"Kuba",9:"Kuba",10:"Both",11:"Both"}

def number(slide):
    footer=next(sh.text_frame.text for sh in slide.shapes if sh.name=="Footer")
    return int(footer.split()[0])

def drop(deck,slide):
    ids=deck.slides._sldIdLst
    for slide_id in list(ids):
        if deck.slides.get(int(slide_id.get("id"))) is slide:
            deck.part.drop_rel(slide_id.rId);ids.remove(slide_id)

def card(slide,x,y,w,h,head,body,name,size=15):
    shape=slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Pt(x),Pt(y),Pt(w),Pt(h));shape.name=name;shape.adjustments[0]=.05
    shape.fill.solid();shape.fill.fore_color.rgb=TINT;shape.line.fill.background();shape.shadow.inherit=False
    text(slide,head,x+8,y+8,w-16,34,18,TEAL,True,f"{name} heading")
    text(slide,body,x+8,y+44,w-16,h-50,size,INK,name=f"{name} text")

def add_hypotheses(deck):
    x=json.loads((ROOT/"results/quality/hypothesis_tests.json").read_text())
    with open(ROOT/"results/quality/power_achieved.csv",newline="") as f: power=list(csv.DictReader(f))
    h1=next(p for p in x["H1_power_assumed_rates"] if (p["rate_1"],p["rate_2"])==(.3,.6))
    h2=next(p for p in power if float(p["assumed_dz"])==.5)
    s=new_slide(deck,"One main question, one exploratory",4,"Sources: report/sections/02_hypotheses_group.md, 02_hypotheses_quality.md, 02_testing_policy.md and the power sections; results/quality/hypothesis_tests.json and power_achieved.csv. Power values use assumed effects, not observed power. The October 30 plan listed the group test as exploratory and quality and overall detection as primary. The team reports that the AI-assisted plan added overall detection, which it did not intend and dropped after results were seen (p = .239); say this aloud if asked. The emphasis and stricter check rule also came after earlier results.")
    width=423
    for i,(head,body) in enumerate((
        ("H1: group difference (main)",f"Do international and domestic students differ in the share correct?\n\nH0: the proportions are equal\nFisher's exact test\n\nPower for 30% vs 60%: {h1['power_at_05']:.0%}"),
        ("H2: quality (exploratory)",f"Do students rate the original and the rewrite differently?\n\nH0: mean difference = 0\nPaired t-test\n\nPower for dz = 0.5: {float(h2['power_at_planned_n']):.0%}"),
    )): card(s,48+i*(width+18),136,width,276,head,body,f"Hypothesis {i+1}",16)
    text(s,"Two-sided at α = .05. The emphasis and stricter check rule were set after earlier results were seen.",48,428,864,36,16.5,MUTED,name="Threshold")

def add_limitations(deck):
    flow=json.loads((ROOT/"results/quality/quality.json").read_text())["exclusion_flow"]
    s=new_slide(deck,"Limits on what we can conclude",10,"Sources: report/sections/08_limitations_stimulus_sampling.md and 08_limitations_ratings_data.md. Fixed order is the most important limit: recognition and second-position choice cannot be separated, and the quality result is confounded with rating a passage second. Passage order rests on the team's report, because the form at the link in earlier documentation shows the reverse. There is no causal claim about background. The team reports that the final ten responses were different people, not one class or group, and timing does not prove coordinated answers. The team reports no pilots, instructor acceptance of nondisclosure and closed collection. No separate ethics-board review is documented. Legacy assignment and generation date remain uncertain.")
    width,height=276,160
    for i,(head,body) in enumerate((
        ("Fixed order","Correct always means Passage 2, and the AI rewrite was always second, so position cannot be separated from either result."),
        ("Retrospective decisions","The lead question and the stricter check rule changed after earlier results were seen."),
        ("Small convenience sample",f"Exclusions took {flow['submissions']} responses to {flow['included']}. Groups of {flow['included_by_background']['International']} and {flow['included_by_background']['Domestic']} give low power and imprecise estimates."),
        ("Independence","The team reports different people, not one group, but H1 weakens without the last 10 responses."),
        ("Measurement","Ratings are bounded and subjective, and the three items agreed only partly, especially clarity."),
        ("Data checks","Duplicates could not be verified, and AI-use and English proficiency were not collected."),
    )): card(s,48+(i%3)*(width+18),134+(i//3)*(height+14),width,height,head,body,f"Limit {i+1}")

def consistent_charts(deck):
    """Match chart labels across both members' slides, and use unsigned axis IDs so other readers can import them."""
    for slide in deck.slides:
        for shape in slide.shapes:
            if not shape.has_chart: continue
            chart=shape.chart
            for tag in ("c:axId","c:crossAx"):
                for node in chart._chartSpace.iter(qn(tag)): node.set("val",str(int(node.get("val"))&0xffffffff))
            chart.font.size=Pt(14)
            for axis in (chart.category_axis,chart.value_axis): axis.tick_labels.font.size=Pt(14)
            chart.plots[0].data_labels.font.size=Pt(14)
            if chart.has_legend: chart.legend.font.size=Pt(14)

def build(template,output):
    deck=Presentation(template);remove_template_slides(deck)
    build_design_slides.add_slides(deck)
    build_slides.add_slides(deck)
    halves=[slide for slide in deck.slides if number(slide) in (4,10)]
    # Add before dropping: new slide part names come from the slide count, so dropping first would overwrite a slide.
    add_hypotheses(deck);add_limitations(deck)
    for slide in halves: drop(deck,slide)
    consistent_charts(deck)
    ids=deck.slides._sldIdLst
    order=sorted(zip(list(deck.slides),list(ids)),key=lambda pair:number(pair[0]))
    for _,slide_id in order: ids.remove(slide_id)
    for slide,slide_id in order:
        ids.append(slide_id)
        notes=slide.notes_slide.notes_text_frame
        notes.text=f"Presenter: {PRESENTERS[number(slide)]}. {notes.text}"
    deck.core_properties.title="Do international and domestic students differ in identifying an AI rewrite?"
    deck.core_properties.author="Debshree Chowdhury and Jakub Romańczuk"
    Path(output).parent.mkdir(parents=True,exist_ok=True)
    deck.save(output)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--template",required=True);p.add_argument("--output",required=True)
    a=p.parse_args();build(a.template,a.output)
if __name__=="__main__":main()
