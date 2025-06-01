import colors from 'tailwindcss/colors'

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector',
  content: [
    './_includes/**/*.html',
    './_layouts/**/*.html',
    './_posts/*.md',
    './*.html',
  ],
  theme: {
    extend: {
      colors: {
        primary: colors.stone,
      },
      typography: {
        DEFAULT: {
          css: (theme) => ({
            a: {
              color: theme('colors.primary.200'),
              'text-decoration': 'underline',
              'text-decoration-style': 'dotted',
              '&:hover': {
                color: theme('colors.primary.400'),
              },
              '@screen dark': {
                color: theme('colors.primary.400'),
              },
            }
          }),
        },
      },
    },
    fontFamily: {
      display: ['LibertinusMonoMono'],
      sans: ['sans-serif'],
    },

  },
  variants: {},
  plugins: [require('@tailwindcss/typography')],
}