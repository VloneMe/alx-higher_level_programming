#!/usr/bin/node
// A script that display the status code of a GET request.

const request = require('request-promise-native');

const url = process.argv[2];

if (!url) {
  console.error('Please provide a URL as an argument');
  process.exit(1);
}

request.get(url)
  .then((response) => {
    // Parse the response and display the status code
    console.log(`code: ${response.statusCode}`);
  })
  .catch((error) => {
    console.error('Error:', error.message);
  });
