"""Check Debshree's current report/deck evidence without changing protected inputs."""
import hashlib
import json
from pathlib import Path
from pptx import Presentation
ROOT=Path(__file__).resolve().parents[2]


def check():
    x=json.loads((ROOT/'results/quality/hypothesis_tests.json').read_text())
    a=ROOT/'study/stimuli'
    checksums=json.loads((a/'checksums.json').read_text())
    for name,digest in checksums.items():
        assert hashlib.sha256((a/name).read_bytes()).hexdigest()==digest, name
    original=(a/'original.txt').read_text().strip()
    rewrite=(a/'ai_rewrite.txt').read_text().strip()
    assert len(original.split('\n\n'))==len(rewrite.split('\n\n'))==4
    assert original.split('\n\n')[2]==rewrite.split('\n\n')[2], 'Quotation changed'
    assert original.endswith('90 minutes”'), 'Administered punctuation must be preserved'
    assert '90 minutes.' in (ROOT/'study/instrument.md').read_text()
    prompts=(a/'prompt.txt').read_text()
    assert prompts.index('1st prompt:')<prompts.index('2nd prompt:')
    assert "'m running a research study" in prompts and 'do it again but:' in prompts
    assert x['n']==26 and x['threshold']==.05
    deck=Presentation(ROOT/'presentation/design_detection.pptx')
    assert len(deck.slides)==7
    expected=[1,2,3,4,6,10,11]
    for number,slide in zip(expected,deck.slides):
        footer=next(sh.text for sh in slide.shapes if sh.name=='Footer')
        assert footer.startswith(f'{number}  ')
        assert slide.has_notes_slide and slide.notes_slide.notes_text_frame.text
    charts=[sh.chart for slide in deck.slides for sh in slide.shapes if sh.has_chart]
    assert len(charts)==1
    assert list(charts[0].series[0].values)==[x['H1_group_difference']['groups'][g]['proportion'] for g in ('International','Domestic')]
    for chart in charts:
        for node in chart._chartSpace.xpath('.//c:axId'):
            assert 0<=int(node.get('val'))<=0xffffffff
    print('Current result/deck mapping, slide order, archive hashes, quotation and punctuation distinction checked.')

if __name__=='__main__':check()
