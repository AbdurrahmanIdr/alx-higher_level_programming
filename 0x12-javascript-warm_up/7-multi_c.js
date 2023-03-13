#!/usr/bin/node

const arg = 'C is fun';
const arrg = process.argv;
const step = parseInt(arrg[2]);
if (isNaN(step)) {
  console.log('Missing number of occurrences');
} else {
  for (let start = 0; start < step; start++) {
    console.log(arg);
  }
}
