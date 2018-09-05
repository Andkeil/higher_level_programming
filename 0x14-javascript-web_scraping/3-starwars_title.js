#!/usr/bin/node
const epNum = process.argv[2];
const url = 'http://swapi.co/api/films/';
const request = require('request');

request(url + epNum, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
