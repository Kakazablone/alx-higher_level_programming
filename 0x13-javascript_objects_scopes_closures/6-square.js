#!/usr/bin/node
/**
 * Create an instance method called charPrint(c) that prints the rectangle using the character c
 * If c is undefined, use the character X
 */

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
