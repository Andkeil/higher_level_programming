#!/usr/bin/node
exports.esrever = function (list) {
  var last = list.length - 1;
  let new_arr = []
  for (let i = last; i >= 0; i--) {
    new_arr.push(list[i]);
    }
  return new_arr;
};
