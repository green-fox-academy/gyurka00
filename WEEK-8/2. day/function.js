'use strict';

// var button = document.querrySelector('button');
//
// button.addEventListener('click', shout);
//
// function shout() {
//   console.log('ajajajajajajajajaj');
//   console.log('ajajajajajajajajaj');
//   console.log('ajajajajajajajajaj');
//   console.log('ajajajajajajajajaj');
//   console.log('ajajajajajajajajaj');
//   console.log('ajajajajajajajajaj');
//   console.log('ajajajajajajajajaj');
//   console.log('ajajajajajajajajaj');
// }


var human = {
  word: ['kacsa', 'macsaka', 'mamlasz'],
  name: 'Tibi',
  speak: speak
}

function speak() {
  var _this = this;
  this.word.forEach(function(w) {
    console.log('I am ' + _this.name);
    console.log('bla-bla-bla ' + w)
  }
  );
}

human.speak();
