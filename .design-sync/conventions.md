# Conventions — Shaden Shaar's academic site

A small design system for a personal academic site: a research homepage,
publications list, and blog. Editorial and text-first — serif for anything that
reads as content, sans for UI chrome, mono for metadata.

## Setup

**No provider or wrapper is required.** Components read no React context; drop
them straight into a page. Two things are set on the root element instead:

- **Dark mode is class-based.** Put `class="dark"` on `<html>` (or any
  ancestor) to switch themes. Every component already carries its own `dark:`
  variants — never fork a component for dark mode.
- **Give the page a background.** Components are transparent; the page owns its
  surface. Use `bg-paper text-ink` on `<body>`.

## Styling idiom

Tailwind utility classes, plus a handful of named component classes. Use the
named classes when one fits — they encode the system's type and colour
decisions, and they keep designs consistent:

| Class | Use for |
|---|---|
| `link` | Any inline text link. Underlined, accent on hover. |
| `meta` | Mono metadata — dates, venues, counts. |
| `card` | A raised, hairline-bordered surface. |
| `section-heading` | Serif heading opening a section. |
| `section-label` | Mono uppercase eyebrow above a heading. |
| `nav-link` / `is-active` | Header nav items; add `is-active` for the current page. |
| `btn` / `btn-primary` | Secondary and primary buttons. |
| `container-prose` | Single reading column (article pages). |
| `container-wide` | Wider column for list-heavy pages. |

**Colour vocabulary** — always use these, never raw hex or stock Tailwind
greys for text and surfaces:

- Text: `text-ink` (primary), `text-ink-muted` (secondary), `text-ink-subtle`
  (tertiary — captions, placeholders)
- Surfaces: `bg-paper` (page), `bg-paper-raised` (cards)
- Accent: `accent-50` … `accent-900`, e.g. `text-accent-700`,
  `hover:decoration-accent-600`. `accent-600/700` for light mode,
  `accent-300/400` for dark.
- Borders: `border-zinc-200 dark:border-zinc-800` is the standard hairline.

**Type**: `font-serif` (Source Serif 4) for names, headings and paper titles.
Default sans (Inter) for body and UI. `font-mono` (JetBrains Mono) for dates,
venues and labels — usually with `uppercase tracking-[0.18em]` when used as an
eyebrow.

## Where the truth lives

Read `_ds/<folder>/styles.css` and the `_ds_bundle.css` it imports before
styling anything — that stylesheet is the complete, authoritative vocabulary.
Per-component API contracts are in each `<Name>.d.ts`; usage notes are in each
`<Name>.prompt.md`.

## Idiomatic example

```jsx
<section className="container-wide py-14">
  <p className="section-label mb-3">News</p>
  <h2 className="section-heading mb-6">Recent activity</h2>

  <NewsCard
    items={[
      { date: 'Jun 2026', body: <><em>MovieRecapsQA</em> appeared at <strong>CVPR 2026</strong>.</> },
      { date: 'May 2026', body: 'JHLT paper with NewYork-Presbyterian.' },
    ]}
  />

  <p className="mt-6 text-sm text-ink-muted dark:text-zinc-400">
    More on the <a href="/publications/" className="link">publications page</a>.
  </p>
</section>
```

Library components carry the design decisions; your own layout glue is plain
Tailwind using the vocabulary above.
