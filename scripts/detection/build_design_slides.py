"""Build Debshree's assigned slides from committed results; preserve the shared theme."""
import argparse
import json
import sys
from pathlib import Path
from pptx import Presentation
from pptx.oxml.ns import qn
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT/'scripts/quality'))
from build_slides import MUTED, TEAL, column_chart, fmt_p, limit_cards, new_slide, remove_template_slides, text


def portable_axes(chart):
    """Use unsigned axis IDs consistently so other OOXML readers can import charts."""
    for tag in ('c:axId', 'c:crossAx'):
        for node in chart._chartSpace.iter(qn(tag)):
            node.set('val', str(int(node.get('val')) & 0xffffffff))
    from pptx.util import Pt
    for axis in (chart.category_axis, chart.value_axis):
        axis.tick_labels.font.size = Pt(16)
        axis.tick_labels.font.name = 'Helvetica Neue'
    chart.plots[0].data_labels.font.size = Pt(16)
    return chart


def add_slides(deck):
    x = json.loads((ROOT/'results/quality/hypothesis_tests.json').read_text())
    h1, sens, conf = (x[k] for k in ('H1_group_difference', 'H1_sensitivity', 'confidence_exploratory'))
    intl, dom = (h1['groups'][g] for g in ('International', 'Domestic'))
    power = next(p for p in x['H1_power_assumed_rates'] if (p['rate_1'],p['rate_2']) == (.3,.6))
    low, high = [-100*v for v in reversed(h1['difference_ci95_welch_t'])]

    s = new_slide(deck, 'AI detection across student backgrounds', 1,
                  'Research question: do respondents reporting international and domestic student backgrounds differ in which passage they identify as AI? The analysis uses 26 respondents who reported one of those backgrounds and passed both checks. Student background does not always match current-status Student. The current numbering and stricter exclusions were set after earlier results were seen. Source: report/sections/01_background.md; results/quality/hypothesis_tests.json.')
    text(s, 'Do international and domestic students differ in identifying an AI rewrite?', 51,165,851,130,39,TEAL,True,'Question')
    text(s, 'Debshree Chowdhury and Jakub Romańczuk\nAIPI 510 • Responses downloaded November 2, 2026',51,356,851,75,20.25,MUTED,name='Authors')

    s = new_slide(deck, 'Why authorship judgments matter', 2,
                  'Sources: report/sections/01_background.md; Jakesch et al. (2023), https://doi.org/10.1073/pnas.2208839120 ; Gao et al. (2023), https://doi.org/10.1038/s41746-023-00819-6 . Those studies used different tasks and do not supply expected detection rates for our sample. This study measures source choices and perceived quality, not learning or memory performance.')
    text(s, 'A clear passage can still be misidentified.\n\nReaders may rely on misleading cues about AI writing.\n\nWe compare source choices across student backgrounds\nand measure writing quality separately.',51,146,851,319,23.25,name='Motivation')

    s = new_slide(deck, 'Design and passage order', 3,
                  'Sources: report/sections/03_design.md; study/stimuli/provenance.md. The team reports that the collection form was original first from the start; earlier documentation recorded the reverse. Every coded correct response is therefore a Passage 2 choice. One legacy response has uncertain actual order; the report shows omission/reversal sensitivities. Explain aloud: a group gap could be a tendency to choose the second passage as AI, rather than an ability difference. Same topic, plain formatting, shared quotation and NIH references. Team reports GPT-6.1 SOL; second output selected; generation date unknown.')
    text(s, 'Passage 1: NIH original\nPassage 2: AI rewrite',51,142,428,98,28.5,TEAL,True,'Passages')
    text(s, 'Both passages rated for clarity, engagement and writing\nThen one source choice and confidence rating',51,266,844,75,23.25,name='Ratings')
    text(s, 'Correct in the analysis = choosing Passage 2\nRecognition and second-passage preference cannot be separated',51,375,844,85,22,TEAL,name='Detection')

    s = new_slide(deck, 'H1: detection hypothesis', 4,
                  'Sources: report/sections/02_hypotheses_group.md, 02_testing_policy.md, 04_power_group.md; results/quality/hypothesis_tests.json. H1 null: equal source-choice proportions, two-sided. The October 30 plan listed the group test as exploratory; the emphasis and stricter checks came after earlier results. Power uses assumed rates, not observed power. H2 quality is the exploratory paired comparison covered by Kuba.')
    text(s, f"H1: equal international/domestic proportions correct?\nTwo-sided Fisher's exact test at α = .05\nAssume 30% vs 60%: {power['power_at_05']:.1%} power with 14 vs 12",51,136,851,300,21,name='Hypotheses')

    s = new_slide(deck, 'H1: different source choices between groups', 6,
                  f"Source: results/quality/hypothesis_tests.json. International {intl['correct']}/{intl['n']}; Domestic {dom['correct']}/{dom['n']}. Fisher p={h1['p']:.8f} is below .05. Expected domestic-correct count={h1['expected_counts'][1][0]:.2f}; sparse cells motivate Fisher. Difference CI is approximate Welch t on 0/1 scores, marginal95%, not an exact Fisher interval or multiplicity-adjusted interval. Correct=Passage2 under the applied mapping, so ability and position choice are confounded. Planned-rule p={sens['planned_both_wrong_rule']['p']:.4f}; legacy omit/reverse p={sens['legacy_record_omitted']['p']:.4f}/{sens['legacy_record_reversed']['p']:.4f}; stated-Student-only p={sens['status_student_only']['p']:.4f}. Subset changes are not a formal test of changing effects. The team reports that the last ten responses came from different people, not one class or group; timing alone does not prove dependence.")
    portable_axes(column_chart(s,48,142,440,346,['International','Domestic'],[('Share choosing Passage 2',[intl['proportion'],dom['proportion']],TEAL)],'Source choices by background','0%',0,1,'Share choosing Passage 2',major_unit=.2))
    text(s,f"{intl['correct']}/{intl['n']} vs {dom['correct']}/{dom['n']} correct\nFisher p = {fmt_p(h1['p'])}",520,146,392,110,28,TEAL,True,'H1 result')
    text(s,f"Domestic higher by {-100*h1['difference_in_proportions']:.1f} points\nApprox. 95% CI [{low:.1f}, {high:.1f}]\n\nMay reflect choosing Passage 2\nWithout the last 10 responses: p = {fmt_p(sens['without_responses_after_row_54']['p'])}",520,270,392,215,18.5,name='H1 caveats')

    s = new_slide(deck, 'Limits on the detection findings', 10,
                  'Sources: report/sections/08_limitations_stimulus_sampling.md, 07_interpretation_group.md. Second-position preference cannot be separated from recognition; no causal background claim. The team reports that the final ten responses were different people, not one class or group. Timing does not prove coordinated answers. H1 direction persists, while significance depends on some subset definitions. Student-background is self-reported; legacy assignment and generation date remain uncertain. The team reports no pilots, instructor acceptance of nondisclosure, and closed collection. No separate ethics-board review is documented. Report retrospective analysis decisions alongside statistical significance.')
    limit_cards(s, (('Fixed order','Correct means Passage 2. Recognition and second-position choice are confounded.'),('Retrospective decisions','The lead question and stricter check rule changed after earlier results were seen.'),('Small convenience sample','Groups of 14 and 12 give low power and imprecise population estimates.'),('Independence assumption','The team reports different people, not one class or group. Timing does not prove collaboration.')))

    s = new_slide(deck, 'Conclusion and recommendations', 11,
                  'Sources: results/quality/hypothesis_tests.json; report/sections/07_interpretation_group.md; report/sections/09_conclusion.md remains for joint review. This is a discussion summary, not approval of the final shared conclusion. H2 is exploratory and confounded with position. Do not claim general superiority, chance equivalence or a causal background effect. For replication, about 48 per group gives 80% power for 30% vs 60% at .05; state the assumed effect.')
    text(s,'The groups differed in source choices for this passage pair.\nThis does not establish better AI-detection ability.\n\nThe AI rewrite was rated higher in an exploratory analysis.\n\nNext: counterbalance order, use several passage pairs,\nand recruit about 48 students per group.',51,142,851,340,22.5,name='Conclusion')


def build(template, output):
    deck = Presentation(template); remove_template_slides(deck)
    add_slides(deck)
    Path(output).parent.mkdir(parents=True,exist_ok=True);deck.save(output)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template',required=True);parser.add_argument('--output',required=True)
    args=parser.parse_args();build(args.template,args.output)

if __name__=='__main__': main()
