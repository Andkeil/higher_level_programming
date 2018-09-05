#!/usr/bin/node
let fs = require('fs');
let url = process.argv[2];
let filePath = process.argv[3];
let request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
