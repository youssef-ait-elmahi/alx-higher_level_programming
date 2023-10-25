#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const id = process.argv[2];

// Define the URL for the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// Make a GET request to the Star Wars API
request.get(url, (error, response, body) => {
  if (error) {
    // Print the error if one occurred
    console.error(error);
  } else {
    // Parse the response body (string) into a JavaScript object
    const data = JSON.parse(body);

    // Print the title of the movie
    console.log(data.title);
  }
});
