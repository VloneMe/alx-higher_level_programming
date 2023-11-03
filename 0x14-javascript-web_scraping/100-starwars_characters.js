#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const url = 'https://swapi-api.alx-tools.com/api/films/'
const filePath = process.argv[3];

const request = require('request');
const fs = require('fs');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
