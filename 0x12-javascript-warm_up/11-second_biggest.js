#!/usr/bin/node
const argc = process.argv.length;
if (argc <= 3) {
  console.log('0');
} else {
  if (process.argv[2] < process.argv[3]) {
    console.log(process.argv[3]);
  } else {
    console.log(process.argv[2]);
  }
}
