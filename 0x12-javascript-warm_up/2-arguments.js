#!/usr/bin/node

const numArguements = process.argv.length - 2;

if (numArguements === 0) {
  console.log('No argument');
} else if (numArguements === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
