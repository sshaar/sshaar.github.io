/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Muted teal. Reads as considered rather than default-framework blue,
        // and holds contrast on both the warm paper and the near-black dark bg.
        accent: {
          50: '#eff6f5',
          100: '#d8eae7',
          200: '#b2d5d0',
          300: '#82b9b2',
          400: '#549b93',
          500: '#367e76',
          600: '#26665f',
          700: '#1e534e',
          800: '#1a433f',
          900: '#173835',
        },
        ink: {
          DEFAULT: '#1c1b18',
          muted: '#56534c',
          subtle: '#817d74',
        },
        paper: {
          DEFAULT: '#f6f3ed',
          raised: '#fdfbf7',
        },
        // Light-mode zinc shades are warmed to sit on the paper without a grey
        // cast; 400 and up keep Tailwind's neutrals, which dark mode relies on.
        zinc: {
          50: '#f8f6f2',
          100: '#efece5',
          200: '#e3ded3',
          300: '#cfc9bc',
          400: '#a1a1aa',
          500: '#71717a',
          600: '#52525b',
          700: '#3f3f46',
          800: '#27272a',
          900: '#18181b',
          950: '#09090b',
        },
      },
      fontFamily: {
        sans: ['"Inter"', 'ui-sans-serif', 'system-ui', 'sans-serif'],
        serif: ['"Source Serif 4"', 'Georgia', 'serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      typography: ({ theme }) => ({
        DEFAULT: {
          css: {
            maxWidth: '68ch',
            color: theme('colors.ink.DEFAULT'),
            a: {
              color: theme('colors.accent.700'),
              textDecoration: 'underline',
              textUnderlineOffset: '2px',
              '&:hover': { color: theme('colors.accent.900') },
            },
            'h1,h2,h3,h4': {
              fontFamily: theme('fontFamily.sans').join(', '),
              fontWeight: '600',
              letterSpacing: '-0.02em',
            },
          },
        },
        invert: {
          css: {
            color: '#e4e4e7',
            a: {
              color: theme('colors.accent.400'),
              '&:hover': { color: theme('colors.accent.300') },
            },
            'h1,h2,h3,h4,strong': { color: '#fafafa' },
          },
        },
      }),
    },
  },
  plugins: [require('@tailwindcss/typography')],
};
