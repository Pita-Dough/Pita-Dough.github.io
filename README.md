# peterdoe.com

Personal research and teaching website, built with [Quarto](https://quarto.org) and deployed to GitHub Pages by GitHub Actions.

## Everyday edits

| To change… | Edit |
|---|---|
| About blurb, headings | `index.qmd` |
| Name, title, sidebar links (Scholar, CV, email), portrait | the YAML header of `index.qmd` |
| Working papers (add, reorder, abstracts, notes) | `papers.yml` (PDFs go in `files/`) |
| CV | replace `files/CV-Doe.pdf` in place (same filename keeps all links valid) |
| Course schedule, due dates, handout links | `econ212/schedule.yml`, `econ312/schedule.yml` (PDFs go in that course's `files/`) |
| Course info (rooms, times, textbook) | `econ212/index.qmd`, `econ312/index.qmd` |
| Colors / fonts | `styles/light.scss`, `styles/dark.scss`; paper-list layout in `styles/papers.css` |

## Preview locally

```bash
quarto preview
```

## Publish

Commit and push to `main`. The workflow in `.github/workflows/publish.yml` renders the site and deploys it; nothing in `_site/` is ever committed.
One-time repo setting: **Settings → Pages → Source: GitHub Actions**, custom domain `www.peterdoe.com`.

## Rules of thumb

- Commit finished PDFs only, never every recompile (git keeps every version forever).
- No student information on this site.
- No analytics: there is deliberately no `google-analytics` key in `_quarto.yml`.
