"""Original editable BA 02 illustrations, exported to SVG and vector PDF.

Visual grammar carried over from BA 01 (lecturer, 2026-10-27): cards are nodes
only (organizations, replicas, identities); pills are steps, options or
messages; coloured rows list concepts. Red marks a member that deviates from
the protocol, grey a stopped member. State versions become chips (version_chips).
"""
from pathlib import Path
import sys, subprocess
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / 'scripts'))
from diagram_style import box, text, arrow, markers, BLUE, RED, INK
from version_chips import chips

P = Path(__file__).parent
MUTED, GREEN, AMBER = '#6b7f8e', '#28674b', '#b38337'
ROW_COLOURS = [BLUE, '#7770a5', AMBER, GREEN]


def node(x, y, w, h, label, sub='', state=''):
    """A participant card; state is '', 'bad' (deviates) or 'down' (stopped)."""
    s = box(x, y, w, h, label, sub)
    if state == 'bad':
        s = s.replace('fill="#f8fbfd" stroke="#c6dbe8"', 'fill="#fdf1f2" stroke="#e3a9ae"').replace(f'fill="{BLUE}"/>', f'fill="{RED}"/>')
        s = s.replace(f'fill="{INK}">', f'fill="{RED}">', 1)
    elif state == 'down':
        s = s.replace('fill="#f8fbfd" stroke="#c6dbe8"', 'fill="#f1f3f5" stroke="#c9d1d8" stroke-dasharray="6 5"').replace(f'fill="{BLUE}"/>', 'fill="#a4b0ba"/>')
        s = s.replace(f'fill="{INK}">', f'fill="{MUTED}">', 1)
    return s


def pill(cx, cy, w, label, tone='plain', size=20, h=50):
    fill, stroke, ink = {'plain': ('#f3f8fb', '#c6dbe8', INK), 'bad': ('#fbeaec', '#e3a5ad', RED),
                         'good': ('#e9f5ee', '#9fcdb1', GREEN), 'note': ('#fff6ea', '#ebcf9f', '#8a5a1c'),
                         'down': ('#f1f3f5', '#c9d1d8', MUTED)}[tone]
    return (f'<rect x="{cx - w / 2}" y="{cy - h / 2}" width="{w}" height="{h}" rx="{h / 2}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
            + text(cx, cy + size * .36, label, size, ink, 600))


def rows(items, y0=15, h=78, gap=12, title_x=235, sub_x=700, sub_size=21):
    s = ''
    for i, item in enumerate(items):
        title, sub = item.split('|', 1)
        y, c = y0 + i * (h + gap), ROW_COLOURS[i % 4]
        s += f'<rect x="25" y="{y}" width="990" height="{h}" rx="12" fill="#f3f8fb"/><rect x="25" y="{y}" width="7" height="{h}" fill="{c}"/>'
        s += text(title_x, y + h / 2 + 8, title, 23, c, 600) + text(sub_x, y + h / 2 + 8, sub, sub_size)
    return s


def dot(cx, cy, label, state='', r=34):
    fill, stroke, ink = {'': ('#f8fbfd', '#8fb6cd', INK), 'bad': ('#fbeaec', RED, RED),
                         'down': ('#f1f3f5', '#b5c0c8', MUTED), 'sybil': ('#fbeaec', RED, RED)}[state]
    dash = ' stroke-dasharray="5 4"' if state == 'down' else ''
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2.2"{dash}/>' + text(cx, cy + 8, label, 22, ink, 700)


def bracket(x1, x2, y, label, colour=BLUE, up=True):
    d = -14 if up else 14
    return (f'<path d="M{x1},{y - d} L{x1},{y} L{x2},{y} L{x2},{y - d}" fill="none" stroke="{colour}" stroke-width="2.6"/>'
            + text((x1 + x2) / 2, y + (-12 if up else 30), label, 19, colour, 600))


