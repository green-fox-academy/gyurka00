'use strict';

function Student (){
  this.grade = [];
  this.addGrade = function (grade) { this.grade.push(grade);}
  // this.getAverage = function() {
  //   var sum = 0;
  //   this.grade.forEach(function(grade){
  //     sum += grade
  //   });
  //   return sum / this.grade.length;
  // }
  this.getAverage = function () {
    var sum = this.grade.reduce(function (acc,num) {
      return acc += num;
    },0);
    return sum / this.grade.length;
  }
}

var jozsi = new Student ();
jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(2);
console.log(jozsi.getAverage());
