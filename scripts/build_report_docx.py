"""Build a Word report from the authoritative Markdown source."""
import re
from pathlib import Path
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
root=Path(__file__).resolve().parents[1]
doc=Document();sec=doc.sections[0]
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=sec.bottom_margin=sec.left_margin=sec.right_margin=Inches(.85)
for name,size in [('Normal',11),('Title',21),('Heading 1',14),('Heading 2',12),('Caption',10)]:
 s=doc.styles[name];s.font.name='Times New Roman';s.font.size=Pt(size);s.font.color.rgb=RGBColor(0,0,0)
 s.paragraph_format.space_after=Pt(6)
doc.styles['Normal'].paragraph_format.line_spacing=1.12
for name in ('Heading 1','Heading 2'):
 doc.styles[name].paragraph_format.space_before=Pt(11)
 doc.styles[name].paragraph_format.keep_with_next=True
# Page numbers support review of a multi-page course report.
f=sec.footer.paragraphs[0];f.alignment=WD_ALIGN_PARAGRAPH.CENTER
field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');f._p.append(field)

def clean(t):
 t=re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'\1 (\2)',t)
 return t.replace('**','').replace('`','')
lines=(root/'report/report.md').read_text().splitlines();i=0
while i<len(lines):
 line=lines[i].strip()
 if not line:i+=1;continue
 if line.startswith('|'):
  rows=[]
  while i<len(lines) and lines[i].strip().startswith('|'):
   cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
   if not all(re.fullmatch(r':?-+:?',c or 'x') for c in cells):rows.append(cells)
   i+=1
  table=doc.add_table(rows=1,cols=len(rows[0]));table.autofit=False
  width=6.8/len(rows[0]); widths=[width]*len(rows[0])
  if len(rows[0])==4:widths=[2.65,1.38,1.38,1.39]
  if len(rows[0])==5:
   widths=[2.15,.85,.7,1.5,1.0]
   if rows[0][0]=='Background':widths=[1.7,.9,1.0,1.1,2.1]
   if rows[0][0]=='Assumed accuracies':widths=[1.8,1.25,1.25,1.25,1.25]
  for j,w in enumerate(widths):table.columns[j].width=Inches(w)
  for ri,values in enumerate(rows):
   cells=table.rows[0].cells if ri==0 else table.add_row().cells
   for j,value in enumerate(values):
    c=cells[j];c.width=Inches(widths[j]);c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER;c.text=clean(value)
    pr=c._tc.get_or_add_tcPr();borders=OxmlElement('w:tcBorders')
    for side in ('top','left','bottom','right'):
     el=OxmlElement(f'w:{side}');el.set(qn('w:val'),'single');el.set(qn('w:sz'),'4');el.set(qn('w:color'),'D9D9D9');borders.append(el)
    pr.append(borders);m=OxmlElement('w:tcMar')
    for side in ('top','left','bottom','right'):
     el=OxmlElement(f'w:{side}');el.set(qn('w:w'),'90');el.set(qn('w:type'),'dxa');m.append(el)
    pr.append(m)
    if ri==0 or ri%2==0:
     shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'DCE6F1' if ri==0 else 'F5F7FA');pr.append(shade)
    for p in c.paragraphs:
     p.paragraph_format.space_after=Pt(2);p.paragraph_format.line_spacing=1.05
     p.alignment=WD_ALIGN_PARAGRAPH.LEFT if j==0 else WD_ALIGN_PARAGRAPH.CENTER
     for r in p.runs:r.font.size=Pt(10);r.bold=ri==0
   trpr=table.rows[ri]._tr.get_or_add_trPr();trpr.append(OxmlElement('w:cantSplit'))
   if ri==0:trpr.append(OxmlElement('w:tblHeader'))
  doc.add_paragraph().paragraph_format.space_after=Pt(2)
  continue
 if line.startswith('!['):
  path=re.search(r'\]\(([^)]+)\)',line)[1]
  p=doc.add_paragraph();p.paragraph_format.keep_with_next=True
  p.add_run().add_picture(str(root/'report'/path),width=Inches(6.65))
 elif line.startswith('# '):doc.add_paragraph(clean(line[2:]),'Title')
 elif line.startswith('## '):doc.add_paragraph(clean(line[3:]),'Heading 1')
 elif line.startswith('### '):doc.add_paragraph(clean(line[4:]),'Heading 2')
 elif line.startswith('Figure '):doc.add_paragraph(clean(line),'Caption')
 else:doc.add_paragraph(clean(line))
 i+=1
# Remove decorative paragraph borders inherited from the Word template.
for element in (doc.styles.element, doc.element):
 for border in element.xpath('.//w:pBdr'):
  border.getparent().remove(border)
doc.core_properties.title='Perceived writing quality and AI detection in a sleep and memory passage study'
doc.core_properties.author='Debshree Chowdhury and Jakub Romańczuk'
doc.core_properties.comments=''
doc.save(root/'report/Sleep_memory_study_report.docx')
print('Saved report/Sleep_memory_study_report.docx')
