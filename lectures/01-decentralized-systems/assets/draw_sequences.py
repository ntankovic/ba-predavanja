"""Sequence diagram for a lost reply, in the style of RS 01 draw_sequences.py (lecturer, 2026-10-21)."""
from html import escape
from pathlib import Path
import subprocess
from version_chips import chips

ROOT = Path(__file__).parent
FONT = 'Arial, sans-serif'
MONO = 'Courier New, monospace'  # rsvg/fontconfig cannot see Menlo on macOS
INK, MUTED, BLUE, RED, GREEN = '#18344b', '#546573', '#3886ad', '#b33e44', '#28674b'

DEFS = f'''<defs>
<marker id="arrow-blue" markerUnits="userSpaceOnUse" markerWidth="18" markerHeight="18" refX="14" refY="9" orient="auto"><path d="M2,2 L18,9 L2,16 Z" fill="{BLUE}"/></marker>
<marker id="arrow-red" markerUnits="userSpaceOnUse" markerWidth="18" markerHeight="18" refX="14" refY="9" orient="auto"><path d="M2,2 L18,9 L2,16 Z" fill="{RED}"/></marker>
<marker id="arrow-axis" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" refX="12" refY="8" orient="auto"><path d="M2,2 L16,8 L2,14 Z" fill="#90a5b3"/></marker>
</defs>'''


def text(x, y, s, size=20, weight=400, fill=INK, anchor='middle', family=FONT):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{family}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}">{escape(s)}</text>')


def card(x, y, w, h, fill='#f8fbfd', stroke='#c6dbe8', accent=BLUE):
    return (f'<rect x="{x + 1}" y="{y + 5}" width="{w - 2}" height="{h}" rx="14" fill="#24445c" opacity=".035"/>'
            f'<rect x="{x}" y="{y + 2}" width="{w}" height="{h}" rx="14" fill="#24445c" opacity=".025"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>'
            f'<rect x="{x + 12}" y="{y + h / 2 - 15}" width="6" height="30" rx="3" fill="{accent}"/>')


def arrow(d, colour=BLUE, marker='blue', dash=''):
    dash = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{d}" fill="none" stroke="{colour}" stroke-width="3.2" stroke-linecap="round"'
            f'{dash} marker-end="url(#arrow-{marker})"/>')


def loss(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="17" fill="#fbecee" stroke="{RED}" stroke-width="2.4"/>'
            f'<path d="M{x - 7} {y - 7}L{x + 7} {y + 7}M{x + 7} {y - 7}L{x - 7} {y + 7}" '
            f'stroke="{RED}" stroke-width="3.6" stroke-linecap="round"/>')


def svg(w, h, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
            f'<title>{escape(title)}</title>{DEFS}<rect width="{w}" height="{h}" fill="white"/>'
            + ''.join(body) + '</svg>\n')


def reply_lost():
    cx, sx = 225, 810
    return [
        card(80, 14, 290, 60), text(cx + 6, 52, 'Klijent organizacije', 23, 600),
        card(650, 14, 320, 60), text(sx + 6, 52, 'Koordinator', 23, 600),
        f'<path d="M{cx} 86V132 M{sx} 86V372" stroke="#b5c7d2" stroke-width="2" stroke-dasharray="5 7"/>',
        # The client waits until its deadline expires.
        f'<rect x="{cx - 8}" y="132" width="16" height="246" rx="5" fill="#fff1df" stroke="#e1be89" stroke-width="1.4"/>',
        text(cx - 22, 262, 'čeka odgovor', 18, 400, '#976023', 'end'),
        '<path d="M1062 100V352" stroke="#90a5b3" stroke-width="2" marker-end="url(#arrow-axis)"/>',
        text(1062, 386, 'Vrijeme', 18, 400, MUTED),
        text(517, 112, 'isplati(F, X, 80, v7)', 20, 400, INK, family=MONO),
        arrow(f'M{cx + 10} 134L{sx - 6} 182'),
        card(640, 198, 340, 52, '#eef7f2', '#b9dcc8', GREEN),
        text(sx + 6, 231, 'Upisano: F:20 · X:80 · v8', 21, 600, GREEN),
        arrow(f'M{sx} 274L466 323', RED, 'red', '9 7'),
        text(652, 281, 'potvrda tx1', 20, 400, RED),
        loss(440, 327),
        text(440, 372, 'Odgovor izgubljen', 21, 600, RED),
        card(47, 392, 356, 54, '#fbecee', '#e8c2c5', RED),
        text(cx + 6, 426, 'Timeout: ishod nepoznat', 22, 600, '#a23b43'),
    ]


path = ROOT / 'figure-15.hr.svg'
path.write_text(chips(svg(1120, 460, 'Isplata je upisana, potvrda se izgubila', reply_lost())))
subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', str(path.with_suffix('.pdf')), str(path)], check=True)
