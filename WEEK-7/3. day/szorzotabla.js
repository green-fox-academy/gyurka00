'use strict';
function szorzotabla(){

  for (var i = 1; i < 11; i++) {
    for (var j = 1; j < 11; j++ ){
      console.log(i + ' x ' + j + ' = ' + i*j);
    }
    console.log('\n');
  }
}

szorzotabla();

console.log('rekurzivan:\n');

function szorzotabla2(num, pos){
  if (num < 11) {
    if (pos < 11) {
      console.log(num + ' x ' + pos + ' = ' + num*pos);
      pos++;
      szorzotabla(num,pos);
    } else {
      num++;
      pos = 1;
      console.log('\n');
      szorzotabla(num,pos);
    }
  }
}

szorzotabla2(1,1);

var szorzotabla3 = '';

for (var i = 1; i <=10; i++) {
  szorzotabla3 += i + 'x' + 3 + '=' + i*3 + '\n';
}
console.log(szorzotabla3);
var szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var szorzotabla4 = '';
szamok.forEach(function (e) {
  szorzotabla4 += e + 'x' + 4 + '=' + e*4 + '\n';
})
console.log(szorzotabla4);

var szorzotabla5 = '';
var sorok = szamok.map(function (e) {
  return e + 'x' + 5 + '=' + e*5;
});
szorzotabla5 = sorok.join('\n');
console.log(szorzotabla5);
