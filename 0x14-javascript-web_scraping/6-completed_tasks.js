#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const t in tasks) {
      if (tasks[t].completed === true) {
        if (completed[tasks[t].userId]) completed[tasks[t].userId]++;
        else completed[tasks[t].userId] = 1;
      }
    }
    console.log(completed);
  }
});
