#!/usr/bin/node
// script that prints all characters of a Star Wars movie
// Display one character name by line in the same order
// and use the Star wars API
const request = require('request');
const endPoint = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(endPoint, function (err, response, body) {
  if (err) {
    throw err;
  } else if (response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request.get(character, function (err, response, body) {
        if (err) {
          throw err;
        } else if (response.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
