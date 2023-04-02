/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {}
  },
  plugins: [
    require('daisyui')
  ],
  daisyui: {
    themes: [
      'night',
      'winter',
      'valentine',
      'retro',
      'forest',
      'luxury',
      'cyberpunk',
      'coffee',
      'dracula'
    ],
  },
};