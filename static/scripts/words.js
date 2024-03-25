let word_array = []
let word = document.getElementById("word");
let counter = document.getElementById("count");
let input = document.getElementById("textbox");
function filter(data) {
    for (let i = 0; i < data.length; i++) {
        word_array.push(data[i]);
      }
}

function textHandler() {
    var currentValue = input.value;
    if (currentValue.charAt(currentValue.length-1) === " ") {
      input.value = "";
    }
}


fetch("https://random-word-api.herokuapp.com/word?number=25")
.then(res => res.json())
.then(data => filter(data));

textHandler();
