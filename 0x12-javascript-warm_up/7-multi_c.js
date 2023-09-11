#!/usr/bin/node

// The script that prints x times “C is fun”

const numOccur = parseInt(process.argv[2]);

if (!isNaN(numOccur)) {
  for (let i = 0; i < numOccur; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
