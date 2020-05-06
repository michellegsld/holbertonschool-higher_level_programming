#!/usr/bin/node
exports.addMeMaybe = function (x, theFunction) {
  return x + theFunction(x + 1);
};
