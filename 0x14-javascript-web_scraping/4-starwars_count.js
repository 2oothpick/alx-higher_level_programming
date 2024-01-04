#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const info = JSON.parse(body);
    const movies = info.results;
    for (let i = 0; i < movies.length; i++) {
      if (movies[i].characters) {
        for (const j of movies[i].characters) {
          if (j.includes('18')) {
            count++;
          }
        }
      }
    }
    console.log(count);
  }
});
