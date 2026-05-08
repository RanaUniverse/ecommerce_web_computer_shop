// static/js/search_icon_change.js
// here i will try to maket the code to change the serach icon always


document.addEventListener("DOMContentLoaded", function () {

    const icons = [
        "bi-laptop",
        "bi-pc-display",
        "bi-motherboard",
        "bi-cpu",
        "bi-gpu-card",
        "bi-memory",
        "bi-hdd",
        "bi-nvme",
        "bi-usb-drive",
        "bi-router",
        "bi-display"
    ];

    const colors = [
        "text-primary",
        "text-danger",
        "text-success",
        "text-warning",
        "text-info",
        "text-secondary"
    ];

    const iconElement = document.getElementById("searchIcon");

    if (!iconElement) return;

    setInterval(() => {

        // pick random icon
        const randomIcon = icons[Math.floor(Math.random() * icons.length)];

        // pick random color
        const randomColor = colors[Math.floor(Math.random() * colors.length)];

        // remove old bi-* icon classes
        icons.forEach(i => iconElement.classList.remove(i));

        // remove old color classes
        colors.forEach(c => iconElement.classList.remove(c));

        // apply new ones
        iconElement.classList.add(randomIcon);
        iconElement.classList.add(randomColor);

    }, 1000); // 1000ms = 1 s
});