#!/usr/bin/node

const request = require('../../../usr/lib/node_modules/request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  console.log('code:', response.statusCode);
});
