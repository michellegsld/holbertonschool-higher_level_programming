#!/usr/bin/node

var oldList = Object.values(require('./100-data'))[0];

console.log(oldList);
const newList = oldList.map((x, index) => (x * index));
console.log(newList);
