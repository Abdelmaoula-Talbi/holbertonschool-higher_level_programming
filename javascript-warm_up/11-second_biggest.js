#!/usr/bin/node
function biggest (array) {
  array.shift();
  array.shift();
  for (let m = 0; m < (array.length - 1); m++) {
    for (let i = 0; i < (array.length - m - 1); i++) {
      if (Number(array[i]) > Number(array[i + 1])) {
        const temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
  console.log(array[(array.length - 2)]);
}
const args = process.argv;
if (args.length < 4) {
  console.log('0');
} else {
  biggest(args);
}
