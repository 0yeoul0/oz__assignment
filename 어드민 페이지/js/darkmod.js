document.addEventListener("DOMContentLoaded", () => {
  const toggleButton = document.getElementById("toggle-dark-mode");
  const darkModeClass = "dark-mode";

  const isDarkMode = localStorage.getItem("darkMode") === "true";
  if (isDarkMode) {
    document.body.classList.add(darkModeClass);
  }

  toggleButton.addEventListener("click", () => {
    document.body.classList.toggle(darkModeClass);

    const isDarkModeNow = document.body.classList.contains(darkModeClass);
    localStorage.setItem("darkMode", isDarkModeNow);
  });
});
