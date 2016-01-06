'use strict';

function Car(color, type, km) {
  this.color = color;
  this.type = type;
  this.km = km;
  this.ride = function (km) { this.km += km;}
}

var trabant = new Car('szurke', '1es', '2000000');

trabant.ride(400)
console.log(trabant.km);
