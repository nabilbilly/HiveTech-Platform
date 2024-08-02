module.exports = {
  content: ["./Template/**/*.html", "./Mainapp/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
      },
      colors: {
        "custom-yellow": "#FDCE02", // Add your custom color
      },
      screens: {
        "custom-md": "770px", // Added  custom screen size
        "custom-lg": "900px",
      },
    },
  },
  plugins: [],
};
  
  
  