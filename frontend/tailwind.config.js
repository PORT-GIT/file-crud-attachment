/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
  variants: {
    extend: {
      display: ["focus-group"]
    }
  }
  // the focus group here will be used to display the dropdown menu at the 
  // navbar.jsx file
}

