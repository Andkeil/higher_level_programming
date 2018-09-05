#!/usr/bin/node
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');

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
