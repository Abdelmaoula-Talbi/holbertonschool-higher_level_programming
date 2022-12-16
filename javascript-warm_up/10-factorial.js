#!/usr/bin/node
function fact (a) {
  let result;
  if (a < 0) {
    result = -1;
  } else if (a === 0 || isNaN(a)) {
    result = 1;
  } else {
    result = a * fact(a - 1);
  }
  return result;
}
console.log(fact(process.argv[2]));
