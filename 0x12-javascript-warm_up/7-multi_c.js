#!/usr/bin/node
const argv = process.argv;
const string = 'C is fun';
if (!(isNaN(parseInt(argv[2], 10)))) { for (let i = 0; i < argv[2]; i++) { console.log(string); } } else { console.log('Missing number of occurrences'); }
