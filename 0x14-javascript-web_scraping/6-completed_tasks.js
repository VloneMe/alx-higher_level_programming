#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');
let tasks = {};

const apiUrl = process.argv[2]; // Get the API URL from the command line arguments

if (!apiUrl) {
  console.error('Please provide the API URL as a command line argument');
  process.exit(1);
}

request(apiUrl, function (error, response, body) {
  if (error) {
    throw (error);
  } else {
    let taskList = JSON.parse(body); // Use 'body' directly instead of 'response.body'
    for (let item of taskList) { // Use 'item' instead of 'items'
      if (!(tasks[item['userId']]) && item['completed'] === true) {
        tasks[item['userId']] = 0;
      }
      if (item['completed'] === true) {
        tasks[item['userId']] += 1;
      }
    }
    console.log(tasks);
  }
});
