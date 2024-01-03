#!/usr/bin/node
const request = require('request');

const apiURL = process.argv[2];

const wedgeAntillesID = 18;

request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error('Error:', error.message);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Error:', `Received status code ${response.statusCode}`);
    return;
  }

  try {
    const filmsData = JSON.parse(body);
    const moviesWithWedgeAntilles = filmsData.results.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesID}/`)
    );

    console.log(moviesWithWedgeAntilles.length);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError.message);
  }
});
