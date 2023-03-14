#!/usr/bin/node
const argv = process.argv;
if (isNaN(parseInt(argv[2], 10))) {
  console.log(0);
} else if (!(parseInt(argv[3], 10))) {
  console.log(0);
} else {
  let maxElement2 = 0;
  maxElement2 = argv.sort((a, b) => b - a)[3];
  console.log(maxElement2);
}
