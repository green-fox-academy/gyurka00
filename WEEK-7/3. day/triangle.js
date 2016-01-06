'use strict';

function triangle (n) {
  for (var i = 1; i < n+1; i++) {
      console.log(' '.repeat(n - i) + '#'.repeat((2 * i) - 1));
  }
}
triangle(3);
console.log('\n\n');
triangle(84);
