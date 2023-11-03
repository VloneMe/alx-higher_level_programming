#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const request = require('request');

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

    // Fetch and print character names
    movieData.characters.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('Error fetching character:', error);
        } else if (response.statusCode !== 200) {
          console.error('Request failed with status code:', response.statusCode);
        } else {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  }
});
