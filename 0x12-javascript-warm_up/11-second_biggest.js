#!/usr/bin/node
const process = require('process');
let [check, tmp] = [0, 0];
const arr = [];
if (process.argv.length === 3 || process.argv.length === 2) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }

  while (true) {
    check = 0;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] <= arr[i + 1]) {
        tmp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = tmp;
        check = 1;
      }
    }
    if (check === 0) {
      break;
    }
  }
  console.log(arr[1]);
}
