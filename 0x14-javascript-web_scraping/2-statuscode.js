#!/usr/bin/node

const request = require('request');

const argv = process.argv.slice(2);
const url = argv[0];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
