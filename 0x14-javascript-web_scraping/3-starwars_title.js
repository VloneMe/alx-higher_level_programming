#!/usr/bin/node
// A script that prints the title of a Star Wars movie
// where the episode number matches a given integer.

const request = require('request');
const movieId = process.argv[2];
const url = 'http://swapi.co/api/films/' + movieId;

request(url, function (err, response, body) {
  if (err) {
    console.log('code: ' + response.statusCode);
  }
  console.log(JSON.parse(body)['title']);
});
