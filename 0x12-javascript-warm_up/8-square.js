#!/usr/bin/node
const argc = process.argv[2];
if (isNaN(Number(argc))) {
  console.log('Missing size');
} else if (argc >= 0) {
  for (let i = 0; i < argc; i++) {
    let m = '';
    for (let j = 0; j < argc; j++) {
      m = m + 'X';
    }
    console.log(m);
  }
}
