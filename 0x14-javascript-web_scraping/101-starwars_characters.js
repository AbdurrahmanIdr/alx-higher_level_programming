#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response) {
  if (!err) {
    const charlist = JSON.parse(response.body).characters;
    console.log(charlist);
    let i = 0;
    while (i < charlist.length) {
      now(charlist[i], i);
    }
  }
});

async function now (urlfun, count) {
  request.get(urlfun, function (error, response) {
    if (!error) {
      const people = JSON.parse(response.body).name;
      console.log(people);
    }
  });
  await sleep(5000);
  console.log('wait over');
  count++;
}

async function sleep (ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
