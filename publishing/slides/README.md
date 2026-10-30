# Shared slides

Reveal.js configuration is in `revealjs.yml`. Build with `just slides 01-decentralized-systems hr`. Slides embed assets and use the FIPU logo, course footer, progress bar, definition boxes and table styling. Browser tab titles use BA-NN.

Use level-two headings for slides and fenced `.notes` blocks for concise teaching cues and timing. Keep editorial review notes in the lecture brief. No attendance slide is automatically inserted: add a course-specific link only after the lecturer supplies it.

Shell commands on slides use the terminal look: inline `` `npm start`{.cmd} `` and multi-line ```` ```{.terminal code-line-numbers="false"} ```` blocks (CSS in `revealjs.yml`; rule in `COURSE.md`).
