# CLAUDE.md — Peter Doe's academic website

## What this is
Personal academic website served at **www.peterdoe.com** (custom domain in `CNAME`).
It is a **Jekyll** site built on the *Minimal Light* theme (yaoyao-liu/minimal-light),
hosted on **GitHub Pages** (repo name: `Pita-Dough.github.io-main`).

Owner: Peter Doe, Assistant Professor of Economics, Hope College.
Field: microeconomic theory / algorithmic market design (matching theory, school choice).

## How the site is assembled
Jekyll stitches these together at build time:

- `_config.yml` — site-wide variables (name, position, field, affiliation, email,
  avatar, favicons, SEO keywords, Google Analytics). **Edit identity/affiliation here first.**
- `index.md` — the homepage body (front matter `layout: homepage`). Contains the
  "About Me" text, the CV + email buttons, and `{% include_relative %}` calls that
  pull in the section files below.
- `_layouts/homepage.html` — the page shell: `<head>`, the header block (avatar, name,
  position/field/affiliation, social icons), and where `{{ content }}` (index.md) renders.
  The header now reads `{{ site.position }}`, `{{ site.field }}`, `{{ site.affiliation }}`
  from `_config.yml` — do NOT hardcode these strings again.
- `_includes/` — section partials pulled into `index.md`:
  - `workingpapers.md` — renders the "Working Papers" list from `_data/workingpapers.yml`.
    **This is the only section currently included on the homepage.**
  - `publications.md` — renders "Publications" from `_data/publications.yml`.
    Not included on the homepage yet (Peter has no journal pubs listed). The data file
    is an empty template; add papers there and add the include to `index.md` to show it.
  - `services.md` — referee/service list. Empty template, not included.
- `_data/*.yml` — the actual content records (title, authors, abstract, pdf, arXiv…).
  **To add/edit a paper, edit the YAML here, not the HTML.**
- `_sass/`, `assets/css/` — styling (SCSS + compiled CSS). Light/dark variants exist;
  `auto_dark_mode: true` in config picks `style.css` vs `style-no-dark-mode.css`.
- `assets/js/` — small scripts (favicon switcher, dark-mode toggle, scale fix).
- `assets/files/` — PDFs (CV, papers, poster) linked from the site.
- `assets/img/` — images. **Current avatar: `self_picture_hope.jpg`** (square headshot,
  cropped from `Doe,Peter001.JPG`). Set via `avatar:` in `_config.yml`.

## Editing cheatsheet
- Change name/title/affiliation/email/SEO → `_config.yml`.
- Change the intro paragraph or the CV/email buttons → `index.md`.
- Add/edit a working paper → `_data/workingpapers.yml`.
- Add a published paper → `_data/publications.yml` **and** add the
  `{% include_relative _includes/publications.md %}` line to `index.md`.
- Change the profile photo → drop a square image in `assets/img/`, point `avatar:` at it.
- Change page structure/header/social links → `_layouts/homepage.html`.

## Build / deploy
- Local preview: `bundle install` then `bundle exec jekyll serve` (needs Ruby + Bundler;
  see `Gemfile`). Site builds to `_site/`.
- Production: push to the GitHub Pages repo; GitHub builds and serves it at the `CNAME`
  domain automatically. No manual build step needed for deploy.
- `_config.yml`'s `exclude:` list keeps READMEs, the Gemfile, LICENSE, and
  `html_source_file/` out of the built site.

## Notes / gotchas
- Leftover template content was cleaned out of `_data/publications.yml` and
  `_includes/services.md` (they previously held the theme author's CS papers).
- The stale `html_source_file/` static export (original author's CV/medical-imaging
  content) and the unused legacy images have been deleted. `assets/img/` now holds only
  the favicons and the live avatar `self_picture_hope.jpg`.
- The high-res headshot original (`Doe,Peter001.JPG`) was removed from the repo. If you
  need to re-crop the avatar, re-add a source image to the folder first.
- Global rule for this machine: only touch files under the `Lake` folder.
