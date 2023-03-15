#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    let print = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        print += c;
      }
      if (i < (this.height - 1)) {
        print += '\n';
      }
    }
    console.log(print);
  }
}
module.exports = Square;
