#!/usr/bin/node
function add(a, b) {
  return a + b;
}
const [arg1, arg2] = process.argv.slice(2);
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);
if (!isNaN(num1) && !isNaN(num2)) {
  console.log(`The addition of ${num1} and ${num2} is: ${add(num1, num2)}`);
} else {
  console.log("Invalid input. Please provide two integers.");
}