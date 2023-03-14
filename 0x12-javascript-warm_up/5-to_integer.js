#!/usr/bin/node
const argc = process.argv[2];
if (isNaN(argc) || argc === '') {
  console.log('Not a number');
} else {
  console.log('My number: ' + (Number.isInteger(argc) ? Number(argc) : parseInt(argc)));
}
