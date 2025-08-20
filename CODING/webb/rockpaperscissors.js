// Rock, Paper, Scissors

let random = Math.floor(Math.random() * 3) + 1;
var comp_sign;
var your_sign = prompt("pick a sign: ").toLowerCase();

if (random == 1) {
  comp_sign = "rock";
} else if (random == 2) {
  comp_sign = "paper";
} else {
  comp_sign = "scissors";
}

if (your_sign == comp_sign) {
  alert("Draw");
} else if ((your_sign == "rock") & (comp_sign == "paper")) {
  alert("You Lose");
} else if ((your_sign == "rock") & (comp_sign == "scissors")) {
  alert("You Won");
} else if ((your_sign == "paper") & (comp_sign == "rock")) {
  alert("You Won");
} else if ((your_sign == "paper") & (comp_sign == "scissors")) {
  alert("You Lose");
} else if ((your_sign == "scissors") & (comp_sign == "rock")) {
  alert("You Lose");
} else (your_sign == "scissors") & (comp_sign == "paper");
{
  alert("You Lose");
}
