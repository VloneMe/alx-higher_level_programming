#!/usr/bin/node

// The script that prints the addition of 2 integers.

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const passVar = add(process.argv[2], process.argv[3]);
console.log(passVar);