def side_arrow(x, y, x2, y2, label, colour=BLUE, side='l', gap=16):
    """Diagonal arrow whose label sits beside the shaft, never on it."""
    import math
    mx, my = (x + x2) / 2, (y + y2) / 2
    dx, dy = x2 - x, y2 - y
    d = math.hypot(dx, dy)
    nx, ny = (-dy / d, dx / d)
    if (side == 'l') != (nx < 0):
        nx, ny = -nx, -ny
    lx, ly = mx + nx * (gap + 8), my + ny * (gap + 8)
    t = text(lx, ly + 6, label, 18, colour, 600).replace('text-anchor="middle"', f'text-anchor="{"end" if side == "l" else "start"}"')
    t = t.replace('<text ', '<text paint-order="stroke" stroke="white" stroke-width="5" stroke-linejoin="round" ')
    return arrow(x, y, x2, y2, color=colour) + t


def line(x, y, x2, y2, colour='#9fb3c2', dash=True):
    return f'<path d="M{x},{y} L{x2},{y2}" stroke="{colour}" stroke-width="2" fill="none"' + (' stroke-dasharray="6 6"' if dash else '') + '/>'


def venn(left, mid, right, cap_l, cap_r, mid_state='good', top='', cap_cols=(INK, INK)):
    mc = RED if mid_state == 'bad' else GREEN
    s = (f'<ellipse cx="385" cy="150" rx="185" ry="105" fill="#e7f3fb" stroke="{BLUE}" stroke-width="2"/>'
         f'<ellipse cx="655" cy="150" rx="185" ry="105" fill="#fff2df" fill-opacity=".75" stroke="{AMBER}" stroke-width="2"/>')
    s += text(300, 158, left, 32, BLUE, 700) + text(520, 158, mid, 32, mc, 700) + text(740, 158, right, 32, AMBER, 700)
    s += text(265, 285, cap_l, 22, cap_cols[0]) + text(775, 285, cap_r, 22, cap_cols[1])
    if top:
        s += text(520, 30, top, 22, mc, 600)
    return s


def seq(lanes, msgs, ends, y0=100, step=44):
    """Message sequence: lanes = [(key, label, state)], msgs = (from, to, label, tone) or ('note', key, label)."""
    xs = {k: 130 + i * (780 / (len(lanes) - 1)) for i, (k, _, _) in enumerate(lanes)}
    s = ''
    for k, label, state in lanes:
        x = xs[k]
        fill, stroke, col = {'': ('#f8fbfd', '#c6dbe8', INK), 'bad': ('#fbeaec', '#e3a5ad', RED)}[state]
        s += f'<rect x="{x - 95}" y="10" width="190" height="54" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="1.2"/>' + text(x, 45, label, 20, col, 600)
        s += line(x, 64, x, y0 + step * len(msgs) - 10)
    y = y0
    for m in msgs:
        if m[0] == 'note':
            s += pill(min(xs[m[1]], 1040 - 135), y - 6, 260, m[2], 'note', 16, 34)
        else:
            a, b, label, tone = m
            x1, x2 = xs[a], xs[b]
            d = 1 if x2 > x1 else -1
            col = RED if tone == 'bad' else BLUE
            s += arrow(x1 + d * 6, y, x2 - d * 8, y, color=col) + text((x1 + x2) / 2 if abs(x2 - x1) < 300 else x1 + d * 150, y - 12, label, 17, col)
        y += step
    for k, (label, tone) in ends.items():
        s += pill(xs[k], y + 18, 220, label, tone, 18, 46)
    return s, y + 60


def export(name, height, body, caption=''):
    if caption:
        body += text(520, height - 22, caption, 22)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1040" height="{height}" viewBox="0 0 1040 {height}">'
           + markers() + f'<rect width="1040" height="{height}" fill="white"/>' + body + '</svg>')
    path = P / f'{name}.hr.svg'
    path.write_text(chips(svg))
    subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', str(path.with_suffix('.pdf')), str(path)], check=True)


FIG = {}


def fig(fn):
    FIG[fn.__name__.replace('_', '-')] = fn
    return fn


@fig
def recap_two_of_three():
    return 345, venn('B', 'A', 'C', 'tx1: glasovi A + B', 'tx2: glasovi A + C', 'bad', 'A glasa za oba prijedloga'), \
        'Lekcija 01: pravilo „dva od tri” dalo je 140 iz 100'


