#!/usr/bin/node
const [, , ...args] = process.argv;
const numbers = args.map(Number).filter(num => !isNaN(num));
const numArgs = numbers.length;
if (numArgs <= 1) {
  console.log(0);
} else {
  const secondBiggest = numbers.sort((a, b) => b - a)[1];
  console.log(secondBiggest);
}
