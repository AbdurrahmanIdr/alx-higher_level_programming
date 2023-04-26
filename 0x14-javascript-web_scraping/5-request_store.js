#!/usr/bin/node
// script that gets the contents of a webpage
// and stores it in a file
const request = require('request');
const fs = require('fs');
const route = process.argv[2];
const fileName = process.argv[3];

request(route, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileName, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
