// i will make the logic here to allow a button press
// to chagne my theme there
// https://dev.to/whitep4nth3r/the-best-lightdark-mode-theme-toggle-in-javascript-368f


/*
static/js/theme_toggle.js
Handles Bootstrap dark/light theme toggle
*/

document.addEventListener("DOMContentLoaded", () => {

    const themeToggleBtn = document.getElementById("themeToggleBtn");

    // Load saved theme from the browser's storage else light 
    const savedTheme = localStorage.getItem("theme") || "light";

    // change the attribute in the html tag at top
    document.documentElement.setAttribute(
        "data-bs-theme",
        savedTheme
    );

    updateButtonIcon(savedTheme);

    // Button click event
    if (themeToggleBtn) {

        themeToggleBtn.addEventListener("click", () => {

            const currentTheme =
                document.documentElement.getAttribute("data-bs-theme");

            const newTheme =
                currentTheme === "dark" ? "light" : "dark";

            // change the value of the attribute so that dark and light theme will chagne
            document.documentElement.setAttribute(
                "data-bs-theme",
                newTheme
            );

            // Save theme in the broser's storage
            localStorage.setItem("theme", newTheme);

            updateButtonIcon(newTheme);

        });

    }

    function updateButtonIcon(theme) {

        if (!themeToggleBtn) return;

        if (theme === "dark") {

            themeToggleBtn.innerHTML = `
                <i class="bi bi-sun-fill me-2"></i>
                Light Mode
            `;

        } else {

            themeToggleBtn.innerHTML = `
                <i class="bi bi-moon-stars-fill me-2"></i>
                Dark Mode
            `;

        }

    }

});