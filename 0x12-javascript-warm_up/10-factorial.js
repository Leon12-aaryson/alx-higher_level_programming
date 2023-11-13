#!/usr/bin/node
function factorial(n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
const [arg1] = process.argv.slice(2);
const num = parseInt(arg1);
console.log(`The factorial of ${num} is: ${factorial(num)}`);
