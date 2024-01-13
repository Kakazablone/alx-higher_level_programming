#!/usr/bin/node
/**
 * Print class Rectangle with width and height
 */

class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const value = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(value.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
