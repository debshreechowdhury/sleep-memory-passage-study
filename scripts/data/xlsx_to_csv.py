"""Convert the private Forms workbook to a private CSV, keeping every column unchanged for the importer."""
import argparse, csv
from pathlib import Path
import openpyxl

def cell(value):
    # Excel stores the rating scale as floats; the cleaner accepts only whole numbers.
    if isinstance(value,float) and value.is_integer(): return str(int(value))
    return "" if value is None else str(value)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True);p.add_argument("--output",required=True)
    a=p.parse_args()
    book=openpyxl.load_workbook(a.input,read_only=True,data_only=True)
    if len(book.sheetnames)!=1: raise ValueError("Expected one response sheet; review the workbook")
    rows=book[book.sheetnames[0]].iter_rows(values_only=True)
    headers=next(rows)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    count=0
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f);w.writerow(cell(h) for h in headers)
        for row in rows:
            if all(v is None for v in row): continue
            w.writerow(cell(row[i]) if i<len(row) else "" for i in range(len(headers)));count+=1
    print(f"Converted {count} rows to the private CSV.")
if __name__=="__main__":main()
