#!/usr/bin/node
/*
 * Write a script that gets the contents of a webpage and stores it in a file.
 * 1. The first argument is the URL to request
 * 2. The second argument the file path to store the body response
 * 3. The file must be UTF-8 encoded
 * 4. You must use the module request
 * */
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    }
  }
  );
});
