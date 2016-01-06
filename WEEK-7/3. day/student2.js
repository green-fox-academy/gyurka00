'use stict';

function Student (){
  this.grades = {};
  this.addGrade = addGrade;
  this.getCount = getCount;
  this.getAverage = getAverage;
  this.getAverageBySubject = getAverageBySubject;
}

function addGrade(subject, grade) {
  if(this.grades[subject] === undefined){
    this.grades[subject] = [];
    this.grades[subject].push(grade);
  } else {
    this.grades[subject].push(grade);
  }
}
function getCount() {
  for(var subject in this.grades) {
    console.log(subject, ':', this.grades[subject].length);
  }
}

function getAverage() {
  var averages = [];
  for(var subject in this.grades) {
    var subject = this.grades[subject]
    averages.push(subject.reduce(function(acc, num) {
      return acc + num;
    }) / subject.length);
  }
  console.log(averages.reduce(function(acc, num) {
    return acc + num;
  }) / averages.length);
}


function getAverageBySubject() {
  for(var i in this.grades) {
    var subject = this.grades[i]
    console.log(i, ':', subject.reduce(function(acc, num) {
      return acc + num;
    }) / subject.length);
  }
}

var dezso = new Student();

dezso.addGrade('matek',5);
dezso.addGrade('matek',4);
dezso.addGrade('rajz',3);
dezso.addGrade('rajz',2);

console.log(dezso.grades);
dezso.getCount();
dezso.getAverage();
dezso.getAverageBySubject();
