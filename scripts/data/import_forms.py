"""Import CSV exports using reviewed, zero-based column positions; discard identifiers."""
import argparse, csv, json
from pathlib import Path
FIELDS = ["consent", "status", "student_background", "check_1", "check_2", "detect", "confidence", "ai_use", "english"] + [f"{item}_{pos}" for pos in (1, 2) for item in ("clear", "engage", "write")]

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()
    manifest_path = Path(a.manifest)
    manifest = json.loads(manifest_path.read_text())
    rows = []
    for source in manifest["sources"]:
        if source["order"] not in ("AI first", "Original first"):
            raise ValueError("Each source must have a verified passage order")
        mapping = source["columns"]
        required = {"consent", "status", "check_1", "check_2", "detect"} | {f"{x}_{i}" for i in (1,2) for x in ("clear","engage","write")}
        if not required <= mapping.keys() or set(mapping) - set(FIELDS):
            raise ValueError("Missing required or unsupported mapped fields")
        if len(set(mapping.values())) != len(mapping):
            raise ValueError("Do not map one export column to multiple variables")
        path = manifest_path.parent / source["path"]
        with path.open(newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            headers = next(reader)
            if headers != source["expected_headers"]:
                raise ValueError(f"Headers changed for {path}; review mapping before import")
            for raw in reader:
                if len(raw) != len(headers):
                    raise ValueError("Unexpected CSV row width")
                row = {key: raw[index].strip() for key, index in mapping.items()}
                row.update(response_id=f"R{len(rows)+1:05}", order=source["order"])
                rows.append(row)
    Path(a.output).parent.mkdir(parents=True, exist_ok=True)
    with open(a.output, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["response_id", "order"] + FIELDS)
        w.writeheader(); w.writerows(rows)
    print(f"Imported {len(rows)} rows; names, email, timestamps and free text not exported.")
if __name__ == "__main__": main()
