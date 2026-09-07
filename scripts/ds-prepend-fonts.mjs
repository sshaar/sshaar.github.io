/**
 * The site loads its three families from font hosts via <link> tags in
 * BaseLayout.astro. A design built from the synced design system never sees
 * that layout — it receives only styles.css and its @import closure — so
 * without this the DS renders in system fallbacks.
 *
 * Prepends a single remote @import to the compiled dist-ds/styles.css. It must
 * lead the file: CSS requires @import before any other rule.
 */
import { readFileSync, writeFileSync } from 'node:fs';

const OUT = 'dist-ds/styles.css';
const FONTS =
  "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap');";

const css = readFileSync(OUT, 'utf8');
if (css.includes('fonts.googleapis.com')) {
  console.log('fonts: @import already present');
} else {
  writeFileSync(OUT, `${FONTS}\n${css}`);
  console.log('fonts: prepended @import for Inter, JetBrains Mono, Source Serif 4');
}
