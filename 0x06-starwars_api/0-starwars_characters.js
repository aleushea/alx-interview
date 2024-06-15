#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function handleError(error) {
  console.error('Error:', error);
}

async function getStarWarsCharacters() {
  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request(movieEndpoint, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });

    const movie = JSON.parse(movieResponse);
    const characterPromises = movie.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });

    const characterNames = await Promise.all(characterPromises);
    characterNames.forEach((name) => console.log(name));
  } catch (error) {
    handleError(error);
  }
}

getStarWarsCharacters();
