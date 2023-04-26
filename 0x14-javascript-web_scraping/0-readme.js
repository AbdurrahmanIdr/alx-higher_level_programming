#!/usr/bin/node
// interact with a file
// print out the text in utf8
// print error if error

const arg = process.argv;
const fs = require('fs');

fs.readFile(arg[2], 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
