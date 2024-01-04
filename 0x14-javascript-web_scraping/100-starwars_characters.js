#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + (process.argv[2]);
request(url, 'utf8', (error, response, body) => {
  if (error) throw error;
  else {
    for (const i of JSON.parse(body).characters) {
      request(i, 'utf8', (error, response, body) => {
        if (error) throw error;
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
