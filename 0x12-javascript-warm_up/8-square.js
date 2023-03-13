#!/usr/bin/node

let arg = 'X';
const arrg = process.argv;
const step = parseInt(arrg[2]);
if (isNaN(step)) {
  console.log('Missing size');
} else {
  for (let xxx = 1; xxx < step; xxx++) {
    arg += 'X';
  }
  for (let start = 0; start < step; start++) {
    console.log(arg);
  }
}
