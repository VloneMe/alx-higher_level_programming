// JavaScript script that fetches and lists the title for all movies
// by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$(document).ready(function() {
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        const movies = data.results;
        const ulElement = $("#list_movies");
        movies.forEach(function(movie) {
            const liElement = $("<li>").text(movie.title);
            ulElement.append(liElement);
        });
        
    });
});
