#!/usr/bin/node
let list = require('./100-data').list;
let newList = [];
newList = list.map((v, i) => {
  return v * i;
});
console.log(list);
console.log(newList);
