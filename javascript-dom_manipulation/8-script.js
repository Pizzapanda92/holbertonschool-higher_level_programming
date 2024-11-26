const hola = "https://hellosalut.stefanbohacek.dev/?lang=fr";

fetch(hola)
	.then(response => response.json())
	.then(data => {
		let trade = document.querySelector("#hello");
		trade.textContent = data.hello;
	})


	.catch(error => {
		console.error("Error while fetching data:", error);
	});
