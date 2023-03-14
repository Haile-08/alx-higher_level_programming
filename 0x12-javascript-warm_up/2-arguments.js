#!/usr/bin/node
const num = process.argv.length;
if (num <= 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
