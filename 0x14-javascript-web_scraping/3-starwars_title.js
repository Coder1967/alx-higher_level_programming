#!/usr/bin/node
const request = require('request');
let jsonString = '';
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (err, res, data) {
  if (err) {
    console.log(err);
  }
  jsonString = JSON.parse(data);
  console.log(jsonString.title);
});
