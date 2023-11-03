#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');
const tasks = {};

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as a command line argument');
  process.exit(1);
}

request(apiUrl, function (error, response, body) {
  if (error) {
    throw (error);
  } else {
    let taskList = JSON.parse(body);
    for (let item of taskList) {
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
