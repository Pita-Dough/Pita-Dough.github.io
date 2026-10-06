# CLAUDE.md — peterdoe.com (Quarto)

Peter Doe's research website (Assistant Professor of Economics, Hope College). Quarto website (About, Research, and one page per course), deployed to GitHub Pages via GitHub Actions at `www.peterdoe.com`. Replaces the old Jekyll "Minimal Light" site in `../Pita-Dough.github.io-main/`, which is kept only as a reference snapshot.

## Structure

- `_quarto.yml`: site config. `render: ["**/*.qmd"]` keeps README.md/CLAUDE.md out of the build. `resources` lists `files/`, `econ212/files/`, `econ312/files/` and `CNAME`, because PDFs are linked only from YAML data files, which Quarto does not scan. Navbar is flat and never collapses: the "Peter Doe" brand (About, `index.qmd`), Research, ECON 212, ECON 312, so every page is one click away (rule: never nest pages in a menu, never use a hamburger). No sidebars. Light theme is listed first, so the site always opens in light mode; dark is available from the navbar toggle.
- Light palette (`styles/light.scss`) reproduces the old Minimal Light site: cream background `#fffaf2`, text `#000d12`, teal headings/links `#005169` (weight 500), paper buttons `#2086c9` outline on cream. Portrait is a rounded square (10% radius, 1px `#ddd` frame, 3px padding), `image-width: 11em`.
- `index.qmd`: the About page (the brand link). Quarto `about` page with `template: trestles` (portrait, name, subtitle, link buttons) plus a short bio.
- `research.qmd`: the Research page; a `#papers` div filled by the `papers.yml` listing.
- `papers.yml` + `_paper-list.ejs`: data-driven working-paper list. Fields: `title`, `coauthors` (renders "with X"), `pdf`, `arxiv`, `mathematica`, `code`, `notes` (red italic), `abstract` (Bootstrap collapse button). Order in the YAML is display order (`sort: false`).
- The EJS template is wrapped in a ```` ```{=html} ```` raw block. Without it, Pandoc treats indented template lines as code blocks.
- `styles/papers.css`: paper-list styling; colors come from CSS variables set in the two theme files.
- `.github/workflows/publish.yml`: renders on GitHub and deploys the `_site` artifact (no rendered output in git). No R/Python needed in CI; if R chunks are added later, set `execute: freeze: auto` and commit `_freeze/`.

## Course pages (`econ212/`, `econ312/`)

- `schedule.yml` in each course folder is the single source of truth. Fields: `week` (number or "Finals"), `iso` (YYYY-MM-DD; deliberately not `date`, which Quarto listings reformat), `day`, `topic`, `type` (class | exam | noclass), `notes`, `submit: true` (adds a "Submit on Moodle" chip), `materials` (list of `{label, href}` pointing into that course's `files/`). Initially generated from the `*_TentativeSchedule.tex` files on 2026-10-01; edit the YAML directly now.
- One page per course (`index.qmd`): Moodle banner, jump links, "Coming up" (next 3 meetings computed client-side from today's date), full schedule (past rows dimmed, next meeting highlighted, card layout under 640px; the Materials column holds the file links), and the course-info table. Two listings over the one YAML, using `_templates/upcoming.ejs` and `schedule.ejs`. Heading ids are explicit (`#coming-up`, `#full-schedule`, `#course-info`) because the listing div is `#schedule`.
- The Moodle URL is passed to templates via `template-params: moodle:` in both listings of the course page, and repeated in its Moodle banner. ECON 312's Moodle URL is still a placeholder (TODO).
- Listings set `page-size: 500` (default 30 would paginate the schedule). Raw HTML tables need `data-quarto-disable-processing="true"` or Quarto forces 50/50 column widths.
- Example materials so far: Ch. 5–7 notes + handouts (212), Ch. 2–5 notes + handouts (312). Never post answer keys (`*_KEY`, `*-ANSWERS`), student info sheets, or copyrighted readings (e.g., the Popper PDF).

## Side-panel diagrams (`_figures/`)

- Each course page is a three-column grid (`.course-shell` in `styles/course.css`): diagram | content | diagram. Under 1250px the two diagrams become a banner row above the content; under 560px they are hidden (the navbar and page title already name the course). `page-layout: custom` is set in each course's front matter so the grid can use the full window, and Quarto's own title block is hidden (`#title-block-header`) in favor of an `<h1>` inside `.course-main`.
- ECON 212: left = supply and demand with elasticity regions along D (S through the origin, so ε_S = 1); right = monopoly (D, MR, MC, ATC, profit rectangle, DWL triangle). ECON 312: left = the Ch. 8 Slutsky (pivot) decomposition in the lecture notes' own numbers and notation (x-bar, x^s, x^*; p1 4 to 1, m = 12) above the derivative-form equation dx*/dp1 = dx^s/dp1 - x-bar1 dx*/dm, with matching colored braces; right = Edgeworth box (indifference curves through the endowment, lens, contract curve, core). The panels carry symbols only, no sentences; keep it that way.
- The four `.html` files are generated. Edit parameters (prices, tastes, endowment, labels) in `_figures/build_figures.py`, run `python3 _figures/build_figures.py`, then preview. The script asserts the tangencies, MR = MC, and MRS_A = MRS_B along the contract curve.
- The pages pull the files in with `{{< include ../_figures/e212-left.html >}}`; `_`-prefixed folders are never rendered or published.
- Colors come from `--fig-1`, `--fig-2`, `--fig-red` in `light.scss`/`dark.scss`; line, label and wash classes (`.f-*`) are at the bottom of `course.css`.

## Constraints

- No Google Analytics or other tracking (deliberately removed, October 2026).
- No student information, ever.
- Commit only finished PDFs; replace `files/CV-Doe.pdf` in place.
- Course sections live in this repo for now (same URLs, `peterdoe.com/econ212/`, as a later split into separate project repos would use).
