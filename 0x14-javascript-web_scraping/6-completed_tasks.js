#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const apiUrl = process.argv[2];
const filePath = process.argv[3];

const request = require('request');
const fs = require('fs');

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
