let word_array = []
let word = document.getElementById("word");
let counter = document.getElementById("count");
let input = document.getElementById("textbox");
let seconds = document.getElementById("seconds");
let index = 0;
let allotedTime = 15;
let secondCounter = 1;
let totalCharacters = 0;
let correctCharacters = 0;
const interval = setInterval(incrementSeconds,1000);
let flag = false;

function incrementSeconds() {
  if (secondCounter > allotedTime) {
    sendData();
    word.innerHTML = "Time's up";
    input.removeAttribute("onkeyup");
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
        word_array.push(data[i]);
      }
    word.innerHTML = word_array[0];
}

function textHandler() {
  flag = true;
    var currentValue = input.value;
    input.style.color = "rgb(10, 255, 47)";
    input.style.caretColor = "rgb(10, 255, 47)";
    if (index >= word_array.length - 1) {
      word.innerHTML = "No more words avaliabe";
      counter.innerHTML = 0;
      // TODO: fix this in the case someone somehow types more than 200 words
      // in the span of 30 seconds
    }
    else if (secondCounter > allotedTime) {
        word.innerHTML = "Time's up";
    }
    else if (currentValue.charAt(currentValue.length-1) === ' ') {
      input.value = "";
      totalCharacters += currentValue.length; 
      if (currentValue.substring(0,currentValue.length  - 1) === word_array[index]) {
        correctCharacters += currentValue.length;
      }
      index ++;
      word.innerHTML = word_array[index];
      counter.innerHTML = index;
    }
    // color changer
    else if (currentValue.length > word_array[index].length ||
            word_array[index].substring(0,currentValue.length) !== currentValue
      ) {
        input.style.color = "red";
        input.style.caretColor = "red";
      } 
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

