#!/usr/bin/node

//defining the fxn
callMeMoby = function (x, theFunction){
    for(let i = 0; i < x; i++) {
        theFunction();
    }
};

//making the fxn visible from outside
module.exports = {callMeMoby};