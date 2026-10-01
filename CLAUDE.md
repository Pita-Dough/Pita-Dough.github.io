# CLAUDE.md — peterdoe.com (Quarto)

Peter Doe's research website (Assistant Professor of Economics, Hope College). Quarto website (research page + ECON 212/312 course sections), deployed to GitHub Pages via GitHub Actions at `www.peterdoe.com`. Replaces the old Jekyll "Minimal Light" site in `../Pita-Dough.github.io-main/`, which is kept only as a reference snapshot.

## Structure

- `_quarto.yml`: site config. `render: ["**/*.qmd"]` keeps README.md/CLAUDE.md out of the build. `resources` lists `files/`, `econ212/files/`, `econ312/files/` and `CNAME`, because PDFs are linked only from YAML data files, which Quarto does not scan. Navbar: Research + Teaching menu. One docked sidebar per course (Home, Schedule, Materials, Syllabus PDF, Moodle link). Light theme is listed first, so the site always opens in light mode; dark is available from the navbar toggle.
- Light palette (`styles/light.scss`) reproduces the old Minimal Light site: cream background `#fffaf2`, text `#000d12`, teal headings/links `#005169` (weight 500), paper buttons `#2086c9` outline on cream. Portrait is a rounded square (10% radius, 1px `#ddd` frame, 3px padding), `image-width: 11em`.
- `index.qmd`: the research page. Quarto `about` page with `template: trestles` (sidebar portrait, name, subtitle, link buttons). The body holds About Me and a `#papers` div filled by the listing.
- `papers.yml` + `_paper-list.ejs`: data-driven working-paper list. Fields: `title`, `coauthors` (renders "with X"), `pdf`, `arxiv`, `mathematica`, `code`, `notes` (red italic), `abstract` (Bootstrap collapse button). Order in the YAML is display order (`sort: false`).
- The EJS template is wrapped in a ```` ```{=html} ```` raw block. Without it, Pandoc treats indented template lines as code blocks.
- `styles/papers.css`: paper-list styling; colors come from CSS variables set in the two theme files.
- `.github/workflows/publish.yml`: renders on GitHub and deploys the `_site` artifact (no rendered output in git). No R/Python needed in CI; if R chunks are added later, set `execute: freeze: auto` and commit `_freeze/`.

## Course sections (`econ212/`, `econ312/`)

- `schedule.yml` in each course folder is the single source of truth. Fields: `week` (number or "Finals"), `iso` (YYYY-MM-DD; deliberately not `date`, which Quarto listings reformat), `day`, `topic`, `type` (class | exam | noclass), `notes`, `submit: true` (adds a "Submit on Moodle" chip), `materials` (list of `{label, href}` pointing into that course's `files/`). Initially generated from the `*_TentativeSchedule.tex` files on 2026-10-01; edit the YAML directly now.
- Three pages per course, all Quarto listings over that one YAML with shared templates in `_templates/`: `index.qmd` (Moodle banner, "Coming up" = next 3 meetings computed client-side from today's date, course-info table), `schedule.qmd` (full table; past rows dimmed, next meeting highlighted; card layout under 640px), `materials.qmd` (only rows with materials).
- The Moodle URL is passed to templates via `template-params: moodle:` in each page's front matter, and also appears in the course sidebar in `_quarto.yml`. ECON 312's Moodle URL is still a placeholder (TODO).
- Listings set `page-size: 500` (default 30 would paginate the schedule). Raw HTML tables need `data-quarto-disable-processing="true"` or Quarto forces 50/50 column widths.
- Example materials so far: Ch. 5–7 notes + handouts (212), Ch. 2–5 notes + handouts (312). Never post answer keys (`*_KEY`, `*-ANSWERS`), student info sheets, or copyrighted readings (e.g., the Popper PDF).

## Constraints

- No Google Analytics or other tracking (deliberately removed, October 2026).
- No student information, ever.
- Commit only finished PDFs; replace `files/CV-Doe.pdf` in place.
- Course sections live in this repo for now (same URLs, `peterdoe.com/econ212/`, as a later split into separate project repos would use).
