#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    let donetasks = {};
    let todos = JSON.parse(body);
    for (let task in todos) {
      if (todos[task].completed === true) {
        if (donetasks[todos[task].userId]) donetasks[todos[task].userId]++;
        else donetasks[todos[task].userId] = 1;
      }
    }
    console.log(donetasks);
  }
});
