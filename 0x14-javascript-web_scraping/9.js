#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, function (err, response) {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(response.body).characters;
  const dict = {};
  characters.forEach((character) => {
    dict[character] = req(character);
  });
  console.log(dict);
});

function req (character) {
  request(character, function (err, response) {
    sleep(9000);
    if (!err) {
      console.log((JSON.parse(response.body).name));
      return (JSON.parse(response.body).name);
    }
  });
}

function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}
