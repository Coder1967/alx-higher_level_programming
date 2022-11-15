#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (err, res, data) {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
