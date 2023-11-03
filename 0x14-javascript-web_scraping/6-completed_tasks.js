#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');
let tasks = {};

request(process.argv[2], function (error, response, body) {
  if (error) {
    throw (error);
  } else {
    let taskList = JSON.parse(response.body);
    for (let items in taskList) {
      if (!(tasks[taskList[items]['userId']]) && taskList[items]['completed'] === true) {
        tasks[taskList[items]['userId']] = 0;
      }
      if (taskList[items]['completed'] === true) {
        tasks[taskList[items]['userId']] += 1;
      }
    }
    console.log(tasks);
  }
});
