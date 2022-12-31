#!/usr/bin/node
let myArray = [];
if (process.argv.length <= 3){
    console.log(0);
} else {
    for (x = 2; process.argv[x] !== undefined; x++){       //takes arguments from CL and puts them ina useable array
        myArray.push(Number(process.argv[x]));             //converts arguments to numbers and concatenates to myArray                         
    }
    let sortedArray = myArray.sort();
    const secondBiggest = sortedArray.length - 2;    //index position of the second biggest value in sortedArray
    console.log(sortedArray[secondBiggest]);
}
