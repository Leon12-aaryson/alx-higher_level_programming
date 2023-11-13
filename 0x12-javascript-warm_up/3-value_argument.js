#!/usr/bin/node
let numArguments = 0;
for (let i = 2; process.argv[i]; i++) {
  numArguments++;
}

switch (numArguments) {
  case 0:
    console.log("No argument");
    break;
  case 1:
    console.log("Argument found");
    break;
  default:
    console.log("Arguments found");
    break;
}
