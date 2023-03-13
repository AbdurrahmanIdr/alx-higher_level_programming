#!/usr/bin/node

const arg = process.argv;
const int1 = parseInt(arg[2]);
const int2 = parseInt(arg[3]);
function add (a, b) {
  return (a + b);
}
console.log(add(int1, int2));
