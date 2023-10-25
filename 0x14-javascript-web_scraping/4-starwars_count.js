#!/usr/bin/node
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Define the character ID for Wedge Antilles
const characterId = 18;

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if one occurred
    console.error(error);
  } else {
    // Parse the response body (string) into a JavaScript object
    const data = JSON.parse(body);

    // Filter the movies to include only those where Wedge Antilles is present
    const moviesWithWedge = data.results.filter((movie) =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    // Print the number of movies where Wedge Antilles is present
    console.log(moviesWithWedge.length);
  }
});

