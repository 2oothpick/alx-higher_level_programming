#!/usr/bin/node
const {argv} = require('process');    //importing the in_built process.argv module
let x = Number(argv[2]);
if (isNaN(x)){
    console.log("Missing number of occurrences");
} else {
    while( x > 0){
        console.log("C is fun");
        x--;
    }
}