@fig
def two_questions():
    return 230, rows(['Neki sudionici lažu|Koliko poštenih treba? (bizantski članovi)',
                      'Identiteti se mogu stvarati|Što tada broji glasanje? (Sybil napad)']), \
        'Dva dijela predavanja, isti budžet F:100'


@fig
def consensus_task():
    s = node(30, 20, 300, 120, 'B', 'predlaže tx1 · v7') + node(370, 20, 300, 120, 'C', 'predlaže tx2 · v7') + node(710, 20, 300, 120, 'A', 'ne predlaže ništa')
    for x in (180, 520, 860):
        s += arrow(x, 150, x, 200)
    s += pill(520, 240, 760, 'Svi ispravni članovi odluče isto: npr. tx1 · v8', 'good', 21, 56)
    return 330, s, 'Konsenzus: od različitih prijedloga do jedne zajedničke odluke'


@fig
def agreement_broken():
    s = node(60, 20, 400, 130, 'B', 'odlučio: tx1 konačan · F:20', 'bad') + node(580, 20, 400, 130, 'C', 'odlučio: tx2 konačan · F:40', 'bad')
    s += text(520, 95, '≠', 46, RED, 700)
    return 230, s, 'Dva ispravna člana, dvije različite odluke: dogovor je prekršen'


@fig
def validity_trivial():
    s = ''.join(node(30 + i * 340, 20, 300, 120, k, 'odlučio: ništa') for i, k in enumerate('ABC'))
    s += pill(270, 205, 440, 'dogovor ✓ (svi isto)', 'good') + pill(770, 205, 440, 'valjanost ✗ (nije prijedlog)', 'bad')
    return 300, s, 'Protokol „uvijek odbij sve” ispunjava dogovor, ali je beskoristan'


@fig
def termination_wait():
    s = node(30, 20, 300, 120, 'A', 'čeka glas C…') + node(370, 20, 300, 120, 'B', 'čeka glas C…') + node(710, 20, 300, 120, 'C', 'stao je', 'down')
    s += pill(520, 205, 620, 'nitko nikad ne odluči', 'bad')
    return 300, s, 'Protokol „čekaj sve” nikad ne krši dogovor, ali može zauvijek čekati'


@fig
def properties():
    return 320, rows(['Dogovor|Nijedna dva ispravna člana ne odluče različito.',
                      'Valjanost|Odluka poštuje prijedloge, nije izmišljena.',
                      'Okončanje|Svaki ispravan član na kraju odluči.'], sub_x=620) + \
        ''.join(text(1000, 60 + i * 90, lab, 17, MUTED, 600).replace('middle', 'end') for i, lab in enumerate(['sigurnost', 'sigurnost', 'živost'])), ''


@fig
def timing_models():
    """Space-time diagram per model: sender lane on top, receiver below, time to the right."""
    def lane_lines(y):
        return (line(270, y, 1000, y, '#b5c7d2', False) + line(270, y + 50, 1000, y + 50, '#b5c7d2', False)
                + text(258, y + 6, 'B', 17, MUTED, 700).replace('middle', 'end') + text(258, y + 56, 'C', 17, MUTED, 700).replace('middle', 'end'))

    def window(x1, x2, y, label):
        # The deadline: C must receive within Δ of the send time.
        return (f'<rect x="{x1}" y="{y + 44}" width="{x2 - x1}" height="12" fill="#cfe4f0"/>'
                + f'<path d="M{x1},{y + 64} L{x1},{y + 70} L{x2},{y + 70} L{x2},{y + 64}" fill="none" stroke="{BLUE}" stroke-width="1.8"/>'
                + text((x1 + x2) / 2, y + 88, label, 15, BLUE, 600))

    def msg(x1, x2, y, colour=BLUE):
        return f'<circle cx="{x1}" cy="{y}" r="5" fill="{colour}"/>' + arrow(x1, y, x2, y + 46, color=colour)

    s, rows = '', [('Sinkrono', 'rok Δ je poznat', BLUE), ('Asinkrono', 'roka nema', RED), ('Djelomično', 'rok Δ tek nakon GST', AMBER)]
    for i, (title, sub, c) in enumerate(rows):
        y0 = 15 + i * 125
        s += f'<rect x="25" y="{y0}" width="990" height="112" rx="12" fill="#f3f8fb"/><rect x="25" y="{y0}" width="7" height="112" fill="{c}"/>'
        s += text(135, y0 + 44, title, 21, c, 600) + (text(135, y0 + 68, 'sinkrono', 21, c, 600) if i == 2 else '') + text(135, y0 + (94 if i == 2 else 70), sub, 15, MUTED)
        y = y0 + 22
        s += lane_lines(y)
        if i == 0:
            s += window(330, 530, y, 'rok Δ') + msg(330, 470, y)
        elif i == 1:
            s += msg(330, 960, y, RED) + text(645, y - 6, 'stiže kad stigne, bez gornje granice', 15, RED)
        else:
            s += f'<path d="M640,{y - 12} L640,{y + 62}" stroke="{AMBER}" stroke-width="2.4" stroke-dasharray="5 4"/>'
            s += text(640, y - 15, 'GST: od tada se mreža smirila', 15, AMBER, 700)
            s += msg(300, 610, y, RED) + text(455, y + 82, 'prije GST: kasni proizvoljno', 15, RED)
            s += window(680, 880, y, 'nakon GST: rok Δ') + msg(680, 820, y)
    return 430, s, 'Gornja traka šalje, donja prima; vrijeme teče slijeva nadesno'


