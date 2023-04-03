let isDigit = true,
	isSign = true,
	isInv = true,
	isPoint = true,
	isEqual = true;
const digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
	signs = ["+", "-", "x", "*", "/", "%", "^", "**"],
	invertors = ["-", "+/-"];
// textarea
const screen = document.querySelector(".calc-screen-wrapper textarea");
// <p></p> with answer under textarea
const answer = document.querySelector(".calc-screen-wrapper p");


