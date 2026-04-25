import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import mdx from '@astrojs/mdx';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import rehypeSlug from 'rehype-slug';

export default defineConfig({
  site: 'https://sshaar.github.io',
  integrations: [
    react(),
    mdx(),
    tailwind({ applyBaseStyles: false }),
    sitemap(),
  ],
  markdown: {
    rehypePlugins: [rehypeSlug],
    shikiConfig: {
      theme: 'github-light',
      wrap: true,
    },
  },
});
