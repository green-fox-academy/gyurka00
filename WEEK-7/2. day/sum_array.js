'use strict';

function sumArray(array){
  var sum = 0;
  for (var i =0; i < array.length; i++) {
    sum += array[i];
  }
  return sum;
}

console.log(sumArray([1,2]));
