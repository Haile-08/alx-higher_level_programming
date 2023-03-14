#!/usr/bin/node
const argc = process.argv.length;
if (argc <= 1) {
  console.log('undefined is undefined');
} else if (argc === 2) {
  console.log(process.argv[2] + ' is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