@fig
def growing_timeouts():
    """Unknown Δ: each failed round doubles the timeout until it exceeds the real delay."""
    s, unit, x0 = '', 150, 230
    real = x0 + 3 * unit
    for i, (t, ok) in enumerate([(1, False), (2, False), (4, True)]):
        y = 30 + i * 70
        w = t * unit
        fill, stroke, ink = ('#e9f5ee', '#9fcdb1', GREEN) if ok else ('#fbeaec', '#e3a5ad', RED)
        s += text(130, y + 30, f'{i + 1}. krug', 20, INK, 600)
        s += f'<rect x="{x0}" y="{y + 8}" width="{w}" height="34" rx="17" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>'
        s += text(x0 + w / 2, y + 32, f'istek roka {t} s ' + ('✓' if ok else '✗'), 18, ink, 600)
    s += f'<path d="M{real},18 L{real},250" stroke="{AMBER}" stroke-width="2.4" stroke-dasharray="6 5"/>'
    s += text(real, 275, 'stvarno kašnjenje: 3 s (protokol ga ne zna)', 17, AMBER, 700)
    return 330, s, 'Neuspjeli krug udvostruči istek roka dok ne premaši stvarno kašnjenje'


@fig
def flp_dilemma():
    s = node(30, 95, 290, 130, 'B', 'nema glasa od C')
    s += line(330, 160, 420, 160, BLUE, False) + line(420, 75, 420, 250, BLUE, False)
    s += arrow(420, 75, 470, 75) + arrow(420, 250, 470, 250)
    s += pill(740, 75, 520, 'čeka dalje → možda zauvijek (C je stao)', 'bad', 19, 56)
    s += pill(740, 250, 520, 'odluči bez C → C je možda odlučio drukčije', 'bad', 19, 56)
    return 345, s, 'B ne može razlikovati spor i zaustavljen čvor (lekcija 01)'


@fig
def quorum_majority():
    # Show the outcome, not two formed quorums: honest B votes once, so only one quorum completes (lecturer, 2026-11-03).
    return 345, venn('A', 'B', 'C', 'tx1: A + B → kvorum skupljen', 'tx2: samo C → kvorum nepotpun', 'good',
                     'B je pošten: glasa samo za tx1', (GREEN, RED)), \
        'Dvije većine od tri dijele člana; pošten član omogućuje samo jednu odluku'


@fig
def crash_threshold():
    s = text(140, 40, 'n = 3, f = 1', 22, INK, 700) + text(140, 210, 'n = 5, f = 2', 22, INK, 700)
    for i, st in enumerate(['', '', 'down']):
        s += dot(320 + i * 110, 75, 'ABC'[i], st)
    s += bracket(286, 464, 135, 'kvorum 2 = n − f', GREEN, False)
    for i, st in enumerate(['', '', '', 'down', 'down']):
        s += dot(320 + i * 110, 245, 'ABCDE'[i], st)
    s += bracket(286, 574, 305, 'kvorum 3 = n − f', GREEN, False)
    return 400, s, 'Uz padove: n ≥ 2f + 1, kvorum je većina'


