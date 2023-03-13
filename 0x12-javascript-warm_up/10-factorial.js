#!/usr/bin/node

const arg = process.argv;
const num = parseInt(arg[2]);
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(num));
