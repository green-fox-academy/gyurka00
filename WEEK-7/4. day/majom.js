'use strit';

console.log('Kaki');
var cim = document.querySelector('.majom');
console.log(cim);
//cim.style.backgroundColor = 'pink';
cim.classList.add('piros');
var majomKep = document.querySelector('img');
// majomKep.setAttribute('src','https://media.giphy.com/media/2u11zpzwyMTy8/giphy.gif');
function changeImg(object) {
  //var majomKep = document.querySelector('img');
  object.setAttribute('src','https://media.giphy.com/media/2u11zpzwyMTy8/giphy.gif');
  //var button = document.querySelector('button');
}
var body = document.querySelector('body');
function kepcsinalo(src) {
  var ujkep = document.createElement('img');
  ujkep.setAttribute('src',src);
  body.appendChild(ujkep);
 }
 //kepcsinalo('https://juno.hu/magazin/wp-content/uploads/2014/08/kecske06.jpg');
var kep = [
  'http://lorempixel.com/image_output/animals-q-c-250-250-1.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-3.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-6.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-2.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-4.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-8.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-7.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-5.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-9.jpg',
  'http://lorempixel.com/image_output/animals-q-c-250-250-10.jpg',
  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoTa7X_PmawGRcIKNqKtSRCAsQ9N7VR38req5b4YYsUnGi0xGyYAH8oA'
];
// for (var i = 0; i < 11; i++) {
//   kepcsinalo(kep[i]);
// }
kep.forEach(function(src) {
  kepcsinalo(src);
});
