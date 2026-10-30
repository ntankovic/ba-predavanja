# Agent working rules

Read `COURSE.md` before creating or editing course material.

- Use headless Chrome for browser rendering and verification. Do not control the lecturer's desktop, browser windows or tabs through Computer Use. If headless execution fails, report the blocker instead of switching to desktop automation.

- The lecturer authorizes routine project `just` build and verification commands without further confirmation. Run them directly, subject to the execution environment's enforced permissions.

- Develop and tune teaching material in Croatian first, then translate the reviewed Croatian version into English. Read `references/terminology.md` before writing or translating; record lecturer-approved translations there and reuse them across lectures. Plan each full lecture for 90–120 minutes, including discussion and recap, and record timing in the brief and speaker notes.
- Follow the illustration workflow in `COURSE.md`: plan explanatory diagrams with the content, preserve source attribution, and verify them in both PDF and HTML output.

- Work lecture by lecture using `lectures/_template/`.
- Check the lecture registry before starting. Respect existing ownership and changes.
- Keep an assigned lecture's chapter, slides, sources, and assets together in its directory.
- Coordinate changes to shared files, the lecture registry, and book assembly order with the coordinating agent.
- Do not edit another agent's assigned lecture without coordination.
- Treat `chapter.hr.qmd` as the complete Croatian lecturer script and student-readable explanation; derive `slides.hr.qmd` from it, then translate reviewed sources into English. Keep both artifacts and languages consistent.
- Follow the 12-week sequence in `COURSE.md`; use 3–6 outcomes and approximately 30–40 substantive slides per developed lecture. Teach trust, consensus and application design through the evolving shared-state problem; follow the delayed Bitcoin and IPFS introductions in COURSE.md.
- Keep scaffolds `planned`; do not treat a structural build as content completion. Declare 90–120-minute duration in `lecture.json` and add per-slide `timing.json` when developing a full lecture.
- Verify technical claims and references. Explicitly flag unresolved questions rather than inventing facts or citations.
- Before handoff, complete the lecture review checklist and report changed files, checks performed, and unresolved issues.
- A draft is not a finished export. Mark a lecture `ready` only when its chapter and slides have passed review.
