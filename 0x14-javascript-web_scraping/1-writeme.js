#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];

fs.writeFile(filename, process.argv[3], 'utf-8', (err, content) => {
  if (err) throw err;
});
