#!/usr/bin/node
const Square_ = require('./5-square');

class Square extends Square_ {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let s = '';
        for (let i = 0; i < this.height; i++) {
          s += c;
        }
        console.log(s);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
