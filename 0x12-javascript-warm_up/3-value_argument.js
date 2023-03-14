#!/usr/bin/node
let argc = 0;
process.argv.forEach((val, index) => {
  argc = argc + 1;
});
if (argc > 2) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
