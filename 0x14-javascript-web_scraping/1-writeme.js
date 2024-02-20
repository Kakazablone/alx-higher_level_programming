#!/usr/bin/node

const fileSys = require('fs');

const argv = process.argv.slice(2);

fileSys.writeFile(argv[0], argv[1], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
