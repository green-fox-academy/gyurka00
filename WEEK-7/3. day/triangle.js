'use strict';

function triangle (n) {
  for (var i = 1; i < n+1; i++) {
      console.log(' '.repeat(n - i) + '#'.repeat((2 * i) - 1));
  }
}
triangle(3);
console.log('\n\n');
triangle(4);

//pasca triangle

function pascalTriangle(n) {
  var pascalArray = [[1]];
  if (n > 1) {
    for (var i = 1; i <= n-1; i++) {
        var line = [];
        line.push(1);
        for (var j = 1;j < pascalArray.length; j++) {
            line.push(pascalArray[i-1][j] + pascalArray[i-1][j-1])
        }
        line.push(1);
        pascalArray.push(line);
    }
  } else {console.log('invalid size');}
  console.log('\n');
  for (var i = 0; i < n; i++) {
      console.log(' '.repeat(n - i) + pascalArray[i]);
  }
}

pascalTriangle(10);
