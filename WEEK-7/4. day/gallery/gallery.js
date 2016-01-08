'use strict';
var pictures = [
  'pic/0.jpg',
  'pic/1.jpg',
  'pic/2.jpg',
  'pic/3.jpg',
  'pic/4.jpg',
  'pic/5.jpg',
  'pic/6.jpg',
  'pic/7.jpg'
];

var currentPosition = 0;


//create Thumbnails
for (var i = 0; i < pictures.length; i++) {
  var picture = document.createElement('img');
  picture.setAttribute('src', pictures[i] );
  picture.setAttribute('id', 'pic' + i );
  document.querySelector('.thumbnails').appendChild(picture);
}
selectedThumbnails();

function selectedThumbnails() {
  // var picture = document.getElementById(pic0);
  document.getElementById('pic' + currentPosition).classList.add('selected');
}

function reselectedThumbnails() {
  document.getElementById('pic' + currentPosition).classList.remove('selected');
}

document.querySelector('.thumbnails').addEventListener('click', function(event) {
  var src = event.target.getAttribute('src');
  var id = event.target.getAttribute('id');
  if (src) {
    setBigPic(src);
    console.log(src);
    console.log(id.substring(3));
    setCurrentPosition(Number(id.substring(3)));
  }
});

function setBigPic(source) {
  document.querySelector('.bigPic').setAttribute('src', source);
}

function setCurrentPosition(num) {
  reselectedThumbnails();
  currentPosition = num;
  console.log('currentPosition:', currentPosition);
  selectedThumbnails();
}

document.querySelector('.left').addEventListener("click", function() {
  previousPic();
});

function previousPic(){
    if (currentPosition === 0) {
      setCurrentPosition(7);
      setBigPic(pictures[currentPosition]);
    } else {
      setCurrentPosition(currentPosition-1);
      setBigPic(pictures[currentPosition]);
    }
}

document.querySelector('.right').addEventListener("click", function() { nextPic();});

function nextPic(){
    if (currentPosition === 7) {
      setCurrentPosition(0);
      setBigPic(pictures[currentPosition]);
    } else {
      setCurrentPosition(currentPosition+1);
      setBigPic(pictures[currentPosition]);
    }
}

document.addEventListener("keypress", keyEventHandler);
function keyEventHandler(e) {
    var keyCode = e.keyCode;
    if(keyCode == 112) {
        previousPic();
    } else if (keyCode == 32) {
      nextPic();
    }
};
