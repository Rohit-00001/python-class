// const btn = document.getElementById("btn");
// btn.addEventListener("click", function () {
//   var first = Number(document.getElementById("firstNumber").value);
//   var second = Number(document.getElementById("secondNumber").value);
//   var output = first + second;

//   console.log(output);
//   //   document.getElementById("output").value = output;

//   document.getElementById("para").innerHTML = output;
// });

// const value = "hello from js pannel";

const a = 10;
const b = "10"

function add() {
  var first = Number(document.getElementById("firstNumber").value);
  var second = Number(document.getElementById("secondNumber").value);
  var output = first + second;

  document.getElementById("para").innerHTML = output;
}

function sub() {
  var first = Number(document.getElementById("firstNumber").value);
  var second = Number(document.getElementById("secondNumber").value);
  var output = first - second;

  document.getElementById("para").innerHTML = output;
// }

console.log(Math.round(2.2)); // 3
console.log(Math.floor(2.9)); // 2
console.log(Math.ceil(2.4)); // 3
console.log(Math.random()); //

// console.log("A " + 2);
var A = 10;

console.log(eval("A -" + 2));
