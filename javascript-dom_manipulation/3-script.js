let header = document.querySelector("header");
let toggle_header = document.querySelector("#toggle_header");

toggle_header.addEventListener("click", function () {
    if (header.classList.contains("red")) {
        header.classList.remove("red")
        header.classList.add("green")
    } else if (header.classList.contains("green")) {
        header.classList.remove("green")
        header.classList.add("red")
    }
});
