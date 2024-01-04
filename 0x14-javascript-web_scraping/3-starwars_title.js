#!/usr/bin/node

const request = require('request');

// Make a simple GET request
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  // console.log('code:', response && response.statusCode);
  const JS_object = JSON.parse(body);
  console.log(JS_object.title);
});
