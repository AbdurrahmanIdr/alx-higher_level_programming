#!/usr/bin/node
// script that writes a string to a file
// content of the file must be written in utf-8
const fs = require('fs');
const fileName = process.argv[2];
const content = process.argv[3];

fs.writeFile(fileName, content, 'utf8', (err) => {
  if (err) throw err;
});
