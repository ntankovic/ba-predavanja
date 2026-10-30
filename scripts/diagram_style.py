"""Shared visual style for original Croatian course diagrams (SVG/PDF)."""
from html import escape
import textwrap
BLUE = '#3886ad'
INK = '#20384d'
RED = '#b63842'

def text(x, y, value, size=24, color=INK, weight=400):
    return (f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Arial, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>')

def box(x, y, w, h, label, sub=''):
    title_size = 25 if w >= 230 else 23
    sub_size = 18
    # Keep explicit inner margins, wrapping descriptions rather than shrinking text.
    max_chars = max(12, int((w - 42) / (sub_size * .52)))
    lines = textwrap.wrap(sub, width=max_chars, break_long_words=False, break_on_hyphens=False)
    title_height = title_size * 1.15
    # Centre the title and its subtitle as one group; a one-line subtitle reserves one line (lecturer, 2026-10-28).
    subtitle_height = len(lines) * 24
    group_height = title_height + (12 + subtitle_height if lines else 0)
    top = y + (h - group_height) / 2
    radius = 16
    result = (f'<rect x="{x+1}" y="{y+5}" width="{w-2}" height="{h}" rx="{radius}" fill="#24445c" opacity=".035"/>'
              f'<rect x="{x}" y="{y+2}" width="{w}" height="{h}" rx="{radius}" fill="#24445c" opacity=".025"/>'
              f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="#f8fbfd" '
              f'stroke="#c6dbe8" stroke-width="1.2"/>'
              f'<rect x="{x+12}" y="{y+min(28,h*.28)}" width="7" height="{h-2*min(28,h*.28)}" rx="3.5" fill="#3886ad"/>')
    result += text(x+w/2, top+title_size*.82, label, title_size, INK, 600)
    for i, line in enumerate(lines):
        result += text(x+w/2, top+title_height+12+(subtitle_height-len(lines)*24)/2+sub_size*.82+i*24, line, sub_size, '#536b7b')
    return result

def state_box(x, y, w, h, label, sub=''):
    # A state is a record, not a node: tinted card, solid blue rim, STANJE band inside, no side bar (lecturer, 2026-10-29).
    band = 24
    title_size = 24 if w >= 200 else 22
    sub_size = 17
    max_chars = max(10, int((w - 30) / (sub_size * .52)))
    lines = textwrap.wrap(sub, width=max_chars, break_long_words=False, break_on_hyphens=False)
    title_height = title_size * 1.15
    subtitle_height = len(lines) * 22
    group_height = title_height + (10 + subtitle_height if lines else 0)
    top = y + band + (h - band - group_height) / 2
    result = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#e6f1f8" stroke="#3886ad" stroke-width="2"/>'
              f'<path d="M{x+1},{y+band} L{x+w-1},{y+band}" stroke="#3886ad" stroke-width="1.2" opacity=".5"/>'
              f'<path d="M{x+10},{y+1} H{x+w-10} A9,9 0 0 1 {x+w-1},{y+10} V{y+band} H{x+1} V{y+10} A9,9 0 0 1 {x+10},{y+1} Z" fill="#3886ad" opacity=".14"/>')
    result += text(x+w/2, y+17, 'STANJE', 13, '#2a6f93', 700)
    result += text(x+w/2, top+title_size*.82, label, title_size, INK, 700)
    for i, line in enumerate(lines):
        result += text(x+w/2, top+title_height+10+sub_size*.82+i*22, line, sub_size, '#2f526b')
    return result

def cut(x, y, r=15):
    # A cut link: white disc with red rim and a red cross centred on the line (lecturer, 2026-10-29).
    d = r * .45
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" stroke="{RED}" stroke-width="2.4"/>'
            f'<path d="M{x-d},{y-d} L{x+d},{y+d} M{x+d},{y-d} L{x-d},{y+d}" stroke="{RED}" stroke-width="3.4" stroke-linecap="round"/>')

TONES = {'blue': ('#eef6fa', '#9cc4da', INK, '#3886ad'), 'red': ('#fdf1f2', '#e3a9ae', RED, RED)}

def pill(x, y, w, h, title, sub='', num=None, tone='blue'):
    # Steps, actions and messages are pills, never node cards (lecturer, 2026-10-29).
    fill, stroke, ink, accent = TONES[tone]
    result = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>'
    cx, cy = x + w / 2, y + h / 2
    if num is not None:
        r = min(17, h / 2 - 7)
        result += f'<circle cx="{x+h/2}" cy="{cy}" r="{r}" fill="{accent}"/>' + text(x + h / 2, cy + 6.5, str(num), 18, '#ffffff', 700)
        cx = x + h / 2 + (w - h / 2) / 2
    if sub:
        result += text(cx, cy - 3, title, 20, ink, 700) + text(cx, cy + 20, sub, 16, '#536b7b' if tone == 'blue' else ink)
    else:
        result += text(cx, cy + 7, title, 21, ink, 700)
    return result

def panel(x, y, w, h, label, body, color=BLUE, size=20):
    # Scenarios, cases and facts are open panels with a coloured top rule; no frame, no side bar (lecturer, 2026-10-29).
    lines = textwrap.wrap(body, width=max(12, int((w - 30) / (size * .5))), break_long_words=False)
    result = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" opacity=".06"/>'
              f'<rect x="{x}" y="{y}" width="{w}" height="5" fill="{color}"/>')
    result += text(x + w / 2, y + 42, label, 23, color, 700)
    top = y + 42 + 14 + (h - 56 - len(lines) * (size + 8)) / 2
    for i, line in enumerate(lines):
        result += text(x + w / 2, top + size * .82 + i * (size + 8), line, size, INK)
    return result

def markers():
    return '<defs>' + ''.join(
        f'<marker id="arrow-{name}" markerWidth="18" markerHeight="18" refX="14" refY="9" orient="auto" markerUnits="userSpaceOnUse"><path d="M2,2 L18,9 L2,16 Z" fill="{color}"/></marker>'
        for name, color in [('blue', BLUE), ('red', RED)]) + '</defs>'

def arrow(x, y, x2, y2, label='', color=BLUE, dash=False):
    marker = 'red' if color == RED else 'blue'
    result = (f'<path d="M{x},{y} L{x2},{y2}" fill="none" stroke="{color}" stroke-width="3.2" '
              f'stroke-linecap="round" '+('stroke-dasharray="7 6" ' if dash else '')+
              f'marker-end="url(#arrow-{marker})"/>')
    return result + (text((x+x2)/2, (y+y2)/2-13, label, 19, color) if label else '')
