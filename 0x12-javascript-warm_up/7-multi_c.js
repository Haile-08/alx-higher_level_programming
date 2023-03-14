#!/usr/bin/node
const argc = process.argv[2];
if (argc > 0) {
  for (let i = 0; i < argc; i++) {
    console.log('C is fun');
  }
} else if (process.argv.length <= 2) {
  console.log('Missing number of occurrences');
}
