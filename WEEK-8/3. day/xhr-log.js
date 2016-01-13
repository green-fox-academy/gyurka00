'use strict';

var ACCESS_TOKEN = 'JNDzfN0Pz8mshV6DHISeFTRHJy00p1LvLoKjsnSUpz0krIeYGX';





//probaRequest.open('GET', urlWithParams);



function createRequest (url, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
  probaRequest.setRequestHeader('X-Mashape-Key', ACCESS_TOKEN);
  probaRequest.send();
  probaRequest.onreadystatechange = function () {
    console.log('allapot:', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}


var yodeButton = document.querySelector('.yoda-button');
var yodeInput = document.querySelector('.yoda-input');
var responseContainer = document.querySelector('.yoda-response');

function onDone(response) {
  console.log('valasz:', response);
  responseContainer.innerText = response;
}

yodeButton.addEventListener('click', function () {
  var url = 'https://yoda.p.mashape.com/yoda';
  var mondat = yodeInput.value;
  var urlWithParams = url + '?sentence=' + encodeURIComponent(mondat);
  console.log(encodeURIComponent(mondat));
  responseContainer.innerText = 'loading';
  createRequest(urlWithParams, onDone);
});
