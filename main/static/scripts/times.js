let word_array = []
let word = document.getElementById("word");
let counter = document.getElementById("count");
let input = document.getElementById("textbox");
let seconds = document.getElementById("seconds");
let index = 0;
let allotedTime = 5;
let secondCounter = 1;
let totalCharacters = 0;
let correctCharacters = 0;
const interval = setInterval(incrementSeconds, 1000);
let flag = false;

function incrementSeconds() {
  if (secondCounter > allotedTime) {
    sendData();
    word.innerHTML = "Time's up";
    input.removeAttribute("onkeyup");
    clearInterval(interval);
    window.location.href = "http://127.0.0.1:5000/results";
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
  }
  word.innerHTML = word_array[0];
}

function textHandler() {
  flag = true;
  var currentValue = input.value;
  setInputStyle("rgb(10, 255, 47)");

  if (isTestComplete()) {
    handleTestCompletion();
  } else if (isTimeUp()) {
    handleTimeUp();
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
  return index >= word_array.length - 1;
}

function handleTestCompletion() {
  word.innerHTML = "No more words available";
  counter.innerHTML = 0;
  // TODO: fix this in the case someone somehow types more than 200 words
  // in the span of 30 seconds
}

function isTimeUp() {
  return secondCounter > allotedTime;
}

function handleTimeUp() {
  word.innerHTML = "Time's up";
}

function isSpaceCharacter(currentValue) {
  return currentValue.charAt(currentValue.length - 1) === ' ';
}

function handleSpaceCharacter(currentValue) {
  input.value = "";
  totalCharacters += currentValue.length;
  if (currentValue.substring(0, currentValue.length - 1) === word_array[index]) {
    correctCharacters += currentValue.length;
  }
  index++;
  word.innerHTML = word_array[index];
  counter.innerHTML = index;
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
    data: JSON.stringify({
      'Correct': correctCharacters,
      "Total": totalCharacters, "Time": secondCounter
    }),
    success: console.log("Success"),
    error: function (error) {
      console.log("You got an error");
      console.log(error);
    }
  });
}


fetch("https://random-word-api.herokuapp.com/word?number=200")
  .then(res => res.json())
  .then(data => filter(data));

