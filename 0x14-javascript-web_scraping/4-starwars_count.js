#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const f = JSON.parse(body);
    for (let i = 0; i < f.results.length; i++) {
      // console.log(i)
      const characterList = f.results[i].characters;
      // const characterId = 'https://swapi-api.alx-tools.com/api/people/18/';
      for (const x of characterList) {
        // console.log(x)
        if (x.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
