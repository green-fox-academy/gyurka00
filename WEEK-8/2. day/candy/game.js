'use strict';

function Candy() {
  this.candysCounter = 0;
  this.lollipopCounter = 0;
  this.speed = 0;
  this.candiesNumber = document.querySelector('.candiesNumber');
  this.candyButton = document.querySelector('.candyButton');
  this.lollipopButton = document.querySelector('.lollipopButton');
  this.lollipopsNumber = document.querySelector('.lollipopsNumber');
  this.candiesPerSec = document.querySelector('.speed');
  this.addCandy = addCandy;

  var _this = this;

  this.candyButton.addEventListener('click', function() {
    _this.addCandy(1);
  });

  this.lollipopButton.addEventListener('click', function() {
    if (_this.candysCounter >= 10) {
      _this.lollipopCounter++;
      _this.candysCounter -= 10;
      _this.candiesNumber.innerText = _this.candysCounter;
      _this.lollipopsNumber.innerText = _this.lollipopCounter;
    }
  });

  setInterval(function() {
    if (_this.lollipopCounter >= 10) {
      _this.speed = Math.floor(_this.lollipopCounter/10);
      _this.candiesPerSec.innerText = _this.speed;
    _this.addCandy(_this.speed);
    }
  }, 1000);
};

function addCandy(number) {
  this.candysCounter += number;
  this.candiesNumber.innerText = this.candysCounter;
}

var candy = new Candy();
