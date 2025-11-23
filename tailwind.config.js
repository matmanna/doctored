import colors from 'tailwindcss/colors'

/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'selector',
  content: [
    './_includes/**/*.html',
    './_layouts/**/*.html',
    './_pages/**/*.html',
    './*.html',
  ],
  theme: {
    extend: {
      colors: (function () {
        const defaultPaletteName = 'stone'
        const paletteName = (process.env.PRIMARY_PALETTE || defaultPaletteName).toLowerCase()
        let primaryPalette = colors[paletteName]
        if (!primaryPalette) {
          primaryPalette = colors[defaultPaletteName]
        }

        const primaryShade = process.env.PRIMARY_SHADE
        if (primaryShade && primaryPalette && primaryPalette[primaryShade]) {
          const mapped = {}
          Object.keys(primaryPalette).filter(k => /^\d+$/.test(k)).forEach(k => {
            mapped[k] = primaryPalette[primaryShade]
          })
          return { primary: mapped }
        }
        return { primary: primaryPalette }
      })(),
      typography: {
        DEFAULT: {
          css: (theme) => ({
            a: {
              color: theme('colors.primary.200') + ' !important',
              'text-decoration': 'underline !important',
              'text-decoration-style': 'dotted !important',
              '&:hover': {
                color: theme('colors.primary.400') + ' !important',
              },
              '@screen dark': {
                color: theme('colors.primary.400') + ' !important',
              },
            }
          }),
        },
      },
    },
    fontFamily: {
      display: ['LibertinusMonoMono'],
      sans: ['sans-serif'],
      icon: ['FontAwesome'],
    },
    borderWidth: {
      DEFAULT: '1px',
      '1': '1px',
      '2': '2px',
      '3': '3px',
    },
    borderStyle: {
      dashed: 'dashed',
      dotted: 'dotted',
      solid: 'solid',
    },
  },
  variants: {},
  plugins: [require('@tailwindcss/typography')],
}