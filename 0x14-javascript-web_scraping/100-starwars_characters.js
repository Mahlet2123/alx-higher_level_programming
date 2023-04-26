#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films';
const movieId = process.argv[2];


request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(body).results;
    for (const i in results) {
        if (i == movieId) {
            const characters = results[i].characters;
            for (const j in characters) {
                request.get(characters[j], (error, response, body) => {
                    if (error) {
                        console.error(error);
                    } else {
                        const name = JSON.parse(body).name
                        console.log(name);
                    }
                });
            }
        }
      }
    }
});
