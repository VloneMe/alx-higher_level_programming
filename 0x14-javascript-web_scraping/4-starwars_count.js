#!/usr/bin/node
// A script that prints the number of movies
// where the character “Wedge Antilles” is present.

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes('18')) counter++;
      }
    }
    console.log(counter);
  }
});
