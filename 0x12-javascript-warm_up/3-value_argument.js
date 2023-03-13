#!/usr/bin/node
const len = process.argv.length;
const argv = process.argv;
if (len <= 2) {
  console.log('No argument');
} else if (len >= 3) {
  console.log(argv[2]);
}
