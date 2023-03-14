#!/usr/bin/node
const argc = process.argv.length;

if (argc <= 2) {
  console.log('No argument');
} else {
  console.log('Argument' + (argc > 3 ? 's' : '') + ' found');
}
