#!/usr/bin/node
// script that reads and prints the content of a file

const fileName = process.argv[2];
const fs = require('fs');
// Use fs.readFile() method to read the file
fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
