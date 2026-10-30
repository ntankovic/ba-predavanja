# Blockchain Applications — teaching foundation

Course materials based on the lecturer's supplied 12-week syllabus. Read COURSE.md first.

**Status:** Croatian orientation 00 and lecture 01 are drafts; lectures 02–12 remain planned scaffolds. Croatian first; English files are structural placeholders. The course titles are confirmed: Blockchain aplikacije / Blockchain Applications. Administrative details require review.

## Included

- Exact 12-week topics and scopes, conceptual progression and teaching constraints.
- Twelve technical lecture folders. Lecture 01 has a full Croatian script, 42 slides, 34 illustrations and a 120-minute plan; lectures 02–12 retain planning outlines.
- Orientation 00: Croatian slides draft with timing and lecturer-confirmed grading; book registry and chapter order.
- FIPU branding, latest card/arrow style, Reveal layouts, Quarto/just build commands, PDF/HTML verification and headless-only browser tooling.
- No inherited course-specific assessment rules, attendance QR, student links or stale exports.

## Local setup

Install Quarto, just, Python 3 and XeLaTeX (e.g. MacTeX). For diagram exports install librsvg (`rsvg-convert`). Optional browser/PDF QA:

```sh
python3 -m venv .tools/qa-venv
.tools/qa-venv/bin/pip install -r requirements-qa.txt
just browser-install
```

Use an installed Quarto or set QUARTO_BIN. Tool binaries/virtual environments are not bundled. Headless browser downloads require network access; never switch to desktop control.

```sh
just slides 01-decentralized-systems hr
just lecture 01-decentralized-systems hr
just book hr
just all hr
just browser-check 01-decentralized-systems hr
```

`just test` retains the full English structural-export check; English placeholders must not be mistaken for approved translations. Builds prove structure only.

## Suggested next step

Review Lecture 01 in Croatian and complete its headless HTML layout check; translate after review. Do not introduce Bitcoin in weeks 1–2. Teach IPFS after Solidity/Web3. Weeks 7–12 evolve one dApp; proposed example is a collaborative creative-work/provenance registry, subject to lecturer choice.

## Provenance

Build scripts, formatting, templates and shared FIPU assets derive from the lecturer's Web Applications workspace. Academic identity retained as template metadata, staff confirmation pending. No other course's content completion or review status is inherited.
