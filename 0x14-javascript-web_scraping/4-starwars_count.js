#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const whlbdy = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < whlbdy.length; i++) {
    for (let j = 0; j < whlbdy[i].characters.length; j++) {
      if (whlbdy[i].characters[j].endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
