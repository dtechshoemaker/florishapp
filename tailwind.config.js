/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  // Add prefix to all Tailwind classes to avoid conflicts with Bootstrap
  prefix: 'tw-',
  // Make Tailwind classes have higher specificity than Bootstrap
  important: true,
  theme: {
    extend: {
      colors: {
        primary: '#0e627b',
        secondary: '#4298b1',
        light: '#f8fafc',
        accent: 'rgb(255, 215, 166)',
      },
    },
  },
  plugins: [],
}