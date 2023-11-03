#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

// Import the 'request' module for making HTTP requests
const request = require('request');

// Create an empty object to store the count of completed tasks for each user
const tasks = {};

// Get the API URL from the command-line arguments
const apiUrl = process.argv[2];

// Check if an API URL is provided as a command-line argument
if (!apiUrl) {
  console.error('Please provide the API URL as a command line argument');
  process.exit(1); // Exit the script with an error code
}

// Make an HTTP GET request to the provided API URL
request(apiUrl, function (error, response, body) {
  // Check if there's an error during the request
  if (error) {
    throw error;
  } else {
    // Parse the JSON response into an array
    const taskList = JSON.parse(body);

    // Iterate through the task list
    for (const item of taskList) {
      if (!tasks[item.userId] && item.completed === true) {
        tasks[item.userId] = 0;
      }
      if (item.completed === true) {
        tasks[item.userId] += 1;
      }
    }

    // Log the 'tasks' object, which contains the count of completed tasks for each user
    console.log(tasks);
  }
});
