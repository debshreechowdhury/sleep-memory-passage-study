"""Score mapped participant data and apply the study rules; retain exclusions for a count audit."""
import argparse, csv, re
from pathlib import Path

def score(value, low, high):
    text = str(value or "").strip()
    if not text: return None
    match = re.fullmatch(r"(\d+)(?:\s*(?:[—–-].*|minutes))?", text)
    if not match or not low <= int(match[1]) <= high:
        raise ValueError(f"Unexpected value: {text!r}")
    return int(match[1])

def clean_row(row):
    if row["order"] not in ("AI first", "Original first"):
        raise ValueError("Unknown passage order")
    out = {k: row.get(k, "") for k in ("response_id", "order", "status")}
    reasons = []
    if row.get("consent", "").strip().lower() not in ("yes, i agree", "yes", "true", "1"):
        reasons.append("consent_not_affirmed")
    checks = [score(row.get(f"check_{i}"), 0, 120) for i in (1,2)]
    if any(x not in (None,30,60,90,120) for x in checks):
        raise ValueError("Comprehension answer must be 30, 60, 90 or 120")
    if None in checks: reasons.append("missing_comprehension_review")
    elif all(x != 90 for x in checks): reasons.append("both_checks_wrong")
    for i, value in enumerate(checks, 1): out[f"check_{i}"] = value
    for pos in (1,2):
        version = "AI" if (pos == 1) == (row["order"] == "AI first") else "O"
        values = []
        for item in ("clear", "engage", "write"):
            value = score(row.get(f"{item}_{pos}"),1,7)
            out[f"{item}_{version}"] = value
            values.append(value)
        out[f"quality_{version}"] = sum(values)/3 if None not in values else None
    answer = row.get("detect", "").strip()
    if answer not in ("", "Passage 1", "Passage 2"):
        raise ValueError("Detection answer must be Passage 1 or Passage 2")
    correct = "Passage 1" if row["order"] == "AI first" else "Passage 2"
    out["detect_correct"] = int(answer == correct) if answer else None
    for name, high in (("confidence",5),("ai_use",5),("english",7)):
        out[name] = score(row.get(name),1,high)
    out["included"] = int(not reasons)
    out["exclusion_reason"] = ";".join(reasons)
    return out

def student_background(value):
    text = str(value or "").strip().lower()
    if not text: return None
    for prefix, label in (("international","International"),("domestic","Domestic"),("not applicable","Not applicable")):
        if text.startswith(prefix): return label
    raise ValueError("Unexpected student-background category; review mapping")

def analysis_row(row):
    """Study rule: current students only, with both comprehension checks correct. clean_row keeps the earlier both-wrong rule."""
    out = clean_row(row)
    out["student_background"] = student_background(row.get("student_background"))
    out["included_both_wrong_rule"] = out["included"]
    reasons = [r for r in out["exclusion_reason"].split(";") if r]
    if out["student_background"] is None: reasons.append("missing_student_background")
    elif out["student_background"] == "Not applicable": reasons.append("not_a_student")
    if sum(out[f"check_{i}"] == 90 for i in (1,2)) == 1: reasons.append("one_check_wrong")
    out["included"] = int(not reasons)
    out["exclusion_reason"] = ";".join(reasons)
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True); p.add_argument("--output",required=True)
    a=p.parse_args()
    with open(a.input,newline="") as f: rows=[analysis_row(r) for r in csv.DictReader(f)]
    if not rows: raise ValueError("No participant rows")
    ids=[r["response_id"] for r in rows]
    if len(ids)!=len(set(ids)): raise ValueError("Duplicate response IDs; review input")
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    with open(a.output,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f"Rows: {len(rows)}; included: {sum(r['included'] for r in rows)}")
if __name__ == "__main__": main()
