#!/usr/bin/node

const fileSys = require('fs');
const filename = process.argv[2];

fileSys.readFile(filename, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
