const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";

fetch(url)
  .then(response => response.json())
  .then(data => {
    let characterElement = document.querySelector("#character");

    characterElement.textContent = data.name;
  })
  .catch(error => {
    console.error("Error while fetching data :", error);
  });
