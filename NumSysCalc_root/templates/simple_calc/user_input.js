/**
 * when click on "ac"
 */
function clearAll() {
	screen.value = "0";
	screen.textContent = "0";
	answer.textContent = "0";
	isDigit = true;
	isSign = true;
	isInv = true;
	isPoint = true;
	isEqual = true;
}

/**
 * when user click on "Inv"
 */
function changeButtons() {
	const fstLineBtn = document.querySelector(".btn-row");
	let replace_html, replace_cls;
	if (fstLineBtn.children[1].classList.contains("bg-gray")) {
		replace_html = [
			["+/-", "("],
			["%", ")"],
			["/", "^"],
		];
		replace_cls = ["bg-gray", "bg-green"];
	} else {
		replace_html = [
			["(", "+/-"],
			[")", "%"],
			["^", "/"],
		];
		replace_cls = ["bg-green", "bg-gray"];
	}
	fstLineBtn.children[0].classList.replace(replace_cls[0], replace_cls[1]);
	for (let i = 1; i < fstLineBtn.children.length; i++) {
		fstLineBtn.children[i].innerHTML = fstLineBtn.children[i].innerHTML.replace(
			replace_html[i - 1][0],
			replace_html[i - 1][1]
		);
		fstLineBtn.children[i].classList.replace(replace_cls[0], replace_cls[1]);
	}
}

/**
 * autoresize textarea
 */
function autoResize() {
	screen.style.height = "auto";
	if (screen.scrollHeight >= 97) {
		screen.style.height = 97 + "px";
	} else {
		screen.style.height = screen.scrollHeight + "px";
	}
}

screen.oninput = function (userInput) {
	console.log(userInput, typeof userInput);
	// check for "=" in InputEvent
	autoResize();
	let isFinish = false;
	if (typeof userInput === "object") {
		if ((isFinish = userInput.data === "=")) {
			screen.value = screen.value.slice(0, -1);
		} else if (userInput.data === ".") {
			if (screen.value[-2] === "-") {
				screen.value = screen.value.slice(0, -1);
				screen.value += "0.";
			}
		}
	}
	let calculation = eval(editToEval(screen.value.trim()));
	//console.log(answer);
	//  console.log(calculation, typeof calculation);
	//  console.log(String(calculation));
	if (calculation === undefined) {
		answer.innerHTML = "";
	} else if (calculation === Infinity) {
		answer.innerHTML = "∞";
	} else if (calculation === -Infinity) {
		answer.innerHTML = "-∞";
	} else {
		answer.innerHTML = calculation;
	}
	// if user press "=" on keyboard
	if (isFinish) {
		screen.value = answer.innerHTML;
	}
};


document.querySelector(".buttons").onclick = (event) => {
	//  console.log(event);
	// not click on buttons
	if (!event.target.classList.contains("calc-btn-parent")) return;
	// click on "ac"
	if (event.target.classList.contains("ac")) {
		clearAll();
		return;
	}
	// click on Invertor
	if (event.target.classList.contains("invertor")) {
		changeButtons();
		return;
	}
	// get text from button
	const key = event.target.textContent;

	if (digits.includes(key) && isDigit) {
		if (screen.value === "0") {
			screen.value = "";
			isPoint = true;
		}
		screen.value += key;
		isSign = true;
		isInv = true;
		isEqual = true;
	} else if (signs.includes(key) && isSign) {
		screen.value += key;
		if (key !== "%") {
			isSign = false;
			isEqual = false;
		}
		isDigit = true;
		isInv = true;
		isPoint = true;
	} else if (invertors.includes(key) && isInv) {
		if (key === "+/-") {
			screen.value = "-(" + screen.value + ")";
			isSign = true;
			isDigit = false;
			isEqual = true;
		} else {
			if (screen.value === "0") screen.value = "";
			screen.value += key;
			isDigit = true;
			isEqual = false;
		}
		isInv = true;
		isPoint = true;
	} else if (key === "." && isPoint) {
		if (!digits.includes(screen.value[screen.value.length - 1])) {
			screen.value += "0";
		}
		screen.value += key;
		isDigit = true;
		isPoint = false;
		isSign = false;
		isEqual = false;
	} else if (key === "=" && isEqual) {
		screen.value = answer.textContent;
		if (screen.value === "0") {
			clearAll();
		} else {
			isDigit = true;
			isSign = true;
			isInv = true;
			if (screen.value.includes(".")) isPoint = false;
			isEqual = true;
		}
	} else if ("()".includes(key)) {
		screen.value += key;
	}
	screen.oninput();
};

