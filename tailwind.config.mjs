/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        accent: {
          50: '#eff6ff',
          100: '#dbeafe',
          200: '#bfdbfe',
          300: '#93c5fd',
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
        },
        ink: {
          DEFAULT: '#1a1a1f',
          muted: '#55555e',
          subtle: '#75757e',
        },
        paper: {
          DEFAULT: '#fbfaf8',
          raised: '#ffffff',
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
