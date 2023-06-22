/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    colors: {
      purple: {
        50: '#fcf5fe',
        100: '#f9eafd',
        200: '#f2d3fb',
        300: '#ebb1f6',
        400: '#da6eed',
        500: '#ce52e3',
        600: '#b433c6',
        700: '#9727a4',
        800: '#7d2286',
        900: '#69216e',
        950: '#440949',
      },
      gray: {
        50: '#f7f7f7',
        100: '#e3e3e3',
        200: '#c8c8c8',
        300: '#a4a4a4',
        400: '#787878',
        500: '#666666',
        600: '#515151',
        700: '#434343',
        800: '#383838',
        900: '#313131',
        950: '#1a1a1a',
      },

      yellow: {
        50: '#feffe7',
        100: '#fcffc1',
        200: '#feff86',
        300: '#fff941',
        400: '#ffec0d',
        500: '#ffdd00',
        600: '#d1a300',
        700: '#a67502',
        800: '#895b0a',
        900: '#744a0f',
        950: '#442704',
      },

      black: '#000',
      white: '#ffffff',
    },
    extend: {
      gridTemplateColumns: {
        main: '1fr 4fr',
      },
    },
  },
  plugins: [],
};
