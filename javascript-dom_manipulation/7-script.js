const movie = "https://swapi-api.hbtn.io/api/films/?format=json";

fetch(movie)
  .then(response => response.json())
  .then(data => {
    let movieList = document.querySelector("#list_movies");
    data.results.forEach(movie => {
      let listItem = document.createElement("li");
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error("Error while fetching data:", error);
  });
