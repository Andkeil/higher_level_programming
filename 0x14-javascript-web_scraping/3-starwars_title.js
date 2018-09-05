#!/usr/bin/node
let epNum = process.argv[2];
let url = 'http://swapi.co/api/films/';
let request = require('request');

request(url + epNum, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
