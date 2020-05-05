#!/usr/bin/node
function swap (arr, left, right) {
  const temp = arr[left];
  arr[left] = arr[right];
  arr[right] = temp;
}

function sort (arr, len) {
  for (let i = 0; i < len; i++) {
    for (let j = 0, stp = len - i; j < stp; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1);
      }
    }
  }
  return arr;
}

if (isNaN(parseInt(process.argv[2])) || isNaN(parseInt(process.argv[3]))) {
    console.log(0);
  } else {
  let arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  arr = sort(arr, process.argv.length - 2);
  console.log(arr[process.argv.length - 4]);
  }
