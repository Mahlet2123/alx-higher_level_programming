#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request(process.argv[2], (error, response, body) => {
  if (error) throw new Error(error);
  fs.writeFile(process.argv[3], body, err => {
    if (err) throw new Error(error);
  });
});
