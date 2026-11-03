"""Build the three-page report from its reviewable Markdown source."""
from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'report/three_page_report.md'
OUTPUT = ROOT / 'report/Sleep_memory_study_three_pages.docx'

def main():
    doc = Document()
    section = doc.sections[0]
    section.page_width, section.page_height = Inches(8.5), Inches(11)
    section.top_margin = section.bottom_margin = Inches(.62)
    section.left_margin = section.right_margin = Inches(.7)
    section.footer_distance = Inches(.25)
    for name, size in [('Normal', 10.5), ('Title', 16), ('Heading 1', 11.5)]:
        style = doc.styles[name]
        style.font.name = 'Times New Roman'
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.space_after = Pt(4)
        style.paragraph_format.line_spacing = 1.0
    doc.styles['Heading 1'].paragraph_format.space_before = Pt(6)
    doc.styles['Heading 1'].paragraph_format.keep_with_next = True
    doc.styles['Title'].paragraph_format.keep_with_next = True
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    field = OxmlElement('w:fldSimple'); field.set(qn('w:instr'), 'PAGE'); footer._p.append(field)
    lines = SOURCE.read_text(encoding='utf-8').splitlines()
    i = 0; references = False
    while i < len(lines):
        line = lines[i].strip()
        if not line: i += 1; continue
        if line == '<!-- pagebreak -->': doc.add_page_break()
        elif line.startswith('# '): doc.add_paragraph(line[2:], 'Title')
        elif line.startswith('## '):
            heading = line[3:]
            references = heading == 'References'
            doc.add_paragraph(heading, 'Heading 1')
        elif line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [s.strip() for s in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(':?-+:?', s) for s in cells): rows.append(cells)
                i += 1
            table = doc.add_table(rows=0, cols=3)
            table.autofit = False
            widths = [1.5, 3.0, 2.6]
            for col, width in zip(table.columns, widths): col.width = Inches(width)
            for j, values in enumerate(rows):
                row = table.add_row()
                pr = row._tr.get_or_add_trPr(); pr.append(OxmlElement('w:cantSplit'))
                for cell, value, width in zip(row.cells, values, widths):
                    cell.width = Inches(width); cell.text = value
                    for para in cell.paragraphs:
                        para.paragraph_format.space_after = Pt(3)
                        for run in para.runs: run.font.size = Pt(10); run.bold = j == 0
                    tcpr = cell._tc.get_or_add_tcPr()
                    if j == 0:
                        shade = OxmlElement('w:shd'); shade.set(qn('w:fill'), 'ECEFF2'); tcpr.append(shade)
                if j == 0: pr.append(OxmlElement('w:tblHeader'))
            continue
        else:
            p = doc.add_paragraph(line)
            if references:
                p.paragraph_format.space_after = Pt(3)
                for run in p.runs: run.font.size = Pt(9)
        i += 1
    for element in (doc.styles.element, doc.element):
        for border in element.xpath('.//w:pBdr'): border.getparent().remove(border)
    doc.core_properties.title = 'AI rewrite identification and writing quality by student background'
    doc.core_properties.author = 'Debshree Chowdhury and Jakub Romańczuk'
    doc.core_properties.comments = ''
    doc.save(OUTPUT)
    print(OUTPUT)

if __name__ == '__main__': main()
