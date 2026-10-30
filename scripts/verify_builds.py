"""Check course build coverage, PDF/HTML content, and planned lecture timing."""
from html.parser import HTMLParser
from pathlib import Path
import re
import json
import fitz

ROOT = Path(__file__).resolve().parents[1]


def normalized(text):
    return ' '.join(text.split())


class Deck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = 0
        self.notes = 0
        self.local_resources = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section' and ('slide' in attrs.get('class', '').split() or attrs.get('id') == 'title-slide'):
            self.slides += 1
        if tag == 'aside' and 'notes' in attrs.get('class', '').split():
            self.notes += 1
        if tag in ('script', 'img', 'link'):
            url = attrs.get('src') or attrs.get('href', '')
            if url and not url.startswith(('data:', 'http:', 'https:', '#')):
                self.local_resources.append(url)


def main():
    sources = sorted((ROOT / 'lectures').glob('[0-9][0-9]-*/chapter.qmd'))
    assert sources, 'No numbered lectures found'
    configuration = (ROOT / 'publishing/book/_quarto.yml').read_text()
    paths = re.findall(r'^    - (lectures/.+/chapter\.qmd)$', configuration, re.M)
    assert paths == [str(p.relative_to(ROOT)) for p in sources], 'Book order differs from lecture sequence'
    with fitz.open(ROOT / 'output/book/blockchain-applications.pdf') as doc:
        book_text = normalized(' '.join(page.get_text() for page in doc))
        book_pages = len(doc)
    assert 'Nikola Tankovic' in book_text and 'Juraj Dobrila' in book_text
    assert '[Lecture title]' not in book_text, 'Template leaked into book'
    records = []
    for source in sources:
        name = source.parent.name
        metadata = json.loads((source.parent / 'lecture.json').read_text())
        scaffold = metadata.get('scaffold', False)
        title = re.search(r'^title: "(.+)"$', source.read_text(), re.M)[1]
        with fitz.open(ROOT / 'output/lectures' / f'{name}.pdf') as doc:
            text = normalized(' '.join(page.get_text() for page in doc))
            assert title in text, f'{name}: missing PDF title'
            assert 'Nikola Tankovic' in text and 'Juraj Dobrila' in text, f'{name}: missing identity'
            if not scaffold:
                assert ('Example' in text or 'Worked scenario' in text) and ('Discussion' in text or 'discussion' in text), f'{name}: incomplete PDF'
                assert len(text) > 300, f'{name}: unexpectedly short PDF'
            page_count = len(doc)
        assert title in book_text, f'{name}: missing from complete book'
        html = (ROOT / 'output/slides' / f'{name}.html').read_text()
        deck = Deck()
        deck.feed(html)
        slide_source = (source.parent / 'slides.qmd').read_text()
        expected_slides = 1 + len(re.findall(r'^## ', slide_source, re.M))
        assert deck.slides == expected_slides, f'{name}: expected {expected_slides} slides, found {deck.slides}'
        assert deck.notes >= expected_slides - 1, f'{name}: missing speaker notes'
        timing_file = source.parent / 'timing.json'
        declared = metadata.get('duration_minutes')
        assert isinstance(declared, (int, float)) and 90 <= declared <= 120, f'{name}: declare 90–120 minutes in lecture.json'
        if not scaffold:
            assert timing_file.exists(), f'{name}: developed lecture requires timing.json'
        if timing_file.exists():
            timing = json.loads(timing_file.read_text())
            assert len(timing) == expected_slides, f'{name}: timing/slide count mismatch'
            elapsed = 0
            for number, segment in enumerate(timing, 1):
                assert segment['slide'] == number and segment['start'] == elapsed
                assert segment['minutes'] > 0 and segment['end'] - segment['start'] == segment['minutes']
                elapsed = segment['end']
            assert elapsed == declared, f'{name}: timing total {elapsed} differs from declared {declared} minutes'
        assert not deck.local_resources, f'{name}: non-embedded resources {deck.local_resources}'
        assert title in html and 'Nikola Tankovic' in html and 'Juraj Dobrila' in html
        review_label = 'scaffold — structure only' if scaffold else 'structural checks pass; content review separate'
        records.append(f'| {name} | [{page_count}](lectures/{name}.pdf) | [{deck.slides}](slides/{name}.html) | {review_label} |')
    slide_only = [p for p in sorted((ROOT / 'lectures').glob('[0-9][0-9]-*/slides.qmd'))
                  if not (p.parent / 'chapter.qmd').exists()]
    for source in slide_only:
        name = source.parent.name
        metadata = json.loads((source.parent / 'lecture.json').read_text())
        assert metadata.get('slides_only') is True, f'{name}: missing slides-only declaration'
        assert name not in configuration, f'{name}: slides-only deck leaked into book configuration'
        title = re.search(r'^title: "(.+)"$', source.read_text(), re.M)[1]
        assert title not in book_text, f'{name}: administrative title leaked into book'
        html = (ROOT / 'output/slides' / f'{name}.html').read_text()
        deck = Deck()
        deck.feed(html)
        expected = 1 + len(re.findall(r'^## ', source.read_text(), re.M))
        assert deck.slides == expected and deck.notes >= expected - 1, f'{name}: incomplete deck'
        assert not deck.local_resources, f'{name}: non-embedded resources'
        assert title in html and 'Nikola Tankovic' in html and 'Juraj Dobrila' in html
        if not metadata.get('scaffold', False) or (source.parent / 'timing.json').exists():
            timing = json.loads((source.parent / 'timing.json').read_text())
            assert len(timing) == expected
            elapsed = 0
            for number, segment in enumerate(timing, 1):
                assert segment['slide'] == number and segment['start'] == elapsed
                assert segment['minutes'] > 0 and segment['end'] - segment['start'] == segment['minutes']
                elapsed = segment['end']
            assert elapsed == metadata['duration_minutes'], f'{name}: incorrect planned duration'
        records.insert(0, f'| {name} | slides only | [{deck.slides}](slides/{name}.html) | pass |')
    report = f'''# Build verification

Verified {len(sources)} lecture PDFs, {len(sources) + len(slide_only)} standalone HTML slide decks, and the {book_pages}-page combined book PDF.

Checks: book chapter order and coverage; PDF titles, identity, and required sections; slide counts against source; speaker notes; declared 90–120-minute timing for developed technical lectures (scaffolds excluded) and declared timing for slides-only orientations; no local external script, image, or stylesheet dependencies.

These are structural and content checks. Visual review is separate. Successful builds do not replace content review or classroom rehearsal. See lecture briefs for development status.

| Lecture | PDF pages | Slides | Result |
| --- | --- | --- | --- |
'''+ '\n'.join(records)+'\n'
    (ROOT / 'output/build-report.md').write_text(report)
    print(report)


if __name__ == '__main__':
    main()
