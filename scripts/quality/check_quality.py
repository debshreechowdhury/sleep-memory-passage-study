"""Check that the quality report sections state the numbers in results/quality/."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
q=json.loads((ROOT/"results/quality/quality.json").read_text())
reg=json.loads((ROOT/"results/quality/regression.json").read_text())
text="\n".join((ROOT/"report/sections"/f"{n}.md").read_text(encoding="utf-8") for n in ("04_power_quality","05_data_collection_cleaning","06_analysis_group","06_analysis_quality","06_analysis_detection","07_interpretation_group","07_interpretation_quality","08_limitations_ratings_data"))
flow=q["exclusion_flow"];r=q["ratings"]

def require(*values):
    for value in values: assert value in text,value

assert flow["submissions"]==64 and flow["not_a_student"]==35 and flow["students"]==29
assert flow["students_both_checks_wrong"]==2 and flow["students_one_check_wrong"]==1
assert flow["included"]==q["paired_n"]==r["n"]==26==reg["n"]
assert flow["included_by_background"]=={"International":14,"Domestic":12}
assert r["original_higher"]+r["AI_higher"]+r["ties"]==r["n"]
require(f'{-r["mean_difference"]:.3f}',f't({r["df"]}) = {abs(r["t"]):.3f}',f'[{-r["ci95"][1]:.3f}, {-r["ci95"][0]:.3f}]',f'dz = {abs(r["cohen_dz"]):.3f}',f'{r["mean_AI"]:.3f}',f'{r["mean_O"]:.3f}')
for item in q["items"]:
    require(f'{-item["mean_difference"]:.3f}',f'[{-item["ci95"][1]:.3f}, {-item["ci95"][0]:.3f}]',f'{abs(item["t"]):.3f}',f'{abs(item["cohen_dz"]):.3f}')
for key,n in (("without_legacy_record",25),("earlier_rule_all_respondents",59)):
    s=q["sensitivity"][key];assert s["n"]==n
    require(f'{-s["mean_difference"]:.3f}',f'[{-s["ci95"][1]:.3f}, {-s["ci95"][0]:.3f}]',f'{abs(s["t"]):.3f}',f'{abs(s["cohen_dz"]):.3f}')
for c in reg["coefficients"]:
    require(f'{c["estimate"]:.3f}',f'{c["se"]:.3f}',f'[{c["ci95"][0]:.3f}, {c["ci95"][1]:.3f}]')
require(f'F(3, 22) = {reg["f"]:.3f}',f'{reg["r_squared"]:.3f}'.lstrip("0"),f'LM = {reg["breusch_pagan"]["lm"]:.3f}')
for version in q["item_correlations"].values():
    for value in version.values(): require(f"{value:.2f}".lstrip("0"))
assert "Cronbach" not in text
planned=json.loads((ROOT/"results/quality/hypothesis_tests.json").read_text())
assert planned["H2_quality"]["reject_at_threshold"] and abs(planned["H2_quality"]["t"]-abs(r["t"]))<1e-9
assert planned["n"]==r["n"]
require(".0167")
assert planned["H1_future_n_per_group_30_vs_60"]["at_threshold"]==63
h1,h3=planned["H1_group_difference"],planned["H3_overall_detection"]
assert h1["table"]==[[9,5],[1,11]] and h1["reject_at_threshold"] and not h3["reject_at_threshold"]
require(f'{100*h1["difference_in_proportions"]:.1f}',f'[{100*h1["difference_ci95_welch_t"][0]:.1f}, {100*h1["difference_ci95_welch_t"][1]:.1f}]',f'chi-square(1) = {h3["chi2"]:.3f}',f'[{100*h3["ci95_t"][0]:.1f}%, {100*h3["ci95_t"][1]:.1f}%]',f'U = {planned["confidence_exploratory"]["mann_whitney_u"]:.1f}')
for row in planned["H1_sensitivity"].values():
    require(f'{row["table"][0][0]}/{sum(row["table"][0])} | {row["table"][1][0]}/{sum(row["table"][1])}')
for banned in ("odds ratio","Spearman","exact binomial","Cohen w"):
    assert banned.lower() not in text.lower(),banned
print("Quality flow, estimates, intervals and regression terms checked against the report sections.")
