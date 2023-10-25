#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);

    const moviesWithWedge = data.results.filter((movie) =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    console.log(moviesWithWedge.length);
  }
});
