/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./blog/templates/blog/*.html",
        "./users/templates/users/*.html",
        "./templates/**/*.html",
    ],
    theme: {
        extend: {
            height: {
                screen: ["100vh", "100dvh"],
            },
            scale: {
                flip: "-1",
            },
        },
    },
    plugins: [require("@tailwindcss/typography"), require("daisyui")],
    daisyui: {
        themes: ["valentine"],
    },
};
