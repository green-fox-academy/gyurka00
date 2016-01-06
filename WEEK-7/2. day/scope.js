'use strict';

var g = 123;

function printG() {
  console.log(g);
  g = 333;
}

printG();
console.log(g);

function printLocalG() {
  var g = 7;
  console.log(g);
}

printLocalG();
printG();

function printA() {
  var a = 112322;
  console.log(a);
}

printA();
console.log(a);
