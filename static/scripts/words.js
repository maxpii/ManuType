let word_array = []
let word = document.getElementById("word");
let counter = document.getElementById("count");

function filter(data) {
    for (let i = 0; i < data.length; i++) {
        word_array.push(data[i]);
      }
}

fetch("https://random-word-api.herokuapp.com/word?number=25")
.then(res => res.json())
.then(data => filter(data));

console.log(word_array);