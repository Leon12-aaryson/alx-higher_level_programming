#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get({ url, encoding: 'utf-8' }, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (writeError) => {
    if (writeError) {
      console.error('Error writing to file:', writeError.message);
    } else {
      console.log(`Content saved to ${filePath}`);
    }
  });
});
