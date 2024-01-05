#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];
const fs = require('fs');

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
