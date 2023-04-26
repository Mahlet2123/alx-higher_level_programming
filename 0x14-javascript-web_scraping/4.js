#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(body).results;
    for (const i in results) {
      const characters = results[i].characters;
      for (const j in characters) {
        if (characters[j].includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
