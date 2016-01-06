'use strict';

var kids = [
  {name: 'Tihi', candies: 2},
  {name: 'Steve', candies: 3},
  {name: 'Agoston', candies: 0},
  {name: 'Julika', candies: 5},
  {name: 'Krisztian', candies: 4}
];

function getRichestKidsName(kids) {
  var   rich = kids.reduce(function(curr,prev){
    // if (curr.candies > prev.candies) {
    //   return curr;
    // } else {
    //   return prev;
    // }
    return curr.candies > prev.candies ? curr :prev;
  });
  return rich.name;
}

console.log(getRichestKidsName(kids));
