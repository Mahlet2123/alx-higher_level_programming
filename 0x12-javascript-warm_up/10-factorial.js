#!/usr/bin/node
const argv = process.argv;
const number = parseInt(argv[2], 10);

function factorial (a) {
  if (isNaN(a)) {
    return (1);
  } if (a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
const result = factorial(number);
console.log(result);
