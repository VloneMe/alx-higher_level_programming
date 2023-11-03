#!/usr/bin/node
// A script that writes a string to a file.

const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  console.error('Please provide a file path and content as arguments');
  process.exit(1);
}

fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('File content has been written successfully.');
  }
});
