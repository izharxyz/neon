let theme = localStorage.getItem("theme");
if (!theme) {
    theme = "night";
    localStorage.setItem("theme", theme);
}
