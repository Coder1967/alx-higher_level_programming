#!/usr/bin/node
/*
 * Write a script that computes the number of tasks completed by user id.
 * 1. The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * 2. Only print users and number of completed task
 * 3. You must use the module request
 */
const request = require('request');
let data = [];
let myObj = {};
let i = 1;
let currentUser = 1;

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  data = JSON.parse(body);
  data.forEach(function (value) {
    if (currentUser !== value.userId) {
      i = 1;
      currentUser += 1;
    }
	  if (value.completed == true)
	  {
		   myObj[value.userId] = i;
		  i += 1;
	  }
  });
  console.log(myObj);
});
