#!/usr/bin/node

const request = require('request');
const request2 = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    const numCharacters = characters.length;
    const characterNames = [];
    let count = 0;
    for (let i = 0; i < characters.length; i++) {
      request2.get(characters[i], (error, response, body) => {
        if (error) {
          console.error(error);
        } else {
          characterNames[i] = JSON.parse(body).name;
          count++;
          if (count === numCharacters) {
            for (const name of characterNames) {
              console.log(name);
            }
          }
        }
      });
    }
  }
});
