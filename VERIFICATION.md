# Foundation verification — 2026-10-07

Passed: 13 planned lecture folders (00 + 12 weeks); 12 chapters in book order; HR/EN outline presence; metadata and Python syntax checks. Built with just: Croatian Lecture 01 PDF and HTML slides, orientation 00 HTML, and combined Croatian book PDF. Visually inspected first page of Lecture 01 PDF; planning label and typography render correctly.

These are structural scaffolds, not completed lectures or reviewed translations. Full English exports and browser layout QA were not run. Browser QA needs the headless shell installed; PyMuPDF must be installed from requirements-qa.txt for full PDF verification. Technical source verification is pending lecture authoring. No academic rules or links have been carried over from other courses.

Build verification used the parent workspace’s Quarto installation; no tool binaries or virtual environments are bundled. Install dependencies per README.md on the destination machine.

## Update — 2026-10-08

Cleaned inherited CSS across all 14 lecture/template stylesheets; confirmed Croatian title. Developed lecture 00 as a Croatian slides-only draft: 30 slides / 35.5 minutes, lecturer-supplied grading and shared AI/workflow content. Built HR slides 00 and 01 and HR book. Static checks passed for timing, slide count, notes, embedded assets, grading text and naming. Diagram PDF previews inspected. Headless browser launch is blocked by macOS sandbox MachPortRendezvous permission; no HTML layout approval or ready status claimed. See lectures/00-course-introduction/design-review.md and README.md for details and pending review.
