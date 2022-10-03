#!/usr/bin/node
const process = require('process');
const num = parseInt(process.argv[2]);
let i = 0;
let str = '';

if (!num) {
  console.log('Missing size');
} else {
  for (i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      str += 'X';
    }
    console.log(str);
    str = '';
  }
}
