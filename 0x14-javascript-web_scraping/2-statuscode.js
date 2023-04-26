#!/usr/bin/node
// script that display the status code of a GET request
// The status code must be printed like this: code: <status code>

const request = require('request');
const route = process.argv[2];

request(route, (err, res, body) => {
  if (!err) console.log('code:', res.statusCode);
});
