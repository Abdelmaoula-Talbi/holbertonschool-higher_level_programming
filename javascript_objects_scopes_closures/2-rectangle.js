#!/usr/bin/node
module.exports = class Rectangle {
  if (w <= 0 || h <= 0) {
    return {}
  } else {
    constructor (w, h) {
      this.width = w;
      this.height = h;
    }
  }
};
