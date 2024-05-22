
document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        link.addEventListener("click", function () {
            // Supprime la classe active de tous les liens
            navLinks.forEach(link => link.classList.remove("active-nav"));

            // Ajoute la classe active au lien cliqué
            this.classList.add("active-nav");
        });
    });
});