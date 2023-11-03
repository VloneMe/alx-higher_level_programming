#!/usr/bin/node
// A script that prints all characters of a Star Wars movie:

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Please provide the Movie ID as a command line argument');
  process.exit(1);
}

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    console.log(`Characters in ${movieData.title}:`);

    const characterUrls = movieData.characters;

    function fetchCharacter (index) {
      if (index < characterUrls.length) {
        request(characterUrls[index], function (error, response, body) {
          if (error) {
            console.error('Error fetching character:', error);
          } else if (response.statusCode !== 200) {
            console.error('Request failed with status code:', response.statusCode);
          } else {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }

          fetchCharacter(index + 1);
        });
      }
    }

    fetchCharacter(0);
  }
});
