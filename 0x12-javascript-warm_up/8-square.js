#!/usr/bin/node
const argv = process.argv;
const size = parseInt(argv[2], 10);
const string = 'X';
if (!(isNaN(size))) {
  let sq = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      sq += string; }
    if (i < (size - 1)) {
      sq += '\n'; } }
  console.log(sq); }
else {
  console.log('Missing size'); }
