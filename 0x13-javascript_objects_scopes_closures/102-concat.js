#!/usr/bin/node
const fs = require('fs');

function readF(fileName) {
	if (fileName) {
	fs.readFile(fileName, (err, inputD) => {
		if (err) throw err;
		console.log(inputD.toString());
		if (process.argv[4]){
			fs.writeFile(process.argv[4], inputD.toString(), (err, inputD) => {
				if (err) throw err;
				//console.log((fileA + fileB).toString());
			 })
		}
		return (inputD.toString());
	 }) }


}

const fileA = readF(process.argv[2]);
const fileB = readF(process.argv[3]);
console.log(fileA);

/*
if (process.argv[4]){
	fs.writeFile(process.argv[4], (fileA + fileB).toString(), (err, inputD) => {
		if (err) throw err;
		//console.log((fileA + fileB).toString());
	 })
}
*/

