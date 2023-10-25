#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Print the error if one occurred
    console.error(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
