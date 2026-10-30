"""Draw state and transaction labels in BA diagrams as chips (lecturer, 2026-10-27/29).

Inside any <text>, three tokens are rewritten:
- ``v7``    -> state chip S with subscript 7 (slate for 7, green for 8)
- ``tx1``   -> transaction chip tx with subscript 1 (amber, like the TRANSAKCIJA pills)
- ``S_7``   -> plain S with subscript 7 (state-card titles), an optional prime may follow

Widths are measured with the same Arial/Menlo/Courier files that rsvg-convert uses,
and every piece is placed at an absolute x, so the chips sit behind their labels
without a browser in the build.
"""
import html
import re
from PIL import ImageFont

FONTS = {
    'Arial': ('/System/Library/Fonts/Supplemental/Arial.ttf', 0,
              '/System/Library/Fonts/Supplemental/Arial Bold.ttf', 0),
    'Menlo': ('/System/Library/Fonts/Menlo.ttc', 0, '/System/Library/Fonts/Menlo.ttc', 1),
    'Courier': ('/System/Library/Fonts/Supplemental/Courier New.ttf', 0,
                '/System/Library/Fonts/Supplemental/Courier New Bold.ttf', 0),
}
# Matches .ver.v7 / .ver.v8 and .tx in lecture.css: old state slate, new state green, transaction amber.
COLOURS = {'7': ('#edf1f5', '#a9b9c6', '#3d5568'), '8': ('#e3f4ea', '#86c3a0', '#1f6b43')}
TX_COLOURS = ('#fff6ea', '#ebcf9f', '#8a5a1c')
PAD, MARGIN = 6, 3
TEXT = re.compile(r'<text ([^>]*)>([^<]*)</text>')
TOKEN = re.compile(r'(?:·\s*)?\bv(?P<v>\d+)\b|\btx(?P<tx>\d+)\b|\bS_(?P<s>\d+)')

_cache = {}


def _attr(attrs, name, default):
    m = re.search(rf'\b{name}="([^"]*)"', attrs)
    return m.group(1) if m else default


def _width(s, family, bold, size):
    key = 'Courier' if 'Courier' in family else 'Menlo' if 'Menlo' in family else 'Arial'
    path, index, bold_path, bold_index = FONTS[key]
    k = (key, bold, round(size * 10))
    if k not in _cache:
        _cache[k] = ImageFont.truetype(bold_path if bold else path, int(size * 10), index=bold_index if bold else index)
    return _cache[k].getlength(s) / 10


def _render(match):
    attrs, raw = match.groups()
    content = html.unescape(raw)
    if not TOKEN.search(content):
        return match.group(0)
    family = _attr(attrs, 'font-family', 'Arial')
    size = float(_attr(attrs, 'font-size', '20'))
    bold = int(_attr(attrs, 'font-weight', '400')) >= 600
    fill = _attr(attrs, 'fill', '#20384d')
    x, y = float(_attr(attrs, 'x', '0')), float(_attr(attrs, 'y', '0'))
    sub, shift = size * .72, size * .22

    # Pieces: (kind, head, index); kind is 'text', 'state', 'tx' or 'plain'.
    pieces, pos = [], 0
    for m in TOKEN.finditer(content):
        if m.start() > pos:
            pieces.append(('text', content[pos:m.start()], ''))
        if m.group('v'):
            pieces.append(('state', 'S', m.group('v')))
        elif m.group('tx'):
            pieces.append(('tx', 'tx', m.group('tx')))
        else:
            pieces.append(('plain', 'S', m.group('s')))
        pos = m.end()
    if pos < len(content):
        pieces.append(('text', content[pos:], ''))

    def width(p):
        kind, head, idx = p
        if kind == 'text':
            return _width(head, family, bold, size)
        chip_bold = kind != 'plain' or bold
        w = _width(head, family, chip_bold, size) + _width(idx, family, chip_bold, sub)
        return w + (2 * (PAD + MARGIN) if kind in ('state', 'tx') else 0)

    total = sum(width(p) for p in pieces)
    anchor = _attr(attrs, 'text-anchor', 'start')
    cursor = x - total / 2 if anchor == 'middle' else x - total if anchor == 'end' else x
    rects, spans = '', ''
    h = size * 1.25
    for p in pieces:
        kind, head, idx = p
        w = width(p)
        if kind == 'text':
            lead = len(head) - len(head.lstrip(' '))
            body = head.strip(' ')
            if body:
                spans += f'<tspan x="{cursor + _width(" " * lead, family, bold, size):.1f}" y="{y:.1f}">{html.escape(body, quote=False)}</tspan>'
        else:
            chip = kind in ('state', 'tx')
            inner = cursor + (PAD + MARGIN if chip else 0)
            weight = '700' if chip or bold else '400'
            ink = fill
            if chip:
                cfill, stroke, ink = TX_COLOURS if kind == 'tx' else COLOURS.get(idx, COLOURS['7'])
                rects += (f'<rect x="{cursor + MARGIN:.1f}" y="{y - size * .36 - h / 2:.1f}" width="{w - 2 * MARGIN:.1f}" '
                          f'height="{h:.1f}" rx="{h / 2:.1f}" fill="{cfill}" stroke="{stroke}" stroke-width="1.3"/>')
            hw = _width(head, family, weight == '700', size)
            spans += f'<tspan x="{inner:.1f}" y="{y:.1f}" font-weight="{weight}" fill="{ink}">{head}</tspan>'
            spans += f'<tspan x="{inner + hw:.1f}" y="{y + shift:.1f}" font-size="{sub:.1f}" font-weight="{weight}" fill="{ink}">{idx}</tspan>'
        cursor += w
    attrs = re.sub(r'\btext-anchor="[^"]*"', '', attrs) + ' text-anchor="start"'
    return f'{rects}<text {attrs}>{spans}</text>'


def chips(svg):
    return TEXT.sub(_render, svg)
