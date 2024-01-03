#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
