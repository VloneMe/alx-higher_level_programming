#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');
const apiUrl = process.argv[2];

const fs = require('fs');
const filePath = process.argv[3];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
