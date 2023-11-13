#!/usr/bin/node
function executeXTimes (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
function exampleFunction () {
  console.log('Executing!');
}
executeXTimes(3, exampleFunction);
