#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + (process.argv[2]), (error, response, body) => {
  if (error) throw error;
  else {
    send(JSON.parse(body).characters, 0);
  }
});

function send (person, vim) {
  if (vim >= person.length) {
    return;
  }
  request(person[vim], (error, response, body) => {
    if (error) throw error;
    else {
      console.log(JSON.parse(body).name);
      return send(person, ++vim);
    }
  });
}
