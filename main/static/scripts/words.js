let word_array = []
let word = document.getElementById("word");
let counter = document.getElementById("count");
let input = document.getElementById("textbox");
let seconds = document.getElementById("seconds");
let index = 0;
let totalWords = 10;
let secondCounter = 1;
let totalCharacters = 0;
let correctCharacters = 0;
counter.innerHTML = totalWords;
const interval = setInterval(incrementSeconds,1000);
let flag = false;

function incrementSeconds() {
  if (index >= word_array.length -1 ) {
    clearInterval(interval);
  }
  else {
    if (flag) {
   seconds.innerHTML = secondCounter;
    secondCounter++;
    }
  }
}

function filter(data) {
    for (let i = 0; i < data.length; i++) {
        if (data[i].length < 9) {
          word_array.push(data[i]);
        }
        if(word_array.length > totalWords) {
          break;
        }
      }
    word.innerHTML = word_array[0];
}

function textHandler() {
  console.log(totalCharacters + " " + correctCharacters);
  flag = true;
  var currentValue = input.value;
  setInputStyle("rgb(10, 255, 47)");

  if (isTestComplete()) {
    handleTestCompletion();
  } else if (isSpaceCharacter(currentValue)) {
    handleSpaceCharacter(currentValue);
  } else if (isIncorrectInput(currentValue)) {
    setInputStyle("red");
  }
}

function setInputStyle(color) {
  input.style.color = color;
  input.style.caretColor = color;
}

function isTestComplete() {
  return index >= word_array.length - 2;
}

function handleTestCompletion() {
  word.innerHTML = "You finished " + totalWords + " words";
  counter.innerHTML = 0;
  sendData();
  input.removeAttribute("onkeyup");
  window.location.href = "http://127.0.0.1:5000/results";
}

function isSpaceCharacter(currentValue) {
  return currentValue.charAt(currentValue.length - 1) === ' ';
}

function handleSpaceCharacter(currentValue) {
  input.value = "";
  totalCharacters += currentValue.length - 1;
  if (currentValue.substring(0, currentValue.length - 1) === word_array[index]) {
    correctCharacters += currentValue.length - 1;
  }
  index++;
  word.innerHTML = word_array[index];
  counter.innerHTML = totalWords - index;
}

function isIncorrectInput(currentValue) {
  return currentValue.length > word_array[index].length ||
    word_array[index].substring(0, currentValue.length) !== currentValue;
}

function sendData() { 
  $.ajax({ 
      url: '/process', 
      type: 'POST', 
      contentType: 'application/json', 
      data: JSON.stringify({ 'Correct': correctCharacters, 
      "Total":totalCharacters, "Time":secondCounter}), 
      success: console.log("Success"), 
      error: function(error) { 
        console.log("You got an error");
          console.log(error); 
      } 
  }); 
} 

fetch("https://random-word-api.herokuapp.com/word?number=200")
.then(res => res.json())
.then(data => filter(data));

