#!/usr/bin/node
let url = process.argv[2];
let request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let wedgeCount = 0;
    let movieList = JSON.parse(body).results;
    for (let movie in movieList) {
      let characterList = movieList[movie].characters;
      for (let id in characterList) {
        if (characterList[id].includes('18')) {
          wedgeCount += 1;
        }
      }
    }
    console.log(wedgeCount);
  }
});
