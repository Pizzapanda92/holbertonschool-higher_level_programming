let update_header = document.querySelector("#update_header");
let header = document.querySelector("header");

update_header.addEventListener("click", function () {
    header.textContent = "New Header!!!"
})