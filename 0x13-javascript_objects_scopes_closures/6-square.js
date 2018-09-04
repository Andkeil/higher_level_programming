#!/usr/bin/node
const SuperSquare = require('./5-square');
module.exports = class Square extends SuperSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let sqr = '';
      for (let j = 0; j < this.width; j++) {
        sqr += c;
      }
      console.log(sqr);
    }
  }
};
