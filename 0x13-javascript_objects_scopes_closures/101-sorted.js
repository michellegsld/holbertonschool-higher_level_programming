#!/usr/bin/node

const objReq = require('./101-data');

const oldDic = Object.values(objReq)[0];
console.log(oldDic);

var newDic = {};

for (const [key, value] of Object.entries(oldDic)) {
  if (!(value in newDic))
    newDic[value] = [];
  newDic[value].push(key);
}

console.log(newDic);