@fig
def byz_overlap():
    return 345, venn('B', 'A', 'C', 'kvorum za tx1: A + B', 'kvorum za tx2: A + C', 'bad', 'A je bizantski: glasa za oba'), \
        'Presjek postoji, ali je u njemu samo član koji laže'


@fig
def generals():
    s = node(370, 15, 300, 110, 'Zapovjednik', 'šalje zapovijed')
    s += node(60, 230, 300, 110, 'Poručnik 1', 'izvršava zapovijed') + node(680, 230, 300, 110, 'Poručnik 2', 'izvršava zapovijed')
    s += side_arrow(430, 130, 250, 222, '„napad”', BLUE, 'l') + side_arrow(610, 130, 790, 222, '„napad”', BLUE, 'r')
    s += f'<path d="M370,285 L670,285" stroke="{BLUE}" stroke-width="2.6" stroke-dasharray="7 6" fill="none"/>' + text(520, 272, 'prepričavaju što su čuli', 18, BLUE)
    return 410, s, 'Lamport, Shostak i Pease (1982): izdajica može biti i zapovjednik'


@fig
def generals_two_views():
    s = ''
    for k, (title, cmd_state, l2_state, to2, says) in enumerate([
            ('Slučaj a: izdajica je poručnik 2', '', 'bad', '„napad”', '„rekao je povlačenje”'),
            ('Slučaj b: izdajica je zapovjednik', 'bad', '', '„povlačenje”', '„rekao je povlačenje”')]):
        ox = k * 520
        s += text(ox + 260, 28, title, 20, RED, 600)
        s += node(ox + 150, 45, 220, 80, 'Zapovjednik', '', cmd_state)
        s += node(ox + 20, 225, 200, 80, 'Poručnik 1', '') + node(ox + 300, 225, 200, 80, 'Poručnik 2', '', l2_state)
        s += side_arrow(ox + 205, 132, ox + 130, 218, '„napad”', BLUE, 'l') + side_arrow(ox + 315, 132, ox + 390, 218, to2, RED if k else BLUE, 'r')
        s += arrow(ox + 300, 285, ox + 228, 285) + text(ox + 260, 340, says, 16, RED if not k else BLUE)
    s += f'<path d="M520,40 L520,330" stroke="#c6dbe8" stroke-width="2"/>'
    return 420, s, 'Poručnik 1 u oba slučaja vidi isto: „napad” i „rekao je povlačenje”'


@fig
def byz_threshold():
    s = ''
    for i, (k, st) in enumerate([('B', ''), ('A', 'bad'), ('C', ''), ('D', '')]):
        s += dot(300 + i * 150, 150, k, st)
    s += bracket(262, 638, 95, 'kvorum za tx1: B, A, C', BLUE)
    s += bracket(412, 788, 215, 'kvorum za tx2: A, C, D', AMBER, False)
    s += text(140, 140, 'n = 4', 22, INK, 700) + text(140, 168, 'f = 1', 22, INK, 700)
    s += pill(520, 300, 720, 'presjek: A i C (f + 1 = 2) → barem jedan pošten', 'good', 20, 52)
    return 380, s, 'Uz bizantske članove: n ≥ 3f + 1, kvorum 2f + 1'


@fig
def four_orgs():
    s, h = seq([('A', 'A · bizantski', 'bad'), ('B', 'B · predlaže tx1', ''), ('C', 'C · predlaže tx2', ''), ('D', 'D', '')],
               [('A', 'B', 'DA za tx1 · v7', 'bad'), ('A', 'C', 'DA za tx2 · v7', 'bad'), ('D', 'B', 'DA za tx1 · v7', ''),
                ('C', 'D', 'glasaj za tx2?', ''), ('note', 'D', 'već glasao za v7: NE'), ('note', 'B', 'A + B + D = 3 → tx1 konačan')],
               {'B': ('tx1 · v8', 'good'), 'C': ('tx2: samo 2 glasa', 'bad'), 'D': ('tx1 · v8', 'good')})
    return h + 30, s, 'Četiri organizacije: pošten D ne glasa dvaput, tx2 ne skupi kvorum'


