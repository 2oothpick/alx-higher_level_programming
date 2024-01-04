#!/usr/bin/node

const request = require('request');

// Make a simple GET request
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  }
  const JsObject = JSON.parse(body);
  console.log(JsObject.title);
});
