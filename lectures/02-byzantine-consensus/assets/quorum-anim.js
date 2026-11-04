/* Quorum animation for lecture 02 (lecturer requests, 2026-11-04).
 * Each guided scene is its own slide: <div class="qa" data-scene="0..5">; the
 * sandbox is <div class="qa" data-scene="sandbox">. A scene is a list of steps
 * (question, proposals, one step per voter, outcome). The script adds one
 * reveal.js fragment per step, so arrow keys and a clicker stop at every step;
 * the caption says what just happened and what comes next. Going back shows
 * the state after that step without animation.
 * There is no central ballot box: every member keeps its own tally.
 *   - B proposes tx1 (80 to X), C proposes tx2 (60 to Y); a crashed proposer proposes nothing;
 *   - an honest proposer votes for its own proposal, other honest members vote for the first one (tx1);
 *   - every vote is sent to every member; a lying member tells each recipient
 *     whatever that recipient votes for (equivocation); silent and crashed members send nothing;
 *   - messages to a crashed member are still sent but never arrive (drawn as stopping short with a red cross);
 *   - each member has a memory box beside it; received proposals fly into it and stay (lecturer, 2026-11-04);
 *   - an honest member decides a proposal once its own tally reaches q = n - f;
 *   - consensus holds when no two honest members decide differently.
 */
