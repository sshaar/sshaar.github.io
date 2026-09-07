import base from './tailwind.config.mjs';

/**
 * Tailwind config for the design-system stylesheet only (dist-ds/styles.css).
 *
 * The site's own build is purged against the site's markup, which is correct
 * for shipping but wrong for a design system: the Claude Design agent composes
 * new layouts, so it needs the brand scales available even where this site
 * happens not to use them yet. Without the safelist below, a design that reaches
 * for `text-accent-500` or `bg-paper-raised` silently renders unstyled.
 *
 * Deliberately narrow — only the brand token scales are safelisted, not all of
 * Tailwind. The site's own stylesheet is unaffected; it still uses
 * tailwind.config.mjs.
 */
export default {
  ...base,
  safelist: [
    {
      pattern:
        /^(text|bg|border|ring|decoration|divide|from|to)-accent-(50|100|200|300|400|500|600|700|800|900)$/,
      variants: ['hover', 'focus', 'dark', 'dark:hover'],
    },
    {
      pattern: /^(text|bg|border|ring|decoration|divide)-(ink|paper)(-(muted|subtle|raised))?$/,
      variants: ['hover', 'dark', 'dark:hover'],
    },
    // Component classes from global.css that the site does not currently use,
    // but that the design agent should still be able to reach for.
    'btn',
    'btn-primary',
    'card',
    'link',
    'meta',
    'section-heading',
    'section-label',
  ],
};
