"""Check built Reveal.js decks in headless Chrome and save review screenshots."""

import argparse
import json
from pathlib import Path
import re

from playwright.sync_api import sync_playwright
from browser_runtime import launch_browser

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('lecture', nargs='?', default='01-decentralized-systems',
                        help='Lecture directory name, or all')
    parser.add_argument('--lang', choices=['en', 'hr'], default='en')
    args = parser.parse_args()
    source_name = 'slides.hr.qmd' if args.lang == 'hr' else 'slides.qmd'
    output_root = ROOT / 'output' / ('hr' if args.lang == 'hr' else '')
    if args.lecture == 'all':
        sources = sorted((ROOT / 'lectures').glob(f'[0-9][0-9]-*/{source_name}'))
    elif re.fullmatch(r'\d{2}-[a-z0-9-]+', args.lecture):
        sources = [ROOT / 'lectures' / args.lecture / source_name]
    else:
        parser.error('Use a numbered lecture directory name or all.')
    if not sources:
        parser.error(f'No {args.lang} slide sources found.')
    for source in sources:
        if not source.is_file():
            parser.error(f'Missing source: {source}')
        if not (output_root / 'slides' / (source.parent.name + '.html')).is_file():
            parser.error(f'Build the deck first: just slides {source.parent.name}')

    results = []
    with sync_playwright() as playwright:
        browser = launch_browser(playwright)
        try:
            for source in sources:
                name = source.parent.name
                deck = output_root / 'slides' / (name + '.html')
                output = output_root / 'qa' / name
                output.mkdir(parents=True, exist_ok=True)
                expected = 1 + len(re.findall(r'^## ', source.read_text(), re.M))
                errors = []
                page = browser.new_page(viewport={'width': 1280, 'height': 800}, device_scale_factor=1)
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.goto(deck.as_uri())
                page.wait_for_function('window.Reveal && Reveal.isReady()')
                page.evaluate('document.fonts.ready')
                count = page.evaluate('Reveal.getTotalSlides()')
                problems = []
                if count != expected:
                    problems.append({'kind': 'count', 'expected': expected, 'actual': count})
                for index in range(count):
                    page.evaluate('(index) => Reveal.slide(index)', index)
                    page.wait_for_timeout(350)
                    overflow = page.evaluate('''() => {
                      const slide = Reveal.getCurrentSlide(), r = slide.getBoundingClientRect();
                      return [...slide.querySelectorAll('h1,h2,p,li,img,table')]
                        .filter(el => !el.closest('aside'))
                        .filter(el => {
                          const b = el.getBoundingClientRect();
                          return b.width && b.height &&
                            (b.left < r.left-2 || b.right > r.right+2 ||
                             b.top < r.top-2 || b.bottom > r.bottom+2 ||
                             b.top < -2 || b.bottom > innerHeight+2 ||
                             b.left < -2 || b.right > innerWidth+2);
                        }).map(el => el.innerText || el.getAttribute('alt') || el.tagName);
                    }''')
                    missing_images = page.evaluate('''() => [...Reveal.getCurrentSlide().querySelectorAll('img')]
                      .filter(img => !img.complete || !img.naturalWidth)
                      .map(img => img.getAttribute('alt') || 'image')''')
                    if overflow or missing_images:
                        problems.append({'slide': index+1, 'overflow': overflow, 'missing_images': missing_images})
                    page.screenshot(path=str(output / f'slide-{index+1:02d}.png'))
                report = {'lecture': name, 'slides': count, 'expected_slides': expected,
                          'viewport': {'width': 1280, 'height': 800},
                          'runtime_errors': errors, 'problems': problems,
                          'passed': not errors and not problems}
                (output / 'browser-report.json').write_text(json.dumps(report, indent=2))
                results.append(report)
                page.close()
                print(f'{name}: {count} slides; {"PASS" if report["passed"] else "FAIL"}; screenshots in {output.relative_to(ROOT)}')
        finally:
            browser.close()
    if any(not report['passed'] for report in results):
        raise SystemExit('Browser checks failed; see output/qa/<lecture>/browser-report.json')


if __name__ == '__main__':
    main()