(function () {
  'use strict';
  var NAMES = 'ABCDEFG';
  var C = { ink: '#20384d', muted: '#5d7282', tx1: '#1585b4', tx2: '#b7791f', ok: '#f8fbfd', okStroke: '#8cb6cf',
            crash: '#eef1f3', crashStroke: '#a7b3bc', lie: '#fbeaec', lieStroke: '#b23a48', silent: '#f4f0f8',
            silentStroke: '#7d6a99', green: '#2f7a4f', red: '#b23a48', amber: '#a06512' };
  var COL = { tx1: C.tx1, tx2: C.tx2 };
  var TX = { tx1: 'tx₁', tx2: 'tx₂' };
  var AMOUNT = { tx1: 80, tx2: 60 }, TARGET = { tx1: 'X', tx2: 'Y' };
  var ROLE_LABEL = { ok: 'ispravan', crash: 'pao', lie: 'laže', silent: 'šuti' };
  var NEXT_ROLE = { ok: 'crash', crash: 'lie', lie: 'silent', silent: 'ok' };
  var T_PROPOSE = 1800, T_TRAVEL = 2000;

  var SCENES = [
    { n: 3, f: 1, roles: { C: 'crash' }, tx2: false, title: 'n = 3, f = 1, kvorum 2 · model padova',
      text: 'C je pao, a A i B svaki vide dva glasa za tx₁ i odlučuju: kvorum n − f dopušta odluku bez palog člana.' },
    { n: 3, f: 1, roles: {}, tx2: true, title: 'n = 3, f = 1, kvorum 2 · svi pošteni',
      text: 'Pošten B svima je poslao isti glas. Zato svaki član vidi dva glasa za tx₁ i jedan za tx₂, pa i C odlučuje tx₁: konsenzus.' },
    { n: 3, f: 1, roles: { A: 'lie' }, tx2: true, title: 'n = 3, f = 1, kvorum 2 · A laže',
      text: 'B lokalno vidi kvorum za tx₁, a C za tx₂: konsenzus je prekršen, 140 iz 100, kao u predavanju 01. Presjek dvaju kvoruma je samo lažljivac A.' },
    { n: 4, f: 1, roles: { A: 'lie' }, tx2: true, title: 'n = 3f + 1 = 4, kvorum 2f + 1 = 3 · A laže',
      text: 'B i D odlučuju tx₁, a C čeka: proturječne odluke nema. Dva kvoruma od tri među četiri člana dijele dva člana, a najviše jedan laže.' },
    { n: 4, f: 1, roles: { A: 'silent' }, tx2: false, title: 'n = 4, f = 1, kvorum 3 · A šuti',
      text: 'B, C i D sami čine kvorum od tri, pa se odluka donosi i bez A: prag čuva i okončanje.' },
    { n: 4, f: 1, roles: { A: 'lie', D: 'crash' }, tx2: true, title: 'n = 4, f = 1, kvorum 3 · A laže, D je pao',
      text: 'Neispravna su dva člana, više od f. Nitko ne vidi tri glasa: sustav staje, ali ne donosi proturječne odluke.' }
  ];
  var SANDBOX = { n: 4, f: 1, roles: {}, tx2: true, title: 'Slobodno istraživanje',
    text: 'Kliknite člana da mu promijenite stanje (ispravan → pao → laže → šuti). Mijenjajte n i f i pronađite postavku u kojoj se gubi sigurnost ili živost.' };

  var SVGNS = 'http://www.w3.org/2000/svg';
  function el(tag, attrs, text) {
    var e = document.createElementNS(SVGNS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text !== undefined) e.textContent = text;
    return e;
  }
  function h(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    return e;
  }
  function list(xs) { return xs.length < 2 ? xs.join('') : xs.slice(0, -1).join(', ') + ' i ' + xs[xs.length - 1]; }
  function dat(x) { return x + '-u'; }

  var CSS = '' +
    '.qa{display:flex;gap:18px;align-items:stretch;font-family:"Source Sans 3","Source Sans Pro",Arial,sans-serif;color:' + C.ink + ';text-align:left;margin-top:-6px}' +
    '.qa svg{flex:0 0 540px;width:540px;height:500px}' +
    '.qa-panel{flex:1;display:flex;flex-direction:column;gap:9px;font-size:20px;line-height:1.3}' +
    '.qa-step-no{font-size:15px;color:' + C.muted + ';letter-spacing:.04em;text-transform:uppercase}' +
    '.qa-title{font-size:21px;font-weight:700;color:#18344b;line-height:1.2}' +
    '.qa-text{font-size:19px;min-height:76px}' +
    '.qa-next{font-size:17px;color:' + C.muted + ';font-style:italic;min-height:22px}' +
    '.qa-facts{display:grid;grid-template-columns:auto 1fr;gap:3px 12px;font-size:16px;border-top:1px solid #d5e1e8;padding-top:8px}' +
    '.qa-facts b{font-weight:600;color:' + C.muted + '}' +
    '.qa-ok{color:' + C.green + ';font-weight:700}.qa-bad{color:' + C.red + ';font-weight:700}' +
    '.qa-verdict{font-size:18px;font-weight:700;padding:7px 12px;border-radius:10px;min-height:24px}' +
    '.qa-v-one{background:#e8f4ec;color:' + C.green + '}.qa-v-two{background:#fbeaec;color:' + C.red + '}.qa-v-none{background:#fbf1e2;color:' + C.amber + '}' +
    '.qa-controls{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;font-size:16px}' +
    '.qa-controls label{display:flex;gap:6px;align-items:center}' +
    '.qa-controls input[type=range]{width:90px}' +
    '.qa-nav{display:flex;gap:8px;align-items:center;margin-top:auto}' +
    '.qa-nav button{font:inherit;font-size:15px;padding:3px 10px;border:1px solid #b8cad6;border-radius:8px;background:#fff;color:' + C.ink + ';cursor:pointer}' +
    '.qa-dots{display:flex;gap:6px;margin-left:6px;flex-wrap:wrap}.qa-dots span{width:10px;height:10px;border-radius:50%;background:#d5e1e8}' +
    '.qa-dots span.past{background:#9cc4da}.qa-dots span.on{background:' + C.tx1 + '}' +
    '.qa .qa-node{cursor:default}.qa.qa-sandbox .qa-node{cursor:pointer}';

  /* ---------- Engine ---------- */

  // Proposals, honest choices, vote steps (one per voter) and each member's decision.
  function compute(cfg) {
    var n = cfg.n, q = n - cfg.f, roles = cfg.roles;
    var props = [];
    if (roles[1] !== 'crash') props.push({ id: 'tx1', from: 1 });
    if (cfg.tx2 && roles[2] !== 'crash') props.push({ id: 'tx2', from: 2 });
    var choice = [];
    for (var i = 0; i < n; i++) {
      var own = props.filter(function (p) { return p.from === i; })[0];
      choice.push(props.length ? (own || props[0]).id : null);
    }
    var votes = [];   // one entry per voter, in order
    for (i = 0; i < n; i++) {
      var r = roles[i];
      if (r === 'crash' || r === 'silent' || !props.length) continue;
      var msgs = [];
      for (var j = 0; j < n; j++) {
        msgs.push({ from: i, to: j, tx: r === 'lie' ? (choice[j] || props[0].id) : choice[i], lie: r === 'lie', lost: roles[j] === 'crash' });
      }
      votes.push({ voter: i, msgs: msgs });
    }
    // Tally after each vote step, and the step at which each honest member decides.
    var tally = [], decided = [], decidedAt = [], after = [];
    for (i = 0; i < n; i++) { tally.push({ tx1: 0, tx2: 0 }); decided.push(null); decidedAt.push(-1); }
    votes.forEach(function (v, k) {
      v.msgs.forEach(function (m) {
        if (m.lost) return;
        tally[m.to][m.tx]++;
        if (roles[m.to] === 'ok' && !decided[m.to] && tally[m.to][m.tx] >= q) { decided[m.to] = m.tx; decidedAt[m.to] = k; }
      });
      after.push(tally.map(function (t) { return { tx1: t.tx1, tx2: t.tx2 }; }));
    });
    return { q: q, props: props, votes: votes, after: after, decided: decided, decidedAt: decidedAt, overlap: 2 * q - n,
             lying: roles.filter(function (r) { return r === 'lie'; }).length,
             honest: roles.filter(function (r) { return r === 'ok'; }).length };
  }

  // Steps: 0 question, 1 proposals, then one per voter, last outcome.
  function steps(cfg, R) {
    var out = [{ kind: 'idle' }];
    if (R.props.length) out.push({ kind: 'propose' });
    R.votes.forEach(function (v, k) { out.push({ kind: 'vote', k: k }); });
    out.push({ kind: 'result' });
    return out;
  }

  function caption(cfg, R, st, scene) {
    var names = function (pred) { var o = []; cfg.roles.forEach(function (r, i) { if (pred(r, i)) o.push(NAMES[i]); }); return o; };
    if (st.kind === 'idle') {
      return { text: 'Što će odlučiti svaki član? Kvorum je ' + R.q + ' glasa.', next: 'Sljedeće: predlagatelji šalju prijedloge.' };
    }
    if (st.kind === 'propose') {
      var ps = R.props.map(function (p) { return NAMES[p.from] + ' predlaže ' + TX[p.id] + ' (' + AMOUNT[p.id] + ' na ' + TARGET[p.id] + ')'; });
      var t = ps.join(', a ') + (ps.length > 1 ? '; oba prijedloga idu svim članovima.' : ' i šalje prijedlog svim članovima.');
      var crashed = names(function (r) { return r === 'crash'; }), silent = names(function (r) { return r === 'silent'; });
      if (crashed.length) t += ' ' + list(crashed) + (crashed.length > 1 ? ' su pali: poruke prema njima' : ' je pao: poruke prema njemu') + ' ne stižu.';
      if (silent.length) t += ' ' + list(silent) + ' šuti: prima poruke, ali neće glasati.';
      var first = R.votes[0];
      return { text: t, next: first ? 'Sljedeće: ' + NAMES[first.voter] + ' šalje glas.' : 'Sljedeće: ishod.' };
    }
    if (st.kind === 'vote') {
      var v = R.votes[st.k], who = NAMES[v.voter], t2;
      if (cfg.roles[v.voter] === 'lie') {
        var g = { tx1: [], tx2: [] };
        v.msgs.forEach(function (m) { if (m.to !== v.voter && !m.lost) g[m.tx].push(dat(NAMES[m.to])); });
        var parts = ['tx1', 'tx2'].filter(function (x) { return g[x].length; })
          .map(function (x) { return 'glas za ' + TX[x] + ' šalje ' + list(g[x]); });
        t2 = who + ' laže: ' + parts.join(', a ') + '.';
      } else {
        t2 = who + ' svim članovima šalje glas za ' + TX[v.msgs[0].tx] + '.';
      }
      var now = { tx1: [], tx2: [] };
      R.decidedAt.forEach(function (k, i) { if (k === st.k) now[R.decided[i]].push(NAMES[i]); });
      ['tx1', 'tx2'].forEach(function (x) {
        var d = now[x]; if (!d.length) return;
        t2 += ' ' + list(d) + (d.length > 1 ? ' sada imaju po ' : ' sada ima ') + R.q + ' glasa za ' + TX[x] + ' i ' +
              (d.length > 1 ? 'odlučuju ' : 'odlučuje ') + TX[x] + '.';
      });
      var nv = R.votes[st.k + 1];
      return { text: t2, next: nv ? 'Sljedeće: ' + NAMES[nv.voter] + ' šalje glas.' : 'Sljedeće: ishod.' };
    }
    return { text: scene.text, next: '' };
  }

  /* ---------- View ---------- */

  function Anim(root, scene, sandbox) {
    this.root = root; this.base = scene; this.sandbox = sandbox; this.raf = null; this.step = 0;
    this.reset();
    this.build();
    if (sandbox) this.runAll(true); else this.show(0, false);
  }

  Anim.prototype.reset = function () {
    var s = this.base, roles = [];
    for (var k = 0; k < s.n; k++) roles.push(s.roles[NAMES[k]] || 'ok');
    this.cfg = { n: s.n, f: s.f, roles: roles, tx2: s.tx2 };
    this.R = compute(this.cfg); this.steps = steps(this.cfg, this.R);
  };

  Anim.prototype.build = function () {
    var self = this;
    if (!document.getElementById('qa-style')) {
      var st = document.createElement('style'); st.id = 'qa-style'; st.textContent = CSS; document.head.appendChild(st);
    }
    this.root.classList.toggle('qa-sandbox', this.sandbox);
    this.svg = el('svg', { viewBox: '0 0 540 500', role: 'img', 'aria-label': 'Animacija kvoruma' });
    this.root.appendChild(this.svg);
    var p = h('div', 'qa-panel');
    this.stepNo = h('div', 'qa-step-no'); this.title = h('div', 'qa-title', this.base.title);
    this.text = h('div', 'qa-text'); this.next = h('div', 'qa-next');
    this.facts = h('div', 'qa-facts'); this.verdict = h('div', 'qa-verdict');
    this.controls = h('div', 'qa-controls');
    [this.stepNo, this.title, this.text, this.next, this.facts, this.verdict, this.controls].forEach(function (x) { p.appendChild(x); });
    var nav = h('div', 'qa-nav');
    if (this.sandbox) {
      var replay = h('button', '', '↻ ponovi');
      replay.onclick = function (e) { e.stopPropagation(); self.runAll(); };
      nav.appendChild(replay);
      this.renderControls();
    } else {
      var prev = h('button', '', '◀'), next = h('button', '', '▶'), again = h('button', '', '↻ korak');
      prev.title = 'Prethodni korak'; next.title = 'Sljedeći korak'; again.title = 'Ponovi korak';
      prev.onclick = function (e) { e.stopPropagation(); self.go(self.step - 1); };
      next.onclick = function (e) { e.stopPropagation(); self.go(self.step + 1); };
      again.onclick = function (e) { e.stopPropagation(); self.show(self.step, true); };
      this.dots = h('div', 'qa-dots');
      this.steps.forEach(function () { self.dots.appendChild(h('span')); });
      nav.appendChild(prev); nav.appendChild(next); nav.appendChild(again); nav.appendChild(this.dots);
    }
    p.appendChild(nav);
    this.root.appendChild(p);
  };

  Anim.prototype.go = function (i) {
    i = Math.max(0, Math.min(this.steps.length - 1, i));
    if (this.onNavigate) this.onNavigate(i); else this.show(i, i > this.step);
  };

  Anim.prototype.renderControls = function () {
    var self = this, c = this.cfg;
    this.controls.innerHTML = '';
    function stop(x) { ['keydown', 'click', 'mousedown', 'pointerdown', 'touchstart'].forEach(function (ev) { x.addEventListener(ev, function (e) { e.stopPropagation(); }); }); }
    function slider(label, min, max, val, on) {
      var l = h('label'); var span = h('span', '', label + ' = ' + val);
      var r = document.createElement('input'); r.type = 'range'; r.min = min; r.max = max; r.value = val;
      r.oninput = function () { span.textContent = label + ' = ' + r.value; on(+r.value); };
      stop(r); l.appendChild(span); l.appendChild(r); return l;
    }
    this.controls.appendChild(slider('n', 3, 7, c.n, function (v) {
      c.n = v; while (c.roles.length < v) c.roles.push('ok'); c.roles.length = v;
      if (c.f > v - 1) c.f = v - 1;
      self.runAll();
    }));
    this.controls.appendChild(slider('f', 0, 2, c.f, function (v) { c.f = Math.min(v, c.n - 1); self.runAll(); }));
    var l = h('label'); var cb = document.createElement('input'); cb.type = 'checkbox'; cb.checked = c.tx2; stop(cb);
    cb.onchange = function () { c.tx2 = cb.checked; self.runAll(); };
    l.appendChild(cb); l.appendChild(h('span', '', 'drugi prijedlog tx₂'));
    this.controls.appendChild(l);
  };

  Anim.prototype.layout = function (n) {
    var pts = [], cx = 270, cy = 232, r = n <= 4 ? 150 : 165;
    for (var i = 0; i < n; i++) {
      var a = -Math.PI / 2 + (2 * Math.PI * i) / n;
      pts.push({ x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) });
    }
    return pts;
  };

  // Draw members with the tallies after vote step `applied` (-1: no votes yet);
  // memFull: every live member already holds every proposal in memory.
  Anim.prototype.draw = function (applied, memFull) {
    var self = this, c = this.cfg, R = this.R, svg = this.svg;
    if (this.raf) { cancelAnimationFrame(this.raf); this.raf = null; }
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    this.pts = this.layout(c.n);
    var tally = applied >= 0 ? R.after[applied] : null;
    this.nodes = this.pts.map(function (pt, i) {
      var role = c.roles[i];
      var g = el('g', { class: 'qa-node', transform: 'translate(' + pt.x + ',' + pt.y + ')' });
      var ring = el('circle', { r: 32, fill: { ok: C.ok, crash: C.crash, lie: C.lie, silent: C.silent }[role],
                                stroke: { ok: C.okStroke, crash: C.crashStroke, lie: C.lieStroke, silent: C.silentStroke }[role],
                                'stroke-width': role === 'ok' ? 2 : 2.5, 'stroke-dasharray': role === 'crash' ? '6 4' : '' });
      g.appendChild(ring);
      g.appendChild(el('text', { y: 8, 'text-anchor': 'middle', 'font-size': 25, 'font-weight': 700,
                                 fill: role === 'crash' ? C.muted : role === 'lie' ? C.red : role === 'silent' ? C.silentStroke : C.ink }, NAMES[i]));
      var tag = role === 'ok' ? (i === 1 ? 'predlaže tx₁' : i === 2 && c.tx2 ? 'predlaže tx₂' : '') : ROLE_LABEL[role];
      if (tag) g.appendChild(el('text', { y: 49, 'text-anchor': 'middle', 'font-size': 13, fill: C.muted }, tag));
      var tl = null;
      if (role !== 'crash' && R.props.length) { tl = el('text', { y: 67, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 600 }); g.appendChild(tl); }
      var dec = el('text', { y: -42, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 700 });
      g.appendChild(dec);
      if (self.sandbox) g.addEventListener('click', function (e) {
        e.stopPropagation(); c.roles[i] = NEXT_ROLE[c.roles[i]]; self.runAll();
      });
      svg.appendChild(g);
      return { ring: ring, tl: tl, dec: dec, tally: tally ? { tx1: tally[i].tx1, tx2: tally[i].tx2 } : { tx1: 0, tx2: 0 } };
    });
    this.nodes.forEach(function (nd, i) {
      self.drawTally(i);
      if (R.decided[i] && R.decidedAt[i] <= applied) self.decide(i, R.decided[i]);
      // Memory box beside the member, one slot per proposal.
      nd.slots = {};
      if (c.roles[i] === 'crash' || !R.props.length) return;
      var pt = self.pts[i], left = pt.x < 250, w = 46, hgt = 10 + R.props.length * 26;
      var bx = left ? pt.x - 32 - 10 - w : pt.x + 32 + 10, by = pt.y - hgt / 2;
      var mem = el('g', {});
      mem.appendChild(el('rect', { x: bx, y: by, width: w, height: hgt, rx: 7, fill: '#fbfcfd', stroke: '#c9d6df', 'stroke-dasharray': '4 3' }));
      mem.appendChild(el('text', { x: bx + w / 2, y: by - 4, 'text-anchor': 'middle', 'font-size': 10, fill: C.muted }, 'memorija'));
      svg.insertBefore(mem, svg.firstChild);
      R.props.forEach(function (p, k) { nd.slots[p.id] = { x: bx + w / 2, y: by + 5 + 13 + k * 26 }; });
      nd.mem = mem;
      if (memFull) R.props.forEach(function (p) { self.putMem(i, p.id); });
    });
    this.layer = el('g', {}); svg.appendChild(this.layer);
    this.phase = el('text', { x: 270, y: 26, 'text-anchor': 'middle', 'font-size': 16, 'font-weight': 700, fill: C.muted }, '');
    svg.appendChild(this.phase);
    var lg = el('g', { transform: 'translate(0,488)', 'font-size': 13, fill: C.muted });
    lg.appendChild(el('rect', { x: 40, y: -11, width: 34, height: 16, rx: 8, fill: '#fff', stroke: C.muted, 'stroke-width': 1.5 }));
    lg.appendChild(el('text', { x: 82, y: 1 }, 'prijedlog'));
    lg.appendChild(el('circle', { cx: 168, cy: -3, r: 6, fill: C.muted }));
    lg.appendChild(el('text', { x: 180, y: 1 }, 'glas'));
    lg.appendChild(el('circle', { cx: 238, cy: -3, r: 6, fill: C.muted, stroke: C.red, 'stroke-width': 2.5 }));
    lg.appendChild(el('text', { x: 250, y: 1 }, 'glas lažljivca'));
    lg.appendChild(el('text', { x: 360, y: 1 }, 'boja: tx₁ plavo, tx₂ narančasto'));
    svg.appendChild(lg);
  };

  Anim.prototype.drawTally = function (k) {
    var nd = this.nodes[k]; if (!nd.tl) return;
    while (nd.tl.firstChild) nd.tl.removeChild(nd.tl.firstChild);
    this.R.props.forEach(function (p, idx) {
      if (idx) nd.tl.appendChild(el('tspan', { fill: C.muted }, ' · '));
      nd.tl.appendChild(el('tspan', { fill: COL[p.id] }, TX[p.id] + ': ' + nd.tally[p.id]));
    });
  };
  Anim.prototype.putMem = function (k, tx) {
    var nd = this.nodes[k], sl = nd.slots && nd.slots[tx];
    if (!sl || nd['has_' + tx]) return;
    nd['has_' + tx] = true;
    var g = el('g', { transform: 'translate(' + sl.x + ',' + sl.y + ')' });
    g.appendChild(el('rect', { x: -19, y: -10, width: 38, height: 20, rx: 10, fill: '#fff', stroke: COL[tx], 'stroke-width': 2 }));
    g.appendChild(el('text', { y: 5, 'text-anchor': 'middle', 'font-size': 13, 'font-weight': 700, fill: COL[tx] }, TX[tx]));
    nd.mem.appendChild(g);
  };
  Anim.prototype.decide = function (k, tx) {
    var nd = this.nodes[k];
    nd.ring.setAttribute('stroke', COL[tx]); nd.ring.setAttribute('stroke-width', 5);
    nd.dec.setAttribute('fill', COL[tx]); nd.dec.textContent = 'odlučuje ' + TX[tx];
  };

  // Animate one step's messages; call done() when they have arrived.
  Anim.prototype.animate = function (st, done) {
    var self = this, R = this.R, c = this.cfg, pts = this.pts, dots = [];
    if (st.kind === 'propose') {
      this.phase.textContent = 'prijedlozi';
      R.props.forEach(function (p) {
        self.putMem(p.from, p.id);
        pts.forEach(function (pt, i) {
          if (i === p.from) return;
          var lost = c.roles[i] === 'crash', slot = self.nodes[i].slots[p.id];
          dots.push({ x0: pts[p.from].x, y0: pts[p.from].y, x1: lost ? pt.x : slot.x, y1: lost ? pt.y : slot.y,
                      dur: T_PROPOSE, prop: p.id, lost: lost, to: i });
        });
      });
    } else if (st.kind === 'vote') {
      this.phase.textContent = 'glas: ' + NAMES[R.votes[st.k].voter];
      R.votes[st.k].msgs.forEach(function (m) {
        if (m.from === m.to) { self.arrive(m, st.k); return; }
        dots.push({ x0: pts[m.from].x, y0: pts[m.from].y, x1: pts[m.to].x, y1: pts[m.to].y, dur: T_TRAVEL, msg: m, lost: m.lost });
      });
    }
    dots.forEach(function (d) {
      if (d.lost) {   // stop short of the crashed member: the message never arrives
        var dx = d.x1 - d.x0, dy = d.y1 - d.y0, len = Math.sqrt(dx * dx + dy * dy), cut = Math.max(0, (len - 62) / len);
        d.x1 = d.x0 + dx * cut; d.y1 = d.y0 + dy * cut;
      }
      if (d.prop) {
        d.node = el('g', {});
        d.node.appendChild(el('rect', { x: -24, y: -13, width: 48, height: 26, rx: 13, fill: '#fff', stroke: COL[d.prop], 'stroke-width': 2.5 }));
        d.node.appendChild(el('text', { y: 6, 'text-anchor': 'middle', 'font-size': 15, 'font-weight': 700, fill: COL[d.prop] }, TX[d.prop]));
      } else {
        d.node = el('circle', { r: 8, fill: COL[d.msg.tx], stroke: d.msg.lie ? C.red : '#fff', 'stroke-width': d.msg.lie ? 3 : 1.5 });
      }
      self.layer.appendChild(d.node);
    });
    var dur = dots.reduce(function (m, d) { return Math.max(m, d.dur); }, 0), start = null;
    if (this.raf) cancelAnimationFrame(this.raf);
    function frame(ts) {
      if (start === null) start = ts;
      var t = ts - start;
      dots.forEach(function (d) {
        if (d.done) return;
        var u = Math.min(1, t / d.dur), e = u < .5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2;
        var x = d.x0 + (d.x1 - d.x0) * e, y = d.y0 + (d.y1 - d.y0) * e;
        if (d.prop) d.node.setAttribute('transform', 'translate(' + x + ',' + y + ')');
        else { d.node.setAttribute('cx', x); d.node.setAttribute('cy', y); }
        if (u >= 1) {
          d.done = true; d.node.remove();
          if (d.lost) {
            var xg = el('g', { transform: 'translate(' + d.x1 + ',' + d.y1 + ')', stroke: C.red, 'stroke-width': 3, 'stroke-linecap': 'round' });
            xg.appendChild(el('line', { x1: -6, y1: -6, x2: 6, y2: 6 })); xg.appendChild(el('line', { x1: -6, y1: 6, x2: 6, y2: -6 }));
            self.layer.appendChild(xg);
          } else if (d.msg) self.arrive(d.msg, st.k);
          else if (d.prop) self.putMem(d.to, d.prop);
        }
      });
      if (t < dur) self.raf = requestAnimationFrame(frame);
      else { self.raf = null; self.phase.textContent = ''; if (done) done(); }
    }
    this.raf = requestAnimationFrame(frame);
  };

  Anim.prototype.arrive = function (m, k) {
    var nd = this.nodes[m.to], R = this.R;
    nd.tally[m.tx]++; this.drawTally(m.to);
    if (R.decided[m.to] && R.decidedAt[m.to] === k && nd.tally[R.decided[m.to]] >= R.q) this.decide(m.to, R.decided[m.to]);
  };

  // Show step i of a guided scene: the state after step i; animate it when moving forward.
  Anim.prototype.show = function (i, animate) {
    var self = this, st = this.steps[i];
    this.step = i;
    var voteIdx = st.kind === 'vote' ? st.k : st.kind === 'result' ? this.R.votes.length - 1 : -1;
    var memFull = st.kind !== 'idle' && !(animate && st.kind === 'propose');
    this.draw(animate && st.kind === 'vote' ? voteIdx - 1 : voteIdx, memFull);
    var cap = caption(this.cfg, this.R, st, this.base);
    this.stepNo.textContent = 'Korak ' + (i + 1) + ' / ' + this.steps.length;
    Array.prototype.forEach.call(this.dots.children, function (d, k) { d.className = k === i ? 'on' : k < i ? 'past' : ''; });
    this.showFacts(st.kind === 'result');
    function finish() { self.text.textContent = cap.text; self.next.textContent = cap.next; }
    if (animate && (st.kind === 'propose' || st.kind === 'vote')) {
      this.text.textContent = st.kind === 'propose' ? 'Prijedlozi putuju…' : NAMES[this.R.votes[st.k].voter] + ' šalje glas…';
      this.next.textContent = '';
      this.animate(st, finish);
    } else finish();
  };

  // Sandbox: run every step in sequence (or just draw the start when `still`).
  Anim.prototype.runAll = function (still) {
    var self = this;
    this.R = compute(this.cfg); this.steps = steps(this.cfg, this.R);
    this.draw(-1);
    this.stepNo.textContent = 'Slobodni način';
    this.text.textContent = this.base.text; this.next.textContent = '';
    this.showFacts(false);
    if (still) return;
    var seq = this.steps.filter(function (s) { return s.kind === 'propose' || s.kind === 'vote'; }), k = 0;
    (function nextStep() {
      if (k >= seq.length) { self.showFacts(true); return; }
      self.animate(seq[k++], nextStep);
    })();
  };

  Anim.prototype.showFacts = function (done) {
    var c = this.cfg, R = this.R, self = this;
    this.facts.innerHTML = '';
    function row(k, v, cls) { self.facts.appendChild(h('b', '', k)); self.facts.appendChild(h('span', cls || '', v)); }
    row('Članova', 'n = ' + c.n + ', pretpostavka f = ' + c.f);
    row('Kvorum', 'n − f = ' + R.q + ' glasa');
    row('Presjek', 'dva kvoruma dijele ≥ ' + Math.max(0, R.overlap) + ' čl.; lažljivaca: ' + R.lying);
    this.verdict.className = 'qa-verdict'; this.verdict.textContent = '';
    if (!done) return;
    var safe = R.overlap > R.lying;
    row('Sigurnost', safe ? 'zajamčena (presjek > lažljivci)' : 'nije zajamčena', safe ? 'qa-ok' : 'qa-bad');
    var live = R.honest >= R.q;
    row('Živost', live ? 'ispravni sami čine kvorum' : 'ispravnih je premalo (' + R.honest + ' < ' + R.q + ')', live ? 'qa-ok' : 'qa-bad');
    var by = { tx1: [], tx2: [] }, waiting = [];
    c.roles.forEach(function (r, i) { if (r === 'ok') { if (R.decided[i]) by[R.decided[i]].push(NAMES[i]); else waiting.push(NAMES[i]); } });
    var vals = ['tx1', 'tx2'].filter(function (x) { return by[x].length; }), v = this.verdict;
    if (vals.length === 2) {
      v.className = 'qa-verdict qa-v-two';
      v.textContent = 'Konsenzus prekršen: ' + list(by.tx1) + ' → tx₁, ' + list(by.tx2) + ' → tx₂: 140 iz 100';
    } else if (vals.length === 1) {
      var x = vals[0];
      v.className = 'qa-verdict qa-v-one';
      v.textContent = waiting.length ? 'Bez proturječja: ' + list(by[x]) + ' → ' + TX[x] + '; ' + list(waiting) + ' još čeka'
                                     : 'Konsenzus: svi ispravni odlučuju ' + TX[x] + ' (F = ' + (100 - AMOUNT[x]) + ')';
    } else {
      v.className = 'qa-verdict qa-v-none';
      v.textContent = R.honest ? 'Zastoj: nijedan ispravan član ne odlučuje (F = 100)' : 'Nema ispravnih članova';
    }
  };

  /* ---------- Wiring to reveal.js ---------- */

  function init() {
    Array.prototype.forEach.call(document.querySelectorAll('.qa'), function (root) {
      if (root.__qa) return;
      var key = root.getAttribute('data-scene'), sandbox = key === 'sandbox';
      var a = root.__qa = new Anim(root, sandbox ? SANDBOX : SCENES[+key || 0], sandbox);
      var section = root.closest('section');
      if (!window.Reveal || !section) return;
      if (sandbox) {
        Reveal.on('slidechanged', function (e) { if (e.currentSlide === section) a.runAll(); });
        return;
      }
      // One fragment per step after the question.
      for (var k = 1; k < a.steps.length; k++) {
        var sp = document.createElement('span'); sp.className = 'fragment qa-step'; section.appendChild(sp);
      }
      function visible() { return section.querySelectorAll('.qa-step.visible').length; }
      a.onNavigate = function (i) { Reveal.navigateFragment(i - 1); };
      Reveal.on('fragmentshown', function (e) { if (section.contains(e.fragment)) a.show(visible(), true); });
      Reveal.on('fragmenthidden', function (e) { if (section.contains(e.fragment)) a.show(visible(), false); });
      Reveal.on('slidechanged', function (e) { if (e.currentSlide === section) a.show(visible(), false); });
    });
    if (window.Reveal && Reveal.sync) Reveal.sync();
  }
  function boot() {
    if (window.Reveal && Reveal.isReady && !Reveal.isReady()) { Reveal.on('ready', init); return; }
    init();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { setTimeout(boot, 0); });
  else setTimeout(boot, 0);
})();