@fig
def silent_member():
    s = dot(230, 110, 'A', 'down') + dot(410, 110, 'B') + dot(590, 110, 'C') + dot(770, 110, 'D')
    s += text(230, 175, 'šuti', 18, MUTED, 600)
    s += bracket(376, 804, 200, 'B + C + D = 3 = 2f + 1 → odluka', GREEN, False)
    return 300, s, 'n − f = 3 poštenih dovoljno je za kvorum i bez A'


@fig
def timing_algorithms():
    """Same observation, two algorithms: only the partially synchronous one keeps timeouts out of the decision (lecturer, 2026-10-28)."""
    s = ''
    cols = [(270, 'Sinkroni algoritam', BLUE, [('zna rok Δ', 'plain'), ('nakon Δ: „C je pao”', 'plain'), ('odluči bez C', 'plain')],
             'ispravno samo ako je Δ stvarna granica', RED),
            (770, 'Djelomično sinkroni algoritam', AMBER, [('ne zna rok Δ', 'plain'), ('istek roka: novi krug, dulji rok', 'note'), ('odluči tek s 2f + 1 glasova', 'good')],
             'istek roka nikad ne mijenja odluku', GREEN)]
    for cx, title, c, steps, note, nc in cols:
        s += text(cx, 30, title, 22, c, 700)
        for i, (lab, tone) in enumerate(steps):
            y = 80 + i * 78
            s += pill(cx, y, 420, lab, tone, 19, 52)
            if i < len(steps) - 1:
                s += arrow(cx, y + 28, cx, y + 48)
        s += text(cx, 315, note, 18, nc, 600)
    s += f'<path d="M520,20 L520,325" stroke="#c6dbe8" stroke-width="2"/>'
    return 380, s, 'Vrijeme smije ubrzati odluku, ali je ne smije učiniti pogrešnom'


@fig
def bft_phases():
    s = ''
    steps = [('Prijedlog', 'vođa predlaže tx1 · v7'), ('Priprema', '2f + 1 prihvaća prijedlog'), ('Potvrda', '2f + 1 zna da su drugi prihvatili'), ('Izvrši', 'tx1 · v8 konačan')]
    for i, (t, sub) in enumerate(steps):
        cx = 135 + i * 257
        s += pill(cx, 70, 220, t, 'plain', 22, 56) + text(cx, 130, sub, 16, MUTED)
        if i < 3:
            s += arrow(cx + 114, 70, cx + 142, 70)
    s += pill(520, 215, 760, 'vođa šuti ili laže → ostali biraju novog vođu', 'note', 19, 52)
    return 300, s, 'Shema BFT protokola, npr. PBFT (Castro i Liskov, 1999)'


