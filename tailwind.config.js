/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './blog/templates/blog/*.html',
    './users/templates/users/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: ["winter"],
  },
}

