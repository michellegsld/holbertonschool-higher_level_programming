#!/usr/bin/node

const objList = require('./100-data');

const oldList = Object.values(objList)[0];
console.log(oldList);

const newList = oldList.map((x, index) => (x * index));
console.log(newList);
