#!/usr/bin/node
// Grab a number from the command line then print a square

const count = parseInt(process.argv[2]);
const char = 'X';

if (typeof count === 'number' && isNaN(count) === false) {
  for (let i = 0; i < count; i++) {
    console.log(char.repeat(count)); // string.repeat() will repeat the string based on the number passed
  }
} else {
  console.log('Missing size');
}
