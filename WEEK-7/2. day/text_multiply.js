'use strict';

function textMultiply(text,number) {
  var output = '';
  for (var i=0; i < number; i++) {
    output += text;
  }
  return output;
}

console.log(textMultiply('alma', 5));
