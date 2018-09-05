#!/usr/bin/node
let url = process.argv[2];
let request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let allTask = JSON.parse(body);
    let doneTask = {};
    for (let i in allTask) {
      let user = allTask[i]['userId'];
      if (allTask[i]['completed'] === true) {
        if (doneTask[user] === undefined) {
          doneTask[user] = 1;
        } else {
          doneTask[user] += 1;
        }
      }
    }
    console.log(doneTask);
  }
});
