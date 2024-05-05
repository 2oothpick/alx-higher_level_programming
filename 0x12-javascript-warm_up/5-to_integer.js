#!/usr/bin/node
const num = Number(process.argv[2]);

isNaN(num[0]) ? console.log('Not a number') : console.log(`My number: ${num[0]}`);
