#!/usr/bin/node
const argv = process.argv;
function add (a, b) {
  a = parseInt(argv[2], 10); b = parseInt(argv[3], 10);
  console.log(a + b);
} add();
