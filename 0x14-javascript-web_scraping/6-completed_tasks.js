#!/usr/bin/node
// count number of completed task
// code written by me gangan

const request = require('request');

request(process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  const dict = {};
  const allbdy = JSON.parse(response.body);
  for (let i = 0; i < allbdy.length; i++) {
    if (allbdy[i].userId in dict) {
      if (allbdy[i].completed === true) {
        const key = allbdy[i].userId;
        dict[key] = dict[key] + 1;
      }
    } else {
      const key = allbdy[i].userId;
      if (allbdy[i].completed === true) {
        dict[key] = 1;
      }
    }
  }
  console.log(dict);
}
);
