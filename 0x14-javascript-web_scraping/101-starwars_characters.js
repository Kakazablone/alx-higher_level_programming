#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters);
  }
});

const printCharacters = (characters, index = 0) => {
  if (index < characters.length) {
    request(characters[index], (error, response, body) => {
      if (!error) {
        console.log(JSON.parse(body).name);
        printCharacters(characters, index + 1);
      }
    });
  }
};
