#!/usr/bin/node

// The script that searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2).map(arg => parseInt(arg));

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);

  const secondLargest = args[1];
  console.log(secondLargest);
}
