#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);

function factorial (a) {
  if (a === 1) {
    return 1;
  }
  return a * factorial(a - 1);
}

if (!num) {
  console.log(1);
} else {
  console.log(factorial(num));
}
