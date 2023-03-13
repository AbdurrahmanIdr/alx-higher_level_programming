#!/usr/bin/node

const arg = process.argv;
const len = arg.length;
function secondlarge (l, array) {
  if (l < 4) {
    return (0);
  }
  array.splice(0, 2);
  const num = Math.max(...array);
  const strint = num.toString();
  let large = array.indexOf(strint);
  array.splice(large, 1);
  large = Math.max(...array);
  return (large);
}
console.log(secondlarge(len, arg));
