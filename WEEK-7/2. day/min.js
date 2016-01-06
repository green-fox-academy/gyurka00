'use strict';
var numbers = [7, 8, -1, 4, 3, 12];
var tmp = Infinity;
for (var i = 0; i < numbers.length; i++) {
  if (tmp > numbers[i]) {
    tmp = numbers[i];
  }
}
console.log(tmp);
