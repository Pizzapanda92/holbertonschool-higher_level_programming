let add_item = document.querySelector("#add_item");
let my_list = document.querySelector(".my_list");

add_item.addEventListener("click", function () {
    let item = document.createElement("li");
    item.textContent = "Item";
    my_list.appendChild(item);
});