#!/usr/bin/node
/*
 * Write a script that computes the number of tasks completed by user id.
 * 1. The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * 2. Only print users and number of completed task
 * 3. You must use the module request
 */
const request = require('request');
const url1 = process.argv[2] + '?completed=true';
let data = [];
const myObj = {};
let i = 1;
let currentUser = 1;

request(url1, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  data = JSON.parse(body);
  data.forEach(function (value) {
    if (currentUser !== value.userId) {
      i = 1;
      currentUser += 1;
    }
    myObj[value.userId] = i;
    i += 1;
  });
  console.log(myObj);
});
