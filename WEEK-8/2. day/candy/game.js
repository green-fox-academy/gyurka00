'use strict';

var candysCounter = 100;
var lollipopCounter = 180;
var speed = 0;

var candiesNumber = document.querySelector('.candiesNumber');
var candyButton = document.querySelector('.candyButton');
var lollipopButton = document.querySelector('.lollipopButton');
var lollipopsNumber = document.querySelector('.lollipopsNumber');
var candiesPerSec = document.querySelector('.speed');

candyButton.addEventListener('click', function() {
  addCandy(1);
});

function addCandy(number) {
  candysCounter += number;
  candiesNumber.innerText = candysCounter;
}

lollipopButton.addEventListener('click', function() {
  if (candysCounter >= 10) {
    lollipopCounter++;
    candysCounter -= 10;
    candiesNumber.innerText = candysCounter;
    lollipopsNumber.innerText = lollipopCounter;
  }
});

setInterval(function() {
  if (lollipopCounter >= 10) {
    speed = Math.floor(lollipopCounter/10);
    candiesPerSec.innerText = speed;
  addCandy(speed);
  }
}, 1000);
