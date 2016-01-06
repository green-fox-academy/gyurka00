'use strict';

function reverse(string) {
  var output = '';
  for (var i = string.length-1; i > -1; i--) {
    output += string[i];
  }
  return output;
}

console.log(reverse('LILLA'));


function recReverse(input, i) {
  if (i < 0) {
    return '';
  } else {
    return input[i] + recReverse(input, i-1);
  }
}
console.log(recReverse('Kacsa', 4));
