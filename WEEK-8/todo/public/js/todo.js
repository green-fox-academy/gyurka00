'use strict';

function createGET (url, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
  probaRequest.send();
  probaRequest.onreadystatechange = function () {
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

function createPOST (url, textMes, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('POST', url);
  probaRequest.setRequestHeader('Content-Type','application/json');
  probaRequest.send(JSON.stringify({text: textMes}));
  probaRequest.onreadystatechange = function () {
    if (probaRequest.readyState === 4) {
      callback(url, todoCallback);
    }
  };
}

function createPUT (url, textMes, completedStatus) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('PUT', url);
  probaRequest.setRequestHeader('Content-Type','application/json');
  probaRequest.send(JSON.stringify({text: textMes, completed: completedStatus}));
}

function createDELETE (url) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('DELETE', url);
  probaRequest.send();
}

var todoContainer = document.querySelector('.todo-container');

var todoCallback = function (response) {
  var todoArray = JSON.parse(response);
  todoContainer.innerHTML = '';
  todoArray.forEach(function (todoItem) {
    var newTodoItem = document.createElement('p');
    newTodoItem.setAttribute('id', todoItem.id );
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
    if (todoItem.completed === false) {
      var newCheckbox = addCheckbox(todoItem);
      newCheckbox.setAttribute('class','completed');
      newTodoItem.appendChild(newCheckbox);
    } else {
      var newComppletedItem = document.createElement('span');
      newComppletedItem.innerText = '  X';
      newTodoItem.appendChild(newComppletedItem);
    }
    var newCheckbox = addCheckbox(todoItem);
    newCheckbox.setAttribute('class','deleted');
    newTodoItem.appendChild(newCheckbox);
  });
  refresh();
}

function addCheckbox(todoItem) {
  var newCheckbox = document.createElement('INPUT');
  newCheckbox.setAttribute('type', 'checkbox');
  newCheckbox.setAttribute('id', todoItem.id);
  return newCheckbox;
}

function refresh() {
  window.scrollTo(0,document.body.scrollHeight);
}

var url = 'http://whispering-forest-6132.herokuapp.com/todos';

var refreshButton = document.querySelector('.refresh-button');
var todoInput = document.querySelector('.todo-input');
var sendButton = document.querySelector('.send-button');
var deleteButton = document.querySelector('.delete-button');
var submitButton = document.querySelector('.submit-button');

refreshButton.addEventListener('click', function () {
  createGET(url, todoCallback);
});

sendButton.addEventListener('click', function () {
  createPOST(url, todoInput.value, createGET);
  todoInput.value = '';
});

deleteButton.addEventListener('click', function () {
  var items = document.querySelectorAll('.deleted');
  for (var i = 0; i < items.length; i++){
    if (items[i].checked === true) {
    createDELETE(url + '/' + items[i].id)
    }
  createGET(url, todoCallback);
  refresh();
  }

});

submitButton.addEventListener('click', function () {
  var items = document.querySelectorAll('.completed');
  for (var i = 0; i < items.length; i++){
    if (items[i].checked === true) {
      var data = items[i].parentNode;
      createPUT(url + '/'+ items[i].id, data.innerText, true)
    }
  createGET(url, todoCallback);
  refresh();
  }

});

// setInterval(function() {
//   createGET(url, todoCallback);
// }, 15000);

window.onkeydown = function keyEventHandler(e) {
    var keyCode = e.keyCode;
    if(keyCode === 13) {
      e.preventDefault();
      createPOST(url, todoInput.value, createGET);
      todoInput.value = '';
    }
};
//page start
createGET(url, todoCallback)
