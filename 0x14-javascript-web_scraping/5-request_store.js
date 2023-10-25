#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request.get(url, (error, response, body) => {
  if (error) {
    // Print the error if one occurred
    console.error(error);
  } else {
    // Write the body of the response to the file
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        // Print the error if one occurred
        console.error(err);
      }
    });
  }
});
