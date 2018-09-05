#!/usr/bin/node
exports.esrever = function (list) {
  let last = list.length - 1;
  let newArr = [];
  for (let i = last; i >= 0; i--) {
    newArr.push(list[i]);
  }
  return newArr;
};
