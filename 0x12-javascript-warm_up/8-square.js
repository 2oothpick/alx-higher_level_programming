#!/usr/bin/node
let i = Number(process.argv[2]); //the size of the square goes here
if(isNaN(i)){
    console.log('Missing size');
} else {
    for (let x = 0; x < i; x++){  
        let itr = 'X';
        console.log(itr.padEnd(i, 'X'));
    }
}
