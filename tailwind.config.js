import colors from 'tailwindcss/colors'

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './_includes/**/*.html',
    './_layouts/**/*.html',
    './_posts/*.md',
    './*.html',
  ],
  theme: {
    extend: {
    typography: {
        DEFAULT: {
          css: {
            a: {
            color: colors.teal[200],
            'text-decoration': 'underline',
            'text-decoration-style': 'dotted'
            }
          },
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