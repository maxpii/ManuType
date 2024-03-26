let word_array = []
let word = document.getElementById("word");
let counter = document.getElementById("count");
let input = document.getElementById("textbox");
let index = 0;
function filter(data) {
    for (let i = 0; i < data.length; i++) {
        word_array.push(data[i]);
      }
    word.innerHTML = word_array[0];
}

function textHandler() {
    var currentValue = input.value;
    input.style.color = "rgb(10, 255, 47)";
    input.style.caretColor = "rgb(10, 255, 47)";
    if (index >= word_array.length) {
      word.innerHTML = "You finished 25 words";
    }
    else if (currentValue.charAt(currentValue.length-1) === " ") {
      input.value = "";
      index ++;
      word.innerHTML = word_array[index];
      counter.innerHTML = 25 - index;
    }
    else if (currentValue.length > word_array[index].length ||
            word_array[index].substring(0,currentValue.length) !== currentValue
      ) {
        input.style.color = "red";
        input.style.caretColor = "red";
      } 
}


fetch("https://random-word-api.herokuapp.com/word?number=25")
.then(res => res.json())
.then(data => filter(data));

