#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide the Movie ID as a command line argument');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    
    // Function to fetch and print character names
    function fetchCharacter(index) {
      if (index < characterUrls.length) {
        request(characterUrls[index], function (error, response, characterBody) {
          if (error) {
            console.error('Error fetching character:', error);
          } else if (response.statusCode !== 200) {
            console.error('Request failed with status code:', response.statusCode);
          } else {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
          }
          // Fetch the next character
          fetchCharacter(index + 1);
        });
      }
    }

    console.log(`Characters in ${movieData.title}:`);
    // Start fetching characters from index 0
    fetchCharacter(0);
  }
});
