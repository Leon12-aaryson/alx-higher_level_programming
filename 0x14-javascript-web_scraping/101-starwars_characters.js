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
    const characters = movieData.characters;

    // Print each character name in the order of the characters array
    characters.forEach(characterUrl => {
      request.get(characterUrl, (characterError, characterResponse, characterBody) => {
        if (characterError) {
          console.error('Error:', characterError.message);
          return;
        }

        if (characterResponse.statusCode !== 200) {
          console.error('Error:', `Received status code ${characterResponse.statusCode}`);
          return;
        }

        const character = JSON.parse(characterBody);
        console.log(character.name);
      });
    });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