@fig
def bft_cost():
    import math
    s = ''
    for k, (n, cx) in enumerate([(4, 260), (8, 780)]):
        pts = [(cx + 120 * math.cos(2 * math.pi * i / n - math.pi / 2), 150 + 110 * math.sin(2 * math.pi * i / n - math.pi / 2)) for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                s += f'<path d="M{pts[i][0]:.0f},{pts[i][1]:.0f} L{pts[j][0]:.0f},{pts[j][1]:.0f}" stroke="#b9cfdd" stroke-width="1.6"/>'
        for x, y in pts:
            s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="13" fill="#f8fbfd" stroke="{BLUE}" stroke-width="2"/>'
        s += text(cx, 305, f'n = {n}: {n * (n - 1)} poruka po koraku', 21, INK, 600)
    return 380, s, 'Svaki član šalje svakome: broj poruka raste s n²'


@fig
def known_membership():
    s = ''.join(node(25 + i * 255, 20, 225, 110, k, 'na popisu') for i, k in enumerate('ABCD'))
    s += pill(520, 200, 700, 'popis članova dogovoren je unaprijed', 'good', 20, 52)
    return 290, s, 'Sve dosad: n i f brojimo po poznatim organizacijama'


@fig
def open_identities():
    s = ''
    for i, (ident, who) in enumerate([('čvor 3f9a', '?'), ('čvor 71c2', '?'), ('čvor b04e', '?'), ('čvor e5d8', '?')]):
        s += node(25 + i * 255, 20, 225, 110, ident, 'tko je iza?')
    s += pill(520, 200, 760, 'pridružiti se može bilo tko, bez popisa', 'note', 20, 52)
    return 290, s, 'Otvorena mreža vidi identitete, ne osobe ni organizacije'


@fig
def sybil():
    s = ''
    for i, k in enumerate('ABCD'):
        s += dot(130 + i * 110, 120, k)
    for i in range(3):
        s += dot(640 + i * 110, 120, f'M{i + 1}', 'sybil')
    s += f'<rect x="595" y="55" width="310" height="130" rx="20" fill="none" stroke="{RED}" stroke-width="2.2" stroke-dasharray="7 5"/>' + text(750, 215, 'jedna strana, tri identiteta', 19, RED, 600)
    s += text(295, 215, 'četiri organizacije', 19, INK, 600)
    s += pill(520, 285, 820, '7 identiteta → „f = 2”, ali M drži 3 glasa od 7', 'bad', 20, 52)
    return 370, s, 'Douceur (2002): Sybil napad'


@fig
def limit_identities():
    s = pill(270, 60, 470, 'Središnji upis identiteta', 'plain', 21, 56) + text(270, 125, 'netko odobrava članove', 18, MUTED) + text(270, 152, '→ opet koordinator (lekcija 01)', 18, RED)
    s += pill(770, 60, 470, 'Cijena po identitetu', 'plain', 21, 56) + text(770, 125, 'svaki glas troši teško umnoživ resurs', 18, MUTED) + text(770, 152, '→ predavanje 04', 18, BLUE)
    return 230, s, 'Dva smjera; nijedan ne dolazi besplatno'


@fig
def counter():
    s = ''
    items = [('„podnosi lažljivca”', 'M doda 3 čvora: od 7 glasova drži 3 > f', 'Sybil napad'),
             ('„konačna kad 3 glasa”', 'od 7 čvorova dva skupa od 3 ne moraju se ni preklapati', 'kvorum 2f + 1'),
             ('„vođa je pao”', 'vođa samo kasni; ostali su tx1 već potvrdili', '„FLP”: spor ili stao?')]
    for i, (t, sub, ref) in enumerate(items):
        y, c = 15 + i * 112, ROW_COLOURS[i]
        s += f'<rect x="25" y="{y}" width="990" height="96" rx="12" fill="#f3f8fb"/><rect x="25" y="{y}" width="7" height="96" fill="{c}"/>'
        s += text(195, y + 56, t, 23, c, 600) + text(665, y + 44, sub, 20) + text(665, y + 75, ref, 16, MUTED)
    return 400, s, 'Popravak: poznato članstvo, kvorum po modelu, istek roka samo za živost'


@fig
def recap():
    return 340, rows(['Konsenzus|dogovor + valjanost (sigurnost) i okončanje (živost)',
                      'Prag|pad: n ≥ 2f + 1 · bizantski: n ≥ 3f + 1',
                      'Članstvo|f broji neovisne članove, ne identitete']), \
        'Svaki prag vrijedi samo uz izričit model vremena, kvarova i članstva'


@fig
def next_question():
    s = pill(270, 60, 470, 'Tko je poslao poruku?', 'plain', 21, 56) + text(270, 122, 'provjerljiv potpis → predavanje 03', 18, BLUE)
    s += pill(770, 60, 470, 'Je li zapis naknadno mijenjan?', 'plain', 21, 56) + text(770, 122, 'povezani zapisi → predavanje 03', 18, BLUE)
    return 210, s, 'Prvo alati za provjeru, zatim otvorena mreža bez popisa članova (predavanje 04)'


if __name__ == '__main__':
    for name, fn in FIG.items():
        height, body, caption = fn()
        export(name, height, body, caption)
    print('Exported', len(FIG), 'SVG/PDF pairs')
