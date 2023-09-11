#!/usr/bin/node

// The script that prints a message depending of the number of arguments passed.

const myVar = process.argv[2];

if (myVar === undefined){
	console.log('No argument');
} else if ( myVar === 1){
	console.log('Argument found');
}else {
	console.log('Arguments found');
};
