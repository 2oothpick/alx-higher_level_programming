#!/usr/bin/node
const num = Number(process.argv[2]);

isNaN(num) ? console.log('Not a number') : console.log(`My number: ${num}`);
