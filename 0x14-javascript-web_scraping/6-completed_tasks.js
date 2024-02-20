#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    const donetasks = {};
    const todos = JSON.parse(body);
    for (const task in todos) {
      if (todos[task].completed === true) {
        if (donetasks[todos[task].userId]) donetasks[todos[task].userId]++;
        else donetasks[todos[task].userId] = 1;
      }
    }
    console.log(donetasks);
  }
});
