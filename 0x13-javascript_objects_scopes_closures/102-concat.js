#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], (err, inputD) => {
  if (err) throw err;
  fs.readFile(process.argv[3], (err, inputD2) => {
    if (err) throw err;
    if (process.argv[4]) {
      fs.writeFile(process.argv[4], inputD.toString() + '\n' + inputD2.toString() + '\n', (err, inputD3) => {
        if (err) throw err;
      });
    }
  });
});
