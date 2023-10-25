#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if one occurred
    console.error(error);
  } else {
    // Parse the response body (string) into a JavaScript object
    const todos = JSON.parse(body);

    // Create an empty object to store the number of completed tasks by user id
    const completedTasks = {};

    // Loop over the todos
    for (const todo of todos) {
      // If the todo is completed
      if (todo.completed) {
        // If the user id is not yet in the completedTasks object, add it with a value of 1
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 1;
        } else {
          // If the user id is already in the completedTasks object, increment its value by 1
          completedTasks[todo.userId]++;
        }
      }
    }

    // Print the completedTasks object
    console.log(completedTasks);
  }
});
