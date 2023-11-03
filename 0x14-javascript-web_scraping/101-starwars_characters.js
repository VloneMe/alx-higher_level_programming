#!/usr/bin/node
// A script that prints all characters of a Star Wars movie:

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const file = process.argv[3];
const req = require('request');
const fs = require('fs');

req(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
