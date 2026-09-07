# design-sync notes — sshaar.github.io

Repo-specific gotchas for future syncs. Read this before re-running.

## Shape of this repo

- **This is an Astro site, not a component library.** The pages are `.astro`
  (compiled to HTML at build time) and cannot be bundled as React. The synced
  design system is `src/design/` — real React components, added so the site has
  a component vocabulary Claude Design can build with. `@astrojs/react` is
  already a dependency, so Astro pages can mount these directly; that is the
  intended direction of travel, not a parallel copy.
- `src/components/*.astro` are the **legacy** implementations of the same UI.
  When a component exists in both places, `src/design/` is the source of truth
  for the design system and the `.astro` file is what the live site still
  renders. Keep them in step or finish migrating the pages.

## Build

- `npm run build:ds` does three things: `tsc -p tsconfig.ds.json` (JS + `.d.ts`
  into `dist-ds/`), the Tailwind CLI (compiles `src/styles/global.css` against
  the site's real `tailwind.config.mjs`), then `scripts/ds-prepend-fonts.mjs`.
- **The font step is load-bearing.** The site loads Inter, Source Serif 4 and
  JetBrains Mono from font hosts via `<link>` tags in `BaseLayout.astro`. A
  design built from the DS never sees that layout — it gets only `styles.css`
  and its `@import` closure. `ds-prepend-fonts.mjs` prepends the remote
  `@import` so the families resolve. Without it, validate prints
  `[FONT_MISSING]` and every design renders in system fallbacks.
- Converter entry is `./dist-ds/index.js`, `--node-modules ./node_modules`
  (the repo root — `react` and `react-dom` live there).

## Gotchas hit during the first sync

- **`preview-rebuild.mjs` does not re-bundle component source.** It recompiles
  preview `.tsx` → `.html` only. After editing anything under `src/design/`,
  run `npm run build:ds` **and** a full `package-build.mjs`, or the change
  silently won't appear in the cards. Cost me one confused grading cycle on
  TagPill's pressed state.
- `cardMode: "column"` is set for `Nav`, `Footer`, `Hero` and `PublicationCard`
  — all are full-width layouts that overflow a multi-column grid cell.
  PublicationCard was flagged by `[GRID_OVERFLOW]`; the other three were set
  pre-emptively for the same reason.

## Known render warns (expected — not new)

- `[RENDER_THIN] SocialLinks: mounts have no text and paint nothing` —
  **benign.** The component is a row of icon-only links; it has no text nodes
  by construction. Confirmed from the screenshot that all five icons paint.
- `[FONT_REMOTE]` for Inter / JetBrains Mono / Source Serif 4 — expected, see
  the font step above. This is the healthy state; `[FONT_MISSING]` is not.

## Component fixes made while authoring previews

- `TagPill` gained a visible `pressed` affordance (`ring-1 ring-inset
  ring-current` + heavier weight). Before this the prop only set
  `aria-pressed`, so an active filter chip looked identical to an inactive one
  — a real accessibility/UX bug surfaced by grading, not a preview artifact.
  The old `.tag-chip[aria-pressed]` CSS that used to do this was dropped from
  `global.css` during an earlier redesign.

## Re-sync risks — what can silently go stale

- **Preview content is hand-copied from the site's data.** `PublicationCard`
  and `NewsCard` previews inline real paper titles, author lists and news
  entries from `src/data/publications.ts` and `src/pages/index.astro`. Those
  files change; the previews will not follow. If a paper is retitled or a news
  item edited, the cards keep showing the old text. Re-check them on any sync
  that follows a content edit.
- **The two implementations can drift.** If `src/components/*.astro` is
  restyled without the matching `src/design/*.tsx` change (or vice versa), the
  design system stops describing the real site. This is the single most likely
  way this sync rots.
- **The font `@import` URL is pinned in `scripts/ds-prepend-fonts.mjs`.** It
  lists specific weights and optical-size ranges. If `BaseLayout.astro`'s font
  `<link>` changes, update the script to match or the DS and the site will
  render in different weights.
- `Hero`'s preview uses an inline SVG data-URI portrait, because the real
  `/portrait.jpg` lives in the site's `public/` and is not shipped in the
  bundle. That is deliberate; don't "fix" it by pointing at a path that 404s.
- Playwright/chromium were installed into `.ds-sync/node_modules` (gitignored).
  A fresh clone needs `npm i playwright && npx playwright install chromium`
  inside `.ds-sync/` before the render check can run.
