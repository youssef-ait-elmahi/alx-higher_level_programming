#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(Number);

if (numbers.length <= 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let secondMax = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max) {
      secondMax = max;
      max = numbers[i];
    } else if (numbers[i] > secondMax && numbers[i] < max) {
      secondMax = numbers[i];
    }
  }

  console.log(secondMax);
}
