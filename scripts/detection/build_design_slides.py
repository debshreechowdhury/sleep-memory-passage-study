"""Build the design and detection slides from results/quality/, matching the shared template. Charts stay native and editable."""
import argparse, json, sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Pt
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"scripts"/"quality"))
from build_slides import GOLD, INK, MUTED, TEAL, column_chart, fmt_p, limit_cards, new_slide, remove_template_slides, text

def build(template,output):
    x=json.loads((ROOT/"results/quality/hypothesis_tests.json").read_text())
    h1,h3,sens,conf=x["H1_group_difference"],x["H3_overall_detection"],x["H1_sensitivity"],x["confidence_exploratory"]
    intl,dom=h1["groups"]["International"],h1["groups"]["Domestic"]
    power=next(p for p in x["H1_power_assumed_rates"] if (p["rate_1"],p["rate_2"])==(.3,.6))
    low,high=[100*v for v in h1["difference_ci95_welch_t"]]
    deck=Presentation(template);remove_template_slides(deck)

    s=new_slide(deck,"AI detection across student backgrounds",1,"Debshree opens. We compared international and domestic students on identifying an AI rewrite of an NIH passage about sleep and memory. Authors Debshree Chowdhury and Jakub Romańczuk. Data downloaded November 2, 2026. Source: report/sections/00_title_abstract.md.")
    text(s,"Do international and domestic students differ in identifying an AI rewrite?",51,165,851,130,39,TEAL,True,"Question")
    text(s,"Debshree Chowdhury and Jakub Romańczuk\nAIPI 510 • Responses downloaded November 2, 2026",51,356,851,75,20.25,MUTED,name="Authors")

    s=new_slide(deck,"Why authorship judgments matter",2,"Sources: report/sections/01_background.md; Jakesch et al. (2023), https://doi.org/10.1073/pnas.2208839120 ; Gao et al. (2023), https://doi.org/10.1038/s41746-023-00819-6 . These studies used other tasks; do not transfer their detection rates to this sample. We had no directional prediction about the student groups.")
    text(s,"Clear or engaging writing does not establish its source.\n\nReaders can use misleading cues when judging AI text.\n\nOur main question: does detection differ by student background? We measure quality ratings separately.",51,146,851,319,23.25,name="Motivation")

    s=new_slide(deck,"Design and passages",3,"Sources: report/sections/03_design.md; study/google_forms.md. Both texts cover the same sleep and memory information; formatting was plain. Shared quotation and textual NIH references remained. The plan called for randomized order, but the form used a fixed order. Student background was observed, not assigned.")
    text(s,"Passage 1: AI rewrite\nPassage 2: NIH original",51,142,428,98,28.5,TEAL,True,"Passages")
    text(s,"Same participants rated both\nClarity, engagement and writing: 1–7",51,266,844,75,23.25,name="Ratings")
    text(s,"Then: forced-choice detection and confidence (1–5)\nFixed order: a correct answer always meant choosing Passage 1",51,375,844,75,23.25,name="Detection")

    s=new_slide(deck,"H1 and H3: detection hypotheses",4,f"Sources: report/sections/02_hypotheses_group.md, 02_hypotheses_detection.md, 04_power_group.md; results/quality/hypothesis_tests.json. The group comparison, its H0 and Fisher's exact test were written down before the first response, and the plan labelled it exploratory. We report it first because it is our main interest. These are assumed-rate calculations, not observed power. Merge with the H2 half in the final deck.")
    text(s,f"H1 (main): do international and domestic students differ in the share correct?\nH0: the proportions are equal • Fisher's exact test\nPower at 14 vs 12 for 30% vs 60%: {power['power_at_05']:.0%} at α = .05\n\nH3 (secondary): is overall detection different from 50%?\nH0: the proportion is .50 • Chi-square goodness-of-fit",51,136,851,300,21,name="Hypotheses")
    text(s,f"Two-sided • α = .05/3 = {x['threshold']:.4f}".replace("0.","."),51,450,855,41,17.25,MUTED,name="Threshold")

    s=new_slide(deck,"H1: a large gap between student groups",6,f"Source: results/quality/hypothesis_tests.json. Welch t-based 95% CI on the 0/1 scores, approximate at this sample size. Domestic-correct expected count is {h1['expected_counts'][1][0]:.2f}, below 5, so we use Fisher's exact. Sensitivities: planned both-wrong rule p = {fmt_p(sens['planned_both_wrong_rule']['p'])}; legacy omitted p = {fmt_p(sens['legacy_record_omitted']['p'])}; legacy reversed p = {fmt_p(sens['legacy_record_reversed']['p'])}; stated Student only p = {fmt_p(sens['status_student_only']['p'])}. Say clearly that correct means Passage 1 and that this does not prove better detection. The team reports that the last ten responses came from different people and not a single class or group.")
    column_chart(s,48,142,440,346,["International","Domestic"],[("Share correct",[intl["proportion"],dom["proportion"]],TEAL)],"Detection by student background","0%",0,1,"Share choosing the AI passage")
    text(s,f"{intl['correct']}/{intl['n']} vs {dom['correct']}/{dom['n']} correct\nFisher p = {fmt_p(h1['p'])}",520,146,392,110,28,TEAL,True,"H1 result")
    text(s,f"Difference: {100*h1['difference_in_proportions']:.0f} points, 95% CI [{low:.0f}, {high:.0f}]\nThe AI passage was always first, so this may reflect a preference for Passage 1\nWithout the last 10 responses: p = {fmt_p(sens['without_responses_after_row_54']['p'])}",520,270,392,215,19,name="H1 caveats")

    s=new_slide(deck,"H3: overall detection stays uncertain",10,f"Source: results/quality/hypothesis_tests.json. Chi-square({h3['df']}) = {h3['chi2']:.3f}, p = {fmt_p(h3['p'])}; we fail to reject H0, which does not show that students were guessing. Confidence is exploratory: Mann-Whitney U = {conf['mann_whitney_u']:.1f}. Background is not a language-proficiency measure.")
    column_chart(s,48,142,440,346,["Correct","Incorrect"],[("Respondents",[h3["correct"],h3["n"]-h3["correct"]],TEAL)],"Overall detection counts","0",0,None,f"{h3['n']} students",100)
    text(s,f"{h3['proportion']:.1%} correct\nChi-square p = {fmt_p(h3['p'])}",520,146,392,110,28,TEAL,True,"H3 result")
    lo,hi=[100*v for v in h3["ci95_t"]]
    text(s,f"95% CI: {lo:.1f}% to {hi:.1f}%, which includes chance\n\nConfidence (exploratory): correct {conf['correct_mean']:.2f} vs incorrect {conf['incorrect_mean']:.2f}, Mann-Whitney p = {fmt_p(conf['p'])}",520,270,392,215,19,name="H3 notes")

    s=new_slide(deck,"Limits on the detection results",11,"Sources: report/sections/08_limitations_stimulus_sampling.md and 07_interpretation_group.md. No causal claim about background. Eligibility changed during launch, and there is no verified age record. The team reports that the instructor accepted the initial nondisclosure; no separate ethics review is documented. Merge with the rating and data points in the final deck.")
    limit_cards(s,(("Passage 1 problem","A correct answer always meant choosing Passage 1, so skill and first-passage preference cannot be separated."),("Last 10 responses","They arrived within about 15 minutes. The team reports different people, but H1 weakens without them."),("Small groups","With 14 and 12 students, only very large gaps are reliably detectable."),("One passage, convenience sample","One rewrite and a shared link cannot represent all AI writing or all students.")))

    s=new_slide(deck,"Conclusion and recommendations",12,"Sources: report/sections/09_conclusion.md and results/quality/hypothesis_tests.json. Do not claim that international students are better at detecting AI, chance equivalence, or a general inability to detect AI. Joint-review draft.")
    text(s,"International and domestic students differed in choosing the AI passage, but this may reflect a preference for the first passage.\n\nStudents rated the original higher; overall detection stayed uncertain.\n\nNext: retest the group difference with randomized order and about 50 students per group, and measure English proficiency.",51,142,851,340,23.25,name="Conclusion")
    Path(output).parent.mkdir(parents=True,exist_ok=True)
    deck.save(output)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--template",required=True);p.add_argument("--output",required=True)
    a=p.parse_args();build(a.template,a.output)
if __name__=="__main__":main()
