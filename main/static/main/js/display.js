// navbar section
function toggleMenu() {

    const navLinks = document.getElementById("vras");
    navLinks.classList.toggle("show");

    // Close sidebar when any link is clicked
    document.querySelectorAll(".nav-menu a").forEach(link => {
        link.addEventListener("click", () => {
            document.getElementById("nav-menu").classList.remove("open");
        });
    });
}


// About section
var tablinks = document.getElementsByClassName("tab-links");
var tabcontents = document.getElementsByClassName("tab-content");
function opentab(tabname, event) {
    for (let tablink of tablinks) {
        tablink.classList.remove("active-link");

    }
    for (let tabcontent of tabcontents) {
        tabcontent.classList.remove("active-tab");
    }
    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab");
}