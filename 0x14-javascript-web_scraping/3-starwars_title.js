#!/usr/bin/node
// script that prints the title of a Star Wars movie where
// the episode number matches a given integer

const request = require('request');
const movieId = process.argv[2];
const route = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(route, (err, res, body) => {
  if (err) throw err;
  // Display the retrieved content
  console.log(JSON.parse(body).title);
});
