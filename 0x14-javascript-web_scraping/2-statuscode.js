#!/usr/bin/node
let url = process.argv[2]
let request = require('request');

request(url, (error, response) => {
  console.log('code: ' + response.statusCode);
});
