#!/usr/bin/node
const fs = require('fs');

if (process.argv[2] && process.argv[3] && process.argv[4]) {
  fs.readFile(process.argv[2], (err, inputD) => {
    if (err) throw err;
    fs.readFile(process.argv[3], (err, inputD2) => {
      if (err) throw err;
      if (process.argv[4]) {
        fs.writeFile(process.argv[4], inputD.toString() + inputD2.toString(), (err, inputD3) => {
          if (err) throw err;
        });
      }
    });
  });
}
