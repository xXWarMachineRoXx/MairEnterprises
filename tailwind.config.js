// tailwind.config.js
import { tailwindConfig } from '@storefront-ui/vue/tailwind-config';

/** @type {import('tailwindcss').Config} */
export default {
  presets: [tailwindConfig],
  content: ['./index.html', './**/*.vue', './node_modules/@storefront-ui/vue/**/*.{js,mjs}'],
  theme: {
    extend: {
      fontSize: {
        xs: "0.75rem",
        sm: "0.875rem",
        base: "1rem",
        lg: "1.125rem",
        xl: "1.25rem",
        "2xl": "1.5rem",
        "3xl": "1.875rem",
        "4xl": "2.25rem",
        "5xl": "3rem",
        "6xl": "4rem",
      },
      colors: {
        'text': {
          50: 'rgb(var(--text-50))', // RGB(234, 233, 252)
          100: 'rgb(var(--text-100))', // RGB(214, 210, 249)
          200: 'rgb(var(--text-200))', // RGB(173, 165, 243)
          300: 'rgb(var(--text-300))', // RGB(132, 120, 237)
          400: 'rgb(var(--text-400))', // RGB(91, 75, 231)
          500: 'rgb(var(--text-500))', // RGB(50, 31, 224)
          600: 'rgb(var(--text-600))', // RGB(40, 24, 180)
          700: 'rgb(var(--text-700))', // RGB(30, 18, 135)
          800: 'rgb(var(--text-800))', // RGB(20, 12, 90)
          900: 'rgb(var(--text-900))', // RGB(10, 6, 45)
          950: 'rgb(var(--text-950))', // RGB(5, 3, 22)
        },
        'background': {
          50: 'rgb(var(--background-50))', // RGB(235, 235, 250)
          100: 'rgb(var(--background-100))', // RGB(214, 214, 245)
          200: 'rgb(var(--background-200))', // RGB(173, 173, 235)
          300: 'rgb(var(--background-300))', // RGB(133, 133, 224)
          400: 'rgb(var(--background-400))', // RGB(92, 92, 214)
          500: 'rgb(var(--background-500))', // RGB(51, 51, 204)
          600: 'rgb(var(--background-600))', // RGB(41, 41, 163)
          700: 'rgb(var(--background-700))', // RGB(31, 31, 122)
          800: 'rgb(var(--background-800))', // RGB(20, 20, 82)
          900: 'rgb(var(--background-900))', // RGB(10, 10, 41)
          950: 'rgb(var(--background-950))', // RGB(5, 5, 20)
        },
        'primary': {
          50: 'rgb(var(--primary-50))', // RGB(248, 243, 237)
          100: 'rgb(var(--primary-100))', // RGB(240, 231, 219)
          200: 'rgb(var(--primary-200))', // RGB(226, 207, 182)
          300: 'rgb(var(--primary-300))', // RGB(211, 183, 146)
          400: 'rgb(var(--primary-400))', // RGB(197, 159, 109)
          500: 'rgb(var(--primary-500))', // RGB(182, 135, 73)
          600: 'rgb(var(--primary-600))', // RGB(146, 108, 58)
          700: 'rgb(var(--primary-700))', // RGB(109, 81, 44)
          800: 'rgb(var(--primary-800))', // RGB(73, 54, 29)
          900: 'rgb(var(--primary-900))', // RGB(36, 27, 15)
          950: 'rgb(var(--primary-950))', // RGB(18, 13, 7)
        },
        'secondary': {
          50: 'rgb(var(--secondary-50))', // RGB(254, 244, 231)
          100: 'rgb(var(--secondary-100))', // RGB(252, 233, 207)
          200: 'rgb(var(--secondary-200))', // RGB(250, 210, 158)
          300: 'rgb(var(--secondary-300))', // RGB(247, 188, 110)
          400: 'rgb(var(--secondary-400))', // RGB(245, 165, 61)
          500: 'rgb(var(--secondary-500))', // RGB(242, 143, 13)
          600: 'rgb(var(--secondary-600))', // RGB(194, 114, 10)
          700: 'rgb(var(--secondary-700))', // RGB(145, 86, 8)
          800: 'rgb(var(--secondary-800))', // RGB(97, 57, 5)
          900: 'rgb(var(--secondary-900))', // RGB(48, 29, 3)
          950: 'rgb(var(--secondary-950))', // RGB(24, 14, 1)
        },
        'accent': {
          50: 'rgb(var(--accent-50))', // RGB(255, 250, 230)
          100: 'rgb(var(--accent-100))', // RGB(255, 245, 204)
          200: 'rgb(var(--accent-200))', // RGB(254, 236, 154)
          300: 'rgb(var(--accent-300))', // RGB(254, 226, 103)
          400: 'rgb(var(--accent-400))', // RGB(254, 217, 52)
          500: 'rgb(var(--accent-500))', // RGB(254, 207, 1)
          600: 'rgb(var(--accent-600))', // RGB(203, 166, 1)
          700: 'rgb(var(--accent-700))', // RGB(152, 124, 1)
          800: 'rgb(var(--accent-800))', // RGB(101, 83, 1)
          900: 'rgb(var(--accent-900))', // RGB(51, 41, 0)
          950: 'rgb(var(--accent-950))', // RGB(25, 21, 0)
        },

      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
